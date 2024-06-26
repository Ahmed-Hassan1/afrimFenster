from django.contrib import admin
from .models import *

from nested_inline.admin import NestedStackedInline, NestedModelAdmin

# Register your models here.
@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    # if there's already an entry, do not allow adding
    count = PhoneNumber.objects.all().count()
    if count == 0:
      return True

    return False
  

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    # if there's already an entry, do not allow adding
    count = Email.objects.all().count()
    if count == 0:
      return True

    return False
  
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    # if there's already an entry, do not allow adding
    count = Location.objects.all().count()
    if count == 0:
      return True

    return False
  
@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    # if there's already an entry, do not allow adding
    count = Map.objects.all().count()
    if count == 0:
      return True

    return False
  

class HoursAdminInline(admin.StackedInline):
    model = Hours
    extra=1
@admin.register(OpeningHours)
class OpeningHoursAdmin(admin.ModelAdmin):
    inlines=(HoursAdminInline, )


class PTagHomeAdminInline(admin.StackedInline):
    model = PTagHome
    extra=1
@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    inlines=(PTagHomeAdminInline, )
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = HomePage.objects.all().count()
        if count == 0:
            return True

        return False




class FensterAdminInline(admin.StackedInline):
    model = Fenster
    extra=1

@admin.register(FensterPage)
class FensterPageAdmin(admin.ModelAdmin):
    inlines=(FensterAdminInline,)
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = FensterPage.objects.all().count()
        if count == 0:
            return True

        return False
    


class AluFensterAdminInline(admin.StackedInline):
    model = AluFenster
    extra=1

@admin.register(KunAluFensterPage)
class AluFensterPageAdmin(admin.ModelAdmin):
    inlines=(AluFensterAdminInline,)
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = KunAluFensterPage.objects.all().count()
        if count == 0:
            return True

        return False
    



class HolzAluImagesInline(admin.StackedInline):
    model = HolzAluImages
    extra=1
    
class HolzAluSidePointsInline(admin.StackedInline):
    model = HolzAluSidePoints
    extra=1

class HolzAluBottomImageInline(admin.StackedInline):
    model = HolzAluBottomImage
    extra=1

@admin.register(HolzAluFenster)
class AluFensterPageAdmin(admin.ModelAdmin):
    inlines=(HolzAluImagesInline,HolzAluSidePointsInline,HolzAluBottomImageInline,)




class HolzImagesInline(admin.StackedInline):
    model = HolzImages
    extra=1
    
class HolzSidePointsInline(admin.StackedInline):
    model = HolzSidePoints
    extra=1

class HolzBottomImageInline(admin.StackedInline):
    model = HolzBottomImage
    extra=1

@admin.register(HolzFenster)
class FensterPageAdmin(admin.ModelAdmin):
    inlines=(HolzImagesInline,HolzSidePointsInline,HolzBottomImageInline,)



@admin.register(TurenPage)
class TurenPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = TurenPage.objects.all().count()
        if count == 0:
            return True

        return False
    



class ToranImageInline(admin.StackedInline):
    model = ToranLangenImage
    extra=1
@admin.register(ToranLagenPage)
class ToranLagenPageAdmin(admin.ModelAdmin):
    inlines=(ToranImageInline,)
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = ToranLagenPage.objects.all().count()
        if count == 0:
            return True

        return False