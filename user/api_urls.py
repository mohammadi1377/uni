from django.urls import path
from .api_views import RegisterView, LoginView, LogoutView, UserDetailView, StudentDetailView, ProfessorDetailView

urlpatterns = [
	path('register/', RegisterView.as_view(), name='user-registration'),
	path('login/', LoginView.as_view(), name='login'),
	path('profile/', UserDetailView.as_view(), name='update-user-profile'),
	path('profile/student/', StudentDetailView.as_view(), name='update-student-profile'),
	path('profile/professor/', ProfessorDetailView.as_view(), name='update-professor-profile'),
	path('logout/', LogoutView.as_view(), name='logout'),

]
