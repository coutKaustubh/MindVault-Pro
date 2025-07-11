from ..imports import *

def update_priority(request, pk, new_priority):
    entry = get_object_or_404(Entry, pk=pk)
    entry.priority = new_priority
    entry.save()
    return redirect('/notes/')