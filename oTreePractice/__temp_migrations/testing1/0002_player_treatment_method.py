# Generated by Django 2.2.4 on 2020-07-20 09:11

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('testing1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='treatment_method',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]
