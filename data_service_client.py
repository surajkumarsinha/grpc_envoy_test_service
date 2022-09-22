import logging

import grpc
import asyncio

from grpc_python import data_service_pb2_grpc
from python import data_service_pb2


def run():
    channel = grpc.insecure_channel('grpc-sample-service-guruchart.jio-bhaaratai-covid.svc.cluster.local')
    stub = data_service_pb2_grpc.DataServiceStub(channel)
    for _ in range(20):
        print("-----GetStudentData-----")
        student_details = data_service_pb2.StudentDetails(id=2, name="Test2")
        response = stub.GetStudentData(student_details)
        print(response)
    channel.close()


if __name__ == "__main__":
    logging.basicConfig()
    run()
