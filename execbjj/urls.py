"""execbjj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls.conf import include


from members.views import index_page, dashboard_page, register, webhook, newsletter, beginners_course, beginners_success, dashboard_redirect, flyer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name="index_page"),
    path('register/', register, name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('dashboard/', dashboard_redirect, name="dashboard_redirect"),
    path('dashboard/<date>', dashboard_page, name="dashboard_page"),
    path('password-reset/', PasswordResetView.as_view(), name="password_reset"),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('membership/', include('members.urls')),
    path('checkin/', include('checkins.urls')),
    path('webhook/', webhook, name='webhook'),
    path('newsletter/', newsletter, name='newsletter'),
    path('beginners-course/', beginners_course, name="beginners_course"),
    path('beginners-course/success/', beginners_success, name="beginners_success"),
    path('flyer/', flyer, name='flyer'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
