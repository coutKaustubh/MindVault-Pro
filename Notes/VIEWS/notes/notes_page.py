from ..imports import *

@login_required
def notes_page(request):
    entries = Entry.objects.filter(user=request.user)

    entries = entries.annotate(
        priority_order=Case(
            When(priority_choice='high', then=Value(0)),
            When(priority_choice='medium', then=Value(1)),
            When(priority_choice='low', then=Value(2)),
            default=Value(3),
            output_field=IntegerField()
        )
    ).order_by('resolved', 'priority_order', '-created_at')

    query = request.GET.get("search-entries", "")
    if query:
        entries = entries.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)|
            Q(problem_type__icontains=query)
        )

    return render(request, "notes.html", {
        "entries": entries,
        "query": query,
    })
