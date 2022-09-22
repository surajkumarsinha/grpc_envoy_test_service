import logging
from concurrent import futures
import grpc
from fastapi import FastAPI
import pydantic
import asyncio

from grpc_python import data_service_pb2_grpc
from python.data_service_pb2 import StudentData
from connections import get_db
from grpc.aio import init_grpc_aio

from connections import GRPC_PORT



class DataServiceServicer(data_service_pb2_grpc.DataServiceServicer):

    def __init__(self):
        self.db = get_db()
        pass

    def GetStudentData(self, request, context):
        logging.info(f"request received from - {request}")
        print("inside GRPC GetStudentsData....")
        response = self.get_student_data(request)
        if not response:
            return StudentData(id=-1, name="NULL", marks=-1)
        return StudentData(**response)

    def get_student_data(self, request):
        student_data = self.db["test"].find_one({"id": request.id, "name": request.name})
        if not student_data:
            return {}
        student_data.pop("_id")
        return student_data
        # return {
        #   "id":1,
        #   "name": "abc",
        #   "marks":100
        # }


# async def serve():
#     init_grpc_aio()
#     server = grpc.aio.server()
#     data_service_pb2_grpc.add_DataServiceServicer_to_server(DataServiceServicer(), server)
#     server.add_insecure_port('[::]:50051')
#     await server.start()
#     await server.wait_for_termination()


class gRPCServer:

    def __init__(self):
        init_grpc_aio()
        self.server = grpc.aio.server()
        self.servicer = DataServiceServicer()
        data_service_pb2_grpc.add_DataServiceServicer_to_server(self.servicer, self.server)

        self.server.add_insecure_port(f"[::]:{GRPC_PORT}")

    async def start(self):
        await self.server.start()
        print("grpc server started")
        await self.server.wait_for_termination()

    async def stop(self):
        await self.server.close()
        await self.server.wait_for_termination()


# class StudentDetailsSchema(pydantic.BaseModel):
#     id: int
#     name: str


# class StudentDataSchema(StudentDetailsSchema):
#     marks: int



# grpc_app = gRPCServer()

# # @app.on_event("startup")
# async def on_start():
#     # asyncio.ensure_future(grpc_app.start())
#     await grpc_app.start()
#     print("grpc on_start started")


# # @app.on_event("shutdown")
# async def on_stop():
#     await grpc_app.stop()
#     print("grpc stopped")


# app = FastAPI(on_startup=[on_start], on_shutdown=[on_stop])
data_service_servicer = DataServiceServicer()


# @app.post("/get_student_data/")
# async def get_student_data_handler(request: StudentDetailsSchema):
#     response = data_service_servicer.get_student_data(request)
#     # if isinstance(response, StudentData):
#     #     return {}
#     return response

async def serve():
    init_grpc_aio()
    server = grpc.aio.server()                                                       
    data_service_pb2_grpc.add_DataServiceServicer_to_server(DataServiceServicer(), server)
    listen_addr = '[::]:8080'                                                  
    server.add_insecure_port(listen_addr)                                       
    logging.info("Starting server on %s", listen_addr)                          
    await server.start()                                                        
    await server.wait_for_termination()
                                                                                
                                                                                
if __name__ == '__main__':                                                      
    logging.basicConfig(level=logging.INFO)                                     
    asyncio.run(serve())


# if __name__ == "__main__":
# #     import uvicorn

#     # uvicorn.run("data_service_server:app", port=5000)
#     asyncio.run(serve())
#     # asyncio.run(on_start())
#     print("grpc started")
