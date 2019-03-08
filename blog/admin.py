from django.contrib import admin
#from django.contrib import session
from .models import Post
from .models import TabUsuario
from .models import TabEventos
from .models import TabImagens

admin.site.register(Post)
admin.site.register(TabUsuario)
admin.site.register(TabEventos)
admin.site.register(TabImagens)