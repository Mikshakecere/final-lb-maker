import pip._vendor.requests as requests

def seconds_to_minutes(seconds):
    if seconds < 0:
        raise ValueError("Seconds cannot be negative.")
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes}:{remaining_seconds:02}"

def time_to_readable(time):
    time_seconds = int(str(time)[:-3])
    time_ms = str(time)[-3:]

    # truncate the ms
    time_ms = str(int(time_ms)//10)

    return str(seconds_to_minutes(time_seconds)) + "." + time_ms

def extract_top_five(leaderboard):
    place_top_5 = {}
    for i in range(5):
        place_top_5[f"place_{i}"] = leaderboard['body'][i]
    return place_top_5

# link to request info
url = "https://data.ninjakiwi.com/"
category = "btd6/races/"
race_id = requests.get(url + category).json()['body'][3]['id']
tab = "leaderboard/"

result = url + category + race_id + "/" + tab

print("Result: " + result)

response = requests.get(result)

# this json is a dictionary so you can just search for items
leaderboard = response.json()

top_five = extract_top_five(leaderboard)
print(top_five)

# # print the time
# print(place_first)
# print(place_first['score'])

# time = place_first['score']
# print(time_to_readable(time))
