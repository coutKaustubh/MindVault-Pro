from Notes.VIEWS.imports import *

# Import view functions directly from each module
from Notes.VIEWS.home.landing_page import landing_page
from Notes.VIEWS.notes.notes_entry import notes_entry
from Notes.VIEWS.notes.update_entry import update_entry
from Notes.VIEWS.notes.delete_entry import delete_entry
from Notes.VIEWS.notes.toggle_resolved import toggle_resolved
from Notes.VIEWS.notes.update_priority import update_priority
from Notes.VIEWS.notes.delete_all import delete_all
from Notes.VIEWS.notes.notes_page import notes_page
from Notes.VIEWS.auth.login_page import login_page
from Notes.VIEWS.auth.logout_page import logout_page
from Notes.VIEWS.auth.register import register
from Notes.VIEWS.notifications.notification_page import notification_page
from Notes.VIEWS.notifications.delete_notification import delete_notification
from Notes.VIEWS.notifications.mark_notification_seen import mark_notification_seen

landing_page
notes_entry
login_page
register
delete_entry
update_entry
update_priority
toggle_resolved
mark_notification_seen
notification_page
delete_notification
logout_page
delete_all
notes_page


    