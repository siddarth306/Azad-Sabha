from public.models import *
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class UserProfileInline(admin.StackedInline):
	model = Customuser
	can_delete = False
	verbose_name_plural = 'profile'

class UserAdmin(UserAdmin):
	inlines = (UserProfileInline, )

"""class PoliticianProfileInline(admin.StackedInline):
	model = Politician
	can_delete = False
	verbose_name_plural = 'profile'

class PoliticianAdmin(UserAdmin):
	inlines = (PoliticianProfileInline, )"""

class PostPrblmAdmin(admin.ModelAdmin):
	list_display = ('locality','subject','Date')
	
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
#admin.site.register(Politician,PoliticianAdmin)
admin.site.register(PostProblems,PostPrblmAdmin)