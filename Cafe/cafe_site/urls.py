from django.urls import path
from django.http import HttpResponse
from .views import *


def testView(request):
    return HttpResponse('Это тестовая страница')

urlpatterns=[
    path('',MenuListView.as_view(), name='menu_list'),
    path('detail/<int:pk>', MenuDetailView.as_view(), name='menu_detail'),
    path('create/', MenuCreate.as_view(), name='menu_create'),
    path('update/<int:pk>', MenuUpdate.as_view(), name='menu_update'),
    path('delete/<int:pk>', MenuDelete.as_view(), name='menu_delete'),

]