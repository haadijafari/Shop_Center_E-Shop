# Generated by Django 4.2.14 on 2024-07-16 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesetting',
            name='about_us_text',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='address',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='email',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='fax',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='phone',
        ),
        migrations.AddField(
            model_name='footerlink',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال / غیرفعال'),
        ),
        migrations.AddField(
            model_name='footerlinkbox',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال / غیرفعال'),
        ),
    ]
