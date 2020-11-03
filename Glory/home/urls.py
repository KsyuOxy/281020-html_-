from django.urls import path
from .views import index, htmltrain

urlpatterns = [
    path('', index),
    path('htmltrain', htmltrain)
]
