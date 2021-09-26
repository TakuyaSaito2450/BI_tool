from django.db import models

# Create your models here.


class ExcelModel(models.Model):
    name = models.CharField('名前', max_length=100)

    class Meta:
        db_table = 'excel'
        verbose_name = '食べ物'
        verbose_name_plural = '食べ物一覧'

    def __str__(self):
        return self.name


class Prefectures(models.Model):
    name = models.CharField("都道府県名", max_length=30, blank=False)

    def __str__(self):
        return str(self.name)


class Littering(models.Model):
    objects = None
    prefectures = models.ForeignKey(Prefectures, on_delete=models.PROTECT)
    collection_date = models.DateField("回収日")
    bottles = models.IntegerField("ペットボトル", default=0)
    tobacco = models.IntegerField("タバコ", default=0)
    can = models.IntegerField("空き缶", default=0)

    def __str__(self):
        return str(self.prefectures)

    def total_rubbish(self):
        l = self.bottles + self.tobacco + self.can
        return l
