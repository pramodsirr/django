from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email_id']
        password = request.POST['password']

        x = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                     email=email, password=password)
        x.save()
        print("user created")
        return redirect('/')
    else:
        return render(request, 'b.html')
