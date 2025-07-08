from ..imports import *

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