from ..imports import *

@login_required(login_url='/login/')
def notification_page(request):
    notification_db = Notifications.objects.filter(user=request.user, seen=True)
    return render(request , "notifications.html" , {
        'notifications' : notification_db})
    