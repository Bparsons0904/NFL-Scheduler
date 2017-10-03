# NFL Schedule

# 32 Teams, 2 Conferences, 4 divisions per Conferences
# 6 games vs teams in division. 3 Home, 3 Away
# 4 games vs same conference divsions. 2 Home, 2 Away
# 4 games vs oppositie conference divsion. 2 Home, 2 Away
# 2 games vs same conference divsion. 1 Home, 1 Away

# 1 @ a, b @ 1,  @ 2, 1 @ 1

import random

afcWest = ('Chiefs', 'Chargers', 'Raiders', 'Broncos')
afcEast = ('Dolphins', 'Bills', 'Patriots', 'Jets')
afcNorth = ('Ravens', 'Steelers', 'Bengals', 'Browns')
afcSouth = ('Titans', 'Jaguars', 'Texans', 'Colts')

nfcWest = ('Seahawks', 'Cardinals', 'Rams', '49ers')
nfcEast = ('Eagles', 'Cowboys', 'Reskins', 'Giants')
nfcNorth = ('Lions', 'Vikings', 'Packers', 'Bears')
nfcSouth = ('Falcons', 'Panthers', 'Buccaneers', 'Saints')

afc = (afcWest, afcEast, afcNorth, afcSouth)
nfc = (nfcWest, nfcEast, nfcNorth, nfcSouth)

nfl = (afc, nfc)

intraConference = [[afcEast, afcWest], [afcNorth, afcSouth], [nfcEast, nfcWest], [nfcNorth, nfcSouth]]
interConference = [[afcEast, nfcWest], [afcNorth, nfcSouth], [afcSouth, nfcWest], [afcWest, nfcEast]]

nflDivisions = [afcWest, afcEast, afcSouth, afcNorth, nfcNorth, nfcEast, nfcSouth, nfcWest]

standings = {'Chiefs':3, 'Chargers':27, 'Raiders':4, 'Broncos':11, 'Dolphins':10, 'Bills':21, 'Patriots':1, 'Jets':26, 'Ravens':17, 'Steelers':7, 'Bengals':24, 'Browns':32, 'Titans':15,
'Jaguars':30, 'Texans':13, 'Colts':18, 'Seahawks':8, 'Cardinals':20, 'Rams':28, '49ers':31, 'Eagles':23, 'Cowboys':2, 'Reskins':16, 'Giants':6, 'Lions':12, 'Vikings':19, 'Packers':9,
'Bears':29, 'Falcons':5, 'Panthers':25, 'Buccaneers':14, 'Saints':22}

nflGames = []
nflSchedule = []

def divisional(div):
    divSchedule = []
    for away in div:
        for home in div:
            if away != home:
                test = [away,home]
                if test not in divSchedule:
                    divSchedule.append(test)
    return divSchedule

def addToMaster(games):
    for e in games:
        nflGames.append(e)

def isHigher(team1, team2):
    if team1 > team2:
        return team1
    else:
        return team2

def sortDivisions(div):
    return sorted(div, key=standings.get)

def final_two_divison(conference):
    final_2 = [[],[],[],[]]
    for division in conference:
        division = sortDivisions(division)
        for team in division:
            pos = division.index(team)
            final_2[pos].append(team)
    return final_2

def finalTwo(conference):
    # afcWestSorted, afcEastSorted, afcSouthSorted, afcNorthSorted = sortDivisions(afcWest), sortDivisions(afcEast), sortDivisions(afcSouth), sortDivisions(afcNorth)
    # nfcWestSorted, nfcEastSorted, nfcSouthSorted, nfcNorthSorted = sortDivisions(nfcWest), sortDivisions(nfcEast), sortDivisions(nfcSouth), sortDivisions(nfcNorth)
    homeGames = []
    awayGames = []
    finalTwoGames = []
    for teams in final_two_divison(conference):
        for away in teams:
            for home in teams:
                test1 = [away, home]
                test2 = [home, away]
                if test1 not in nflGames and test2 not in nflGames and home != away:
                    if away not in awayGames and home not in homeGames and [home, away] not in finalTwoGames:
                        homeGames.append(home), awayGames.append(away)
                        finalTwoGames.append(test1)
    addToMaster(finalTwoGames)



def intraConferenceSchedule(divisions):
    div1 = divisions[0]
    div2 = divisions[1]
    homeGames = []
    awayGames = []
    intraGames = []
    for away in div1:
        for home in div2:
            if away != home:
                test = [away,home]
                if homeGames.count(test[1]) < 2 and awayGames.count(test[0]) < 2:
                        if test not in intraGames:
                            homeGames.append(home)
                            awayGames.append(away)
                            intraGames.append(test)
    for away in div2:
        for home in div1:
            if away != home:
                test = [away,home]
                test2 = [home,away]
                if test2 not in intraGames:
                    if homeGames.count(test[1]) < 2 and awayGames.count(test[0]) < 2:
                        if test not in intraGames:
                            homeGames.append(home)
                            awayGames.append(away)
                            intraGames.append(test)
    addToMaster(intraGames)

def weeklyGames(games):
    testList = games
    weekSchedule = []
    weekTeams = []
    for game in testList:
        if game[0] not in weekTeams and game[1] not in weekTeams:
            weekSchedule.append(game)
            for team in game:
                weekTeams.append(team)
    for games in weekSchedule:
        if games in testList:
            testList.remove(games)
    return weekSchedule, testList

def generateWeeklySchedule():
    testList = nflGames
    weeklySchedule = []
    weeks = 1
    while weeks < 16:
        # random.shuffle(testList)
        result = weeklyGames(testList)
        weeklySchedule.append(result[0])
        testList = result[1]
        weeks += 1
    weeklySchedule.append(testList)
    week = 1
    for schedule in weeklySchedule:
        print("Week {}".format(week), len(schedule), schedule)
        week += 1

# for div in nflDivisions:
#     addToMaster(divisional(div))
# for div in intraConference:
#     intraConferenceSchedule(div)
for div in interConference:
    intraConferenceSchedule(div)
# for conference in nfl:
#     finalTwo(conference)
generateWeeklySchedule()
