from eva.protocol.grpc_auto_generated import user_pb2
from eva.protocol.data import user


class UserDataLoader(object):
    file_path = "resources"

    def __init__(self):
        pass

    def get_user(self, user_id):
        pb_object = self.get_user_pb_object(user_id)
        user_object = user.User(pb_object)
        return user_object

    def get_user_pb_object(self, user_id):
        pb_object = user_pb2.User()
        file_path = self.get_file_path(user_id)

        try:
            f = open(file_path, "rb")
            pb_object.ParseFromString(f.read())
            f.close()
        except IOError:
            print(f"{file_path} : Could not open file.")
            self.set_user_pb_object(user_id, pb_object)

        return pb_object

    def set_user_pb_object(self, user_id, pb_object):
        file_path = self.get_file_path(user_id)

        f = open(file_path, "wb")
        f.write(pb_object.SerializeToString())
        f.close()

    def get_file_path(self, user_id):
        return f"{self.file_path}/{user_id}"
