from django.urls import path
from . import views
app_name="houses"
urlpatterns = [
    path('api/register/',views.register,name="register"),
    path("api/login/",views.login,name="login")
]
