from django.db import models

# Create your models here.


class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)
    # tip) CharField와 TextField와 같이 문자열 기반 필드에서는 null=True를 정의하는 것을 피해야한다.
    # '데이터 없음'에 대해서 None과 빈 문자열 두가지 값('None' - 이거말하는건가?)을 갖게되기 때문이다. 그러므로 blank=True를 사용하는 것이 좋다.
    # null - DB연관 // blank - 유효성 연관
