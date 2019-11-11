from datetime import datetime
import time


def get_current_time():
    return int(time.time())


def is_today_milliseconds(timestamp):
    timestamp = int(timestamp / 1000)
    return is_today(timestamp)


def is_today(timestamp):
    today = datetime.now()
    dt_object = datetime.fromtimestamp(timestamp)
    return today.year == dt_object.year \
        and today.month == dt_object.month \
        and today.day == dt_object.day
