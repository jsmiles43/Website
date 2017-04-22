from django.contrib import admin
from projectCard.models import Card


class CardAdmin(admin.ModelAdmin):
	fields = ('name', 'description', 'code', 'card_choice', 'url', 'group')


admin.site.register(Card, CardAdmin)
