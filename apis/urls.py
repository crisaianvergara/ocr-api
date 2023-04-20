from django.urls import path
from .views import ReceiptApiView

app_name = "apis"

urlpatterns = [
    path("receipts/", ReceiptApiView.as_view()),
    path("receipts/<int:pk>/", ReceiptApiView.as_view()),
]
