from django.db import models
import interns.models as models
import interns.forms as forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def account(request):
    user = forms.PaymentsForm(request.POST or None)
    if user.is_valid():
        user.save()
    if 'edit' in request.POST:
        return redirect('/edit_account/')
    if 'logout' in request.POST:
        logout(request)
        return redirect('/authorization/')
    else:
        user_info = models.User.objects.get(pk=1)
        user_fields = models.User().get_field_names()
        #res = dict(map(lambda i, j: (i, j), user_fields.get_field_names, user_info))
        context = {'values': user_info,
                   'payments': models.Payment.objects.filter(user=1).values()}
    return render(request, 'interns/account.html', context)


def edit_account(request):
    context = {}
    models.User.objects.get(pk=1)
    user = forms.UserForm()
    if user.is_valid():
        user.save()

    context['user'] = user
    return render(request, "interns/edit_account.html", context)


def payments(request):
    user_payment = forms.PaymentsForm(request.POST or None)
    context = {'payment': user_payment}
    payment_list = models.Payment.objects.all().values()
    context['payment_list'] = payment_list
    if user_payment.is_valid():
        user_payment.save()
    return render(request, 'interns/payments.html', context)


def authorization(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if request.user.is_authenticated:
            return redirect('/account')

        if user is not None:
            if username == 'admin':
                return redirect('/admin')
            login(request, user)
            return redirect('/account')
        else:
            form = AuthenticationForm()
            return render(request, 'interns/authorization.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'interns/authorization.html', {'form': form})
