import django_tables2 as tables
from .models import PRODUCTS, Ticket
from django_tables2.utils import A

class RequestTicketTable(tables.Table):
    link = tables.LinkColumn(viewname="request_ticket", text="Подробнее", args=[A("pk")])
    created_at = tables.DateTimeColumn(accessor='created_at', format='Y-m-d H:i', verbose_name="Дата создания")
    class Meta:
        model = Ticket
        template_name = "django_tables2/bootstrap4.html"
        fields = ("created_at", "product", "logistics", "city_cached", "amount", "link")

class ProduceTicketTable(tables.Table):
    link = tables.LinkColumn(viewname="produce_ticket", text="Подробнее", args=[A("pk")])
    created_at = tables.DateTimeColumn(accessor='created_at', format='Y-m-d H:i', verbose_name="Дата создания")
    is_production_delivered = tables.BooleanColumn(accessor='is_production_delivered', verbose_name="Доставлено")
    class Meta:
        model = Ticket
        template_name = "django_tables2/bootstrap4.html"
        fields = ("created_at", "product", "logistics", "city_cached", "amount", "is_production_ready_cached", "is_production_delivered", "link")