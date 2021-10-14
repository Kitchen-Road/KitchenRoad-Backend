# Generated by Django 3.2.7 on 2021-10-14 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Epoca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_epoca', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_receita', models.CharField(max_length=50)),
                ('imagem', models.ImageField(upload_to='post_img')),
                ('link_video_receita', models.URLField()),
                ('ingredientes', models.TextField(default='1.')),
                ('modo_preparo', models.TextField()),
                ('dificuldade', models.CharField(choices=[('I', 'Iniciante'), ('T', 'Intermediario'), ('A', 'Avancado')], max_length=1)),
                ('categoria_receita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receita.categoria')),
                ('epoca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receita.epoca')),
            ],
        ),
    ]
