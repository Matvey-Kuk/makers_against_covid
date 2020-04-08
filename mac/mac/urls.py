from django.contrib import admin
from django.urls import path, include

from apps.base.views import IndexView, LoginView, SignupView, SettingsView
import apps.orders.views as order_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("account/", include("account.urls")),
    path("login/", LoginView.as_view(), name='login'),
    path("account_settings/", SettingsView.as_view(), name='account_settings'),
    path("account/", SignupView.as_view(), name='signup'),

    path("products/", order_views.ProductListView.as_view(), name="products_list"),
    path("product/<str:id>/", order_views.ProductView.as_view(), name="product"),

    path("produce_ticket_create/", order_views.ProduceTicketCreateView.as_view(), name="produce_ticket_create"),
    path("produce_tickets/", order_views.ProduceTicketList.as_view(), name="produce_tickets_list"),
    path("produce_ticket/<int:pk>/", order_views.ProduceTicketView.as_view(), name="produce_ticket"),

    path("request_ticket_create/", order_views.RequestTicketCreateView.as_view(), name="request_ticket_create"),
    path("request_tickets/", order_views.RequestTicketList.as_view(), name="request_tickets_list"),
    path("request_ticket/<int:pk>/", order_views.RequestTicketView.as_view(), name="request_ticket"),

    path('', IndexView.as_view()),
]
