from django.shortcuts import render
from django.http import HttpResponseForbidden

# Create your views here.

def about_view(request, *args, **kwargs):
        print(request.user)
        print(request.user.is_authenticated) # is_authenticated()
        the_username = request.user
        is_logged_in = request.user.is_authenticated
        context = {
            "username": the_username,
            "logged_in": is_logged_in
        }
        return render(request, "about.html", context)

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def error_view(request, *args, **kwargs):
    return HttpResponseForbidden()
