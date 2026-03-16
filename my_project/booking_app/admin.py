from django.contrib import admin
from .models import (Country, City, Hotel, HotelImage,
                     Room, RoomImage, UserProfile,
                     Service, Booking, Review)
from modeltranslation.admin import TranslationAdmin

class CityInline(admin.TabularInline):
    model = City
    extra = 1


class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1


class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1


class TranslationMediaAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Country)
class CountryAdmin(TranslationMediaAdmin):
    inlines = [CityInline]


@admin.register(Hotel)
class HotelAdmin(TranslationMediaAdmin):
    inlines = [HotelImageInline]


@admin.register(Room)
class RoomAdmin(TranslationMediaAdmin):
    inlines = [RoomImageInline]


admin.site.register(City, TranslationMediaAdmin)
admin.site.register(Service, TranslationMediaAdmin)
admin.site.register(UserProfile)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(HotelImage)
admin.site.register(RoomImage)