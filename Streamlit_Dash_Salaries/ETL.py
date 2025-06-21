import pandas as pd
from sqlalchemy import create_engine,inspect
import urllib

# 1. Read & clean
file = pd.read_csv("final-post-college-salaries.csv")

# strip symbols and convert to numeric
file['Early Career Pay']= pd.to_numeric(file['Early Career Pay'].replace(r'[\$,]', '', regex=True),errors='coerce')
file['Mid-Career Pay']=pd.to_numeric(file['Mid-Career Pay'].replace(r'[\$,]', '', regex=True),errors='coerce')
file['% High Meaning']=pd.to_numeric(file['% High Meaning'].replace(r'[%]', '', regex=True),errors='coerce')

# categorize majors
def categorize_major(major):
    if any(k in major for k in ('Engineering','Computer','Math','Science')):
        return 'STEM'
    if any(k in major for k in ('Economics','Finance','Business','Accounting')):
        return 'Business'
    if any(k in major for k in ('Psychology','Sociology','Social')):
        return 'Social Sciences'
    if any(k in major for k in ('Art','Design','Theater','Music','Photography')):
        return 'Arts'
    if any(k in major for k in ('Education','Teaching')):
        return 'Education'
    return 'Other'

file['Category'] = file['Major'].apply(categorize_major)

# prepare regression DataFrame
clean_data = file[['Major','% High Meaning', 'Mid-Career Pay']].dropna(subset=['% High Meaning','Mid-Career Pay'])

# prepare category summary
category_summary = (
    file
    .groupby('Category')[['Mid-Career Pay','% High Meaning']]
    .mean()
    .reset_index()
)

# 2. Connect to SQL Server (Windows Auth example)
odbc_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=SWERVOPC;DATABASE=AnalyticsDB;"
    "Trusted_Connection=yes;"
)
conn_str = "mssql+pyodbc:///?odbc_connect=" + urllib.parse.quote_plus(odbc_str)
engine = create_engine(conn_str, fast_executemany=True)
file.to_sql(
    name="careers_raw",
    con=engine,
    if_exists="replace",
    index=False
)
clean_data.to_sql(
    name="meaning_vs_salary",
    con=engine,
    if_exists="replace",
    index=False
)
category_summary.reset_index().to_sql(
    name="category_summary",
    con=engine,
    if_exists="replace",
    index=False
)

inspector = inspect(engine)
tables = inspector.get_table_names(schema="dbo")
print("Tables in dbo schema after ETL:", tables)
