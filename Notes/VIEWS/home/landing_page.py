from ..imports import *

def landing_page(request):
    return render(request, "index.html")