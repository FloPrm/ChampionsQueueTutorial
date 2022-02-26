import plotly.express as px
import streamlit as st


# https://plotly.com/python/pie-charts/
def champions_pie_graph(champions_df):
    fig = px.pie(champions_df, names='championIcon', title="Champions played")
    fig.update_traces(textinfo='value')
    st.plotly_chart(fig)


# https://plotly.com/python/bar-charts/
def champions_bar_graph(champions_df):
    fig = px.histogram(champions_df, x='championIcon', color='championIcon',
                       y='kills', histfunc='avg', title="Average Kills")
    fig.update_layout(barmode='stack', xaxis={
                      'categoryorder': 'category ascending'})
    st.plotly_chart(fig)

def teammates_pie_graph(teammates_df):
    fig = px.pie(teammates_df, names='name', title="Played with")
    fig.update_traces(textinfo='value')
    st.plotly_chart(fig)

def teammates_bar_graph(teammates_df):
    fig = px.histogram(teammates_df, x="name", color="team", y="win",
                       histfunc="avg", title="Average winrate with")
    fig.update_layout(barmode='stack', xaxis={
                      'categoryorder': 'category ascending'})
    st.plotly_chart(fig)
