def new_follower(some_dict: dict, part_to_split: str) -> dict:
    username = part_to_split

    if username not in some_dict.keys():
        some_dict[username] = {'Likes': 0, 'Comments': 0}
        return some_dict
    return some_dict


def like(some_dict: dict, part_to_split: str) -> dict:
    username, count = part_to_split.split(': ')
    count = int(count)

    if username not in some_dict.keys():
        some_dict[username] = {'Likes': 0, 'Comments': 0}
    some_dict[username]['Likes'] += count
    return some_dict


def comment(some_dict: dict, part_to_split: str) -> dict:
    username = part_to_split

    if username not in some_dict.keys():
        some_dict[username] = {'Likes': 0, 'Comments': 0}
    some_dict[username]['Comments'] += 1
    return some_dict


def blocked(some_dict: dict, part_to_split: str) -> tuple[dict, str]:
    username = part_to_split

    if username in some_dict.keys():
        del some_dict[username]
        return some_dict, ''
    return some_dict, f"{username} doesn't exist."


jane_followers = {}

while (current_command := input()) != "Log out":
    command, arguments = current_command.split(': ', 1)

    if command == "New follower":
        jane_followers = new_follower(jane_followers, arguments)

    elif command == "Like":
        jane_followers = like(jane_followers, arguments)

    elif command == "Comment":
        jane_followers = comment(jane_followers, arguments)

    elif command == "Blocked":
        jane_followers, message = blocked(jane_followers, arguments)
        if message:
            print(message)

print(f"{len(jane_followers)} followers")

if jane_followers:
    for follower, follower_info in jane_followers.items():
        current_likes = follower_info['Likes']
        current_comments = follower_info['Comments']
        user_sum = current_likes + current_comments
        print(f"{follower}: {user_sum}")
