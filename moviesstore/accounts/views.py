from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomErrorList
from django.contrib.auth import logout as auth_logout


# Sign Up view
def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'

    if request.method == 'GET':
        # Display the sign-up form when the request method is GET
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'template_data': template_data})

    elif request.method == 'POST':
        # Handle form submission
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)

        if form.is_valid():
            # Save the user and log them in
            user = form.save()  # Save will automatically store the email field
            auth_login(request, user)  # Log the user in
            return redirect('home.index')  # Redirect to a page after successful sign-up
        else:
            # If the form is not valid, re-render the sign-up page with errors
            template_data['form'] = form
            return render(request, 'accounts/signup.html', {'template_data': template_data})


# Logout view
@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')


# Login view
def login(request):
    template_data = {}
    template_data['title'] = 'Login'

    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'template_data': template_data})

    elif request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html', {'template_data': template_data})
        else:
            auth_login(request, user)
            return redirect('home.index')


# Orders view (for authenticated users)
@login_required
def orders(request):
    template_data = {}
    template_data['title'] = 'Orders'
    template_data['orders'] = request.user.order_set.all()  # Get all orders for the logged-in user
    return render(request, 'accounts/orders.html', {'template_data': template_data})
