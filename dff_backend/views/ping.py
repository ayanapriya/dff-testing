from rest_framework.views import APIView
from rest_framework.response import Response
from dff_backend.utils.firebase import upload_to_firebase


class Ping(APIView):
    authentication_classes = ()
    permission_classes = ()

    @staticmethod
    def get(request):
        return Response("Ping")

