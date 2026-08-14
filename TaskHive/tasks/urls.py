from django.urls import path
from .import views

urlpatterns=[
    
     path('',views.home,name='home'),
     path('login/',views.login,name='login'),
     path('register/',views.register,name='register'),
     path('task_list/',views.task_list,name='task_list'),
     path("task/<int:id>/", views.task_detail, name="task_detail"),
     path('create_task/',views.create_task,name='create_task'),
     path('about/',views.about,name='about'),
     path('contect/',views.contect,name='contect'),
     path("logout/", views.logout_view, name="logout"), 
     path("choose_winner/<int:bid_id>/", views.choose_winner, name="choose_winner"),
]