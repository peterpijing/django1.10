#coding=utf-8
from django.shortcuts import render

from django.db.models import Q
from django.shortcuts import render_to_response
from models import Book

from forms import ContactForm
#1.发送邮件
from django.core.mail import send_mail
#2.重定向
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.template import RequestContext



def search(request):
    #1。寻找名为q的get参数
    query = request.GET.get('q','')
    #2。icontains ＝＝LIKIE
    if query:
        qset = (
            Q(title__icontains=query) |
            Q(authors__first_name__icontains=query) |
            Q(authors__last_name__icontains=query)
        )
        #3.distinct过滤查询结果，消除重复部分
        results = Book.objects.filter(qset).distinct()
    else:
        results = []

    return render_to_response("search.html",{
        "results":results,
        "query":query,
    })

def contact(request):
    #校验
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.clean_dataed.get('sender','123@qq.com')
            send_mail(
                'your site topic:%s ' % topic,
                message,sender,
                ['administrator@qq.com']

            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact.html',{'form':form},RequestContext(request))

def my_image(request):
    image_data = open("static/2.png","rb").read()
    return HttpResponse(image_data,mimetype="image/png")

