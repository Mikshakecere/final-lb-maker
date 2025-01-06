import pip._vendor.requests as requests

def seconds_to_minutes(seconds):
    if seconds < 0:
        raise ValueError("Seconds cannot be negative.")
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes}:{remaining_seconds:02}"

def time_to_readable(time):
    time_seconds = int(str(time)[:-3])
    time_ms = f"{(int(str(time)[-3:])//10):02d}"
    return str(seconds_to_minutes(time_seconds)) + "." + time_ms

def extract_top_five(leaderboard):
    place_top_5 = {}
    for i in range(5):
        place_top_5[f"place_{i}"] = leaderboard['body'][i]
    return place_top_5

def extract_profile_id(data):
    return data['profile'][38:]

def filter_data(data):
    for player in data.values():
        del player['scoreParts']
        del player['submissionTime']
        player['score'] = time_to_readable(player['score'])
        player['id'] = extract_profile_id(player)
    return data

def print_top_five(data):
    for i, j in filtered_top_five.items():
        print(i)
        print(j)    

# link to request info
url = "https://data.ninjakiwi.com/"
category = "btd6/races/"
race_id = ""
tab = "leaderboard/"

race = url + category

# result = url + category + race_id + "/" + tab

# print("Result: " + result)

race_resp = requests.get(race).json()

if race_resp['error'] is not None or race_resp['success'] is False:
    print("Races category unavailable at the moment")
    exit()

counter = 0
target_race = {}

while (target_race == {}):
    print("Search for race using name: ")
    name = input().lower()

    for race in race_resp['body']:
        if race['name'].lower() == name:
            race_id = race['id']
            target_race = race
            break

    if target_race == {}:
        # eventually put this all in a while loop so you just continue trying again but yeah
        print("Couldn't find the target race, please try again")

leaderboard = requests.get(target_race['leaderboard']).json()

# response = requests.get(result)

# # this json is a dictionary so you can just search for items

top_five = extract_top_five(leaderboard)
filtered_top_five = filter_data(top_five)

print_top_five(filtered_top_five)

# # print the time
# print(place_first)
# print(place_first['score'])

# time = place_first['score']
# print(time_to_readable(time))
