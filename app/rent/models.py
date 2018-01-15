from django.db import models
from app.base.models import BaseModel


class Apartment(BaseModel):
    name = models.CharField(max_length=255, null=False,
                            blank=False)
    is_avaliable = models.BooleanField(default=True)

    def current_price(self):
        """
        Returns the last inserted price to apartment
        """
        prices = self.prices.all().reverse()
        return prices[0].value if prices else 0


class Price(BaseModel):
    value = models.DecimalField(max_digits=10, decimal_places=2)

    apartment = models.ForeignKey(
        to=Apartment,
        related_name='prices',
        related_query_name='apartment',
        on_delete=models.PROTECT
    )
