from django.contrib.auth.models import User
from django.db import models


class Profile(models.model):
    user_id = models.OneToOneField(User,
                                   on_delete=models.CASCADE, # User가 사라질 때 어떻게 되는지를 설정하는 부분
                                   related_name='profile') # request.User.profile.nickname과 같이 마더 테이블에서 부터 접근이 가능
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=100,
                                unique=True, # 유일 조건
                                null=True)
    message = models.CharField(max_length=150, null=True)


