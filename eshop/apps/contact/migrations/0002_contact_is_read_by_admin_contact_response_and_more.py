# Generated by Django 4.2.11 on 2024-04-12 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_read_by_admin',
            field=models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین'),
        ),
        migrations.AddField(
            model_name='contact',
            name='response',
            field=models.TextField(blank=True, null=True, verbose_name='متن پاسخ'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(verbose_name='متن پیام'),
        ),
    ]