from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import *
from Image.models import Image
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, message
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from .utils import generate_token
from django.http import HttpResponse


def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        email = request.POST['email']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('/accounts/sign-up')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'E-mail already exists')
                return redirect('/accounts/sign-up')
            elif first_name.isalpha() == False:
                messages.info(request, 'Name should be letters only')
                return redirect('/accounts/sign-up')
            elif last_name.isalpha() == False:
                messages.info(request, 'Name should be letters only')
                return redirect('/accounts/sign-up')
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.is_active = False
                user.save()

                email_subject = "Account Activation Link"

                email_body = render_to_string('activate.html', {
                    'user': user,
                    'domain': get_current_site(request),
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': generate_token.make_token(user),
                })
                email = EmailMessage(
                    email_subject,
                    email_body,
                    'noreply@semycolon.com',
                    [email],
                )
                email.send(fail_silently=False)
                messages.info(
                    request, 'E-mail Verification link has been sent to your e-mail')
                return redirect('/accounts/sign-in')
        else:
            messages.info(request, 'Password not matching')
            return redirect('/accounts/sign-up')
    else:
        return render(request, 'sign up.html')


def activate_user(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and generate_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email verfication. Now you can login your account.')
    else:
        return HttpResponse('Something went wrong :(')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(
                request, 'Invalid Credentials / E-mail Unverified :(')
            return redirect('/accounts/sign-in')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required(login_url='/sign-in')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            return redirect('/accounts/profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        images = Image.objects.filter(user=request.user)

    return render(request, 'profile.html', {'u_form': u_form, 'p_form': p_form, 'images': images})


def viewprofile(request, user):
    images = Image.objects.filter(user=user)
    info = User.objects.filter(id=user)
    return render(request, 'view profile.html', {'images': images, 'info': info})


def about(request):
    return render(request, 'about.html')
