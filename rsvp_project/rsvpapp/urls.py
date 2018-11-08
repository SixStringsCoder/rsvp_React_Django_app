from django.urls import path
from . import views

urlpatterns = [
    path('api/guest/', views.GuestListCreate.as_view() ),
]