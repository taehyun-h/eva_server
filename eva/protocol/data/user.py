from eva.utils import time
from queue import PriorityQueue

NEW_STUDYING_WORDS_COUNT = 30
DAILY_STUDYING_WORDS_COUNT = 45
DAILY_TESTING_WORDS_COUNT = 45
STUDY_PERIOD_DATE = [0, 2, 3, 5]
TEST_PERIOD_DATE = [5, 10, 20, 15, 30, 30, 30]


class User(object):

    def __init__(self, pb_object):
        self.pb_object = pb_object

    def update_last_signing_time(self):
        self.pb_object.last_signing_time = time.get_current_time()

    def update_today_study(self):
        self.pb_object.today_study_date += 1
        self.pb_object.today_studying_words_index = 0
        self.pb_object.today_testing_words_index = 0

    def update_today_studying_words(self):
        queue = PriorityQueue()
        for word_order in self.pb_object.studying_word_orders:
            queue.put((word_order.order, word_order.id))

        del self.pb_object.today_studying_word_ids[:]
        for _ in range(DAILY_STUDYING_WORDS_COUNT):
            self.pb_object.today_studying_word_ids.append(queue.get()[1])

    def update_today_testing_words(self):
        queue = PriorityQueue()
        for word_order in self.pb_object.testing_word_orders:
            queue.put((word_order.order, word_order.id))

        del self.pb_object.today_testing_word_ids[:]
        for _ in range(DAILY_TESTING_WORDS_COUNT):
            self.pb_object.today_testing_word_ids.append(queue.get()[1])

    def add_newly_studying_words(self):
        if not self.is_adding_newly_studying_words():
            return

        for i in range(NEW_STUDYING_WORDS_COUNT):
            word_id = self.pb_object.last_studied_word_id + 1
            # todo : change real word data count
            if word_id >= 100:
                break

            self.pb_object.last_studied_word_id = word_id
            if word_id not in self.pb_object.studying_word_orders:
                word_order = self.pb_object.studying_word_orders[word_id]
                word_order.id = word_id
                word_order.order = self.pb_object.today_study_date

    def is_first_sign_in_today(self):
        return time.is_today(self.pb_object.last_signing_time)

    def is_adding_newly_studying_words(self):
        return self.pb_object.today_study_date % 2 == 1

    @property
    def id(self):
        return self.pb_object.id

    @property
    def today_study_date(self):
        return self.pb_object.today_study_date

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
