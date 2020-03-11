from django.contrib import admin
from .models import Pessoa, Endereço, Estado, Municipio, Paise, Cargo, Empresa

#clientes
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id','nome','email','cpf','cnpj','matricula')
admin.site.register(Pessoa, PessoaAdmin)

#clientes
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome','sigla','pais')
admin.site.register(Estado, EstadoAdmin)

#clientes
class EndereçoAdmin(admin.ModelAdmin):
    list_display = ('pessoa','estado','municipio')
admin.site.register(Endereço, EndereçoAdmin)

#clientes
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nome','estado')
admin.site.register(Municipio, MunicipioAdmin)

#clientes
class PaiseAdmin(admin.ModelAdmin):
    list_display = ('nome','gentilico','sigla')
admin.site.register(Paise, PaiseAdmin)

#clientes
admin.site.register(Cargo)

#clientes
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome','nome_fantasia','logotip')
admin.site.register(Empresa, EmpresaAdmin)












