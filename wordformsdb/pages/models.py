from django.db import models


class Entry(models.Model):
    wordform = models.CharField(max_length=50, verbose_name='Словоформа в корпусе', blank=True, null=True)
    form1 = models.CharField(max_length=50, verbose_name='Форма 1', blank=True, null=True)
    form2 = models.CharField(max_length=50, verbose_name='Форма 2', blank=True, null=True)
    form3 = models.CharField(max_length=50, verbose_name='Форма 3', blank=True, null=True)
    form4 = models.CharField(max_length=50, verbose_name='Форма 4', blank=True, null=True)
    var_type = models.CharField(max_length=10, verbose_name='Вариативность типа', blank=True, null=True)
    notes = models.TextField(verbose_name='Пометки', blank=True, null=True)
    morph = models.CharField(max_length=30, verbose_name='Морфема', blank=True, null=True)
    pos = models.CharField(max_length=30, verbose_name='Часть речи', blank=True, null=True)
    morph_feats = models.TextField(verbose_name='Морфологические признаки', blank=True, null=True)
    freq_or = models.IntegerField(verbose_name='ABS (устный корпус)', blank=True, null=True)
    ipm_or = models.FloatField(verbose_name='IPM (устный корпус)', blank=True, null=True)
    freq_main = models.IntegerField(verbose_name='ABS (основной корпус)', blank=True, null=True)
    ipm_main = models.FloatField(verbose_name='IPM (основной корпус)', blank=True, null=True)
    source = models.TextField(verbose_name='Источник', blank=True, null=True)

    class Meta:
        verbose_name = 'Словоформа'
        verbose_name_plural = 'Словоформы'

    def __str__(self):
        return self.wordform
