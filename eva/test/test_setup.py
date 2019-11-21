import sys
import os

# add root directory
root_directory = f"{__file__}/../../.."
sys.path.append(os.path.abspath(root_directory))

# add grpc directories
data_grpc_directory = f"{root_directory}/eva/protocol/grpc_auto_generated/data"
service_grpc_directory = f"{root_directory}/eva/protocol/grpc_auto_generated/service"
sys.path.append(os.path.abspath(data_grpc_directory))
sys.path.append(os.path.abspath(service_grpc_directory))
