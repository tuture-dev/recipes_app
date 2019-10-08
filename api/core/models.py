from django.db import models


class Recipe(models.Model):
    DIFFICULTY_LEVELS = (
        ('Easy', '容易'),
        ('Medium', '中等'),
        ('Hard', '困难'),
    )
    name = models.CharField(max_length=120, verbose_name='名称')
    ingredients = models.CharField(max_length=400, verbose_name='食材')
    picture = models.FileField(verbose_name='图片')
    difficulty = models.CharField(choices=DIFFICULTY_LEVELS, max_length=10,
                                  verbose_name='制作难度')
    prep_time = models.PositiveIntegerField(verbose_name='准备时间')
    prep_guide = models.TextField(verbose_name='制作指南')

    class Meta:
        verbose_name = '食谱'
        verbose_name_plural = '食谱'

    def __str__(self):
        return '{} 的食谱'.format(self.name)
