from django.db import models


class VpnModel1(models.Model):
    user_name = models.CharField(max_length=255, default=None, null=True, unique=True)
    date_expired = models.DateTimeField(default=None, null=True)
    url = models.CharField(max_length=1255)
    photo_url = models.ImageField(upload_to='images/%Y/%m/%d/', default=None, null=True)
    type = models.ForeignKey('VpnTypeModel1', on_delete=models.PROTECT, default=None, null=True)

    class Meta:
        verbose_name = 'VPN конфигурация'
        verbose_name_plural = 'VPN конфигурации'

    def __str__(self):
        return self.user_name


class VpnTypeModel1(models.Model):
    vpn_type_name = models.CharField(max_length=30, db_index=True)

    class Meta:
        verbose_name = 'VPN тип конфигурации'
        verbose_name_plural = 'VPN тип конфигураций'

    def __str__(self):
        return self.vpn_type_name


class VpnUserUseModel1(models.Model):
    user_id = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    config_name = models.CharField(max_length=30)
    time_exp = models.DateTimeField()
    time_take = models.DateTimeField()

    class Meta:
        verbose_name = 'VPN использование конфигураций пользователями'
        verbose_name_plural = 'VPN использования конфигураций пользователями'

    def __str__(self):
        return self.user_id
