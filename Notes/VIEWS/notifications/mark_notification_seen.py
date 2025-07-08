from ..imports import *

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
    