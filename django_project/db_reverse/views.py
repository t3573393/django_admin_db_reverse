from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'db_reverse/index.html', context)


def save_db_info(request):
    ip = request.POST['ip']
    port = request.POST['port']
    data_base = request.POST['data_base']
    request.session['db_info'] = {
        'ip': ip,
        'port': port,
        'data_base': data_base
    }
    context = {}
    return render(request, 'db_reverse/db_schema.html', context)