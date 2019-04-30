from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
@login_required(login_url="/accounts/login/")
def account_details_view(request, *args, **kwargs):
    # if request.method == 'POST':
    account = forms.AccountDetails(request.POST, request.FILES)
    if account.is_valid():
        # log the user in
        account.save()
        return redirect ('home')
    else:
        return render(request, 'accounts/account_details.html', { 'account': account })

    if account.logout():
        return redirect ('accounts/logout.html')

def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return render(request, 'accounts/account_details.html', { 'form': form })

            else:
                return redirect('accounts:details')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

@login_required(login_url="/accounts/login/")
def logout_view(request, *args, **kwargs):
    if request.method == 'POST':
        logout(request)
        return render(request, 'accounts/logout.html', {})


def signup_view(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             user = form.save()
             #  log the user in
             login(request, user)
             return redirect('accounts:details')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', { 'form': form })


# def account_detail(request, slug):
#     # return HttpResponse(slug)
#     account = account.objects.get(cin=cin)
#     return render(request, 'accounts/account_details.html', { 'account': account })
