# Generated by Django 5.2 on 2025-04-19 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_category_contact_caregory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
