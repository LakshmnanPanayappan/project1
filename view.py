from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView,UpdateAPIView,CreateAPIView,DestroyAPIView
from .models import KMC
from .serializer import DoctorResponseSerializer,DoctorRequestSerializer

class DoctorCreateView(CreateAPIView):
    serializer_class = DoctorResponseSerializer

    def post(self,request):
        try:

            serializer = DoctorResponseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'response_code' : 200,
                    'Message'       : 'data saved successfully',
                    'data'          : serializer.data
                })
            else:
                return Response({
                    'response_code' :400,
                    'Message'       : 'Invalid data',
                    'data'          : serializer.errors
                })
        except Exception as a:
            return ({
                'response_code'  : 500,
                'Message'        : 'Internal Server Error',
                'data'           : str(a)
            })

class DoctorListView(ListAPIView):

    def get(self,request):
        try:
            s = KMC.objects.all()
            serializer = DoctorResponseSerializer(s, many=True)
            return Response({
                "response_code" : 200,
                "message"       : "process completed",
                'data'          : serializer.data
            })
        except Exception as e:
            return ({
                'response_code'  : 500,
                'message'        : 'Internal Server Error',
                'data'           : str(e)
            })

