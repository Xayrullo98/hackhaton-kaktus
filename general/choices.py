from django.db import models


class RequestStatus(models.IntegerChoices):
    intern = 1, 'Stajirovka'
    jobs = 2, 'Ishlar'
    projects = 3, 'Loyihalar'

print(RequestStatus.values)