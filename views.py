from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from datetime import datetime

from django.http import JsonResponse
import json
from django.core.serializers import serialize

import hashlib

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Question, Phone, User

@method_decorator(csrf_exempt, name="dispatch")

# Create your views here.

@method_decorator(csrf_exempt, name="dispatch")
def index(request):
  template = loader.get_template("hello/hello.html")
  context = {
      "time": datetime.today().ctime()
  }

  return HttpResponse(template.render(context, request))

@method_decorator(csrf_exempt, name="dispatch")
def index2(request):
    template = loader.get_template("hello/hello2.html")
    context = {

    }

    return HttpResponse(template.render(context, request))


def kirim(request):
    template = loader.get_template("hello/hello2.html")
    context = {
        "time": datetime.today().ctime(),
        "name": request.POST["txtNama"]
    }

    return HttpResponse(template.render(context, request))

def hello(request):
    items = Question.objects.order_by('-pub_date')[:5]
    output = ", ".join([item.question_text for item in items ])

    return HttpResponse(output)

def detail(request, question_id):
    q = Question.objects.get(pk=question_id)
    template = loader.get_template("hello/detail.html")
    context = {
        "question": q
    }

    return HttpResponse(template.render(context, request))


# =========================================================
# Phone - begin
# =========================================================

def phone_login(request):

    template = loader.get_template("hello/login.html")

    if request.method == 'POST':
        username = 'username' in request.POST
        password = 'password' in request.POST

        if username == True and password == True:
            username = request.POST['username']
            password = request.POST['password']

            if username == "" or password == "":
                context = {
                    "pesan": "You must type in your username AND password",
                }

                return HttpResponse(template.render(context, request))
            else:

                salted_password = '123' + password + '123'
                salted_password = hashlib.md5(salted_password.encode('utf-8')).hexdigest()

                test = User.objects.filter(
                    username__exact=username,
                    password__exact=salted_password
                )

                if len(test) == 0:
                    context = {
                        "username": username,
                        "password": password,
                        "md5_password": salted_password,
                        "status": "Not ok",
                        "pesan": "Username dan password tidak cocok",
                        "exception": ""
                    }

                    return HttpResponse(template.render(context, request))
                else:
                    return HttpResponseRedirect('/hello/list/')


        else:
            context = {
                "pesan": "This is an invalid request",
            }

            return HttpResponse(template.render(context, request))

    else:
        context = {
            "status": "ok"
        }

        return HttpResponse(template.render(context, request))

def phone_list(request):
    template = loader.get_template('hello/list.html')

    phones = Phone.objects.filter(is_delete__exact=0).order_by('name')

    context = {
        "status": "ok",
        "phones": phones
    }

    return HttpResponse(template.render(context, request))

def phone_add(request):

    new = {
        'name': request.POST['nama'],
        'address': request.POST['alamat'],
        'phone': request.POST['telepon'],
        'hobby': request.POST['hobby'],
        'dob': request.POST['dob'],
        'create_time': datetime.today().ctime(),
        'is_delete': False
    }

    phone = Phone.objects.create(**new)

    response = {
        'pesan': 'Record phone berhasil dibuat.'
    }

    return JsonResponse(response, status=201)

@method_decorator(csrf_exempt, name="dispatch")
def phone_delete(request):
    id = request.POST['id']

    phone = Phone.objects.get(pk=id)

    phone.is_delete = 1
    phone.save()

    response = {
        "status": "Ok. Record telah dihapus."
    }

    return JsonResponse(response, status=201)

def phone_get(request):
    id = request.GET['id']

    phone = Phone.objects.get(pk=id)

    response = {
        'id': phone.id,
        'name': phone.name,
        'address': phone.address,
        'phone': phone.phone,
        'hobby': phone.hobby,
        'dob': phone.dob,
    }

    return JsonResponse(response, status=201)

def phone_update(request):

    id = request.POST['id']
    phone = Phone.objects.get(pk=id)

    phone.name = request.POST['name']
    phone.address = request.POST['address']
    phone.phone = request.POST['phone']
    phone.hobby = request.POST['hobby']
    phone.dob = request.POST['dob']
    phone.save()

    response = {
        'status': 'Ok'
    }

    return JsonResponse(response, status=201)


# Menerima JSON untuk membuat record Phone baru
@method_decorator(csrf_exempt, name="dispatch")
def api_phone_add(request):
    payload = json.loads(request.body.decode('utf-8'))

    new = {
        'name': payload.get('name'),
        'address': payload.get('address'),
        'hobby': payload.get('hobby'),
        'phone': payload.get('phone'),
        'dob': payload.get('dob'),
        'create_time': datetime.today().ctime(),
        'is_delete': 0
    }

    phone = Phone.objects.create(**new)

    response = {
        'pesan': f"Record phone baru telah dibuat dengan id = {phone.id}."
    }

    return JsonResponse(response, status=201)

@method_decorator(csrf_exempt, name="dispatch")
def api_phone_update(request):

    payload = json.loads(request.body.decode("utf-8"))

    try:

        phone = Phone.objects.get(pk = payload.get('id'))

        phone.name = payload.get('name')
        phone.address = payload.get('address')
        phone.phone = payload.get('phone')
        phone.hobby = payload.get('hobby')
        phone.dob = payload.get('dob')
        phone.save()

        temp = {
            'name': phone.name,
            'address': phone.address,
            'phone': phone.phone,
            'hobby': phone.hobby,
        }

        response = {
            'pesan': f"Record phone telah diupdate menjadi : {temp}"
        }

        return JsonResponse(response, status=201)

    except:
        response = {
            'pesan': f"Record phone dengan id '{payload.get('id')}' tidak ditemukan."
        }

        return JsonResponse(response, status=201)

@method_decorator(csrf_exempt, name="dispatch")
def api_phone_get(request):
    payload = json.loads(request.body.decode('utf-8'))

    try:
        phone = Phone.objects.get(pk = payload.get('id'))

        temp = {
            'id': phone.id,
            'name': phone.name,
            'address': phone.address,
            'phone': phone.phone,
            'dob': phone.dob,
            'hobby': phone.hobby,
        }

        response = {
            'pesan': f"Record phone adalah {temp}",
            'record': temp
        }

        return JsonResponse(response, status=201)
    except:
        response = {
            'pesan': f"Record phone dengan id '{payload.get('id')}' tidak ditemukan."
        }

        return JsonResponse(response, status=201)

@method_decorator(csrf_exempt, name="dispatch")
def api_phone_delete(request):

    payload = json.loads(request.body.decode("utf-8"))

    phone = Phone.objects.get(pk = payload.get('id'))

    phone.is_delete = 1
    phone.save()

    temp = {
        'id': phone.id
    }

    response = {
        'pesan': f"Record phone telah dihapus : {temp}"
    }

    return JsonResponse(response, status=201)

@method_decorator(csrf_exempt, name="dispatch")
def api_phone_list(request):

    try:
        phones = Phone.objects.filter(is_delete__exact=0).order_by('name')

        records = []
        for item in phones:

            records.append(
            {
                "id": item.id,
                "name": item.name
            })

        response = {
            "status": "ok",
            "records": records
        }

        return JsonResponse(response, status=201)
    except Exception as e:
        response = {
            'status': 'Not ok',
            'pesan': "{}".format(e)
        }

        return JsonResponse(response, status=201)

# =========================================================
# Phone - end
# =========================================================
