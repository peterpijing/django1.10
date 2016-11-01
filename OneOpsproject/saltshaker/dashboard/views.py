#coding=utf-8
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from models import *
import logging


logger = logging.getLogger('django')
@login_required
def index(request):
    try:
        dashboard_status = Dashboard_status.objects.get(id=1)
    except:
        status_list = [0, 0, 0, 0, 0]
    else:
        status_list = [int(dashboard_status.up),
                   int(dashboard_status.down),
                   int(dashboard_status.accepted),
                   int(dashboard_status.unaccepted),
                   int(dashboard_status.rejected),
                   ]
        logger.info(status_list)

    return render(request,'dashboard/index.html',{'status': status_list})