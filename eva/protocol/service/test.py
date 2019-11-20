from eva.db import user_data_loader
import test_pb2
import test_pb2_grpc


def add_servicer_to_server(server):
    test_pb2_grpc.add_TestServicer_to_server(TestServicer(), server)


def i_know(user_id):
    loader = user_data_loader.UserDataLoader()
    user_data = loader.get_user(user_id)

    words_count = len(user_data.today_testing_word_ids)
    current_index = user_data.today_testing_words_index
    if words_count >= current_index:
        return current_index

    user_data.i_know_current_test_index()

    new_index = current_index + 1
    user_data.update_today_testing_words_index(new_index)
    loader.set_user_pb_object(user_id, user_data.pb_object)

    return new_index


def i_dont_know(user_id):
    loader = user_data_loader.UserDataLoader()
    user_data = loader.get_user(user_id)

    words_count = len(user_data.today_testing_word_ids)
    current_index = user_data.today_testing_words_index
    if words_count >= current_index:
        return current_index

    user_data.i_dont_know_current_test_index()

    new_index = current_index + 1
    user_data.update_today_testing_words_index(new_index)
    loader.set_user_pb_object(user_id, user_data.pb_object)

    return new_index


class TestServicer(test_pb2_grpc.TestServicer):

    def __init__(self):
        pass

    def IKnow(self, request, context):
        new_index = i_know(request.user_id)
        return test_pb2.IKnowResponse(new_index=new_index)

    def IDontKnow(self, request, context):
        new_index = i_dont_know(request.user_id)
        return test_pb2.IDontKnowResponse(new_index=new_index)
