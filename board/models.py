from django.db import models

# Create your models here.
from user.models import User


class Board(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    hit = models.IntegerField(default=0)
    regdate = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # User는 User table이다. CASCADE는 User 테이블에서 삭제되었을 때 보드 테이블에서도 함께 삭제되는 것

    def __str__(self):
        return "Board(%s, %s, %d, %s, %d)" % (self.title,
                                              self.content,
                                              self.hit,
                                              str(self.regdate),
                                              self.user.id)