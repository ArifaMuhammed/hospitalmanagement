# Generated by Django 4.2 on 2023-04-25 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_doctors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctors',
            old_name='doc_img',
            new_name='doc_image',
        ),
    ]
