from django.contrib import admin
from .models import NewsletterSubscriber, ContactMessage, GalleryImage
import csv
from django.http import HttpResponse

# CSV'ye aktarma fonksiyonu
def export_as_csv(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={meta}.csv'
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])

    return response

export_as_csv.short_description = "Export selected as CSV"

# 🔹 Newsletter Admin Paneli
@admin.register(NewsletterSubscriber)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    actions = [export_as_csv]

# 🔹 Contact Messages Admin Paneli
@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    actions = [export_as_csv]

# 🔹 Galeri admini – sadece görselleri göstermek için, CSV özelliği yok
@admin.register(GalleryImage)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'uploaded_at')
