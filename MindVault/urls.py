from django.contrib import admin
from django.urls import path

from Notes.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',landing_page, name = "landing_page"),
    path('MindVault/',notes_entry, name = "notes_entry"),
    path('login/',login_page, name = "login_page"),
    path('register/',register, name = "register"),
    path('delete-entry/<int:id>/' , delete_entry , name = "delete-entry"),
    path('update-entry/<int:id>/' , update_entry , name = "update-entry"),
    path('logout/' , logout_page , name = "logout_page"),
    path('update-priority/<int:pk>/<str:new_priority>/', update_priority, name='update_priority'),
    path('toggle-resolved/<int:pk>/', toggle_resolved, name='toggle_resolved'),
    path('delete-all/', delete_all, name='delete_all'),
    path('mark-notification-seen/<int:notif_id>/', mark_notification_seen, name='mark_notification_seen'),
    path('notification/', notification_page, name='notification_page'),
    path('delete_notification/', delete_notification, name='delete_notification'),
   



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
