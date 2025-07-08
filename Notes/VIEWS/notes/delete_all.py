from ..imports import *

def delete_all(request) :
    Entry.objects.all().delete()
    return redirect('/MindVault/')
