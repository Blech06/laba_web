from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название группы')
    course = models.PositiveSmallIntegerField(verbose_name='Курс')
    specialty = models.CharField(max_length=150, verbose_name='Специальность')

    def __str__(self):
        return f'{self.title} ({self.course} курс)'

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['title']


class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    record_book = models.CharField(max_length=20, unique=True, verbose_name='Номер зачётки')
    email = models.EmailField(verbose_name='Email')
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students',
        verbose_name='Группа'
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['last_name', 'first_name']
