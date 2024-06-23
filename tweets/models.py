from django.db import models
from django.contrib.auth.models import User
from utils.time_helpers import utc_now


class Tweet(models.Model):
    # who post this tweet
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             null=True,
                             help_text='who posts this tweet', )
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # composite index
        # create a new datasheet:
        # (user1,created_at1,id1)
        # (user1,created_at2,id2)
        # (user2,created_at3,id3)
        # (user3,created_at4,id4)

        index_together = (('user', 'created_at'),)
        ordering = ('user', '-created_at')

    @property
    def hours_to_now(self):
        # self.created_at has time zone info and datetime.now doesnot
        return (utc_now() - self.created_at).seconds // 3600

    def __str__(self):
        return f'{self.created_at}{self.user}{self.content}'
