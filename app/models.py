from django.db import models

from users.models import User


class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

    # 記事タイトル
    title = models.CharField(
        verbose_name='記事のタイトル',
        max_length=128,
        blank=False,
        null=False,
    )

    # 投稿日付
    post_date = models.DateField(
        verbose_name='投稿日付',
        blank=False,
        null=False,
    )

    # ハッシュタグ
    hashtag = models.CharField(
        verbose_name='#hashtag',
        blank=True,
        null=True,
    )

    # 記事内容
    context = models.TextField(
        verbose_name='記事の内容ß',
        blank=True,
        null=True,
    )

    # おすすめフラグ
    recommended = models.BooleanField(
        verbose_name='おすすめフラグ',
        blank=True,
        null=True,
    )

    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.title

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'サンプル'
        verbose_name_plural = 'サンプル'
