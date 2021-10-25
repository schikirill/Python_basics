time_lenght = [60, 3600, 86400]

duration = int(input("Введите продолжительность в секундах: "))

if duration < time_lenght[0]:
    print("duration = ", duration, " сек")

if time_lenght[0] <= duration < time_lenght[1]:
    print("duration = ", duration // 60, " мин ", duration % 60, " сек")

if time_lenght[1] <= duration < time_lenght[2]:
    print("duration = ", duration // 3600, " час ", duration % 3600 // 60, " мин ", duration % 60, " сек")

if duration >= time_lenght[2]:
    print("duration = ", duration // 86400, " дн. ", duration % 86400 // 3600, " час ", duration % 3600 // 60, " мин ", duration % 60, " сек")