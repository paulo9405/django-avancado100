from django.contrib import admin
from .models import Person, Documento, TabelaExistente


# fields: personalizando formulario, mudando os filds de posição,
# ou colocando apenas filds citados, lembrando q os filds obrigatorios não podem deixer de serem citados.

class PersonAdmin(admin.ModelAdmin):

    #Agrupamento com titulos bem detalhado.
    fieldsets = (
        ('Dados pessoas', {'fields': ('first_name', 'last_name', 'doc')}),
        ('Dados complementares', {
            'classes': ('collapse',), #para esconder ou mostrar as informações
            'fields': ('age', 'salary', 'bio', 'photo'),
        }),
    )

    #Agrupando: organiza na msm linha os atribustos que estão entre parenteses
    #fields = (('doc', 'first_name'), 'last_name', ('age', 'salary'), ('bio', 'photo'))

    #exclude = ('bio',) #remove o campo bio

    # Normal
    #list_display = ('first_name', 'last_name', 'age', 'salary', 'bio', 'photo', 'doc')

    #filtros
    list_filter = ('age', 'salary')

    search_fields = ('id', 'first_name') #definindo a busca do autocomplete, que no ex: é id e first_name

    autocomplete_fields = ['doc', ]

    # colocando tratando o campo 'photo', passanod short description
    list_display = ('first_name', 'last_name', 'age', 'salary', 'bio', 'tem_foto', 'doc')
    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'
    tem_foto.short_description = 'Possui foto'



#admin para os documentos
class DocumentoAdmin(admin.ModelAdmin):
    search_fields = ['num_doc', ]

admin.site.register(Person, PersonAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(TabelaExistente)

