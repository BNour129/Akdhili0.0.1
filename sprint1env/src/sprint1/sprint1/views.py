from django.shortcuts import render

def homepage_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, 'home.html')
