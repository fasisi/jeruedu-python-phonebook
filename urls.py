from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index')
    path('hello/', views.hello, name='hello'),
    path('kirim/', views.kirim, name='kirim'),

    # fasisi.pythonanywhere.com/hello/
    path('', views.phone_login, name='login'),
    path('list/', views.phone_list, name='list'),
    path('add/', views.phone_add, name='add'),
    path('get/', views.phone_get, name='get'),
    path('update/', views.phone_update, name='update'),
    path('delete/', views.phone_delete, name='delete'),

    path('apiphoneadd/', views.api_phone_add, name='apiphoneadd'),
    path('apiphoneupdate/', views.api_phone_update, name='apiphoneupdate'),
    path('apiphoneget/', views.api_phone_get, name='apiphoneget'),
    path('apiphonedelete/', views.api_phone_delete, name='apiphonedelete'),
    path('apiphonelist/', views.api_phone_list, name='apiphonelist')
]