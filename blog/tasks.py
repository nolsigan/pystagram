from __future__ import absolute_import
from celery import shared_task
from .models import Blog
import urllib3
import certifi
import json
import pytz
from datetime import datetime


@shared_task
def test(param):
    return 'The test task executed with argument "%s" ' % param


@shared_task
def crawl_blogs():
    blogs = Blog.objects.all()
    for blog in blogs:
        # TODO : send get call to api and retrieve last date
        # if last date > current date -> update field
        http = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where()
        )
        api_url = blog.get_api_url()
        print('crawling : ' + api_url[1])
        if api_url[0]:
            r = http.request('GET', api_url[1], headers={'User-Agent': 'Mozilla/5.0'})
            obj = json.loads(r.data.decode('utf-8'))
            dt = datetime.strptime(obj['pushed_at'], '%Y-%m-%dT%H:%M:%SZ')
            if dt > blog.pushed_at.replace(tzinfo=None):
                print('Have to update pushed_at!')
                blog.pushed_at = dt.replace(tzinfo=pytz.UTC)
                blog.save()
            else:
                print('Do not need update')

    return 'crawl_blogs has blogs "%d" ' % blogs.__len__()
