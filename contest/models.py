from django.db import models
from django.conf import settings
from koj.models import Problem, Submit, Language


# Create your models here.
class Contest(models.Model):
    contest_id = models.AutoField('대회 번호', null=False, primary_key=True)
    title = models.CharField('제목', max_length=128)
    winner = models.CharField('우승자', max_length=128, null=True, blank=True)
    start_time = models.DateTimeField('시작 시간', null=False)
    end_time = models.DateTimeField('종료 시간', null=False)
    ongoing = models.BooleanField('진행여부', default=False)
    private = models.BooleanField('비공개 대회 여부', default=False)
    participant = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='contest_participants')
    lang = models.ManyToManyField(Language, related_name='contest_language')
    penalty = models.IntegerField('오답 패널티', default=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '대회'


class ConProblem(models.Model):
    conp_id = models.AutoField(null=False, primary_key=True)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('contest', 'problem')


class ParticipantsSolved(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    participants = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    problems = models.ForeignKey(Problem, on_delete=models.CASCADE)
    is_solved = models.BooleanField('정답여부', default=False)
    solved_time = models.TimeField('푼 시간', null=True)
    mistakes = models.IntegerField('오답 횟수', default=0)

    class Meta:
        verbose_name_plural = '참자가가 푼 문제'
