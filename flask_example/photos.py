import requests, random


def dict_by_user(user_id):
    r = requests.get('https://api.vk.com/method/users.get', {'user_ids': user_id,
                                                             'fields': 'photo_id,photo_200'})
    r = r.json()['response'][0]
    u = {'photo': r['photo_200'], 'name': "%s %s" % (r['first_name'], r['last_name']), 'id': r['uid']}
    return u


def get_photos():
    r = requests.get('https://api.vk.com/method/groups.getMembers', {'group_id': 'goto_msk'})
    users = r.json()['response']['users']
    #print(users)
    return (dict_by_user(random.choice(users)), dict_by_user(random.choice(users)))


if __name__ == '__main__':
    print(get_photos())
