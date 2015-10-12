# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscussionZoneBoard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=24)),
                ('PostAmount', models.BigIntegerField()),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DiscussionZoneContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Board', models.CharField(max_length=24)),
                ('PostID', models.BigIntegerField()),
                ('ContentID', models.BigIntegerField()),
                ('Author', models.CharField(max_length=24)),
                ('Content', models.TextField()),
                ('Time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DiscussionZonePost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('PostID', models.BigIntegerField()),
                ('Board', models.CharField(max_length=24)),
                ('Title', models.CharField(max_length=64)),
                ('Author', models.CharField(max_length=32)),
                ('Time', models.DateTimeField()),
                ('LastReply', models.CharField(max_length=32)),
                ('LastReplyTime', models.DateTimeField()),
                ('ReplyAmount', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EmailValidationRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Nonce', models.BigIntegerField()),
                ('RedirectAddr', models.CharField(max_length=192)),
                ('Data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=32)),
                ('Username', models.CharField(max_length=32)),
            ],
        ),
    ]
