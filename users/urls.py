from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users import views

app_name = "users"

urlpatterns = [
    path("register/", views.UserRegistrationAPIView.as_view(), name="create_user"),
]
