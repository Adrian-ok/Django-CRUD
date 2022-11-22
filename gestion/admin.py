from django.contrib import admin

# Register your models here.
from .models import persona, localidad, grup_sangre, sector, estado

admin.site.register(persona)
admin.site.register(localidad)
admin.site.register(grup_sangre)
admin.site.register(sector)
admin.site.register(estado)