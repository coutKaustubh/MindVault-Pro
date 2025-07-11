from ..imports import *

    
def toggle_resolved(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    entry.resolved = not entry.resolved
    entry.save()
    return redirect('/notes/')