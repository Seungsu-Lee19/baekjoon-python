from itertools import combinations

def split_two_teams(people):
    people = list(people)
    n = len(people)

    k = n // 2
    anchor = people[0]
    rest = people[1:]

    splits = []
    for teamA_rest in combinations(rest, k - 1):
        teamA = (anchor,) + teamA_rest
        teamA_set = set(teamA)
        teamB = tuple(p for p in people if p not in teamA_set)

        splits.append((teamA, teamB))

    return splits

n = int(input())
team = []
for _ in range(n):
    team.append(list(map(int, input().split())))
    
people = list(range(0, n))  # [1..n]
ans = split_two_teams(people)

_min = 1e9
k = n // 2
for a, b in ans:
    teamA = 0
    teamB = 0
    for i in range(k):
        for j in range(i, k):
            teamA = teamA + team[a[i]][a[j]] + team[a[j]][a[i]]
            teamB = teamB + team[b[i]][b[j]] + team[b[j]][b[i]]
    _min = min(_min, abs(teamA - teamB))           

print(_min)




