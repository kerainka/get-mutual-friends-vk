import requests

TOKEN = ""
API_URL = "https://api.vk.com/method/"
VERSION = "5.126"

class VkFriend:
    def __init__(self, api_url, token, version):
        self.api_url = api_url
        self.token = token
        self.version = version
        self.params = {
            "access_token": self.token,
            "v": self.version
        }

    def get_mutual(self, source_uid, target_uid):
        mutual_url = self.api_url + "friends.getMutual"
        mutual_params = {
            "source_uid": source_uid,
            "target_uid": target_uid,
            }
        res = requests.get(mutual_url, params={**self.params, **mutual_params})
        return res.json()


class User:
    def __init__(self, user_id):
        self.vk_client = VkFriend(API_URL, TOKEN, VERSION)
        self.user_id = user_id

    def get_id(self):
        return self.user_id

    def __and__(self, other_user):
        common_friends = self.vk_client.get_mutual(self.get_id(), other_user.get_id())["response"]
        common_friends = [User(friend_id) for friend_id in common_friends]
        return common_friends

    def __str__(self):
        return "https://vk.com/id" + str(self.get_id())

    def __repr__(self):
        return self.__str__()


user_1 = User(6492)
user_2 = User(2745)
print(user_1 & user_2)
print(user_1)
