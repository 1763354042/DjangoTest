from django.db import models


class Article(models.Model):
    articleid = models.IntegerField(db_column='articleId', primary_key=True)  # Field name made lowercase.
    ariticleaddress = models.CharField(db_column='ariticleAddress', max_length=255)  # Field name made lowercase.
    keyword = models.CharField(db_column='keyWord', max_length=255)  # Field name made lowercase.
    mainbody = models.TextField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'article'


class Articlecomment(models.Model):
    articleid = models.ForeignKey(Article, models.DO_NOTHING, db_column='articleId')  # Field name made lowercase.
    commentid = models.IntegerField(db_column='commentId', primary_key=True)  # Field name made lowercase.
    commentbody = models.CharField(db_column='commentBody', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'articlecomment'
        unique_together = (('commentid', 'articleid'),)


class AvgSalary(models.Model):
    keyword = models.CharField(db_column='keyWord', max_length=255)  # Field name made lowercase.
    avgsalary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'avg_salary'


class Citylist(models.Model):
    city = models.CharField(max_length=255)
    value = models.FloatField()
    keyword = models.CharField(db_column='keyWord', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'citylist'


class Citysalary(models.Model):
    keyword = models.CharField(db_column='keyWord', max_length=255)  # Field name made lowercase.
    city = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'citysalary'


class Dendrogram(models.Model):
    nodeid = models.ForeignKey('Node', models.DO_NOTHING, db_column='nodeId', primary_key=True)  # Field name made lowercase.
    language_postid = models.ForeignKey('LanguagePost', models.DO_NOTHING
, db_column='language_postId')  # Field name made lowercase.
    nodeinsideid = models.CharField(db_column='nodeInsideId', max_length=
255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dendrogram'
        unique_together = (('nodeid', 'language_postid'),)


class LanguagePost(models.Model):
    language_postid = models.IntegerField(db_column='language_postId', primary_key=True)  # Field name made lowercase.
    language_postname = models.CharField(db_column='language_postName', max_length=255)  # Field name made lowercase.
    state = models.IntegerField()
    essayid = models.IntegerField(db_column='essayId', blank=True, null=True)  # Field name made lowercase.
    introduceid = models.IntegerField(db_column='introduceId', blank=True
, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'language_post'


class News(models.Model):
    date = models.DateTimeField(primary_key=True)
    newsaddress = models.CharField(db_column='newsAddress', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'news'


class Node(models.Model):
    nodeid = models.IntegerField(db_column='nodeId', primary_key=True)  #Field name made lowercase.
    nodename = models.CharField(db_column='nodeName', max_length=255)  #Field name made lowercase.
    essayid = models.IntegerField(db_column='essayId', blank=True, null=True)  # Field name made lowercase.
    introduceid = models.IntegerField(db_column='introduceId', blank=True
, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'node'


class Nodedatum(models.Model):
    nodeid = models.ForeignKey(Node, models.DO_NOTHING, db_column='nodeId', primary_key=True)  # Field name made lowercase.
    datumid = models.IntegerField(db_column='datumId')  # Field name made lowercase.
    datumaddress = models.CharField(db_column='datumAddress', max_length=255)  # Field name made lowercase.
    datumimgaddress = models.CharField(db_column='datumImgAddress', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nodedatum'
        unique_together = (('nodeid', 'datumid'),)


class Salaryrange(models.Model):
    keyword = models.CharField(db_column='keyWord', max_length=255)  # Field name made lowercase.
    range = models.IntegerField()
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'salaryrange'


class Searchdata(models.Model):
    datanumber = models.IntegerField(db_column='dataNumber', primary_key=
True)  # Field name made lowercase.
    language_postid = models.ForeignKey(LanguagePost, models.DO_NOTHING,
db_column='language_postId')  # Field name made lowercase.
    positionname = models.CharField(db_column='positionName', max_length=
255)  # Field name made lowercase.
    city = models.CharField(max_length=255)
    salary = models.IntegerField()
    companyshortname = models.CharField(db_column='companyShortName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'searchdata'
