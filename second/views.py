from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, reverse
from django.utils.decorators import method_decorator
from django.template import loader
from django.shortcuts import render

# 响应对象可给 数据内容  数据格式  状态码
from django.views.generic.base import View


def test_resp(request):
    response = HttpResponse(content='test_resp', content_type='text/pain', status=200)
    return response

# 可以在响应对象中添加自定义响应头 响应状态码可通过属性status_code设置
def test_resp1(request):
    resp = HttpResponse(content='test_resp1')
    resp.status_code = 900
    resp['MY-HEADER'] = '12345'
    return resp

# 使用HttpResponse子类，响应json数据，如果是列表数据，需要给safe参数给值False
def test_jsonresp(request):
    return JsonResponse([{"name": "小明", "age": 19},
                         {"name": "小明", "age": 19}], safe=False)

# 重定向 可以直接重定向到路径 注意：路径应该由/开头 否则是在当前路径下重定向 也就是两个url叠加
# 配合反向解析reverse 可传入试图函数名、路由名、命名空间名：路由名
def test_redirect(request):
    return redirect(reverse('second:test_jsonresp'))

def test_cookie1(request):
    resp = HttpResponse('1')
    resp.set_cookie('1','2',max_age=180)
    return resp

def get_cookie(request):
    re = request.COOKIES.get('1')
    print(re)
    return HttpResponse('123')

def test_session1(request):
    request.session['name'] = '大锤'
    request.session['age'] = '12'
    # print(request.session['key'])
    # request.session['key'].clear()
    # request.session[]
    return HttpResponse('1')

def test_session2(request):
    # request.session['name'] = '大亚'
    # request.session['age'] = '92'
    # print(request.session['key'])
    # request.session.clear() 删除request对应的所有值
    request.session.flush() # 删除request对应的所有值和键
    # del request.session['name'] # 删除特定的key对应的值 key也删除
    # request.session.set_expiry() # 设置request对应的过期时长
    print(request.session['name'])
    print(request.session['age'])
    return HttpResponse('2')


# 装饰器
def outers(func):
    def inners(request, *args, **kwargs):
        print("装饰前")
        f = func(request, *args, **kwargs)
        print("装饰后")
        return f
    return inners

# 视图类
# @method_decorator(outers, name='get')
class Class_View(View):
    @method_decorator(outers)
    def get(self, request):
        print('get 请求')
        return HttpResponse("get 方式")

    def post(self, request):
        print('post 请求')
        return HttpResponse('post 方式')


def render_templates(request):
    template = loader.get_template('index.html')
    content = {
        "title": "模板",
        "body": ['b1', 'b2', 'b3'],
        "foot": {
            "name": "大锤",
            "age": 17,
            "gender": ['b1', 'b2', 'b3']
        }
    }
    return HttpResponse(template.render(content))


# def render_templates(request):
#     # template = loader.get_template('index.html')
#     content = {
#         "title": "模板",
#         "body": "身体"
#     }
#     return render(request, 'index.html', content)


