from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import EmployeeOnboardInfo
from onboardingapp.forms import EmployeeOnboardingForm, EmployeeInfoForm

# Create your views here.
def home(request):
    return render(request, 'onboardingapp/home.html')

def register(request):
    registered = False
    user = None
    if request.method == 'POST':
        userform = EmployeeOnboardingForm(data = request.POST)
        profileform = EmployeeInfoForm(request.POST, request.FILES)

        if userform.is_valid()  and profileform.is_valid() :
            user = userform.save()
            user.set_password(user.password)
            user.save()

            profile = profileform.save(commit=False)
            # Connecting our profile info and userinfo
            profile.employee = user

            if 'profile_img' in request.FILES:
                profile.profile_img  = request.FILES['profile_img']

            profile.save()

            registered = True

        else:
            print(userform.errors, profileform.errors)

    else:
        userform = EmployeeOnboardingForm()
        profileform = EmployeeInfoForm()

    return render(request, 'onboardingapp/register.html',
                    {
                        'userform' : userform,
                        'profileform' : profileform,
                        'registered' : registered,
                        'user_obj' : user
                    })


def preview(request, user_obj):
    user_instance =  get_object_or_404(User, id = user_obj)
    user = get_object_or_404(EmployeeOnboardInfo, employee = user_instance)
    return render(request, 'onboardingapp/preview.html',{'user':user,'instance':user_instance})