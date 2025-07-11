from ..imports import *

@login_required(login_url='/login/')
def notes_entry(request):    # sourcery skip: low-code-quality, use-contextlib-suppress, use-named-expression
    topics = Topic.objects.filter(user=request.user)
    entries = Entry.objects.filter(user=request.user)

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
        'notifications': notifications,
    })
