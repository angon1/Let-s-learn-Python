# Generated by Django 3.0.6 on 2020-10-12 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pullUps', '0007_auto_20201001_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcerciseBlockSets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blockKey', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pullUps.ExcerciseBlock')),
                ('setKey', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pullUps.ExcerciseSet')),
            ],
        ),
        migrations.RemoveField(
            model_name='excerciseblock',
            name='usedExcerciseSets',
        ),
        migrations.AddField(
            model_name='excerciseblock',
            name='usedExcerciseSets',
            field=models.ManyToManyField(through='pullUps.ExcerciseBlockSets', to='pullUps.ExcerciseSet'),
        ),
    ]