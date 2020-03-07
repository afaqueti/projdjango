from django.urls import path
from .views import pessoa_list


urlpatterns = [
    path('list/', pessoa_list ),
]