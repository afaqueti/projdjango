from django.urls import path
from .views import pessoa_list, \
                    endereco_list, \
                    nova_pessoa, \
                    update_pessoa, \
                    delete_pessoa



urlpatterns = [
    path('list/', pessoa_list, name='pessoa_list'),
    path('list/', endereco_list, name='endereço_list'),
    path('nova/', nova_pessoa, name='nova_pessoa'),
    path('update/<int:id>/', update_pessoa, name='update_pessoa'),
    path('delete/<int:id>/', delete_pessoa, name='delete_pessoa'),


]