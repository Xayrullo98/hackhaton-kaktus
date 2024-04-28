from django.db import models
from general.models import TimeStampedMixin
from general.choices import RequestStatus

class Field(TimeStampedMixin):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Field"
        verbose_name_plural = "Fields"
        db_table = "field"

    def __str__(self):
        return self.name


class Junior(TimeStampedMixin):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    picture = models.ImageField(upload_to='media', null=True, blank=True)
    tg_id = models.IntegerField(null=True,blank=True)
    number = models.CharField(max_length=20,null=True,blank=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    technologies = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = "Junior"
        verbose_name_plural = "Juniors"
        db_table = "junior"

    def __str__(self):
        return self.name


class Mentor(TimeStampedMixin):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    picture = models.ImageField(upload_to='media', null=True, blank=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    tg_id = models.IntegerField(null=True, blank=True)
    number = models.CharField(max_length=20,null=True, blank=True)
    technologies = models.CharField(max_length=128, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Mentor"
        verbose_name_plural = "Mentors"
        db_table = "mentor"

    def __str__(self):
        return self.name


class Vacancy(TimeStampedMixin):
    name = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    type = models.IntegerField( choices=RequestStatus.choices)
    picture = models.ImageField(upload_to='media', null=True, blank=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    technologies = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"
        db_table = "vacancy"

    def __str__(self):
        return self.name


class Course(TimeStampedMixin):
    name = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    video_url = models.CharField(max_length=255, null=True, blank=True)
    picture = models.ImageField(upload_to='media', null=True, blank=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    technologies = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        db_table = "course"

    def __str__(self):
        return self.name


class Event(TimeStampedMixin):
    name = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    video_url = models.CharField(max_length=255, null=True, blank=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE,null=True, blank=True)
    picture = models.ImageField(upload_to='media')
    status = models.BooleanField(null=True,blank=True,default=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        db_table = "event"

    def __str__(self):
        return self.name


class Comment(TimeStampedMixin):
    text = models.TextField(null=True, blank=True)
    mentor = models.IntegerField(null=True, blank=True)
    junior = models.IntegerField(null=True, blank=True)
    event = models.IntegerField(null=True, blank=True)
    source = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        db_table = "comment"

    def __str__(self):
        return self.text


class Project(TimeStampedMixin):
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='media', null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True,default=0)
    requirements = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        db_table = "project"

    def __str__(self):
        return self.text


class Referral(TimeStampedMixin):
    text = models.TextField(null=True, blank=True)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    junior = models.ForeignKey(Junior, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Referral"
        verbose_name_plural = "Referrals"
        db_table = "referral"

    def __str__(self):
        return self.text


class Article(TimeStampedMixin):
    name = models.CharField(max_length=255,null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, null=True, blank=True)
    picture = models.ImageField(upload_to='media', null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        db_table = "article"

    def __str__(self):
        return self.text

from django.db.models.signals import post_save
from django.dispatch import receiver

from general.bot import send_telegram_message
from general.keys import TOKEN
 


@receiver(post_save, sender=Vacancy)
def send_notification(sender, instance, created, **kwargs):
    if created:
        field_id = instance.field.id
        juniors = Junior.objects.filter(field_id=field_id)
        for junior in juniors:
            full_text = f"{instance.name}\n" \
                        f"{instance.text}\n" \
                        f"{instance.technologies}"
            send_telegram_message(bot_token=TOKEN,chat_id=junior.tg_id,message_text=full_text)


