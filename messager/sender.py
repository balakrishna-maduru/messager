import json
import requests
from manager import Manager
from wish_messages import WishMessage
from constants import secretsDetails


class Sender:

    def __init__(self):
        self._url = "https://www.fast2sms.com/dev/bulkV2"
        self._manager = Manager()
        self._wish_messages = WishMessage()
        self.__watch_word = self._get_watch_word()

    @property
    def sender_word(self):
        return self.__watch_word[secretsDetails.MySenderKey.value]

    @property
    def recipent_details(self):
        return self.__watch_word[secretsDetails.recepientDetails.value]

    def send(self):
        print(f"recipent_details : {self.recipent_details}")
        querystring = {
            "authorization": self.sender_word,
            "message": self._wish_messages.get_part_of_day(),
            "language": "english",
            "route": "q",
            "numbers": 9741163344}

        headers = {
            'cache-control': "no-cache"
        }
        try:
            print("Started sending message")
            response = requests.request("GET", self._url,
                                        headers=headers,
                                        params=querystring)

            return "SMS Successfully Sent"
        except:
            return "Oops! Something wrong"

    def _get_watch_word(self):
        return json.loads(self._manager.get_my_sender())
