from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.models import User
from .models import Profile


# Create your views here.



def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return render(request, 'accounts/account_details.html', { 'form': form })
                user.profile.completed_form = True

            else:
                if user.profile.completed_form :
                    return render(request, 'accounts/account_details.html', { 'form': form })
                else :
                    return redirect ('home')
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


@login_required(login_url="/accounts/login/")
def customer_info_view(request, *args, **kwargs):
        print(args, kwargs)
        print(request.user)
        return render(request, 'accounts/customerInfo.html', {})

@login_required(login_url="/accounts/login/")
def customer_orders_view(request, *args, **kwargs):
        print(args, kwargs)
        print(request.user)
        return render(request, 'accounts/customerOrders.html', {})

# @login_required(login_url="/accounts/login/")
# def account_details_view(request, *args, **kwargs):
#     if request.method == 'POST':
#         form = forms.Profiles(request.POST, request.FILES)
#         user = form.get_user()
#         print(user)
        # return HttpResponse("<h1>Hello1</h>")
        # if account.is_valid():
            # log the user in
        # if User.profile.completed_form :
    #     account.save()
    #     return redirect ('home')
    # else:
    #     account = forms.Profiles(request.POST, request.FILES)
    #     return render(request, 'accounts/account_details.html', { 'account': account })
    # if account.logout():
    #     return redirect ('accounts/logout.html')

# @api_view(["POST"])
@login_required(login_url="/accounts/login/")
def account_details_view(request, *args, **kwargs):
    if request.method == 'POST':
         account = forms.Profiles(request.POST, instance=request.user.profile)
         if account.is_valid():
            user = Profile.user
            profile = account.save(commit=False)
            # user = profile.create_user_profile(sender, instance, created, raw, **kwarg)
            user.profile.Name = account.cleaned_data['Name']
            user.profile.lastname = account.cleaned_data['lastname']
            user.profile.account_type = account.cleaned_data['account_type']
            if user.profile.completed_form == True:
                profile.save()
                user.save()
                #  log the user in
            return redirect('home')
    else:
        account = forms.Profiles(request.POST)
        return render(request, 'accounts/account_details.html', { 'account': account })



# @login_required(login_url="/accounts/login/")
# def account_details_view(request):
#     if request.method == 'POST':
#         account = forms.Profiles(request.POST)
#         if account.is_valid():
#             account.save()
#             return redirect('home')
#     else:
#         account = forms.Profiles(request.POST)
#     return render(request, 'accounts/account_details.html', { 'account': account })


# def account_detail(request, slug):
#     # return HttpResponse(slug)
#     account = account.objects.get(cin=cin)
#     return render(request, 'accounts/account_details.html', { 'account': account })
