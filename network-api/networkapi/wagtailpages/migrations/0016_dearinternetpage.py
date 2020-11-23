# Generated by Django 2.2.16 on 2020-11-19 23:32

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailmetadata.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0052_pagelogentry'),
        ('wagtailpages', '0015_auto_20201116_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='DearInternetPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro_texts', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link']))])),
                ('intro_texts_en', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link']))], null=True)),
                ('intro_texts_de', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link']))], null=True)),
                ('intro_texts_pt', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link']))], null=True)),
                ('intro_texts_es', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link']))], null=True)),
                ('intro_texts_fr', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link']))], null=True)),
                ('intro_texts_fy_NL', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link']))], null=True)),
                ('intro_texts_nl', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link']))], null=True)),
                ('intro_texts_pl', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link']))], null=True)),
                ('letters', wagtail.core.fields.StreamField([('letters', wagtail.core.blocks.StructBlock([('author', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('author_photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('letter', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'ol', 'ul'], help_text='Main letter content')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video_url', wagtail.core.blocks.URLBlock(help_text='Video url to link out to', required=False))]))])),
                ('letters_en', wagtail.core.fields.StreamField([('letters', wagtail.core.blocks.StructBlock([('author', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('author_photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('letter', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'ol', 'ul'], help_text='Main letter content')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video_url', wagtail.core.blocks.URLBlock(help_text='Video url to link out to', required=False))]))], null=True)),
                ('letters_de', wagtail.core.fields.StreamField([('letters', wagtail.core.blocks.StructBlock([('author', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('author_photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('letter', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'ol', 'ul'], help_text='Main letter content')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video_url', wagtail.core.blocks.URLBlock(help_text='Video url to link out to', required=False))]))], null=True)),
                ('letters_pt', wagtail.core.fields.StreamField([('letters', wagtail.core.blocks.StructBlock([('author', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('author_photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('letter', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'ol', 'ul'], help_text='Main letter content')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video_url', wagtail.core.blocks.URLBlock(help_text='Video url to link out to', required=False))]))], null=True)),
                ('letters_es', wagtail.core.fields.StreamField([('letters', wagtail.core.blocks.StructBlock([('author', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('author_photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('letter', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'ol', 'ul'], help_text='Main letter content')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video_url', wagtail.core.blocks.URLBlock(help_text='Video url to link out to', required=False))]))], null=True)),
                ('letters_fr', wagtail.core.fields.StreamField([('letters', wagtail.core.blocks.StructBlock([('author', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('author_photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('letter', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'ol', 'ul'], help_text='Main letter content')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video_url', wagtail.core.blocks.URLBlock(help_text='Video url to link out to', required=False))]))], null=True)),
                ('letters_fy_NL', wagtail.core.fields.StreamField([('letters', wagtail.core.blocks.StructBlock([('author', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('author_photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('letter', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'ol', 'ul'], help_text='Main letter content')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video_url', wagtail.core.blocks.URLBlock(help_text='Video url to link out to', required=False))]))], null=True)),
                ('letters_nl', wagtail.core.fields.StreamField([('letters', wagtail.core.blocks.StructBlock([('author', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('author_photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('letter', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'ol', 'ul'], help_text='Main letter content')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video_url', wagtail.core.blocks.URLBlock(help_text='Video url to link out to', required=False))]))], null=True)),
                ('letters_pl', wagtail.core.fields.StreamField([('letters', wagtail.core.blocks.StructBlock([('author', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('author_photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('letter', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'ol', 'ul'], help_text='Main letter content')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video_url', wagtail.core.blocks.URLBlock(help_text='Video url to link out to', required=False))]))], null=True)),
                ('cta', models.CharField(max_length=500)),
                ('cta_en', models.CharField(max_length=500, null=True)),
                ('cta_de', models.CharField(max_length=500, null=True)),
                ('cta_pt', models.CharField(max_length=500, null=True)),
                ('cta_es', models.CharField(max_length=500, null=True)),
                ('cta_fr', models.CharField(max_length=500, null=True)),
                ('cta_fy_NL', models.CharField(max_length=500, null=True)),
                ('cta_nl', models.CharField(max_length=500, null=True)),
                ('cta_pl', models.CharField(max_length=500, null=True)),
                ('cta_button_text', models.CharField(max_length=100)),
                ('cta_button_text_en', models.CharField(max_length=100, null=True)),
                ('cta_button_text_de', models.CharField(max_length=100, null=True)),
                ('cta_button_text_pt', models.CharField(max_length=100, null=True)),
                ('cta_button_text_es', models.CharField(max_length=100, null=True)),
                ('cta_button_text_fr', models.CharField(max_length=100, null=True)),
                ('cta_button_text_fy_NL', models.CharField(max_length=100, null=True)),
                ('cta_button_text_nl', models.CharField(max_length=100, null=True)),
                ('cta_button_text_pl', models.CharField(max_length=100, null=True)),
                ('cta_button_link', models.URLField()),
                ('cta_button_link_en', models.URLField(null=True)),
                ('cta_button_link_de', models.URLField(null=True)),
                ('cta_button_link_pt', models.URLField(null=True)),
                ('cta_button_link_es', models.URLField(null=True)),
                ('cta_button_link_fr', models.URLField(null=True)),
                ('cta_button_link_fy_NL', models.URLField(null=True)),
                ('cta_button_link_nl', models.URLField(null=True)),
                ('cta_button_link_pl', models.URLField(null=True)),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Search image')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailmetadata.models.MetadataMixin, 'wagtailcore.page', models.Model),
        ),
    ]