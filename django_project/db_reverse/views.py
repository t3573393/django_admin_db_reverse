#coding:utf8

from django.shortcuts import render

# Create your views here.
from .dbpool import dbpool
from MySQLdb.cursors import DictCursor
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.static import serve
import os
from django_project.settings import BASE_DIR
from db_reverse.codegen import main

def index(request):
    context = {}
    return render(request, 'db_reverse/index.html', context)


def save_db_info(request):
    ip = request.POST['ip']
    port = int(request.POST['port'])
    data_base = request.POST['data_base']
    user = request.POST['user']
    passwd = request.POST['passwd']
    request.session['db_info'] = {
        'ip': ip,
        'port': port,
        'data_base': data_base
    }
    db_config = {
        "host": ip,
        "user": user,
        "passwd": passwd,
        "port": port,
        "charset": "utf8mb4",
        "maxconnections": 5,
        "maxcached": 5,
        "blocking": 1
    }
    if data_base:
        db_config['db'] = data_base
    dbpool.initPool(db_config)
    context = {}
    return HttpResponseRedirect(reverse('db_reverse:table_list'))


def table_list(request):
    conn = dbpool.connection()
    sqlstr = '''
    SELECT
        TABLE_SCHEMA, TABLE_NAME, TABLE_TYPE
    FROM
        information_schema.TABLES
    WHERE
        TABLE_SCHEMA = DATABASE()
            and Table_type = 'BASE TABLE'
    '''
    cursor = conn.cursor(cursorclass=DictCursor)
    cursor.execute(sqlstr)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    context = {
        'table_list': result
    }
    return render(request, 'db_reverse/db_schema.html', context)


def generate_code(request):
    main.generate_file()
    root_folder = BASE_DIR
    filepath = '%s/result.zip' % root_folder
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))