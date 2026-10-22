from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('content', models.TextField(blank=True, verbose_name='Содержание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название задачи')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('deadline', models.DateTimeField(blank=True, null=True, verbose_name='Срок выполнения')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Выполнена')),
                ('priority', models.IntegerField(default=1, verbose_name='Приоритет')),
                ('category', models.CharField(blank=True, default='', max_length=50, verbose_name='Категория')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создана')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'ordering': ['priority', 'deadline'],
            },
        ),
    ]
