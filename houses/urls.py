from django.urls import path
from . import views
app_name="houses"
urlpatterns = [
    path('api/register/',views.register,name="register"),
    path("api/login/",views.login,name="login"),
    path('api/user/to_landlord',views.update_user_to_landlord,name="to_landlord"),
]
