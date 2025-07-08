from ..imports import *

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