# Generated by Django 5.0.3 on 2024-04-26 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0010_sklad_alter_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='Оплата'),
        ),
    ]
