def my_middleware(get_response):
    print('my_middleware中间件初始化')
    def inners(request, *args, **kwargs):
        print("中间件在视图进入前")
        response = get_response(request, *args, **kwargs)
        print("中间件在视图处理后")
        return response
    return inners