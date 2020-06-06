"""
Python Developement Techdegree
Project 2 - Basketball-Stats-Tool

Author: Felix Andrew Sapalaran (felixandrewsapalaran@gmail.com)
---------------------------------------------------------------
"""

import constants
import random
import copy

#
#
#
'''
Please note: AVOID "altering"  IMPORTED DATA
use this function below

visit link to learn more: https://stackabuse.com/deep-vs-shallow-copies-in-python/

click link below to understand the difference between deepcopy() and copy()


#    def clean_data():
#     new_players_list = constants.PLAYERS
#     for player in new_players_list:
#         for key, value in player.items():
#             if key == "experience":
#                 if value == "YES":
#                     player[key] = True
#                 else:
#                     player[key] = False
#             if key == "height":
#                 height_list = value.split(" ")
#                 height = int(height_list[0])
#                 player[key] = height
#     return new_players_list
'''

def clean_data():
    # print(constants.PLAYERS)
    new_players_list = copy.deepcopy(constants.PLAYERS)
    for player in new_players_list:
        for key, value in player.items():
            if key == "experience":
                if value == "YES":
                    player[key] = True
                else:
                    player[key] = False
            if key == "height":
                height_list = value.split(" ")
                height = int(height_list[0])
                player[key] = height
    # print(constants.PLAYERS)
    # print(new_players_list)

    return new_players_list


#create new list and return lists of players based on their experience
def new_player_list(players):
    experienced_players = []
    inexperienced_players = []
    for player in players:
        for key, value in player.items():
            if key == "experience":
                if value == False:
                    inexperienced_players.append(player)
                else:
                    experienced_players.append(player)
    return experienced_players, inexperienced_players


# Function for creating the teams that takes two list of players
def build_teams(exp_players, inexp_players):

    #setting up a 2 dimensional list (a list of list)
    #this allows me to not care how many teams there will be
    teams = [[],[],[]]

    #set an index that allows me to determine which team I'm adding to
    #in the while loop below
    team_index = 0

    still_have_players = True

    #this loop takes players with experience and no experience and
    #add them randomly to each team
    while still_have_players:

        # Add players to the teams
        exp_index = random.randint(0, len(exp_players) - 1)
        inexp_index = random.randint(0, len(inexp_players) - 1)

        #use team_index to detemine which list list to add to
        #teams[0] for example is the first team
        #but it's all random in the same way
        teams[team_index].append(exp_players[exp_index])
        teams[team_index].append(inexp_players[inexp_index])

        del exp_players[exp_index]
        del inexp_players[inexp_index]

        #increment the team index each time I add a player
        #end up with even teams
        team_index += 1

        # if the team index > 2 that means we reset to the first team and start over
        if team_index > 2:
            team_index = 0

        if len(exp_players) > 0:
            continue
        else:
            still_have_players = False

    return teams


def show_teams():
    print("""
    1.Panthers
    2.Bandits
    3.Warriors
    """)


def display_team(team_of_team, players_list):

    out = [
      "Team: {} stats.".format(team_of_team),
      "---------------------",
      "Total players: {}".format(len(players_list)),
      "Players on team:",
      ", ".join(get_player_names(players_list))
    ]

    outString = "\n".join(out)

    print("\n"+outString+"\n")


# Returns a list of player names given a players list
def get_player_names(players_list):
    player_names = []
    for val in players_list:
        for key, value in val.items():
            if key == "name":
                player_names.append(value)
    return player_names


if __name__ == "__main__":
    exp, inexp = new_player_list(clean_data())

    # get all teams
    teams = build_teams(exp, inexp)

    # add team names to list
    team_names = ["Panthers","Bandits","Warriors"]

    print("""
    |----------------------------|
    | BASKETBALL TEAM STATS TOOL |
    |----------------------------|

     Main Menu
    ------------

    Here are your choices:

    1. Display Team Stats
    2. Quit
    """)
    proceed = True
    display_team_stats = False

    # Loop for initial menu selection
    while proceed:
        try:
            selection = int(input("Enter an option: "))
        except:
            print("Please enter 1 or 2 only")
            continue
        #check if user input more  2 or less 1
        if selection > 2 or selection < 1:
            print("Please choose either 1 or 2")
            continue
        elif selection == 1:
            display_team_stats = True
            # Loop for choosing between teams
            while display_team_stats:
                show_teams()
                try:
                    selection =int(input("Enter an option: "))
                except:
                    print("Please enter 1, 2 or 3 only")
                    continue
                #check if user input num > 3 or num < 1
                if selection > 3 or selection < 1:
                    print("Please enter a number option(1, 2 or 3")
                    continue

                if selection > 0 and selection <= len(team_names):
                    display_team(team_names[selection-1], teams[selection-1])
                continue_again = True
                # Loop for choosing between teams again or quitting
                while continue_again:
                    would_continue = input("Please enter (Y) to continue or (Q) to quit: ")
                    if would_continue.upper() == "Y":
                        continue_again = False
                    elif would_continue.upper() == "Q":
                        continue_again = False
                        display_team_stats = False
                        proceed = False
                        print("The program has exited...")
                    else:
                        print(f"({would_continue}) is NOT a valid value. Please try again...")
        elif selection == 2:
            print("The program has exited...")
            proceed = False
