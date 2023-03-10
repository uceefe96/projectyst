# Generated by Django 4.1.7 on 2023-03-03 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('cin', models.CharField(max_length=255)),
                ('cne', models.CharField(max_length=255)),
                ('num_tel', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('date_de_naissance', models.DateField()),
                ('date_d_inscription', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('note', models.FloatField()),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='guichet.etudiant')),
            ],
        ),
    ]
