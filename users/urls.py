from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users import views

app_name = "users"

urlpatterns = [
    path("list/", views.UserListAPIView.as_view(), name="user-list"),
]
