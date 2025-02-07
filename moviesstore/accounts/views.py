from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = UserCreationForm()
        return render(request, 'accounts/signup.html',
            {'template_data': template_data})
