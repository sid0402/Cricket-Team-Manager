from django.db import models
from machine.models import Trades

class Comments(models.Model):
    trade = models.ForeignKey(Trades,on_delete=models.CASCADE,related_name='comments')
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return 'Comment {} at {}'.format(self.body, self.created_at)

