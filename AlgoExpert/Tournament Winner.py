def tournamentWinnerMine(competitions, results):
    dictionary = {}
    for i in range(len(results)):
        if competitions[i][results[i] - 1] not in dictionary:
            dictionary[competitions[i][results[i] - 1]] = 3
        else:
            dictionary[competitions[i][results[i] - 1]] += 3
    
    x  =dict(sorted(dictionary.items(), key=lambda item: item[1]))
    for k,v in x.items():
        return k
    return ""

def tournamentWinnerTrial2(competitions, results):
    dictionary = {}
    dictionary[""] = 0
    bestTeam = ""
    for i in range(len(results)):
        if competitions[i][results[i] - 1] not in dictionary:
            dictionary[competitions[i][results[i] - 1]] = 3
            if(dictionary[bestTeam] < dictionary[competitions[i][results[i] - 1]]):
                bestTeam = competitions[i][results[i] - 1]

        else:
            dictionary[competitions[i][results[i] - 1]] += 3
            if(dictionary[bestTeam] < dictionary[competitions[i][results[i] - 1]]):
                bestTeam = competitions[i][results[i] - 1]
    
    return bestTeam

Home_Team_Won = 1
def tournamentWinner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        hometeam, awayteam = competition
        winningTeam = hometeam if result == Home_Team_Won else awayteam
        updateScores(winningTeam, 3, scores)

        if(scores[winningTeam] > scores[currentBestTeam]):
            currentBestTeam = winningTeam
    return currentBestTeam


def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points
