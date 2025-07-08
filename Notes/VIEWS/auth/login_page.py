from ..imports import *

def login_page(request):

    if request.method != 'POST':
        return render(request , "login.html")

    username = request.POST.get('username')
    password = request.POST.get('password')
    
    if not User.objects.filter(username=username).exists():
        messages.error(request,'Invalid Username')
        return redirect('/login/')
    
    user = authenticate(username=username,password=password)
    if user is None:
        messages.error(request , 'Invalid Password')
        return redirect('/login/')
    
    else:
        login(request , user)
        return redirect('/MindVault/')