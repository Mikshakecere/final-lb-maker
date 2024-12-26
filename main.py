import pip._vendor.requests as requests

lmao = "https://data.ninjakiwi.com/btd6/races/Treet_Yourself_Extreme_Edition_m4ukr9d4/leaderboard"

url = "https://data.ninjakiwi.com/"
cat = "btd6/races/"
race_id = "Corvus_Carry_m4unf7th/leaderboard/"

url = url + cat + race_id

print(lmao)

response = requests.get(lmao)                                                       

print(response.json())
