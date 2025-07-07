from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Case, When, Value, IntegerField ,Q
from datetime import timedelta
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone


def landing_page(request):
    return render(request, "index.html")


@login_required(login_url='/login/')
def notes_entry(request):    # sourcery skip: low-code-quality, use-contextlib-suppress, use-named-expression
    topics = Topic.objects.filter(user=request.user)
    entries = Entry.objects.filter(user=request.user)
    
    query = request.GET.get('search-entries')
    if query:
        entries = entries.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)|
            Q(problem_type__icontains=query)
        )

    
    entries = entries.annotate(
        priority_order=Case(
            When(priority_choice='high', then=Value(0)),
            When(priority_choice='medium', then=Value(1)),
            When(priority_choice='low', then=Value(2)),
            default=Value(3),
            output_field=IntegerField()
        )
    ).order_by('resolved', 'priority_order', '-created_at')

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        # Handle Topic creation
        if form_type == 'add_topic':
            topic_name = request.POST.get('topic')
            if topic_name:
                Topic.objects.create(
                    user=request.user,
                    name=topic_name,
                )
            return redirect('/MindVault/')

        # Handle Note creation
        elif form_type == 'add_note':
            topic_id = request.POST.get('selected_topic')
            title = request.POST.get('title')
            description = request.POST.get('description')
            image = request.FILES.get('image')
            problem_type = request.POST.get('problem_type')
            priority_choice = request.POST.get('priority_choice')
            if problem_type == 'other':
                problem_type = request.POST.get('custom_problem_type')

            try:
                topic = Topic.objects.get(id=topic_id)
                Entry.objects.create(
                    user=request.user,
                    topic=topic,
                    title=title,
                    description=description,
                    image=image,
                    problem_type=problem_type,
                    priority_choice=priority_choice
                )
            except Topic.DoesNotExist:
                pass

            return redirect('/MindVault/')

    
    #Reminder Logic 
    now = timezone.now()

     # 24-hour no entry reminder
    latest_entry = Entry.objects.filter(user=request.user).order_by('-created_at').first()
    if not Entry.objects.filter(user=request.user).exists():
        if not Notifications.objects.filter(user=request.user, notification_type="first_entry").exists():
            Notifications.objects.create(
                user=request.user,
                message="Welcome! You haven’t added your first problem yet.",
                notification_type="first_entry"
            )
    elif not latest_entry or latest_entry.created_at < (now - timedelta(hours=24)):
        if not Notifications.objects.filter(user=request.user, notification_type="no_entry_24h").exists():
            Notifications.objects.create(
                user=request.user,
                message= "You haven’t logged any new problem in the last 24 hours.",
                notification_type="no_entry_24h"
            )

    # 48-hour unresolved problem reminder
    stale_entries = Entry.objects.filter(   
        user=request.user,
        resolved=False,
        created_at__lt=now - timedelta(hours=48)
    )
    for entry in stale_entries:
        msg = f"You haven’t resolved this issue: “{entry.title}” in 48 hours."
        if not Notifications.objects.filter(user=request.user, notification_type="unresolved_48h").exists():
            Notifications.objects.create(
                user=request.user,
                message=msg,
                notification_type="unresolved_48h"
            )

    #  Fetch all unseen notifications
    notifications = Notifications.objects.filter(user=request.user, seen=False)

    return render(request, 'home.html', {
        'topics': topics,
        'entries': entries,
        'notifications': notifications,
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
        problem_type = request.POST.get('problem_type')
        priority_choice = request.POST.get('priority_choice')

        if problem_type == 'other':
            problem_type = request.POST.get('custom_problem_type')


        if topic_id:
            entry.topic = get_object_or_404(Topic, id=topic_id)

        entry.title = title
        entry.description = description
        entry.problem_type = problem_type
        entry.priority_choice = priority_choice
        if image:
            entry.image = image

        entry.save()
        return redirect('/MindVault/')

    context = {
        'mindvault': entry,
        'topics': Topic.objects.filter(user=request.user)
    }
    return render(request, 'update_entry.html', context)

def update_priority(request, pk, new_priority):
    entry = get_object_or_404(Entry, pk=pk)
    entry.priority = new_priority
    entry.save()
    return redirect('/MindVault/')
    
def toggle_resolved(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    entry.resolved = not entry.resolved
    entry.save()
    return redirect('/MindVault/')

@csrf_exempt
@login_required(login_url='/login/')
def  mark_notification_seen(request,notif_id):
    if request.method == 'POST':
        try:
            notif = Notifications.objects.get(id=notif_id, user=request.user)
            notif.seen = True
            notif.save()
            return JsonResponse({'status': 'success'})
        except Notifications.DoesNotExist:
            return JsonResponse({'status': 'not found'}, status=404)
    return JsonResponse({'status': 'invalid method'}, status=405)
    


@login_required(login_url='/login/')
def notification_page(request):
    notification_db = Notifications.objects.filter(user=request.user, seen=True)
    return render(request , "notifications.html" , {
        'notifications' : notification_db})
    

@login_required(login_url='/login/')
def delete_notification(request):
    Notifications.objects.all().delete()
    return redirect('/notification/')

def logout_page(request):
    logout(request)
    return redirect('/home/')

def delete_all(request) :
    Entry.objects.all().delete()
    return redirect('/MindVault/')



