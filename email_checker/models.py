from django.db import models

class EmailVerificationResult(models.Model):
    email = models.EmailField(unique=True)
    is_valid = models.BooleanField(default=False)
    verification_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - Valid: {self.is_valid}"