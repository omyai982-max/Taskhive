from django.shortcuts import render
from .models import Category, Task
from django.shortcuts import render, get_object_or_404
from .models import Task
from django.shortcuts import render, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect
from .forms import TaskForm, RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import Q
from .forms import TaskForm, BidForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import BidForm
from .models import Bid




def home(request):

    query = request.GET.get("search")
    category_id = request.GET.get("category")

    tasks = Task.objects.all()
    categories = Category.objects.all()

    if query:
        tasks = tasks.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    if category_id:
        tasks = tasks.filter(category_id=category_id)

    context = {
        "tasks": tasks,
        "categories": categories,
    }

    return render(request, "home.html", context)
def login(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()

            auth_login(request, user)

            return redirect("home")

    else:

        form = AuthenticationForm()

    return render(request, "login.html", {
        "form": form
    })

def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")

    else:

        form = RegisterForm()

    return render(request, "register.html", {
        "form": form
    })

def task_list(request):

    tasks = Task.objects.all()

    return render(request, "task_list.html", {
        "tasks": tasks
    })


def task_detail(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.task = task
            bid.freelancer = request.user
            bid.save()
            return redirect("task_detail", id=task.id)
    else:
        form = BidForm()

    bids = task.bid_set.all()

    return render(request, "task_detail.html", {
        "task": task,
        "form": form,
        "bids": bids,
    })
@login_required
def create_task(request): 

    if request.method == "POST":

        form = TaskForm(request.POST)

        if form.is_valid():

            task = form.save(commit=False)
            task.owner = request.user
            task.save()
         
            return redirect("task_list")

    else:

        form = TaskForm()

    return render(request, "create_task.html", {"form": form})


def about(request):
    return render(request,'about.html')

def contect(request):
    return render(request,'contect.html')

def logout_view(request):
    logout(request)
    return redirect("home")


def choose_winner(request, bid_id):
    bid = get_object_or_404(Bid, id=bid_id)

    task = bid.task
    task.status = "Assigned"
    task.save()

    return redirect("task_detail", id=task.id)