# Generated by Django 5.0.3 on 2024-04-09 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0006_category_menuitem_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot', models.CharField(max_length=100)),
                ('img', models.ImageField(null=True, upload_to='blog_images/')),
            ],
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(null=True, upload_to='dish_images/'),
        ),
    ]
