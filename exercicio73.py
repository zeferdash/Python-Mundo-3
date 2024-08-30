# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#
# a) Os 5 primeiros times.
#
# b) Os últimos 4 colocados.
#
# c) Times em ordem alfabética.
#
# d) Em que posição está o time do Corinthians.

times = (
    "Palmeiras",
    "Botafogo",
    "Grêmio",
    "Fluminense",
    "Athletico-PR",
    "Internacional",
    "Corinthians",
    "São Paulo",
    "Bahia",
    "Cruzeiro",
    "Fortaleza",
    "Santos",
    "Goiás",
    "Cuiabá",
    "Vasco da Gama",
    "Red Bull Bragantino",
    "América-MG",
    "Coritiba",
    "Flamengo",
    "Atlético-MG"
)

print(f"Lista de times do brasileirão: {times}")
print(f"Os 5 primeiros times: {times[0:5]}")
print(f"Os 4 últimos times: {times[-4:]}")
print(f"Times em ordem alfabética: {sorted(times)}")
print(f"Em que posicao encontra-se o Corinthians: {times.index('Corinthians')+1}ª posicao") #Acrescentei o +1 pois o primeiro do indice equivale a 0.