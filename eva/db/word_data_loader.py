from eva.utils import singleton
import word_pb2


class WordDataLoader(singleton.Singleton):
    file_path = "resources/static"

    def __init__(self):
        if not hasattr(self, '_words'):
            self._words_count = 0
            self._words = self.load()

    def load(self):
        pb_object = word_pb2.Words()
        word_id = 0

        f = open(f"{self.file_path}/WordData.txt", "r")
        for line in f.readlines():
            s = [w.strip() for w in line.split(':')]
            pb_word = pb_object.words[word_id]
            pb_word.id = word_id
            pb_word.spelling = s[0]
            if len(s) >= 3:
                pb_word.meaning2 = s[2]
            if len(s) >= 2:
                pb_word.meaning = s[1]

            word_id += 1
        f.close()

        self._words_count = word_id

        return pb_object

    def save(self):
        f = open(f"{self.file_path}/WordData", "wb")
        f.write(self._words.SerializeToString())
        f.close()

    def get_word_count(self):
        return self._words_count

    def get_word(self, word_id):
        return self._words.words[word_id]
