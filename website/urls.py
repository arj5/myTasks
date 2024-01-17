
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('task/<int:pk>', views.user_task, name='task'),
    path('delete_task/<int:pk>', views.delete_task, name='delete_task'),
    path('add_task/', views.add_task, name='add_task'),
    path('update_task/<int:pk>', views.update_task, name='update_task'),
    path('sorting/', views.sorting, name='sorting'), 
    path('priority/', views.priority, name='priority'), 
]
