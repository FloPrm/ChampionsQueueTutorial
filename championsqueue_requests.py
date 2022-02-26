import requests
import streamlit as st

BASE_URL = 'https://d1fodqbtqsx6d3.cloudfront.net'

# Cache the data for 30 minutes


@st.cache(ttl=1800)
def get_leaderboards():
    url = BASE_URL + '/leaderboards.json'
    r = requests.get(url, verify=False)
    return r.json()


@st.cache(ttl=1800, allow_output_mutation=True)
def get_matches():
    url = BASE_URL + '/matches.json'
    r = requests.get(url, verify=False)
    return r.json()
