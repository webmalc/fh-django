"""fh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from ratelimitbackend import admin
from django.views.generic.base import RedirectView
from users.views import PasswordChangeRedirectView
from users.forms import ValidatingPasswordChangeForm

admin.autodiscover()

admin.site.site_header = 'FamilyHelper administration'

urlpatterns = [
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout', auth_views.logout, {'next_page': '/'}),
    url(r'^finances/', include('finances.urls', namespace="finances")),
    url(r'^analytics/', include('analytics.urls', namespace="analytics")),
    url(r'users/profile/password$', auth_views.password_change, {
        'template_name': 'users/password_change_form.html', 'password_change_form': ValidatingPasswordChangeForm},
        name='password_change'),
    url(r'users/profile/password/done$', PasswordChangeRedirectView.as_view(), name='password_change_done'),
    url(r'^users/', include('users.urls', namespace="users")),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^$', RedirectView.as_view(pattern_name='finances:payments_list', permanent=True), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
