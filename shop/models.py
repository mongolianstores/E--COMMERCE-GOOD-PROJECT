from        django.conf             import      settings
from        django.db               import      models
from        django.shortcuts        import      reverse
from        django.db.models        import      Sum
#from        django_contries.fields    import      CountryField
from        django_countries.fields import CountryField


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
    title           = models.CharField(max_length=100)
    price           = models.FloatField()
    discount_price  = models.FloatField(blank=True, null=True)
    category        = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label           = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    slug            = models.SlugField()
    image           = models.ImageField(upload_to='photo/')
    description     = models.TextField()
    
    
    
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shop:product", kwargs={"slug": self.slug})#shop app_name, product name urls

    def get_add_to_cart_url(self):
        return reverse("shop:add-to-cart", kwargs={"slug": self.slug})

    def get_remove_from_cart_url(self):
        return reverse("shop:remove-from-cart", kwargs={"slug": self.slug})



class OrderItem(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered         = models.BooleanField(default=False)
    item            = models.ForeignKey(Item,  on_delete=models.CASCADE)
    quantity        = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    
    
    # method for the price 
    def get_total_item_price(self):
        return self.quantity * self.item.price 
    
    # method for discount price
    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price 
    
    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price() 
    
    # get final price 
    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()



class Order(models.Model):
    #associate an order with a user
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered         = models.BooleanField(default=False)
    items           = models.ManyToManyField(OrderItem)
    start_date      = models.DateTimeField(auto_now_add=True)
    ordered_date    = models.DateTimeField()
    #billing address must be attache to the order
    billing_address    = models.ForeignKey('BillingAddress', on_delete=models.SET_NULL, blank=True, null=True)
    payment    = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)
    
    
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
            return total 
    
    # def __str__(self):
    #     return self.user.email
    

class BillingAddress(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=150)
    apartment_address = models.CharField(max_length=150)
    country = CountryField(multiple=False)
    zip = models.CharField( max_length=150)
    
    def __str__(self):
        return self.user.username
    
class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    class Meta: # new
        indexes = [models.Index(fields=['amount'])]
        ordering = ['-amount']
        verbose_name = 'Payment' # change inside when you fill in with data 
        verbose_name_plural = 'Payment' # change naming plural ouside admin
    
    
    def __str__(self):
        return self.user.username
    
    