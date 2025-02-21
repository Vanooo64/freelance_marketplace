from django.db import models
from django.contrib.auth.models import User

class Orders(models.Model):
    WORK_TYPES = [
        ('tutor', 'Онлайн-репетитор'),
        ('control', 'Контрольна'),
        ('tasks', 'Розв’язання задач'),
        ('coursework', 'Курсова'),
        ('essay', 'Реферат'),
        ('online_help', 'Онлайн-допомога'),
        ('test', 'Тест дистанційно'),
        ('diploma', 'Диплом'),
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

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    type_of_work = models.CharField(max_length=20, choices=WORK_TYPES, default='coursework')
    subject = models.CharField(max_length=255)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    plagiarism_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.00, help_text="Рівень унікальності (%)"
    )
    order_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, help_text="Сума замовлення в грн"
    )  # Сума замовлення
    file_upload = models.FileField(
        upload_to='order_files/', blank=True, null=True, help_text="Додайте файл (якщо потрібно)"
    )  # Поле для завантаження файлів

