# Generated by Django 4.1.3 on 2022-11-28 00:13

from django.db import migrations
import prose.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_body',
            field=prose.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=prose.fields.RichTextField(),
        ),
    ]
