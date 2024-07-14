# Generated by Django 4.2.14 on 2024-07-14 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterLinkBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'دسته بندی لینک های فوتر',
                'verbose_name_plural': 'دسته بندی های لینک های فوتر',
            },
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(max_length=128, verbose_name='عنوان سایت')),
                ('address', models.CharField(blank=True, max_length=512, null=True, verbose_name='آدرس')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='شماره تماس')),
                ('fax', models.CharField(blank=True, max_length=128, null=True, verbose_name='فکس')),
                ('email', models.CharField(blank=True, max_length=128, null=True, verbose_name='ایمیل')),
                ('copy_right', models.TextField(verbose_name='متن کپی رایت سایت')),
                ('about_us_text', models.TextField(verbose_name='متن درباره ما سایت')),
                ('logo', models.ImageField(upload_to='images/settings/logo', verbose_name='لوگو')),
                ('is_main_setting', models.BooleanField(default=False, verbose_name='تنظیمات اصلی')),
            ],
            options={
                'verbose_name': 'کانفیگ تنظیمات پایه',
                'verbose_name_plural': 'کانفیگ های تنظیمات پایه',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='عنوان')),
                ('url', models.URLField(max_length=512, verbose_name='لینک')),
                ('url_title', models.URLField(max_length=128, verbose_name='عنوان لینک')),
                ('description', models.TextField(verbose_name='توضیحات اسلایدر')),
                ('image', models.ImageField(upload_to='images/sliders', verbose_name='تصویر اسلایدر')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدر ها',
            },
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='عنوان')),
                ('url', models.URLField(max_length=512, verbose_name='لینک')),
                ('footer_link_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_settings.footerlinkbox', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'لینک فوتر',
                'verbose_name_plural': 'لینک های فوتر',
            },
        ),
    ]
