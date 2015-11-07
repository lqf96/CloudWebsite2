# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=64)),
                ('Users', models.ManyToManyField(to='main.User')),
            ],
        ),
        migrations.DeleteModel(
            name='DiscussionZoneBoard',
        ),
        migrations.DeleteModel(
            name='DiscussionZoneContent',
        ),
        migrations.DeleteModel(
            name='DiscussionZonePost',
        ),
        migrations.AlterField(
            model_name='emailvalidationrecord',
            name='RedirectAddr',
            field=models.CharField(max_length=128),
        ),
    ]
