from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, events
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm

def home_page (request):
    categories = Category.objects.all()[:5]
    event = events.objects.all().order_by('-created_at')[:6]

    context = {
        'categories': categories,
        'event': event
    }
    return render(request, "./home_page.html", context)

def categories_page (request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request,"categories.html", context)

def all_events_page (request):
    event = events.objects.all().order_by('-created_at')
    context = {
        'event': event
    }
    return render(request,"all_events.html", context)
    
def event_detail_page (request, pk):
    event = get_object_or_404(events, pk=pk)
    context = {
        'events': event
    }
    return render(request, "event_detail.html", context)

def event_by_category_page(request, slug):
    category = get_object_or_404(Category, slug=slug)
    event = events.objects.filter(category=category)    
    context = {
        'category': category,
        'event': event
    }
    return render(request, "event_by_category.html", context)

def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login_page')
    else:
        form = NewUserForm()
    context = {
        'form': form
    }
    return render(request, "./sign-up.html", context)
def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
    else:
        form = AuthenticationForm()

    
    context = {
        'form': form
    }
    return render(request, "./login.html", context)

def logout_action(request):
    logout(request)
    return redirect('home_page')