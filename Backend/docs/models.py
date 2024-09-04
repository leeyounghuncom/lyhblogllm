from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from unidecode import unidecode
from django.db.models.signals import pre_save

class LyhDoc(models.Model):
    id = models.BigAutoField(primary_key=True)
    doc_title = models.TextField()
    doc_content = models.TextField()
    doc_name = models.CharField(max_length=200, blank=True, unique=True)
    doc_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.doc_date:
            # 날짜 데이터가 입력되지 않은 경우 전체 날짜와 시간을 현재 시간으로 설정
            self.doc_date = timezone.now()
        else:
            # 날짜는 입력된 값 사용, 시간은 현재 시간으로 설정
            now = timezone.now()
            self.doc_date = self.doc_date.replace(hour=now.hour, minute=now.minute, second=now.second, microsecond=now.microsecond)

        if not self.doc_name:
            self.doc_name = self.generate_slug()

        super().save(*args, **kwargs)

    def generate_slug(self):
        base_slug = slugify(unidecode(self.doc_title))
        slug = base_slug
        num = 1
        while LyhDoc.objects.filter(doc_name=slug).exists():
            slug = f"{base_slug}-{num}"
            num += 1
            if len(slug) > 200:
                slug = slug[:200]
                break
        return slug

def pre_save_lyhdoc_receiver(sender, instance, *args, **kwargs):
    if not instance.doc_name:
        instance.doc_name = instance.generate_slug()

pre_save.connect(pre_save_lyhdoc_receiver, sender=LyhDoc)
