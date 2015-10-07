from django.conf.urls import url
import users.views as views


urlpatterns = [
    url(r'profile$', views.Profile.as_view(), name='profile'),
    url(r'profile/edit$', views.UserUpdate.as_view(), name='profile_edit'),
]
