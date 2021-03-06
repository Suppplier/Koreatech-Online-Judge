from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
import hashlib
import time


# Create your models here.
class Language(models.Model):
    name = models.CharField('언어', max_length=20)
    filename = models.CharField('파일명', default='', max_length=32)
    compile_option = models.CharField('컴파일 옵션', default='', max_length=256)
    exe = models.CharField('실행 바이너리', default='', max_length=32)
    args = models.CharField('명령 인수', default='', max_length=256, blank=True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural = '언어'


class Problem(models.Model):
    prob_id = models.IntegerField('문제 번호', null=False, unique=True)  # autofield?, (unique=True)
    title = models.CharField('제목', max_length=256)
    body = models.TextField('본문')
    input = models.TextField('입력')
    output = models.TextField('출력')
    time_limit = models.IntegerField('시간 제한 (초)', default=1)
    memory_limit = models.IntegerField('메모리 제한 (MB)', default=128)
    made_by = models.CharField('작성자', default='admin', max_length=32)
    is_closed = models.BooleanField('비공개 여부', default=False)

    def __str__(self):
        return str(self.prob_id)

    class Meta:
        verbose_name_plural = '문제'


def prob_path(instance, filename):
    return f'testcase/{instance.problem}/{hashlib.sha256(str(time.time()).encode()).hexdigest()}.txt'


class Testcase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input_data = models.FileField('입력 데이터', upload_to=prob_path)
    output_data = models.FileField('정답 데이터', upload_to=prob_path)
    is_example = models.BooleanField('예시로 사용', default=False)

    def __str__(self):
        return str(self.problem)

    class Meta:
        verbose_name_plural = '테스트케이스'


class Submit(models.Model):

    class SubmitResult(models.IntegerChoices):
        AC = 0
        WA = 1
        TLE = 2
        MLE = 3
        OLE = 4
        CE = 5
        RE = 6
        ER = 7
        ING = 8

    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lang = models.ForeignKey(Language, verbose_name='언어', null=False, on_delete=models.DO_NOTHING)
    code = models.TextField('코드', null=False)
    length = models.IntegerField('길이', null=False)
    time = models.DateTimeField('제출 시간', null=False)

    result = models.IntegerField('결과', null=True, choices=SubmitResult.choices)
    memory = models.IntegerField('메모리', null=True)
    runtime = models.IntegerField('시간', null=True)

    for_contest = models.BooleanField('대회용 제출', default=False)
    contest_id = models.IntegerField('대회 번호', null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = '제출 이력'
