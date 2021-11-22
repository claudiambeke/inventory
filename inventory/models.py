from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

class Stores(BaseModel):
    uuid=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store_name=models.TextField()
    user_uuid=models.UUIDField()
    location_uuid=models.UUIDField()

class Products(BaseModel):
    uuid=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name=models.TextField()
    price=models.TextField()
    store_uuid=models.ForeignKey(
        Stores,
        on_delete=models.CASCADE,
        null=False
    )
    quantity=models.TextField()
    image=models.ImageField()

