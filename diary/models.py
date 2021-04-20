from django.db import models


class diaryModel(models.Model):
    user = models.ForeignKey(
        'accounts.User', related_name='diary', on_delete=models.CASCADE
        )
    diary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()


class todoModel(models.Model):
    SUCCESS = 'S'
    FAIL = 'F'
    STATUS_CHOICE = [
        (SUCCESS, '성공'),
        (FAIL, '실패')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default=FAIL)
    user = models.ForeignKey(
        'accounts.User', related_name='todo', on_delete=models.CASCADE
        )
    todo = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['end_date']