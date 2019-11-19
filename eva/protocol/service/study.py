from eva.db import user_data_loader
import study_pb2
import study_pb2_grpc


def add_servicer_to_server(server):
    study_pb2_grpc.add_StudyServicer_to_server(StudyServicer(), server)


def move_to_word(user_id, word_index_delta):
    loader = user_data_loader.UserDataLoader()
    user_data = loader.get_user(user_id)

    words_count = len(user_data.today_studying_word_ids)
    current_index = user_data.today_studying_words_index
    new_index = (current_index + word_index_delta + words_count) % words_count

    user_data.study_current_index()
    user_data.update_today_studying_words_index(new_index)

    return new_index


class StudyServicer(study_pb2_grpc.StudyServicer):

    def __init__(self):
        pass

    def MoveToNextWord(self, request, context):
        new_index = move_to_word(request.user_id, 1)
        return study_pb2.MoveToNextWordResponse(index=new_index)

    def MoveToPreviousWord(self, request, context):
        new_index = move_to_word(request.user_id, -1)
        return study_pb2.MoveToPreviousWordResponse(index=new_index)
