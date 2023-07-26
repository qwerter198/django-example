from django.db import models

# Create your models here.

# 新增元祖用愈設定訊息類型列舉
KIND_CHOICES = (
    ('Python技術', 'Python技術'),
    ('資料庫技術', '資料庫技術'),
    ('經濟學', '經濟學'),
    ('文體資訊', '文體資訊'),
    ('個人心情', '個人心情'),
    ('其他', '其他'),
)


class Moment(models.Model):
    content = models.CharField(max_length=300)
    user_name = models.CharField(max_length=20)
    # 修改kind定義，加入choices參數
    kind = models.CharField(
        max_length=20, choices=KIND_CHOICES, default=KIND_CHOICES[0])
