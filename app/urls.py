from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about_us_view, name='about'),
    path('user/profile/', views.profile, name='profile'),
    path('python/interpreter', views.python_interpreter_view, name="python-intepreter"),
    path('python/run', views.run_python, name="run"),


]