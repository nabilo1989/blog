from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.say_hello),
    path('detail/<int:todo_id>/', views.detail),
]
