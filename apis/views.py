from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from services.elasticsearch import elasticsearch_client
from .serializers import IngestSerializer

class IngestDataAPIView(APIView):
    
    def post(self, request, **kwargs):

        ingest_serializer = IngestSerializer(data=request.data)
        ingest_serializer.is_valid(raise_exception=True)

        validated_data = ingest_serializer.validated_data

        try:
            data = elasticsearch_client.create_document(
                index_name=validated_data.get("index"),
                body=validated_data.get("payload")
            )
        except:
            return Response(
                data=self.get_response(status=False, message="Failed to ingest document"), 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )      

        return Response(
            data=self.get_response(status=True, data=data, message="Document inserted successfully"), 
            status=status.HTTP_200_OK
        )


    def get_response(self, status=True, data=None, message=""):
        return {
            "status" : status,
            "data" : data,
            "message" : message
        }