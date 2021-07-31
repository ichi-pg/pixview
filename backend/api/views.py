from django.shortcuts import render
from django.http import HttpResponse
from pixivpy3 import PixivAPI

# Create your views here.

def favorites(req):
    api = PixivAPI()
    api.login(req.POST.get('user'), req.POST.get('password'))
    # TODO ログイン方法がリフレッシュトークンに変わったので、対応が必要
    res = api.me_favorite_works(req.POST.get('page', 1))
    return HttpResponse(res, content_type='application/json; charset=UTF-8')
