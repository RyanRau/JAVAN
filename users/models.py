from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass
    # Additional fields here
    forcePasswordChange = models.BooleanField(default=True)
    CLASSIFICATION = {
        (0, "Student"),
        (1, "Mentor"),
        (2, "Work Study"),
        (3, "Master Teacher"),
        (4, "Admin"),
    }
    classification = models.IntegerField(choices=CLASSIFICATION, default=0)

    def __str__(self):
        return self.username
