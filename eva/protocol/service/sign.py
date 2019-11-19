from eva.db import user_data_loader
import entities_pb2
import sign_pb2
import sign_pb2_grpc


def add_servicer_to_server(server):
    sign_pb2_grpc.add_SignServicer_to_server(SignServicer(), server)


def sign_in(user_data):
    is_first_sign_in_today = user_data.is_first_sign_in_today()
    user_data.update_last_signing_time()

    if is_first_sign_in_today:
        user_data.update_today_study()
        user_data.add_newly_studying_words()

        user_data.update_today_studying_words()
        user_data.update_today_testing_words()


def convert_user_data_to_user_service(user_data):
    user_service = entities_pb2.User()

    user_service.id = user_data.id
    user_service.today_study_date = user_data.today_study_date

    user_service.today_studying_words_index = user_data.today_studying_words_index
    for word_id in user_data.today_studying_word_ids:
        user_service.today_studying_word_ids.append(word_id)

    user_service.today_testing_words_index = user_data.today_testing_words_index
    for word_id in user_data.today_testing_word_ids:
        user_service.today_testing_word_ids.append(word_id)

    return user_service


class SignServicer(sign_pb2_grpc.SignServicer):

    def __init__(self):
        pass

    def SignIn(self, request, context):
        loader = user_data_loader.UserDataLoader()
        user_data = loader.get_user(request.user_id)
        sign_in(user_data)
        loader.set_user_pb_object(request.user_id, user_data.pb_object)

        user_service = convert_user_data_to_user_service(user_data)
        return sign_pb2.SignInResponse(user=user_service)
