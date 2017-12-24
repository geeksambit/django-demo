from django.shortcuts import render
from django.http import JsonResponse
#import blog.DBConnection 
import MySQLdb
from django.core import serializers
import simplejson as json
import collections

db = MySQLdb.connect(user='root', db='blog',  passwd='root', host='localhost')  

# Create your views here.
def HomePageView(request):
    throw = {
        'page_name':'Home page',
        'created':'now'
    }
    data = JsonResponse(throw)
    return data

#blog lists 
def Bloglists(request):
    throw = {
            'page_name':'Bloglist',
            'created':'now'
    }
    cursor = db.cursor()
    cursor.execute('SELECT * FROM blog_post')
    datas = cursor.fetchall()
    column = [t[0] for t in cursor.description]
    db.close()
    myJsons = []
    for data in datas:
        d = collections.OrderedDict()
        print(column[0])
        print(column[1])
        print(data[0])
        print(data[1])
        d[column[0]] = data[0]
        d[column[1]] = data[1]
        myJsons.append(d)
    return json.dumps(myJsons)
    #db.close()
    #json_data = serializers.serialize('json', data)
    #return HttpResponse(json_data, mimetype='application/json')
    #datas = JsonResponse(posts,safe=False)
    #return posts
    #json_data = json.dumps(datas)
    #return json_data

#single blog according to blog_id
def SingleBlog(request,blog_id):
    throw = {
            'page_name':'Single Blog',
            'created':'now',
            'blog_id':'123'
    }
    throw['blog_id'] = blog_id
    data = JsonResponse(throw)
    return data
