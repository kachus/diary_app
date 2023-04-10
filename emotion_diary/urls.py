from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.UsersView.as_view(), name = 'main'),
    path('test/', views.TestView.as_view(), name = 'test'),
    path('info/', views.UserInfoView.as_view(), name = 'info'),
    path('diary/', views.CreateRecord.as_view(), name = 'create_record')
    #path('admin/', admin.site.urls),
]
