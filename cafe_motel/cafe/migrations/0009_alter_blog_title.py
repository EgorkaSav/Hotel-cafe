# Generated by Django 5.0.3 on 2024-04-11 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0008_blog_pub_date_blog_title_alter_blog_plot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='Новости', max_length=100),
        ),
    ]
