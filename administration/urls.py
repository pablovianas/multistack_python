from django.urls import path, reverse_lazy
from .views import service_views, user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('services/register', service_views.service_register, name="service_register"),
    path('services/list', service_views.service_list, name='service_list'),
    path('services/edit/<int:id>', service_views.edit_service, name='edit_service'),
    path('user/register', user_views.user_register, name='user_register'),
    path('user/list', user_views.user_list, name='user_list'),
    path('user/edit/<int:id>', user_views.edit_user, name='edit_user'),
    path('auth/login', auth_views.LoginView.as_view(), name='login'),
    path('auth/logout', auth_views.LogoutView.as_view(), name='logout'),
    path('auth/password_change', auth_views.PasswordChangeView.as_view(success_url = reverse_lazy('service_list')), name='password_change'),
    path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/success', auth_views.PasswordResetDoneView.as_view(), name='password_reset_success'),
    path('password_reset/<str:uidb64>/<str:token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
]