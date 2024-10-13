from django.contrib import admin 
 
# Register your models here. 
 
from psiuApp.models import Atividade, Carona, Estudos, Extracurriculares, Liga

admin.site.register(Atividade)
admin.site.register(Carona)
admin.site.register(Estudos)
admin.site.register(Extracurriculares)
admin.site.register(Liga)