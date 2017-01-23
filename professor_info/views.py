from django.shortcuts import render, HttpResponse, Http404

# Create your views here.

def index(request):
    template_name = 'index.html'
    context = {}

    return render(request, template_name, context)

def search_query(request):
    if request.method == "POST":
        pass
    else:
        return HttpResponse("NOT Allowed!")
