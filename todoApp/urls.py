from django.urls import path,re_path
from . import views

app_name = "todo"

urlpatterns = [
        path('',views.home,name='index'),
        re_path(r'(?P<todo_id>[0-9]+)',views.detail,name='detail')
]
