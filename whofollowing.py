import json

following = open("following.json", "r")
followers = open("followers.json", "r")

followingJson = json.load(following)
followersJson = json.load(followers)

def parse_json(json_file, str_):
    curr_set = set()
    for user in json_file[str_]:
        curr_set.add(user['string_list_data'][0]['value'])
    return curr_set

not_following = parse_json(followingJson, 'relationships_following') - parse_json(followersJson, 'relationships_followers')

f = list(not_following)

f.sort()

for users_not_following in f:
    print(users_not_following)


