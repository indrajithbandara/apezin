from django.urls import re_path
from app.rent.views import apartments


urlpatterns = [
    re_path(r'^apartments/$', apartments, name='apartments')
]
