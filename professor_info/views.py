from django.shortcuts import render, HttpResponse, Http404
from django.db.models import Q
import json
import os
from professor_info.models import *
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def index(request):
    template_name = 'index.html'
    context = {}

    return render(request, template_name, context)

def prof_search():
    #check if its professor's name
    profs= Professor.objects.filter(name__iexact=query)
    if profs:
        print("got exact match")
        print(profs)
    else:#didn't find exact match (case-insensitive), let's search query is as substring
        profs = Professor.objects.filter(name__icontains=query)
        if profs:
            print("got match containing query")
            print(profs)
        else:# not as substring, let's split and search
            print("didnt get exact or matching term")
            qset = Q()
            for term in query.split():
                qset |= Q(name__contains=term)
            print("qset", qset)
            profs = Professor.objects.filter(qset)
            if profs:
                print('got some profs')
                print(profs.count())
                # print(profs)
                for prof in profs:
                    print(prof)

def search_query(request):
    response_data = {}
    if request.method == "POST":
        query = request.POST['search_query'].strip()
        print('\n\nquery', query)
        #brute force check if there something in the query with same
        qset = Q()
        for term in query.split():
            qset |= Q(area_of_interest__icontains=term)
        profs = Professor.objects.filter(qset)
        # data = serializers.serialize("json", profs, fields=('name', 'area_of_interest'))
        data_count = profs.count()
        data = json.dumps([prof.as_dict() for prof in profs])
        print(data)

        response_data['result_count'] = data_count
        response_data['results'] = data
        response_data['status'] = "success"

        return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
            )

    else:
        return HttpResponse("NOT Allowed!")
