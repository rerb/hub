# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def copy_images(apps, schema_editor):
    
    Image = apps.get_model("content", "Image")
    
    for img in Image.objects.all():
        try:
            img.image = img.image_archived.url
            img.save()
        except ValueError: # some may not have associated files
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0068_add_image_image_field'),
    ]

    operations = [
        migrations.RunPython(copy_images),
    ]
