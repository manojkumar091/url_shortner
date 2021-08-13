from django.conf.urls import url
from django.urls import path
from shorturl import views

urlpatterns = [
    path('geturl/', views.GetshortenURl.as_view(), name='get shorten URL')
]