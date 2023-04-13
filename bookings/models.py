from django.db import models
from common.models import CommonModel

# Create your models here.


class Booking(CommonModel):
    """Booking Model Definition"""

    class BookingKindChoices(models.TextChoices):
        ROOM = "room", "Room"
        EXPERIENCE = "experience", "Experience"

    kind = models.CharField(
        max_length=15,
        choices=BookingKindChoices.choices,
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    check_in = models.DateField(
        null=True,
        blank=True,
    )
    check_out = models.DateField(
        null=True,
        blank=True,
    )
    # 시간은 room model에서 다룹니다.
    # 왜 체크인 체크아웃이 null? experience는 체크인 체크아웃이 없기 때문에
    experience_time = models.DateTimeField(
        null=True,
        blank=True,
    )

    guests = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.kind.title()} booking by - {self.user}"