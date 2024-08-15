from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from GPC.models import CustomUser

from GPC.models.aluno import Aluno
from GPC.models.mentor import Mentor
from GPC.models.empresa import Empresa
from GPC.models.vagas import Vaga
from GPC.models.projetovida import ProjetoVida
from GPC.models.gestor import Gestor, PageConfiguration


#aqui vamos configurar a tela do adm (se adicionar algum campo no model deverá adicionar aqui para aparecer na area do adm)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'user_type', 'is_staff', 'is_active')
    list_filter = ('user_type', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('User Type', {'fields': ('user_type',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'user_type', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Aluno)
admin.site.register(Mentor)
admin.site.register(Empresa)
admin.site.register(Vaga)
admin.site.register(ProjetoVida)
admin.site.register(Gestor)
admin.site.register(PageConfiguration)