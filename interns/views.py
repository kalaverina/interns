from django.http import HttpResponse, HttpResponseRedirect
from faker import Faker
from django.db import models
import interns.models as models
import interns.forms as forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def account(request):
    p = 1
    context = {'values': models.User.objects.filter(id=p).values(),
               'payments': models.Payment.objects.filter(user=p).values()}
    return render(request, 'interns/account.html', context)


def edit_account(request):
    initial_data = fake_date()
    context = {}
    user = forms.UserForm(initial=initial_data)
    if user.is_valid():
        user.save()

    context['user'] = user
    #context['fields'] =
    #for field in forms.UserForm.get_field_names():
        #print(field)
    # obj = Class.objects.get(pk=this_object_id)
    return render(request, "interns/edit_account.html", context)


def fake_date():
    fake = Faker()
    '''
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
   = models.IntegerField()
    e_mail = models.EmailField(max_length=50)
    city = models.CharField(max_length=5)
    telegram_nickname = models.CharField(max_length=5)
    youtrack_login = models.CharField(max_length=5)
    edu_lvl = models.CharField(max_length=5)
    edu_institut = models.CharField(max_length=5)
    edu_spec = models.CharField(max_length=5)
    resume_title = models.CharField(max_length=5)
    cover_letter_text = models.CharField(max_length=5)
    skills = models.CharField(max_length=5)
    skills_detailed = models.CharField(max_length=5)
    role = models.CharField(max_length=5)
    '''
    return {
        'user_name': 'Student1',
        'last_name': 'ln',
        'phone': int(fake.country_calling_code() + str(fake.random_number(digits=7))),
    }


def payments(request):
    user_payment = forms.PaymentsForm(request.POST or None)
    context = {'payment': user_payment}
    payment_list = models.Payment.objects.all().values()
    context['payment_list'] = payment_list
    if user_payment.is_valid():
        user_payment.save()
    return render(request, 'interns/payments.html', context)


def authorization(request):
        if request.user.is_authenticated:
            return redirect('/')

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if username == 'admin':
                    return redirect('/admin')
                login(request, user)
                return redirect('/')
            else:
                form = AuthenticationForm()
                return render(request, 'interns/authorization.html', {'form': form})

        else:
            form = AuthenticationForm()
            return render(request, 'interns/authorization.html', {'form': form})