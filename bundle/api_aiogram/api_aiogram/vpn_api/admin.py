from django.contrib import admin
from .models import *


class VpnModelAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'date_expired',)


class VpnTypeAdmin(admin.ModelAdmin):
    list_display = ('vpn_type_name',)


class VpnUserUseModelAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'last_name', 'config_name', 'time_exp', 'time_take')


admin.site.register(VpnModel1, VpnModelAdmin)
admin.site.register(VpnTypeModel1, VpnTypeAdmin)
admin.site.register(VpnUserUseModel1, VpnUserUseModelAdmin)
