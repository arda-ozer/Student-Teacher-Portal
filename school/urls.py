from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(template_name='school/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('home/', views.home, name='home'),
    path('add_grade/<int:student_id>/', views.add_grade, name='add_grade'),
    path('edit_grade/<int:student_id>/', views.edit_grade, name='edit_grade'),
]