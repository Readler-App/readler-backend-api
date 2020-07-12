# Generated by Django 3.0.7 on 2020-07-12 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('url', models.URLField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraphIndex', models.IntegerField()),
                ('startWordIndex', models.IntegerField()),
                ('endWordIndex', models.IntegerField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendAPI.Article')),
            ],
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='phone',
            new_name='username',
        ),
        migrations.AddField(
            model_name='library',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='library',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fontFamily', models.CharField(default='Times New Roman', max_length=50)),
                ('fontSize', models.CharField(default='16px', max_length=10)),
                ('parMargin', models.CharField(default='1em', max_length=10)),
                ('lineHeight', models.CharField(default='normal', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField(auto_now_add=True)),
                ('endTime', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendAPI.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SelectionNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('highlight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendAPI.Selection')),
            ],
        ),
        migrations.AddField(
            model_name='selection',
            name='selectionNote',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backendAPI.SelectionNotes'),
        ),
        migrations.AddField(
            model_name='selection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ArticleNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendAPI.Article')),
            ],
        ),
        migrations.AddField(
            model_name='library',
            name='articles',
            field=models.ManyToManyField(related_name='libraries', to='backendAPI.Article'),
        ),
    ]