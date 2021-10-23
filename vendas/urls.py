from django.urls import path
from .views import DashboardView, NovoPedido


urlpatterns = [
    path('novo-pedido/', NovoPedido.as_view(), name="novo-pedido"),
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
]
