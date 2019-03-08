from django.contrib import admin
#from django.contrib import session
from .models import TabUsuario
from .models import TabEventos
from .models import TabImagens

admin.site.register(TabUsuario)
admin.site.register(TabEventos)
admin.site.register(TabImagens)