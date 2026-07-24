from django.contrib import admin
from .models import (
    Experience, Service, CategoriBlog, Blog, Temoignage,
    Contact, CategorieProjet, Projet, Profil
)

admin.site.register(Experience)
admin.site.register(Service)
admin.site.register(CategoriBlog)
admin.site.register(Blog)
admin.site.register(Temoignage)
admin.site.register(Contact)
admin.site.register(CategorieProjet)
admin.site.register(Projet)
admin.site.register(Profil)
