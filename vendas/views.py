from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Venda


class DashboardView(View):
    # verificação comm class based views
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.ver_dashboard'):
            return HttpResponse('Acesso negado, você precisa de permissão!')
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        data = {}
        data['media'] = Venda.objects.media()
        data['media_desconto'] = Venda.objects.media_desconto()
        data['min'] = Venda.objects.min()
        data['max'] = Venda.objects.max()
        data['num_ped'] = Venda.objects.num_ped()
        data['n_nfe'] = Venda.objects.n_nfe()

        return render(request, 'vendas/dashboard.html', data)
