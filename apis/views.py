from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import (
    Receipt,
)

from .serializers import (
    ReceiptSerializer,
)

from doctr.models import ocr_predictor


class ReceiptApiView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        receipts = Receipt.objects.filter(status=1)
        serializer = ReceiptSerializer(receipts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
