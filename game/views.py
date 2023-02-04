from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">术士之战</h1>'
    line2 = '<img src="https://bkimg.cdn.bcebos.com/pic/c2cec3fdfc039245efdd58288f94a4c27d1e25a8?x-bce-process=image/resize,m_lfit,w_536,limit_1" width=800>'
    line3 = '<a href="/play/">进入游戏界面</a>'
    return HttpResponse(line1 + line3 + line2)


def play(request):
    line1 = '<h1 style="text-align: center">游戏界面</h1>'
    line2 = '<a href="/">返回主界面</a>'
    return HttpResponse(line1 + line2)
