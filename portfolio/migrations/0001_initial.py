# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 15:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('docs_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('project_url', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=100)),
                ('project_description', models.TextField()),
                ('picture', models.ImageField(upload_to='./static/img/')),
                ('url', models.URLField()),
                ('start_date', models.DateField()),
                ('github_link', models.URLField()),
                ('trello_link', models.URLField()),
                ('status', models.CharField(choices=[('D', 'Designing'), ('A', 'Active'), ('C', 'Complete')], max_length=1)),
                ('packages', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.Package')),
            ],
        ),
    ]
