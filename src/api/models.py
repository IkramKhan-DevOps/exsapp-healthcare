from django.db import models


class Capture(models.Model):
    image = models.ImageField(upload_to='images/captures/')
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=False, blank=True)
    accuracy = models.FloatField(default=0)
    calories = models.FloatField(default=0)
    category = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.url

    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        super(Capture, self).delete(*args, **kwargs)


class CaloriesConsumption(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    food_item = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    calories = models.FloatField(default=0)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.food_item
