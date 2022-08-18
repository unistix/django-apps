from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('delete/<str:pk>', views.delete, name='delete'), #dynamic url taks input
	path('task/<str:pk>', views.get_task, name='task') 
	#path('/<str:pk>', views.get_task, name='update')
	

	

]