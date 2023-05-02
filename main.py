import sqlite3
import pandas as pd
from faker import Faker
import streamlit as st

fake = Faker()
conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

def check_query(q: str) -> bool:
    q = q.upper()
    if q.startswith('SELECT'):
        return True
    else:
        return False

def runsqlquery(q):
    if check_query(q):
        try:
            df = pd.read_sql_query(q, conn)
            st.write(df)
        except Exception as e:
            raise e

    else:
        st.text("You can't add edit & new data to database")

def query():
    q = str(st.text_area("WRITE YOUR SQL CODE HERE"))
    if st.button("RUN SQL CODE"):
        runsqlquery(q)

if __name__ == "__main__":
    query()
