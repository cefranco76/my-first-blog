from django.contrib import admin
#from django.contrib import session
from .models import TabUsuario
from .models import TabEventos

admin.site.register(TabUsuario)
admin.site.register(TabEventos)