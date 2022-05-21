from . import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^create$', views.create, name='create'),
    re_path(r'^list$', views.list, name='list'),
    re_path(r'^fileupload$', views.fileupload, name='fileupload'),
    re_path(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    re_path(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    re_path(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    re_path(r'^ajax/$', views.ajax, name='ajax'),
    re_path(r'^ajax/ajax$', views.ajax, name='ajaxpost'),
    re_path(r'^ajax/delete$', views.ajax_delete, name='ajax_delete'),
    re_path(r'^ajax/getajax$', views.getajax, name='getajax'),
    re_path(r'^register/$', views.register,name='register'),
    re_path(r'^register/success/$',views.register_success,name='register_success'),
    re_path(r'^users/$',views.users,name='users'),
    re_path(r'^users/delete/(?P<id>\d+)$', views.user_delete, name='user_delete'),
    re_path(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
    re_path(r'^change_password$', views.changePassword, name='changePassword'),
    re_path(r'^file/delete$', views.changePassword, name='changePassword'),
    re_path(r'^file/delete/(?P<id>\d+)$', views.deleteFiles, name='deleteFiles'),
    re_path(r'^view$', views.view, name='view'),
]