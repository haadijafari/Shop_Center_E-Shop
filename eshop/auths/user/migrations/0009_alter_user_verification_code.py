# Generated by Django 4.2.14 on 2024-07-16 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_user_verification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(db_index=True, default='EUb1KicSJoRStuc3bjwVZMJfe2OQkeodsBmpnX4T8rIPnBmqHJjgCqqbRpqxaKaaown2NJvnqabVmA8aMN7ap8xcCOElFEqqOHbLWUrNEXawf3oTUHaKhjjRq7SZ0rhY', editable=False, max_length=128),
        ),
    ]
