from django.contrib import admin
from blog.models import Configuracion
from blog.models import Post

admin.site.register(Configuracion)

admin.site.register(Post)
# Register your models here.
