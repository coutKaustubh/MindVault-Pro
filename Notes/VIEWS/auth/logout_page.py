from ..imports import *

def logout_page(request):
    logout(request)
    return redirect('/home/')