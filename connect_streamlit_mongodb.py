# streamlit_app.py

import streamlit as st
import pymongo
import time
# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    time.sleep(2)
    return pymongo.MongoClient(**st.secrets["mongo"],connect=False)

client = init_connection()

# Pull data from the collection.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def get_data():
    db = client['IRCdatabase']
    items = db['IRB1210axis2_03_endurance'].find_one()
    items = list(items)  # make hashable for st.experimental_memo
    return items

items = get_data()

# Print results.
for item in items:
    st.write(item)
