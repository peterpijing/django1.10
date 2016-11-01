#coding=utf-8
# from django.http import HttpResponse
#
# from django.template import Context
#
# from django.shortcuts import render_to_response
#
# from django.shortcuts import render



from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader

from django.http import Http404
# from django.shortcuts import render

from django.shortcuts import get_object_or_404


import datetime

import datetime


def current_datetime(request):

    # html = "<html><body>it is now %s.</body></html>" % now
    # 1.通过模版名称。找出模版位置，返回一个编译好的template对象
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date':now}))
    # return HttpResponse(html)

    # 2
    current_date = datetime.datetime.now()
    #return render_to_response('current_datetime.html', locals())

    return render(request,'current_datetime.html',{'current_date':current_date})



def hours_ahead(request,offset):
    #offset参数是url中的参数－－－>/time/plus/2  offset=2
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>in %s hour(s) , it will be %s.</body></html>" % (offset,dt)
    return HttpResponse(html)
