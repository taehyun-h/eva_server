from eva.utils import time
from eva.db import word_data_loader
from queue import PriorityQueue
import user_pb2

NEW_STUDYING_WORDS_COUNT = 30
DAILY_STUDYING_WORDS_COUNT = 30
DAILY_TESTING_WORDS_COUNT = 30
STUDY_PERIOD_DATE = [0, 2, 3, 5]
TEST_PERIOD_DATE = [5, 10, 20, 15, 30, 30, 30]


def create_time(timestamp):
    pb_time = user_pb2.Time()
    pb_time.time = timestamp
    return pb_time


def create_default_time():
    return create_time(0)


def create_default_user(user_id):
    pb_object = user_pb2.User()
    pb_object.id = user_id
    pb_object.last_signing_time.CopyFrom(create_default_time())
    pb_object.today_study_date = 0
    pb_object.last_studied_word_id = -1
    pb_object.today_studying_words_index = 0
    pb_object.today_testing_words_index = 0
    return pb_object


class User(object):

    def __init__(self, pb_object):
        self.pb_object = pb_object

    def update_last_signing_time(self):
        current_time = create_time(time.get_current_time())
        self.pb_object.last_signing_time.CopyFrom(current_time)

    def update_last_studied_word_id(self, word_id):
        self.pb_object.last_studied_word_id = word_id

    def update_today_study(self):
        self.pb_object.today_study_date += 1
        self.pb_object.today_studying_words_index = 0
        self.pb_object.today_testing_words_index = 0

    def clear_today_studying_word_ids(self):
        del self.today_studying_word_ids[:]

    def clear_today_testing_word_ids(self):
        del self.today_testing_word_ids[:]

    def add_studying_word(self, word_id):
        studying_word = self.studying_words[word_id]
        studying_word.id = word_id
        studying_word.studied_count = 0

    def add_testing_word(self, word_id):
        testing_word = self.testing_words[word_id]
        testing_word.id = word_id
        testing_word.passed_count = 0

    def add_studying_word_order(self, word_id, order):
        word_order = self.studying_word_orders[word_id]
        word_order.id = word_id
        word_order.order = order

    def add_testing_word_order(self, word_id, order):
        word_order = self.testing_word_orders[word_id]
        word_order.id = word_id
        word_order.order = order

    def add_today_studying_word_ids(self, word_id):
        self.today_studying_word_ids.append(word_id)

    def add_today_testing_word_ids(self, word_id):
        self.today_testing_word_ids.append(word_id)

    def increase_studied_count(self, word_id):
        studying_word = self.studying_words[word_id]
        studying_word.studied_count += 1

    def update_today_studying_words(self):
        queue = PriorityQueue()
        for word_id in self.studying_word_orders:
            word_order = self.studying_word_orders[word_id]
            queue.put((word_order.order, word_order.id))

        self.clear_today_studying_word_ids()
        for _ in range(DAILY_STUDYING_WORDS_COUNT):
            if queue.empty():
                break

            self.add_today_studying_word_ids(queue.get()[1])

    def update_today_testing_words(self):
        queue = PriorityQueue()
        for word_id in self.testing_word_orders:
            word_order = self.testing_word_orders[word_id]
            queue.put((word_order.order, word_order.id))

        self.clear_today_testing_word_ids()
        for _ in range(DAILY_TESTING_WORDS_COUNT):
            if queue.empty():
                break

            self.add_today_testing_word_ids(queue.get()[1])

    def add_newly_studying_words(self):
        if not self.is_adding_newly_studying_words():
            return

        for i in range(NEW_STUDYING_WORDS_COUNT):
            word_id = self.last_studied_word_id + 1
            if word_id >= word_data_loader \
                    .WordDataLoader().instance.get_word_count():
                break

            self.update_last_studied_word_id(word_id)
            if word_id not in self.studying_word_orders:
                self.add_studying_word_order(word_id, self.today_study_date)
            if word_id not in self.studying_words:
                self.add_studying_word(word_id)

    def study_current_index(self):
        current_index = self.today_studying_words_index
        current_word_id = self.today_studying_word_ids[current_index]
        if current_word_id in self.studying_word_orders:
            return
        if current_word_id in self.testing_word_orders:
            return

        self.increase_studied_count(current_word_id)
        studied_count = self.studying_words[current_word_id].studied_count
        if studied_count >= len(STUDY_PERIOD_DATE):
            next_order = self.today_study_date + TEST_PERIOD_DATE[0]
            self.add_testing_word_order(current_word_id, next_order)
            self.add_testing_word(current_word_id)
        else:
            next_order = self.today_study_date + STUDY_PERIOD_DATE[studied_count]
            self.add_studying_word_order(current_word_id, next_order)

    def is_first_sign_in_today(self):
        return not time.is_today_milliseconds(self.last_signing_time.time)

    def is_adding_newly_studying_words(self):
        return self.today_study_date % 2 == 1

    @property
    def id(self):
        return self.pb_object.id

    @property
    def last_signing_time(self):
        return self.pb_object.last_signing_time

    @property
    def today_study_date(self):
        return self.pb_object.today_study_date

    @property
    def last_studied_word_id(self):
        return self.pb_object.last_studied_word_id

    @property
    def studying_words(self):
        return self.pb_object.studying_words

    @property
    def testing_words(self):
        return self.pb_object.testing_words

    @property
    def studying_word_orders(self):
        return self.pb_object.studying_word_orders

    @property
    def testing_word_orders(self):
        return self.pb_object.testing_word_orders

    @property
    def today_studying_words_index(self):
        return self.pb_object.today_studying_words_index

    @property
    def today_studying_word_ids(self):
        return self.pb_object.today_studying_word_ids

    @property
    def today_testing_words_index(self):
        return self.pb_object.today_testing_words_index

    @property
    def today_testing_word_ids(self):
        return self.pb_object.today_testing_word_ids
