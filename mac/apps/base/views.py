from django.contrib import messages
from django.db.models import Sum

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView


import account.views
import account.forms
import account.views

from apps.orders.models import Ticket, PRODUCTS
from .forms import SignupForm, SettingsForm


# @method_decorator(cache_page(60 * 5), name='dispatch')
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        requests_statistics = []
        produce_statistics = []

        # Just a POC, not prod-ready:

        for product_type in PRODUCTS:
            requests_statistics.append(
                {
                    "id": product_type.id,
                    "name_ru": product_type.name_ru,
                    "requests": Ticket.objects.filter(type=Ticket.TYPE_REQUEST, product=product_type.id).count(),
                    "items": Ticket.objects.filter(type=Ticket.TYPE_REQUEST, product=product_type.id).aggregate(Sum('amount'))['amount__sum'],
                }
            )
            produce_statistics.append(
                {
                    "id": product_type.id,
                    "name_ru": product_type.name_ru,
                    "requests": Ticket.objects.filter(type=Ticket.TYPE_PRODUCE, product=product_type.id).count(),
                    "items": Ticket.objects.filter(type=Ticket.TYPE_PRODUCE, product=product_type.id).aggregate(Sum('amount'))['amount__sum'],
                }
            )

        context['requests_statistics'] = requests_statistics
        context['produce_statistics'] = produce_statistics

        return context


class LoginView(account.views.LoginView):
    form_class = account.forms.LoginEmailForm


class SignupView(account.views.SignupView):
    form_class = SignupForm
    identifier_field = 'email'

    def generate_username(self, form):
        username = form.data['email']
        return username


class SettingsView(account.views.LoginRequiredMixin, UpdateView):
    form_class = SettingsForm
    template_name = "account_settings.html"
    success_url = reverse_lazy('account_settings')

    def form_valid(self, form):
        messages.success(self.request, "Профиль обновлен!")
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user
