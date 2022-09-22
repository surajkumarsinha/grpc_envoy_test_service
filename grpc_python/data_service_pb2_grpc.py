# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import python.data_service_pb2 as data__service__pb2


class DataServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetStudentData = channel.unary_unary(
                '/pb.DataService/GetStudentData',
                request_serializer=data__service__pb2.StudentDetails.SerializeToString,
                response_deserializer=data__service__pb2.StudentData.FromString,
                )


class DataServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetStudentData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetStudentData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStudentData,
                    request_deserializer=data__service__pb2.StudentDetails.FromString,
                    response_serializer=data__service__pb2.StudentData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pb.DataService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetStudentData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.DataService/GetStudentData',
            data__service__pb2.StudentDetails.SerializeToString,
            data__service__pb2.StudentData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
