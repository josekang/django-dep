from django.conf.urls import url
from fifth_app import views

app_name = 'fifth_app'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login')
]
