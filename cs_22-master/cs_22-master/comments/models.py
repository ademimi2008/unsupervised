from django.db import models
from accounts.models import Account
from posts.models import Post


class Comment(models.Model):
    text = models.CharField(max_length=255, verbose_name="Комментарий")
    date = models.DateField(auto_now=True, verbose_name="Время создания")
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="account_comments", verbose_name="Аккаунт")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments", verbose_name="Пост")

    def __str__(self):
        return f"{self.account} - {self.post}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

