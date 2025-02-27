from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from datetime import timedelta

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Orders.Status.NOT_PERFORMER)


class Orders(models.Model):
    class Status(models.IntegerChoices):
        NOT_PERFORMER=0, 'Без виконавця'
        AT_WORK=1, 'В роботі'


    WORK_TYPES = [
        ('tutor', 'Онлайн-репетитор'),
        ('control', 'Контрольна'),
        ('tasks', 'Розв’язання задач'),
        ('coursework', 'Курсова'),
        ('essay', 'Реферат'),
        ('online_help', 'Онлайн-допомога'),
        ('test', 'Тест дистанційно'),
        ('diplom', 'Диплом'),
        ('lab', 'Лабораторна'),
        ('drawing', 'Креслення'),
        ('practice_report', 'Звіт з практики'),
        ('short_essay', 'Есе'),
        ('exam_answers', 'Відповіді на квитки'),
        ('presentation', 'Презентація'),
        ('translation', 'Переклад з ін. мови'),
        ('speech', 'Доповідь'),
        ('article', 'Стаття'),
        ('composition', 'Твір'),
        ('masters_thesis', 'Магістерська дисертація'),
        ('phd_thesis', 'Кандидатська дисертація'),
        ('business_plan', 'Бізнес-план'),
        ('literature_review', 'Підбір літератури'),
        ('cheat_sheet', 'Шпаргалка'),
        ('info_search', 'Пошук інформації'),
    ]

    title = models.CharField(max_length=255, verbose_name="Назва роботи")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True, verbose_name="Опис роботи")
    type_of_work = models.CharField(
        max_length=30, choices=WORK_TYPES, default='coursework', verbose_name="Тип роботи"
    )
    subject = models.CharField(max_length=255, verbose_name="Предмет")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Замовник")
    plagiarism_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.00, help_text="Рівень унікальності (%)", verbose_name="Антиплагіат"
    )
    order_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, help_text="Сума замовлення в грн", verbose_name="Сума"
    )
    file_upload = models.FileField(
        upload_to='order_files/', blank=True, null=True, help_text="Додайте файл (якщо потрібно)", verbose_name="Файл"
    )
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
    deadline = models.DateTimeField(default=now() + timedelta(days=7), help_text="Срок сдачи заказа")
    is_published = models.BooleanField(choices=Status.choices, default=Status.NOT_PERFORMER)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-time_create']
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

    def __str__(self):
        return f"{self.title} ({self.get_type_of_work_display()}) - {self.customer.username} - {self.order_amount} грн - {self.plagiarism_percentage}%"

    def get_absolut_url(self):
        return reverse('order', kwargs={'order_slug': self.slug})

class Customer(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolut_url(self):
        return reverse('customer', kwargs={'customer_slug': self.slug})