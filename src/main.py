from src.functions import acumulateRanking,generateRanking,mvpEvaluate

rounds = [
    {
        'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
        'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
        'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
        'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
        'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
        'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
        'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
        'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
        'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
        'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
        'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
        'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
        'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
        'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
        'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
        'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
        'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
    }
]
def programEjecution():
    actRank = {}
    finalRank = {}

    # Inicializa ranking acumulado
    for player in rounds[0]:
        finalRank[player] = {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'points': 0}
    i = 1
    for round in rounds:
       # actRank.clear() # hago esto para limpiar el actRank en cada ronda, asi no quedan los datos acumulados de rondas anteriores y para no setear todo en 0 nuievamente
        for player, stats in round.items():
            kill = stats["kills"]
            assist = stats["assists"]
            death = stats["deaths"]
            aux = -1 if death else 0
            total_points = (kill * 3) + assist + aux

            if player not in actRank:
                actRank[player] = {'kills': 0, 'assists': 0, 'deaths': 0, 'points': 0}

            generateRanking(kill, assist, death, total_points, player, actRank)
            
        mvpEvaluate(actRank,finalRank)
        acumulateRanking(actRank,finalRank)

        sorted_ranking = sorted(finalRank.items(), key=lambda p: p[1]['points'], reverse=True) #Ordena el ranking total por puntos de mayor a menor

        # Imprimir ranking ronda por ronda
        print(f"\nRanking ronda {i}:")
        print("Jugador      Kills   Asistencias   Muertes   MVPs   Puntos")
        print("----------------------------------------------------------")
        for name, stats in sorted_ranking:
            print(f"{name:<12}{stats['kills']:<8}{stats['assists']:<13}{stats['deaths']:<10}{stats['mvps']:<7}{stats['points']}")
        i += 1

    # Al final, imprimir el ranking final
    print("\n Ranking Final ")
    print("Jugador      Kills   Asistencias   Muertes   MVPs   Puntos")
    print("----------------------------------------------------------")
    for name, stats in sorted_ranking:
        print(f"{name:<12}{stats['kills']:<8}{stats['assists']:<13}{stats['deaths']:<10}{stats['mvps']:<7}{stats['points']}")

if __name__ == "__main__":
    programEjecution()