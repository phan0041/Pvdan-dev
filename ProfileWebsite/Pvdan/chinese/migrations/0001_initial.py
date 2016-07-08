# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('meaning', models.TextField(default=b'')),
                ('priority', models.CharField(default=b'', max_length=50)),
                ('reserve', models.TextField(default=b'')),
            ],
        ),
    ]
