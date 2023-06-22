import time
from datetime import datetime, timedelta, timezone


class WishMessage:

    def __init__(self):
        pass

    def _get_time(self):
        return datetime.now(tz=timezone(timedelta(hours=5, minutes=30)))

    def get_part_of_day(self):
        user_time = self._get_time()
        print(user_time)
        user_hour = user_time.hour
        if 0 <= user_hour < 5:
            return 'Good midnight'
        elif 5 <= user_hour < 11:
            return 'Good morning, keep smiling ....! :)'
        elif 11 <= user_hour < 13:
            return 'Good noon'
        elif 13 <= user_hour < 19:
            return 'Good afternoon'
        else:
            return 'Good night'
