from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('doctor/', RetrieveUserView.as_view()),
    path('user/<id>', GetUser.as_view()),
    path('update/user/<id>', ProfileUpdateView.as_view()),
    path('admin/search/',UserSearchView.as_view()),
]