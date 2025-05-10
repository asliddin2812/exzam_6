from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    home,
    index,
    nato_list,
    member_create,
    member_edit,
    member_delete,
    search,
    profile_update
)
urlpatterns = [
    path('', home, name='home'),
    path('search', search, name='search'),
    path('account/', index, name='index'),
    path('nato/', nato_list, name='nato_list'),
    path('add/', member_create, name='member_create'),
    path('profile/update/', profile_update, name='profile_update'),
    path('edit/<str:country_name>/', member_edit, name='member_edit'),
    path('delete/<str:country_name>/', member_delete, name='member_delete'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='nato/password_reset.html'),name='password_reset' ),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='nato/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='nato/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='nato/password_reset_complete.html'), name='password_reset_complete'),


]