from django.contrib.auth.forms import AuthenticationForm
from django.urls import path
from django.contrib.auth import views as auth_views
from app1 import views


urlpatterns = [
    path('signup/', views.UserSignUp.as_view(), name='signup'),
    path('', auth_views.LoginView.as_view(template_name='loginpage.html',authentication_form=AuthenticationForm), name='login'),
    path('profile/', views.profileView, name='profile'),
    path('update/<int:pk>/', views.Update_View.as_view(), name='updatedata'),
    path('delete/<int:pk>/', views.DeleteData.as_view(), name='deletedata'),
    
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]