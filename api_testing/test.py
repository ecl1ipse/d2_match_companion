import requests

base_url = "https://api.opendota.com/api/"

def getTeams():
    r = requests.get(base_url + "teams")
    teams = r.json()

    print(len(teams))
    '''
    for team in teams:
        print(team["name"])
    '''

def getProPlayers():
    r = requests.get(base_url + "proPlayers")
    players = r.json()
    for player in players:
        if player["team_name"] == "Team Secret":
            break

    print("persona name: " + player["personaname"])
    print("name: " + player["name"])
    print("team name: " + player["team_name"])
    print("fantasy role: " + str(player["fantasy_role"]))

def getProMatches():
    r = requests.get(base_url + "proMatches")
    matches = r.json()

    print(matches)

getProMatches()
