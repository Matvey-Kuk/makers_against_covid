from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic import TemplateView, CreateView, DetailView, FormView
from django_filters.views import FilterView

from account.mixins import LoginRequiredMixin

from .filters import TicketFilter, RequestTicketFilter
from .models import PRODUCTS, Ticket, TicketUpdate
from .forms import ProduceTicketUpdateForm, ProduceTicketUpdateAuthorForm


class ProductListView(TemplateView):
    template_name = "product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = PRODUCTS
        return context


class ProductView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = next(item for item in PRODUCTS if item.id == self.kwargs['id'])
        return context

    def get_template_names(self):
        return f"products/{self.kwargs['id']}.html"


class ProduceTicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = "produce_ticket_create.html"
    fields = [
        'product',
        'amount',
        'logistics',
        'comment',
    ]
    success_url = reverse_lazy('produce_ticket_create')

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        form.instance.type = Ticket.TYPE_PRODUCE
        messages.success(self.request, "Тикет создан!")
        data = super(ProduceTicketCreateView, self).form_valid(form)
        form.instance.update_cached_properties()
        return data


class RequestTicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = "request_ticket_create.html"
    fields = [
        'product',
        'amount',
        'comment',
    ]
    success_url = reverse_lazy('request_ticket_create')

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        form.instance.type = Ticket.TYPE_REQUEST
        messages.success(self.request, "Тикет создан!")
        data = super().form_valid(form)
        form.instance.update_cached_properties()
        return data


class ProduceTicketList(FilterView):
    model = Ticket
    template_name = "produce_ticket_list.html"
    filterset_class = TicketFilter

    def get_queryset(self):
        return super().get_queryset().filter(type=Ticket.TYPE_PRODUCE)


class RequestTicketList(FilterView):
    model = Ticket
    template_name = "request_ticket_list.html"
    filterset_class = RequestTicketFilter

    def get_queryset(self):
        return super().get_queryset().filter(type=Ticket.TYPE_REQUEST)


class ProduceTicketView(DetailView, FormView):
    model = Ticket
    template_name = "produce_ticket.html"

    def get_form_class(self):
        if self.request.user == self.get_object().author:
            return ProduceTicketUpdateAuthorForm
        else:
            return ProduceTicketUpdateForm

    def get_success_url(self, **kwargs):
        return reverse("produce_ticket", kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        # form.instance.type = TicketUpdate.TYPE_COMMENT
        form.instance.target_ticket = self.get_object()
        form.instance.save()
        form.instance.target_ticket.update_cached_properties()
        messages.success(self.request, "Комментарий создан!")
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        return FormView.post(self, request, *args, **kwargs)


class RequestTicketView(DetailView, FormView):
    model = Ticket
    template_name = "request_ticket.html"

    def get_form_class(self):
        return ProduceTicketUpdateForm

    def get_success_url(self, **kwargs):
        return reverse("request_ticket", kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        # form.instance.type = 'comment'
        form.instance.target_ticket = self.get_object()
        messages.success(self.request, "Комментарий создан!")
        form.instance.save()
        form.instance.target_ticket.update_cached_properties()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        return FormView.post(self, request, *args, **kwargs)
