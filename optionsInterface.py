from tkinter import *
from tkinter.ttk import Notebook

root = Tk()
notebook = Notebook(root)

teams = Frame(notebook)
stats = Frame(notebook)
submit = Frame(notebook)
info = Frame(notebook)

#################################
# --- INITIALIZING FUNCTIONS --- #
#################################
team = []
selected_options = []
region = []
username = []

#Function to store the values the user entered within a list
def on_button():
    for key, val in checkbuttons_options.items():
        select = val.get()
        if select:
            selected_options.append(key)
    for key, val in checkbuttons_teams.items():
        select2 = val.get()
        if select2:
            team.append(key)
    for key, val in checkbuttons_regions.items():
        select3 = val.get()
        if select3:
            region.append(key)
    username.append(username_box.get())

#Function to obtain the selected team from the user
def getTeam():
    return team

#Function to obtain the selected stats from the user
def getSelectedOptions():
    return selected_options

#Function to obtain the selected region from the user
def getRegion():
    return region[0]

#Function to obtain the users username
def getUsername():
    return username[0]

#################
# --- TEAMS --- #
#################
checkbuttons_teams = {'winners': IntVar(),
                      'losers': IntVar()}
vars_teams = []

#For loop to place each checkbutton for teams
for key, value in checkbuttons_teams.items():
    ctrl = Checkbutton(teams, text=key, variable=value)
    ctrl.pack(anchor=W)
    vars_teams.append(value)

#################
# --- STATS --- #
#################
checkbuttons_options = {'largestKillingSpree': IntVar(),
                                     'largestMultiKill': IntVar(),
                                     'killingSprees': IntVar(),
                                     'longestTimeSpentLiving': IntVar(),
                                     'totalDamageDealt': IntVar(),
                                     'largestCriticalStrike': IntVar(),
                                     'totalHeal': IntVar(),
                                     'damageDealtToObjectives': IntVar(),
                                     'visionScore': IntVar(),
                                     'timeCCingOthers': IntVar(),
                                     'totalDamageTaken': IntVar(),
                                     'goldEarned': IntVar(),
                                     'totalMinionsKilled': IntVar()}
vars_options = []

#For loop to place each checkbutton for options
for key, value in checkbuttons_options.items():
    ctrl = Checkbutton(stats, text=key, variable=value)
    ctrl.pack(anchor=W)
    vars_options.append(value)

##################
# --- SUBMIT --- #
##################
button = Button(submit, text='Submit Values', command=on_button)
button.pack(pady=5, padx=5)
button.pack(anchor=N)

################
# --- INFO --- #
################
username_label = Label(info,text = 'Username: ')
username_label.pack(anchor = N, side = LEFT)
username_box = Entry(info, bd = 5)
username_box.pack(anchor = N, side = LEFT)
region_label = Label(info,text = 'Region: ')
region_label.pack(anchor = N,side = LEFT)

checkbuttons_regions = {'BR1': IntVar(),
                        'EUN1': IntVar(),
                        'EUW1': IntVar(),
                        'JP1': IntVar(),
                        'KR': IntVar(),
                        'LA1': IntVar(),
                        'LA2': IntVar(),
                        'NA1': IntVar(),
                        'OC1': IntVar(),
                        'TR1': IntVar(),
                        'RU': IntVar()}
vars_regions = []

#For loop to place each checkbutton for regions
for key, value in checkbuttons_regions.items():
    ctrl = Checkbutton(info, text=key, variable=value)
    ctrl.pack(anchor=W)
    vars_regions.append(value)

########################
# --- ADDING PAGES --- #
########################
notebook.pack()
notebook.add(info,text='User Info')
notebook.add(teams,text = 'Team')
notebook.add(stats,text = 'Stat(s)')
notebook.add(submit,text = 'Submit Values')

root.mainloop()



