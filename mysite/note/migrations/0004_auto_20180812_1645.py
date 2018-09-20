# Generated by Django 2.1 on 2018-08-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20180812_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='link',
            field=models.CharField(max_length=100, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='text',
            field=models.TextField(max_length=300, verbose_name='Описание'),
        ),
    ]
