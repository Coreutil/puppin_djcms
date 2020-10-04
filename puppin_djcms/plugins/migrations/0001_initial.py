# Generated by Django 3.0.10 on 2020-10-04 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='plugins_footer', serialize=False, to='cms.CMSPlugin')),
                ('copyright_author', models.CharField(default='', max_length=255, verbose_name='Copyright author')),
                ('social_panel', models.BooleanField(default=False, verbose_name='Social panel')),
                ('scrollup_button', models.BooleanField(default=False, verbose_name='Scroll up button')),
                ('dark_background', models.BooleanField(default=False, verbose_name='Dark background')),
                ('border_top', models.BooleanField(default=False, verbose_name='Top border')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]