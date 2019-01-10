import json

from django.shortcuts import render
from django.http import HttpResponse


def demo_01(request):
    return HttpResponse('demo_01')


def get_loc_arg(request, year, addr):
    print(addr)
    print(year)
    return HttpResponse('get_loc_arg')


def get_quer_arg(request):
    print(request.GET.get('a'))
    print(request.GET.get('b'))
    print(request.GET.getlist('a'))
    return HttpResponse('get_quer_arg')


def get_req_body(request):
    params = request.POST
    print(params.get('a'))
    print(params.get('b'))
    print(params.getlist('a'))
    return HttpResponse('get_req_body')

def get_json_arg(request):
    json_bin = request.body
    json_str = json_bin.decode()
    json_dic = json.loads(json_str)
    print(json_dic)
    return HttpResponse('get_json_arg')


def get_header(request):
    # 获取请求头内容
    metas = request.META
    re_me = metas.get('REQUEST_METHOD')
    # 获取当前用户
    user = request.user
    print(user)
    # 获取当前请求方式
    me = request.method
    print(me)
    # 获取当前请求路径
    pa = request.path
    print(pa)
    # 获取当前请求编码
    en = request.encoding
    print(en)

    return HttpResponse("获取的请求头：%s" % re_me)