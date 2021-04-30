from django.conf import settings
from django.db import models
from django.shortcuts import reverse





#its a tuple
LABEL_CHOICES =(
    ('P', 'primary'), # first database, second to be displayed 
    ('S', 'secondary'), 
    ('D', 'danger'),  
)



CATEGORY_CHOICES =(
    ('S', 'Shirt'), # first database, second to be displayed 
    ('SW', 'Sport Wear'), 
    ('OW', 'Outwear'),  
)



class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    slug = models.SlugField()
    image = models.ImageField(upload_to='photo/')
    description = models.TextField()
    # quantity = models.IntegerField(default=1)
    
    
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shop:product", kwargs={"slug": self.slug})#shop app_name, product name urls

    def get_add_to_cart_url(self):
        return reverse("shop:add-to-cart", kwargs={"slug": self.slug})

    def get_remove_from_cart_url(self):
        return reverse("shop:remove-from-cart", kwargs={"slug": self.slug})



class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item,  on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    

class Order(models.Model):
    #associate an order with a user
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    
    # def __str__(self):
    #     return self.user.email
    
