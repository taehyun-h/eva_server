# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import test_pb2 as test__pb2


class TestStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.IKnow = channel.unary_unary(
        '/service.test.Test/IKnow',
        request_serializer=test__pb2.IKnowRequest.SerializeToString,
        response_deserializer=test__pb2.IKnowResponse.FromString,
        )
    self.IDontKnow = channel.unary_unary(
        '/service.test.Test/IDontKnow',
        request_serializer=test__pb2.IDontKnowRequest.SerializeToString,
        response_deserializer=test__pb2.IDontKnowResponse.FromString,
        )


class TestServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def IKnow(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def IDontKnow(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TestServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'IKnow': grpc.unary_unary_rpc_method_handler(
          servicer.IKnow,
          request_deserializer=test__pb2.IKnowRequest.FromString,
          response_serializer=test__pb2.IKnowResponse.SerializeToString,
      ),
      'IDontKnow': grpc.unary_unary_rpc_method_handler(
          servicer.IDontKnow,
          request_deserializer=test__pb2.IDontKnowRequest.FromString,
          response_serializer=test__pb2.IDontKnowResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'service.test.Test', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
