from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):

	#GET - all Tasks
	
	todo = Todo.objects.all() #gets the list of objects in the to db


	#POST - Create a task  
	if request.method == 'POST':
		new_todo = Todo(
			task = request.POST['task'] 

		)
		new_todo.save()
		return redirect('/')

	return render(request, 'index.html', {'todos': todo})


def get_task(request, pk):
	#Get Single Task by ID
	task = {}
	todo = Todo.objects.get(id=pk)
	task["data"] = todo
	#t = task["data"]
	if request.method == 'POST':
		new_task = request.POST['update']
		
		Todo.objects.filter(id=pk).update(task=new_task)

		

		return redirect('/')

	#print(task)
	return render(request,"task.html", task)






	#Get Single Task by ID
	#task = {}
	#task["data"] = Todo.objects.get(id=pk)
	#return render(request,"task.html", task)





def delete(request, pk): #pk string id passed in to url

	#Delete task
	#get object from model

	todo = Todo.objects.get(id=pk)
	todo.delete()
	return redirect('/')







	

	#update task PATCH