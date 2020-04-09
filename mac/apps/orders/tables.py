import django_tables2 as tables
from .models import PRODUCTS, Ticket
from django_tables2.utils import A

class RequestTicketTable(tables.Table):
    link = tables.LinkColumn(viewname="request_ticket", text="Подробнее", args=[A("pk")])

    class Meta:
        model = Ticket
        template_name = "django_tables2/bootstrap4.html"
        fields = ("created_at", "product", "city_cached", "amount", "link")