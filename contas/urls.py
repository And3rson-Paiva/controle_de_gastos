from django.urls import path
from contas.views import index, listagem, nova_transacao, update, delete


urlpatterns = [
    path('', index, name='index'),
    path('listagem/', listagem, name='listagem'),
    path('nova/', nova_transacao, name='nova'),
    path('update/<int:pk>', update, name='update'),
    path('delete/<int:pk>', delete, name='delete'),
]

