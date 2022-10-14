from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

#프로젝트에 application을 넣고 빼는 작업은
# url을 연결시켜주는 작업과 같다