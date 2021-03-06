# Generated by Django 3.2.11 on 2022-01-17 14:05

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpage',
            name='body',
            field=wagtail.core.fields.StreamField([('h1', wagtail.core.blocks.CharBlock()), ('h2', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image_text', wagtail.core.blocks.StructBlock([('reverse', wagtail.core.blocks.BooleanBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('image_carousel', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('thumbnail_gallery', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))], blank=True),
        ),
    ]
