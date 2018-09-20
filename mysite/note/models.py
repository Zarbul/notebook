from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Notes(models.Model):
    name = models.CharField('Заголовок', max_length=50, blank=True)
    link = models.URLField('Ссылка', max_length=300, default='http://', blank=True)
    create_date = models.DateField('Дата создания', default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    # use = User.
    #     # status = models.IntegerField(choices=)
    #     balance = models.FloatField('Баланс денег', default = 0)
    #     otdel = models.ForeignKey('otdels.Otdel', default=0)    #
    #     # otd = Otdel()
    #
    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

    def __str__(self):
        return '{} ({})'.format(self.name, self.link, self.create_date)
