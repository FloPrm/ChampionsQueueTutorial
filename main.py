import streamlit as st
import pandas as pd

from championsqueue_requests import get_leaderboards, get_matches
from player_stats import get_player_matches_data, get_player_vs
from graphs import champions_pie_graph, champions_bar_graph, teammates_pie_graph, teammates_bar_graph


def main():
    st.set_page_config(page_title="Champions Queue Data", layout='wide')
    st.title('Champions Queue Analysis')

    # Get all of the Champions Queue data
    leaderboard = get_leaderboards()
    matches = get_matches()

    leaderboard_df = pd.DataFrame(leaderboard['leaderboards'][0]['lineup'])

    players_list = leaderboard_df.sort_values('name')['name']

    player_name = st.selectbox("Select a player", players_list)
    player_data = leaderboard_df[leaderboard_df.name == player_name].iloc[0]

    number_of_games = player_data['wins'] + player_data['losses']
    st.write(player_data['name'], ' played a total of ', str(
        number_of_games), " games on the Champions Queue")

    # get all of the matches as a dataframe
    matches_df = pd.DataFrame(matches['matches'])

    player_matches = get_player_matches_data(matches_df, player_name)
    # get all of the matches in which the player was in
    st.write("Match History:")
    st.write(player_matches)

    champions_pie_graph(player_matches)
    champions_bar_graph(player_matches)

    teammates = get_player_vs(matches_df, player_name)
    teammates_pie_graph(teammates)
    teammates_bar_graph(teammates)


if __name__ == "__main__":
    main()

    st.write("Made by [Arailla](https://twitter.com/lol_arailla) - See the [whole tutorial here](https://medium.com/@arailla/an-introduction-to-streamlit-and-plotly-with-champions-queue-as-a-concrete-example-b2803dff7eb4)")
