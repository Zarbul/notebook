from django.contrib import admin
from .models import Notes


class ViewNoteColombs(admin.ModelAdmin):
    list_display = ['id', 'name', 'link', 'create_date', 'user']
    list_display_links = ['id', 'name', 'link', 'create_date', 'user']
    list_filter = ['create_date', 'name']
    search_fields = ['name', ]

    class Meta():
        model = Notes


# class ViewColombsAdress(admin.ModelAdmin):
#     list_display = ['worker', 'indx', 'region', 'sity', 'street', 'home']
#     list_display_links = ['worker', 'indx', 'region', 'sity', 'street', 'home']
#     list_filter = ['region', 'sity']
#     # search_fields = ['name', 'fname']
#     class Meta():
#         model = Adress
#
#
# class ViewColombsContact(admin.ModelAdmin):
#     list_display = ['worker', 'type_contact', 'contact']
#     list_display_links = ['worker', 'type_contact', 'contact']
#     list_filter = ['type_contact']
#     # search_fields = ['name', 'fname']
#     class Meta():
#         model = Contact

admin.site.register(Notes, ViewNoteColombs)
# admin.site.register(Contact, ViewColombsContact)
# admin.site.register(Adress, ViewColombsAdress)


# admin.site.register(Worker)
