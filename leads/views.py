from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm

# Create your views here.

# CLASS BASED VIEWS

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
        return reverse('login')

class LandingPageView(TemplateView):
    template_name = 'landing.html'

class LeadListView(LoginRequiredMixin, ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = 'leads'

class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = 'lead'

class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self) -> str:
        return reverse('leads:lead-list')
    
    def form_valid(self, form) -> HttpResponse:
        # TODO send email
        send_mail(
            subject='A Lead Has Been Crated',
            message='Go to the site to see the new lead',
            from_email='test@test.com',
            recipient_list=['test2@test.com'],
        )
        return super(LeadCreateView, self).form_valid(form)
   
class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self) -> str:
        return reverse('leads:lead-list')

class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()
    
    def get_success_url(self) -> str:
        return reverse('leads:lead-list')




# FUNCTION BASED VIEWS

def landing_page(request):
    return render(request, 'landing.html')
    

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
    form = LeadModelForm()
    if request.method == 'POST':
        # print('Receiving a POST request...')
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')

    context = {
        'form': form
    }
    return render(request, 'leads/lead_create.html', context)


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)

    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')

    context = {
        'form': form,
        'lead': lead
    }
    return render(request, 'leads/lead_update.html', context)


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)

#     form = LeadForm()
#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():            
#             data = form.cleaned_data

#             lead.first_name = data['first_name']
#             lead.last_name = data['last_name']
#             lead.age = data['age']

#             lead.save()
            
#             return redirect('/leads')

#     context = {
#         'form': form,
#         'lead': lead
#     }
#     return render(request, 'leads/lead_update.html', context)


# def lead_create(request):
    # form = LeadForm()
    # if request.method == 'POST':
    #     # print('Receiving a POST request...')
    #     form = LeadForm(request.POST)
    #     if form.is_valid():
    #         # print('The form is valid')

    #         data = form.cleaned_data

    #         first_name = data['first_name']
    #         last_name = data['last_name']
    #         age = data['age']
    #         agent = Agent.objects.first()

    #         Lead.objects.create(
    #             first_name=first_name,
    #             last_name=last_name,
    #             age=age,
    #             agent=agent,
    #         )
    #         # print('The lead has been created!')
    #         return redirect('/leads')

#     context = {
#         'form': form
#     }
#     return render(request, 'leads/lead_create.html', context)