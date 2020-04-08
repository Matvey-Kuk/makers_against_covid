from django.forms import ModelForm

from .models import TicketUpdate


class ProduceTicketUpdateForm(ModelForm):

    class Meta:
        model = TicketUpdate
        fields = ['comment']


class ProduceTicketUpdateAuthorForm(ModelForm):

    class Meta:
        model = TicketUpdate
        fields = ['comment', 'type']
