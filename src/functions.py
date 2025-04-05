
def generateRanking(kill, assist, death, total_points, player, actRank):
    actRank[player]['kills'] = kill
    actRank[player]['assists'] = assist
    actRank[player]['deaths'] = 1 if death else 0
    actRank[player]['points'] = total_points

def mvpEvaluate(actRank,finalRank):
    max_points = -999
    mvp = None
    for player, stats in actRank.items():
        if stats['points'] > max_points:
            max_points = stats['points']
            mvp = player
            
    if mvp is not None: # en el caso de que no haya mvp(todos los participantes hagan 0)
        finalRank[mvp]['mvps'] += 1

def acumulateRanking(actRank,finalRank):
    for player, stats in actRank.items():
        finalRank[player]['kills'] += stats['kills']
        finalRank[player]['assists'] += stats['assists']
        finalRank[player]['deaths'] += stats['deaths']
        finalRank[player]['points'] += stats['points']