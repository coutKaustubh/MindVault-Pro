from ..imports import *

@login_required(login_url='/login/')
def delete_notification(request):
    Notifications.objects.all().delete()
    return redirect('/notification/')