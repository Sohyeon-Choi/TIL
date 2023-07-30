from django.shortcuts import render
from django.http import HttpResponse
from .models import * 


# Create your views here.
# before
'''
def index(request):
   return HttpResponse("My_to_do_app first page")
'''

# after
def index(request):
    return render(request, "my_to_do_app/index.html")

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponse("create Todo를 할 거야! => " + user_input_str)