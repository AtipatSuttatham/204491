"""
Abstract base models — ใช้ร่วมทุกโดเมน (ดู docs/database.md §1 "Abstract / mixin models")

- TimeStampedModel : created_at / updated_at
- Auditable        : marker — signal post_save/post_delete เขียน AuditLog อัตโนมัติ
                     (กลไก signal จะ wire ตอนทำ slice Audit Log — ดู docs/database.md §9)
- SoftDeleteModel  : deleted_at / deleted_by + manager ที่ซ่อนแถวที่ลบแล้ว
                     ใช้เฉพาะ Submission, QuizAttempt, Score
"""

from django.conf import settings
from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Auditable(models.Model):
    """
    Marker abstract — domain model ที่ inherit ตัวนี้จะถูกบันทึกลง AuditLog
    เมื่อ save/delete (ยังไม่ wire signal ใน chunk นี้ — ดู docs/database.md §9).
    """

    class Meta:
        abstract = True


class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        return super().update(deleted_at=timezone.now())

    def hard_delete(self):
        return super().delete()

    def alive(self):
        return self.filter(deleted_at__isnull=True)


class SoftDeleteManager(models.Manager):
    """objects — เห็นเฉพาะแถวที่ยังไม่ถูกลบ."""

    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db).filter(deleted_at__isnull=True)


class AllObjectsManager(models.Manager):
    """all_objects — เห็นทุกแถวรวมที่ลบแล้ว."""

    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db)


class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True, db_index=True)
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    objects = SoftDeleteManager()
    all_objects = AllObjectsManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False, deleted_by=None):
        # ใช้กับ Submission / QuizAttempt / Score ซึ่ง inherit TimeStampedModel ด้วยเสมอ
        self.deleted_at = timezone.now()
        self.deleted_by = deleted_by
        fields = ["deleted_at", "deleted_by"]
        if any(f.name == "updated_at" for f in self._meta.fields):
            fields.append("updated_at")
        self.save(using=using, update_fields=fields)

    def hard_delete(self, using=None, keep_parents=False):
        return super().delete(using=using, keep_parents=keep_parents)
