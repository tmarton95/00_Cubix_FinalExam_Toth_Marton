import json

# define path of json-file:
file_path = "HomeWorks_Module_2\\HW_week_7\\spotify_playlist.json"

# load data of json file into 'data':
with open(file_path, "r") as json_file:
    data = json.load(json_file)

# collect infos and print it:
track_names = []
track_play_counts = []
for track in data['contents']['items']:
    track_names.append(track['name'])
    track_play_counts.append(track['playCount'])


print(f'The name of the 31st tracktrack is {track_names[30]}.')
print(sum(track_play_counts))
print(f'The song with the lowest playcount is {track_names[track_play_counts.index(min(track_play_counts))]}.')