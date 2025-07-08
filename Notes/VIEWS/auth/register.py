from ..imports import *

def register(request):
    if request.method != "POST":
        return render(request , "register.html")
    
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = User.objects.filter(username=username)
    if user.exists():
        messages.info(request, "Username already taken")
        return redirect('/register/')

    user = User.objects.create(
        first_name = first_name,
        last_name = last_name,
        username= username,

    )

    user.set_password(password)
    user.save()

    messages.info(request, "Account Created Successfully")

    return redirect('/register')
