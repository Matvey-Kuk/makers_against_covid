from .models import Ticket
import django_filters


class TicketFilter(django_filters.FilterSet):
    class Meta:
        model = Ticket
        fields = [
            'city_cached',
            'logistics',
            'product',
            'is_production_ready_cached',
            'is_production_delivered_cached',
        ]


class RequestTicketFilter(django_filters.FilterSet):
    class Meta:
        model = Ticket
        fields = [
            'city_cached',
            'product',
        ]
