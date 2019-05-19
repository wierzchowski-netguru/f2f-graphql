from django.contrib.auth.models import AbstractUser
from django.db import models


class CreatedAtUpdatedAtModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(AbstractUser, CreatedAtUpdatedAtModel):
    pass

    def __str__(self):
        return f"User[id={self.id}, username={self.username}]"


class Forum(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"Forum[id={self.id}, name={self.name}]"


class Thread(CreatedAtUpdatedAtModel):
    name = models.CharField(max_length=255)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='threads')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='threads')
    followers = models.ManyToManyField(User, blank=True, related_name='threads_followed')
    views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Thread[id={self.id}, name={self.short_name}]"

    @property
    def short_name(self):
        if len(self.name) < 20:
            return self.name
        return f"{self.name[:20]} (...)"


class Post(CreatedAtUpdatedAtModel):
    text = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    users_mentioned = models.ManyToManyField(User, blank=True, related_name='posts_mentioned_in')
    users_quoted = models.ManyToManyField(User, blank=True, related_name='posts_quoted_in')
    starred_by = models.ManyToManyField(User, blank=True, related_name='posts_starred')

    def __str__(self):
        return f"Post[id={self.id}, text={self.short_text}]"

    @property
    def short_text(self):
        if len(self.text) < 20:
            return self.text
        return f"{self.text[:20]} (...)"
