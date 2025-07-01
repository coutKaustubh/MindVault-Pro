from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def landing_page(request):
    return render(request, "index.html")



@login_required(login_url='/login/')
def notes_entry(request):
    topics = Topic.objects.filter(user=request.user) 
    entries = Entry.objects.filter(user=request.user).order_by('-created_at')
    
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        # Handle Topic creation
        if form_type == 'add_topic':
            topic_name = request.POST.get('topic')
            if topic_name:
                Topic.objects.create(
                    user = request.user,
                    name=topic_name,

                    )
            return redirect('/MindVault/')

        # Handle Note creation
        elif form_type == 'add_note':
            topic_id = request.POST.get('selected_topic')
            title = request.POST.get('title')
            description = request.POST.get('description')
            image = request.FILES.get('image')

            try:
                topic = Topic.objects.get(id=topic_id)
                Entry.objects.create(
                    user = request.user,
                    topic=topic,
                    title=title,
                    description=description,
                    image=image
                )
            except Topic.DoesNotExist:
                pass

            return redirect('/MindVault/')

    return render(request, 'home.html', {
        'topics': topics,
        'entries': entries
    })

def login_page(request):

    if request.method != 'POST':
        return render(request , "login.html")

    username = request.POST.get('username')
    password = request.POST.get('password')
    
    if not User.objects.filter(username=username).exists():
        messages.error(request,'Invalid Username')
        return redirect('/login/')
    
    user = authenticate(username=username,password=password)
    if user is None:
        messages.error(request , 'Invalid Password')
        return redirect('/login/')
    
    else:
        login(request , user)
        return redirect('/MindVault/')


def register(request):
    if request.method != "POST":
        return render(request , "register.html")
    
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = User.objects.filter(username=username)
    if user.exists():
        messages.info(request, "Username already taken")
        return redirect('/register/')

    user = User.objects.create(
        first_name = first_name,
        last_name = last_name,
        username= username,

    )

    user.set_password(password)
    user.save()

    messages.info(request, "Account Created Successfully")

    return redirect('/register')
@login_required(login_url='/login/')
def delete_entry(request, id):
    entry = Entry.objects.get(id=id)
    print("Entry user:", entry.user)
    print("Current user:", request.user)

    if entry.user != request.user:
        print("User mismatch!")
        return redirect('/MindVault/')
    
    entry.delete()
    return redirect('/MindVault/')
    
@login_required(login_url='/login/')
def update_entry(request, id):
    entry = get_object_or_404(Entry, id=id)

    if entry.user != request.user:
        return redirect('/MindVault/')

    if request.method == 'POST':
        
        topic_id = request.POST.get('selected_topic')
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        if topic_id:
            entry.topic = get_object_or_404(Topic, id=topic_id)

        entry.title = title
        entry.description = description

        if image:
            entry.image = image

        entry.save()
        return redirect('/MindVault/')

    context = {
        'mindvault': entry,
        'topics': Topic.objects.filter(user=request.user)
    }
    return render(request, 'update_entry.html', context)

def logout_page(request):
    logout(request)
    return redirect('/home/')