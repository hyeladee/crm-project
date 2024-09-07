from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

# Create your views here.
def lead_list(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads,
    }
    return render(request, 'leads/lead_list.html', context)

    # return HttpResponse('Hello World')
    # context = {
    #     'name': 'Joe',
    #     'age': 35,
    # }


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        'lead': lead
    }
    return render(request, 'leads/lead_detail.html', context)
    
    # return HttpResponse('Here is the detail view')


def lead_create(request):
    # context = {}
    return render(request, 'leads/lead_create.html')#, context)