# Generated by Django 4.0.6 on 2022-07-20 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_subcription_playertwo_alter_registration_points_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcription',
            name='category',
            field=models.CharField(choices=[('F Ini', 'Feminino Iniciante'), ('F Int', 'Feminino Intermediário'), ('F Ava', 'Feminino Avançado'), ('M Ini', 'Masculino Iniciante'), ('M Int', 'Masculino Intermediário'), ('M Ava', 'Masculino Avançado')], max_length=5),
        ),
    ]
