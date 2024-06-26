from django.db import models
from django.contrib.auth.models import User
from tweets.models import Tweet


# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    tweet = models.ForeignKey(Tweet, null=True, on_delete=models.SET_NULL)
    contents = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        index_together = (('tweet', 'created_at'))

    def __str__(self):
        return '{}-{} says {} at tweet{}'.format(
            self.created_at,
            self.user,
            self.contents,
            self.tweet_id

        )