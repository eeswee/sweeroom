from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()  # save user to database
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            # log the user in
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('home')  # redirect to a success page

    else:
        form = RegisterUserForm()  # create an empty form

    return render(request, 'authenticate/register_user.html', {'form': form})


def login_user(request):
    if request.method == 'POST':  # if the user is submitting the form

        username = request.POST['username']  # get username from post data
        password = request.POST['password']  # get password from post data

        # authenticate the user using Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        if user is not None:  # if we have a user object (user exists in db)

            login(request, user)  # log the user in by setting up their session data
            return redirect('home')  # redirect to a success page
        else:
            messages.success(request,("There Was Error Logging In,Try Again... "))
            return redirect('login')
        
    else:
        return render(request, 'authenticate/login.html')  # otherwise just render the login page again

def logout_user(request):  
    logout(request)  
    messages.success(request,("You Were Logged Out!"))
    return redirect('home') 

# Create login,logout,register views here.
