from django.urls import path
from . import views

urlpatterns = [
    path('', views.say_hello, name='home'),
    path('detail/<int:todo_id>/', views.detail, name='detail'),
    path('delete/<int:todo_id>', views.delete, name='delete')
]
