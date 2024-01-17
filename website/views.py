from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddTaskForm
from .models import Task
from django.db.models import Case, Value, When


def home(request):
    tasks = Task.objects.all()


    # check if logging in
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            #check

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('home')
            else:
                messages.success(request, "Login Error!")
                return redirect('home')
    else:
         return render(request, 'home.html', {'tasks':tasks})



# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "Logout successful!")
    return redirect('home')
    
def register_user(request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                 form.save()
                #check and login after making account
                 username = form.cleaned_data['username']
                 password = form.cleaned_data['password1']
                 user = authenticate(username=username, password=password)
                 login(request, user)
                 messages.success(request, "Login successful!")
                 return redirect('home')
        else:
            form = SignUpForm()
            return render(request, 'register.html', {'form':form})
        
        return render(request, 'register.html', {'form':form})
     
def user_task(request, pk):
     if request.user.is_authenticated:
        #look into task
        user_task = Task.objects.get(id=pk)
        return render(request, 'task.html', {'user_task':user_task})
     else:
        messages.success(request, "You must be logged in to see tasks!")
        return redirect('home')
     
def delete_task(request, pk):
     if request.user.is_authenticated:
        delete = Task.objects.get(id=pk)
        delete.delete()
        messages.success(request, "Record deleted successfully!")
        return redirect('home')
     else:
        messages.success(request, "You must be logged in to delete tasks!")
        return redirect('home')
     
def add_task(request):
        form = AddTaskForm(request.POST or None)
        if request.user.is_authenticated:
             if request.method == "POST":
                  if form.is_valid():
                       add_task = form.save()
                       messages.success(request, "Record Added!")
                       return redirect('home')

             return render(request, 'add_task.html', {'form':form})

        else:
            messages.success(request, "You must be logged in to add tasks!")
            return redirect('home')

def update_task(request, pk):
     if request.user.is_authenticated:
        currentTask = Task.objects.get(id=pk)
        form = AddTaskForm(request.POST or None, instance=currentTask)
        if form.is_valid():
             form.save()
             messages.success(request, "Record has been updated!")
             return redirect('home')
        
        return render(request, 'update_task.html', {'form':form})
     else:
        messages.success(request, "You must be logged in to update tasks!")
        return redirect('home')
     

def priority(request):
     if request.user.is_authenticated:
          messages.success(request, "Show Priority Sorting!")
          return render(request, 'priority.html')

     else:
          messages.success(request, "You must be logged in to delete tasks!")
          return redirect('home')


# all sorting methods

#PRIORITY

def sorting(request):

     if request.user.is_authenticated:



          sort = request.GET.get('sort')

          #priority

          if sort == 'orderhigh':

               tasks = Task.objects.order_by("priority")
          elif sort == 'orderlow':
               tasks = Task.objects.order_by("-priority")

          elif sort == 'onlylow':
               tasks = Task.objects.filter(priority='3')

          elif sort == 'onlymed':
               tasks = Task.objects.filter(priority='2')

          elif sort == 'onlyhigh':
               tasks = Task.objects.filter(priority='1')

          # status
               
          elif sort == 'ordertodo':
               tasks = Task.objects.order_by("status")

          elif sort == 'ordercomp':
               tasks = Task.objects.order_by("-status")

          elif sort == 'onlytodo':
               tasks = Task.objects.filter(priority='3')

          elif sort == 'onlyprog':
               tasks = Task.objects.filter(priority='2')
               
          elif sort == 'onlycomp':
               tasks = Task.objects.filter(priority='1')

          # datecreated

          elif sort == 'createdh':
               tasks = Task.objects.order_by("created_at")
          elif sort == 'createdl':
               tasks = Task.objects.order_by("-created_at")

          # due date
               
          elif sort == 'dueh':
               tasks = Task.objects.order_by("due_date")
          elif sort == 'duel':
               tasks = Task.objects.order_by("-due_date")

          # title
               
          elif sort == 'titleh':
               tasks = Task.objects.order_by('task_title')
          elif sort == 'titlel':
               tasks = Task.objects.order_by('-task_title')

          # id

          elif sort == 'givenidh':
               tasks = Task.objects.order_by('given_id')
          elif sort == 'givenidl':
               tasks = Task.objects.order_by('-given_id')
        
          return render(request, 'home.html', {'tasks':tasks})
     else:
          messages.success(request, "You must be logged in to update tasks!")
          return redirect('home')
