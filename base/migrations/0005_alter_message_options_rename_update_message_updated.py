# Generated by Django 5.0.6 on 2024-06-10 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_room_participants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.RenameField(
            model_name='message',
            old_name='update',
            new_name='updated',
        ),
    ]
