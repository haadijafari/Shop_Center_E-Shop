# Generated by Django 4.2.14 on 2024-07-16 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_user_verification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(db_index=True, default='43XxAqOeABQutnQHwmzzlHhKXxwI3DEKgDnGCJXTXXuhDBkHQwSBBZ0SFZJwkAkgBncUJhrSuQ1aJav7w0FtDIOszELogSqz0VzhNWyU2cePieGrb0CXoMEuh6YMlLWI', editable=False, max_length=128),
        ),
    ]