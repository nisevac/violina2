# Generated by Django 3.0.5 on 2020-05-01 09:46

from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.routable_page.models
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleGalleryIndex',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro_title', models.CharField(blank=True, help_text='Optional H1 title for the gallery page.', max_length=250, verbose_name='Intro title')),
                ('intro_text', wagtail.core.fields.RichTextField(blank=True, help_text='Optional text to go with the intro text.', verbose_name='Intro text')),
                ('images_per_page', models.IntegerField(default=8, help_text='How many images there should be on one page.', verbose_name='Images per page')),
                ('use_lightbox', models.BooleanField(default=True, help_text='Use lightbox to view larger images when clicking the thumbnail.', verbose_name='Use lightbox')),
                ('order_images_by', models.IntegerField(choices=[(1, 'Image title'), (2, 'Newest image first')], default=1)),
                ('collection', models.ForeignKey(help_text='Show images in this collection in the gallery view.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Collection', verbose_name='Collection')),
            ],
            options={
                'verbose_name': 'Gallery index',
                'verbose_name_plural': 'Gallery indices',
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
    ]
