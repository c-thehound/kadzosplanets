from django.contrib import admin
from .models import TeamMember,WeeksTheme,KadzosTagline,Logo,Message

admin.site.register(TeamMember)
admin.site.register(WeeksTheme)
admin.site.register(KadzosTagline)
admin.site.register(Logo)
admin.site.register(Message)