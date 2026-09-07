from django.urls import path
from . import views
app_name="houses"
urlpatterns = [
    path("list/",views.house_list,name="list1"),
]
