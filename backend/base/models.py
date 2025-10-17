from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import F, Q


class Guest(models.Model):
    first_name = models.CharField("nombre", max_length=100)
    last_name = models.CharField("apellidos", max_length=150)
    email = models.EmailField("email", blank=True)
    phone = models.CharField("teléfono", max_length=30, blank=True)
    birth_date = models.DateField("fecha de nacimiento", null=True, blank=True)
    notes = models.TextField("notas", blank=True, help_text="Preferencias u observaciones del huésped")

    class Meta:
        verbose_name = "Huésped"
        verbose_name_plural = "Huéspedes"
        ordering = ["last_name", "first_name"]

    def __str__(self) -> str:
        full_name = f"{self.first_name} {self.last_name}".strip()
        return full_name or f"Guest #{self.pk}"

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()


class Stay(models.Model):
    class Source(models.TextChoices):
        BOOKING = "booking", "Booking"
        AIRBNB = "airbnb", "Airbnb"
        DIRECT = "direct", "Directo"
        OTHER = "other", "Otro"

    guest = models.ForeignKey(
        Guest,
        on_delete=models.CASCADE,
        related_name="stays",
        verbose_name="huésped",
    )

    check_in = models.DateField("check-in")
    check_out = models.DateField("check-out")
    companions = models.PositiveSmallIntegerField(
        "acompañantes",
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
        help_text="Número de acompañantes (sin contar al huésped principal)",
    )
    source = models.CharField(
        "fuente",
        max_length=20,
        choices=Source.choices,
        default=Source.DIRECT,
    )
    rating = models.PositiveSmallIntegerField(
        "valoración",
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Valoración del huésped de 1 a 5",
    )
    comments = models.TextField("comentarios", blank=True)

    created_at = models.DateTimeField("creado", auto_now_add=True)
    updated_at = models.DateTimeField("actualizado", auto_now=True)

    class Meta:
        verbose_name = "Estancia"
        verbose_name_plural = "Estancias"
        ordering = ["-check_in", "guest__last_name"]
        indexes = [
            models.Index(fields=["guest", "check_in"], name="stay_guest_checkin_idx"),
        ]
        constraints = [
            models.CheckConstraint(
                check=Q(check_out__gt=F("check_in")),
                name="stay_checkout_after_checkin",
            ),
        ]

    def __str__(self) -> str:
        guest_name = self.guest.full_name if self.guest_id else "(sin huésped)"
        return f"Estancia de {guest_name} del {self.check_in} al {self.check_out}"
