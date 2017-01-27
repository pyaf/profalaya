from django.shortcuts import render, HttpResponse, Http404
import json

# Create your views here.

def index(request):
    template_name = 'index.html'
    context = {}

    return render(request, template_name, context)

def search_query(request):
    response_data = {}
    if request.method == "POST":
        query = request.POST['search_query']
        response_data['search_query'] = query



        response_data['status'] = "success"
        return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
            )

    else:
        return HttpResponse("NOT Allowed!")
