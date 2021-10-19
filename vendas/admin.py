from django.contrib import admin
from .models import Venda
from .models import ItemDoPedido
from .actions import nfe_emitida, nfe_nao_emitida


# essa class serve para poder ter i itens do pedido tudo na mesma pagina do django admin.
# a classe venda vai ter uma coleção de um model dentro da sua edição principal.
class ItemPedidoInLine(admin.TabularInline):
    model = ItemDoPedido
    extra = 1 # define quantos itens vai vir aberto no admin, no exemplo ai vai ser só 1


# combinando filtros, por Forignkey
class VendaAdmin(admin.ModelAdmin):
    list_filter = ('pessoa__doc', 'desconto')

    list_display = ('id', 'pessoa', 'nfe_emitida', 'valor')

    #esse campo é apenas para leitura,
    readonly_fields = ('valor',)

    # esse campo mostra uma busca melhorada, avançada para um determinado campo no ex: campo pessoa, posso selecionar varios campos
    #raw_id_fields = ('pessoa',)

    autocomplete_fields = ('pessoa', )

    # esse campo para pisquisar os campos q a gente quer que seja buscado no model
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')

    actions = [nfe_emitida, nfe_nao_emitida]  #definindo status para notas fiscais emitadas ou não

    #filter_horizontal = ['produtos', ] # deica o campo vertical ou horizontal para poder selecionar e passar para o lado

    inlines = [ItemPedidoInLine, ]

    # essa função vai retornar o total no display_list, o calculo é feito no models
    def total(self, obj):
        return obj.get_total()

    total.short_description = 'Total'


admin.site.register(Venda, VendaAdmin)
admin.site.register(ItemDoPedido)
