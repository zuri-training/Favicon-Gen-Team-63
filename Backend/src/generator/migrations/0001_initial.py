# Generated by Django 4.0.6 on 2022-07-31 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favicons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ImgFavicons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_title', models.CharField(max_length=500)),
                ('icon', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='TextFavicons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_title', models.CharField(max_length=500)),
                ('icon', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generated_icons', models.ManyToManyField(to='generator.favicons')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='favicons',
            name='img_generated_icons',
            field=models.ManyToManyField(to='generator.imgfavicons'),
        ),
        migrations.AddField(
            model_name='favicons',
            name='txt_generated_icons',
            field=models.ManyToManyField(to='generator.textfavicons'),
        ),
        migrations.AddField(
            model_name='favicons',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]