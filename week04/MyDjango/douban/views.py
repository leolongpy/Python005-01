import json

from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .models import Douban


def index(request):
    where = {}
    if 'page' in request.GET and request.GET['page']:
        page = request.GET['page']
    else:
        page = 1
    if 'q' in request.GET and request.GET['q']:
        where.update(film_content__contains=request.GET['q'])
    offsit = (int(page) - 1) * 20
    pagesize = 20 + offsit
    ret = {
        'code': 1,
        'msg': '获取成功'
    }
    contents = Douban.objects.filter(**where).all()[offsit:pagesize]
    data = []
    for i in contents:
        tmp = {}
        tmp['content'] = i.film_content
        tmp['star'] = i.film_star
        data.append(tmp)
    ret['data'] = data
    return HttpResponse(json.dumps(ret, ensure_ascii=False))

# 原生sql
def index2(request):
    where = " 1=1 "
    if 'page' in request.GET and request.GET['page']:
        page = request.GET['page']
    else:
        page = 1
    if 'q' in request.GET and request.GET['q']:
        where += f" and film_content like %{request.GET['q']}% "
    offsit = (int(page) - 1) * 20
    pagesize = 20
    ret = {
        'code': 1,
        'msg': '获取成功'
    }
    with connection.cursor() as cursor:
        cursor.execute("select * from douban where %s limit %s,%s", [where, offsit, pagesize])
        col_names = [desc[0] for desc in cursor.description]
        contents = cursor.fetchall()
    data = []
    for list in contents:
        tMap = dict(zip(col_names, list))
        data.append(tMap)

    ret['data'] = data
    return HttpResponse(json.dumps(ret, ensure_ascii=False))
