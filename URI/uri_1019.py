entrada = int(input())

hora    = int((entrada / 3600))
minuto  = int((entrada - (3600 * hora)) / 60)
segundo = int((entrada - (3600 * hora) - (minuto * 60)))

print(f"{hora}:{minuto}:{segundo}")