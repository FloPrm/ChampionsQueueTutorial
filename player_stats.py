import pandas as pd
import streamlit as st


def get_player_data(teams_data, player_name):
    for team in teams_data:
        for player in team['players']:
            if player['name'] == player_name:
                player['win'] = team['winner']
                return player
    return None


def get_player_team(teams_data, player_name):
    for team in teams_data:
        is_team = False
        for player in team['players']:
            player['win'] = 1 if team['winner'] else 0
            if player['name'] == player_name:
                is_team = True

        if is_team:
            return team['players']
    return None


def get_player_matches(matches_df, player_name):
    matches_df['player_data'] = matches_df['teams'].apply(
        lambda match_teams: get_player_data(match_teams, player_name))
    return matches_df[matches_df['player_data'].notnull()]


def get_player_matches_data(matches_df, player_name):
    player_matches = get_player_matches(matches_df, player_name)
    return pd.DataFrame(player_matches['player_data'].tolist())


def get_player_vs(matches_df, player_name):
    player_matches = get_player_matches(matches_df, player_name)
    player_matches['teammates'] = player_matches['teams'].apply(
        lambda team: get_player_team(team, player_name))

    teammates_list = [element for sublist in player_matches['teammates'].tolist()
                      for element in sublist]
    teammates = pd.DataFrame(teammates_list)
    teammates = teammates[teammates['name'] != player_name]
    teammates['team'] = teammates['name'].apply(
        lambda player_name: player_name.split()[0])

    st.write("All teammates")
    st.write(teammates)

    # let's only return top 10 most played with for more readability
    most_played_with_names = teammates['name'].value_counts().head(
        10).index.tolist()
    most_played_with = teammates[teammates['name'].isin(
        most_played_with_names)]

    return most_played_with
