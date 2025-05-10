from django.urls import path

from Nato.views import nato_list
from .views import (
base_view,
user_login,
register,
user_logout,
change_password,
profile_view
)
urlpatterns = [
    path('', base_view, name='base'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('change-password/', change_password, name='change_password'),
    path('profile/', profile_view, name='profile'),

]
