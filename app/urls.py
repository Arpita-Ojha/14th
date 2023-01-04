from django.urls import path
from app.views import*

app_name='name1'

urlpatterns=[
    path('bts/',bts,name='bts'),
]