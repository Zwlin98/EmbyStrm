from django.db import models


# Create your models here.
class Bangumi(models.Model):
    tmdbid = models.CharField(max_length=20, verbose_name="TMDB ID")
    name = models.CharField(max_length=255, verbose_name="番剧名")
    chinese_name = models.CharField(max_length=255, verbose_name="中文名")
    year = models.IntegerField(verbose_name="年份")
    season = models.IntegerField(verbose_name="季")
    episodes = models.IntegerField(verbose_name="剧集数")

    class Meta:
        verbose_name = "番剧"
        verbose_name_plural = "番剧"

    def __str__(self):
        return "{name} ({year}) Season {season}".format(name=self.name, year=self.year, season=self.season)


class StorageInfo(models.Model):
    bangumi = models.ForeignKey(Bangumi, on_delete=models.CASCADE, verbose_name="番剧")
    folder_path = models.CharField(max_length=255, verbose_name="存储路径")
    folder = models.TextField(verbose_name="文件夹")
    episode_name_format = models.TextField(verbose_name="剧集文件模版")
    ass_path = models.CharField(max_length=255, blank=True, verbose_name="字幕存储路径")
    ass_folder = models.TextField(blank=True, verbose_name="字幕文件夹")
    ass_name_format = models.TextField(blank=True, verbose_name="字幕文件模版")

    class Meta:
        verbose_name = "番剧存储信息"
        verbose_name_plural = "番剧存储信息"

    def __str__(self):
        return "Storage of 「{0}」".format(self.bangumi.__str__())
