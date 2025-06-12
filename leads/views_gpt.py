from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
)
from .models import Lead, Agent
from .forms import LeadModelForm, AssignAgentForm


class LeadListView(LoginRequiredMixin, ListView):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            return Lead.objects.filter(organisation=user.userprofile, agent__isnull=False)
        else:
            return Lead.objects.filter(organisation=user.agent.organisation, agent__user=user)


class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/lead_detail.html"
    context_object_name = "lead"

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            return Lead.objects.filter(organisation=user.userprofile)
        else:
            return Lead.objects.filter(organisation=user.agent.organisation, agent__user=user)


class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    success_url = reverse_lazy("leads:lead-list")

    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.organisation = self.request.user.userprofile
        lead.save()
        messages.success(self.request, "Lead created successfully")

        if lead.agent:
            try:
                send_mail(
                    subject="A lead has been created",
                    message="Go to the site to see the new lead",
                    from_email=None,
                    recipient_list=[lead.agent.user.email],
                )
            except Exception as e:
                messages.warning(self.request, f"Failed to send email: {e}")

        return super().form_valid(form)


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    success_url = reverse_lazy("leads:lead-list")

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation=user.userprofile)


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "leads/lead_delete.html"
    success_url = reverse_lazy("leads:lead-list")

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation=user.userprofile)


class AssignAgentView(LoginRequiredMixin, FormView):
    template_name = "leads/assign_agent.html"
    form_class = AssignAgentForm
    success_url = reverse_lazy("leads:lead-list")

    def get_form_kwargs(self, **kwargs):
        kwargs = super().get_form_kwargs(**kwargs)
        kwargs.update({"request": self.request})
        return kwargs

    def form_valid(self, form):
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()
        messages.success(self.request, "Agent assigned successfully")
        return super().form_valid(form)