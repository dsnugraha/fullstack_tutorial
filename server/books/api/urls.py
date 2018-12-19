from .views import bookAPIView
from django.conf.urls import re_path

app_name = 'books'

urlpatterns = [
  re_path('', bookAPIView.as_view(), name='book-create'),
]
