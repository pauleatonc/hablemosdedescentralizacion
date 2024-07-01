from django.contrib import admin
from .models  import  Tag, Noticias, Multimedia,  PhotoAlbum, Photo

# Register your models here.


admin.site.register(Tag)

admin.site.register(Noticias)

admin.site.register(Multimedia)

class PhotoInline(admin.TabularInline):
    model = Photo
    fields = ['foto', 'descripcion']
    extra = 1  # Número de formas extras para cargar por defecto

class PhotoAlbumAdmin(admin.ModelAdmin):
    list_display = ['titulo_album', 'autor', 'region', 'date', 'public', 'photo_count']
    list_filter = ['public', 'region', 'autor']
    search_fields = ['titulo_album', 'descripcion_album']
    inlines = [PhotoInline]

    def photo_count(self, obj):
        return obj.photo_set.count()
    photo_count.short_description = 'Número de Fotos'

    def save_model(self, request, obj, form, change):
        if not obj.autor_id:  # Asigna el autor solo si es una nueva instancia
            obj.autor = request.user
        obj.save()

admin.site.register(PhotoAlbum, PhotoAlbumAdmin)