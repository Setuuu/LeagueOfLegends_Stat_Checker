from riotwatcher import LolWatcher
import matplotlib.pylab as plt
import pandas as pd
from optionsInterface import *

##############################
# --- DEFINING FUNCTIONS --- #
##############################

# Function that filters the player stats to the values that we specify
def filter_player_stats(list, selected_options):
    # choose which values you want to see
    filtered_player = dict(
        (k, player[k]) for k in ['championId', 'kills', 'deaths', 'assists'] if k in player)
    for key, value in player.items():
        if key in selected_options:
            filtered_player[key] = player.get(key)
    # print(filtered_player)
    champNum = int(filtered_player.get('championId'))
    # print(champNum)
    if champNum in new_dict:
        filtered_player['championId'] = new_dict.get(champNum)
    list.append(filtered_player)


# Function to make the bar graph given the y value you want to display with the x-axis as the champion name
def make_bar_graph(y, kind):
    ax = df.plot(x='championId', y=y, kind=kind)
    # Printing the appropriate values for each bar in the bar graph
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.01, p.get_height() * 1.01))


####################
# --- SETTINGS --- #
####################
KEY = 'RGAPI-fcb40d2a-db6f-44e9-885d-1b31601b64e5'   #Enter your API key
REGION = getRegion()  # Enter your region (na1 for North America)
PLAYER = getUsername() # Player (Summoner) of interest
USER_OPTIONS = getSelectedOptions() #User options obtained from the GUI
TEAM = getTeam()  #Selected teams obtained from the GUI

print("REGION:", REGION)
print("PLAYER:", PLAYER)
print("----------------------")

#################
# --- SETUP --- #
#################

# Create master LolWatcher object
l_w = LolWatcher(KEY)
champ_data = l_w.data_dragon.champions("10.8.1")    #Patch that you currently are playing in (subject to change)
champ_list = champ_data['data']
new_dict = {}
for champ_info in champ_list.values():
    filtered_champ = dict((k, champ_info[k]) for k in ['name', 'key'] if k in champ_info)
    new_dict[int(filtered_champ.get('key'))] = filtered_champ.get('name')

# Get player with summoner name.
player = l_w.summoner.by_name(REGION, PLAYER)
id = player['accountId']

###############################
# --- GET FULL MATCH DATA --- #
###############################

# Get player's most recent match from match data.
match_data = l_w.match.matchlist_by_account(REGION, id, begin_index=0, end_index=1)
match_list = match_data['matches']
for match in match_list:
    # Takes specific gameId per match to get more detail and places into new list
    gameID = l_w.match.by_id(REGION, match.get('gameId'))
    players = gameID.get('participants')

winners = []
losers = []
for player in players:
    champID = player.get('championId')
    indvStats = player.get('stats')
    # adds the championID to the indv stats dictionary (easier to navigate for later)
    indvStats['championId'] = champID
    if indvStats.get('win') == True:
        winners.append(indvStats)
    else:
        losers.append(indvStats)

print("-------------------------")
winners_list = []
losers_list = []
if 'winners' in TEAM:
    for player in winners:
        filter_player_stats(winners_list, USER_OPTIONS)
if 'losers' in TEAM:
    for player in losers:
        filter_player_stats(losers_list, USER_OPTIONS)

####################
# --- PLOTTING --- #
####################
if 'winners' in TEAM:
    df = pd.DataFrame(winners_list)
else:
    df = pd.DataFrame(losers_list)

print(df)
for i in range(len(USER_OPTIONS)):
    make_bar_graph(USER_OPTIONS[i], 'bar')
plt.show()
