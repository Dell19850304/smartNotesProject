from django.urls import path

#my imports
from . import views

urlpatterns = [
     path('', views.HomeView.as_view(),name='home'),
     path('authorized/', views.HomeAuthorized.as_view()),
     path('login/', views.LoginInterfaceView.as_view(),name='login'),
     path('logout/', views.LogoutInterfaceView.as_view(),name='logout'),
     path('signup/',views.SignupInterfaceView.as_view(),name='signup'),
]
