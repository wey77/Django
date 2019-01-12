# \1. 使用类视图扩展类实现下面需求
#
# \1. 定义基类ListModelMixin,实现list方法，在方法中返回任意字符串的HTTP响应对象
#
# \2. 定义基类CreateModelMixin,实现create方法，在方法中返回任意字符串的HTTP响应对象
#
# \3. 定义类视图BookView继承上面2个基类，在类视图中实现get、post方法分别返回list和create方法中的的响应体对象
from django.http import HttpResponse
from django.views import View


class ListModelMixin(object):
    def get_list(self, request, *args, **kwargs):
        return HttpResponse("ListModelMixin")


class CreateModelMixin(object):
    def get_create(self, request, *args, **kwargs):
        return HttpResponse("CreateModelMixin")


class BookView(View, ListModelMixin, CreateModelMixin):
    def get(self, request):
        return self.get_list(request)

    def post(self, request):
        return self.get_create(request)