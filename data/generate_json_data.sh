#!/usr/bin/env bash


echo "Generating JSON files from NBA Data API ..."
python3 get_player_data.py > players.json
python3 get_team_data.py > teams.json
echo "JSON data has been saved to players.json and teams.json."
