from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        #print("inside if")
        #form= UserCreationForm(request.POST)
        form= UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            #print("accpount created")
            messages.success(request,'your account has been created and now u can login!')
            return redirect ('login')
    else:
        #print("inside else")
        #form=UserCreationForm()
        form= UserRegisterationForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,#to get the user data
        request.FILES,#to get the image files
        instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'your account has been updated!')
            return redirect ('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    
    context={
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'users/profile.html',context)

