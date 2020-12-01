from django.urls import path, re_path
from . import views

urlpatterns = [
    path('listapp/', views.List_Edit),
    re_path('listapp/(?P<pk>[0-9]+)$', views.TODO_detail),
]