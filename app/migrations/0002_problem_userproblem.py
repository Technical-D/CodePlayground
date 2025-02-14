# Generated by Django 5.1.5 on 2025-01-20 15:37

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('short_description', models.TextField()),
                ('difficulty', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], default='Easy', max_length=50)),
                ('score', models.PositiveIntegerField()),
                ('starter_file', models.TextField(help_text='Python starter code for the problem')),
                ('description', models.FileField(help_text='Path to detailed description file', upload_to='descriptions/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solved', models.BooleanField(default=False)),
                ('solved_at', models.DateTimeField(blank=True, null=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_problems', to='app.problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_problems', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'problem')},
            },
        ),
    ]
