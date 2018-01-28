from __future__ import unicode_literals

import imagekit.models.fields
import stdimage.utils
from django.db import migrations, models

import imageApp.models


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageKit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to=imageApp.models.get_image_path)),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(null=True, upload_to=imageApp.models.get_image_path)),
            ],
        ),
        migrations.CreateModel(
            name='StdImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', stdimage.models.StdImageField(upload_to=stdimage.utils.UploadToAutoSlugClassNameDir('id'))),
            ],
        ),
    ]
