import sqlite3
import pandas as pd
from faker import Faker
import streamlit as st

fake = Faker()
conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

def query_checker(func):
    def wrapper(q):
        q = q.upper()
        if q.startswith('SELECT'):
            return func(q)
        else:
            st.error("You can't add edit & new data to database")
    return wrapper


@query_checker
def run_sql_query(q):
    try:
        df = pd.read_sql_query(q, conn)
        st.write(df)
    except Exception as e:
        raise e


def query():
    q = str(st.text_area("WRITE YOUR SQL CODE HERE"))
    if st.button("RUN SQL CODE"):
        run_sql_query(q)


if __name__ == "__main__":
    query()
