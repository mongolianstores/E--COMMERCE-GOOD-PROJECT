
from    django.conf                         import      settings
from    django.contrib                      import      messages
from    django.core.exceptions              import      ObjectDoesNotExist
from    django.contrib.auth.decorators      import      login_required
from    django.contrib.auth.mixins          import      LoginRequiredMixin
from    django.shortcuts                    import      render, get_object_or_404, redirect
from    django.views.generic                import      ListView, DetailView, View
from    django.utils                        import      timezone
from    .models                             import      Item , OrderItem, Order, BillingAddress, Payment
from    .forms                              import      CheckoutForm







class HomeView(ListView):
    model = Item
    template_name = 'shop/home-page.html'
    #pagination
    paginate_by = 10



class OrderSummaryView(LoginRequiredMixin, View):
    
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = { 'object': order }
            template_name ='shop/order_summary.html'
            return render(self.request,  template_name  , context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("/")
        




class ItemDetailView(DetailView):
    model = Item
    template_name ='shop/product-page.html'




class CheckoutView(View):
    
    def  get(self, *args, **kwargs):
        form =  CheckoutForm()
        
        template_name ='shop/checkout-page.html'
        context = {'form': form }
        return render(self.request, template_name, context)

    def  post(self, *args, **kwargs):
        form =  CheckoutForm(self.request.POST or None ) 
        # print(self.request.POST)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                # clean data before saving them in database 
                street_address = form.cleaned_data.get("street_address")
                country = form.cleaned_data.get("country")
                apartment_address = form.cleaned_data.get("apartment_address")
                zip = form.cleaned_data.get("zip")
                # TODO later 
                # same_shipping_address = form.cleaned_data.get("same_billing_address")
                # save_info = form.cleaned_data.get("save_info")
                
                billing_address = BillingAddress(
                    user = self.request.user,
                    street_address = street_address,
                    apartment_address  = apartment_address, 
                    country = country,  
                    zip = zip,
                    
                )
                
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                
            #     if payment_option == "S": #S stripe
            #         return redirect('shop:payment', payment_option='stripe')
            #     elif payment_option == "P": # P paypal
            #         return redirect('shop:payment', payment_option='paypal')
            # else:
            #     messages.warning(self.request, "Invalid Payment option selected")
            #     return redirect('shop:checkout')
            
                
            messages.warning(self.request, "Failed Checkout")
            return redirect('shop:checkout')
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("shope:order-summary-view")





# add item to the cart
@login_required
def add_to_cart(request, slug=None):# slug of item add specific item 
    item = get_object_or_404(Item, slug=slug)
    
    #if the user dont have an order we create here
    order_item , created = OrderItem.objects.get_or_create(
        item=item,
        user= request.user,
        ordered=False # no items has been purchased
        
        )
    
    # now check if the user has a order and we modify the quantity of order_item in the order
    order_qs = Order.objects.filter(user=request.user, ordered=False)# we getting the order that has not been completed 
    # beacuse there is some order completed 
    
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():# this item is already in the card # lower case to access the parent //order.items.filter = Order<class>dot<his_field> bcz the OrderItem parent want toaccess his child that why it in lower case
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("shop:order-summary-view")    
        else:
            messages.info(request, "This item was added to your cart")
            order.items.add(order_item)
            return redirect("shop:order-summary-view")
    # if the order dont exits 
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user,  ordered_date= ordered_date)
        order.items.add(order_item )
        messages.info(request, "This item was added to your cart")
    return redirect("shop:order-summary-view")




@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    
    # if there is a user not order yet 
    order_qs = Order.objects.filter(user=request.user, ordered=False)#   
    if order_qs.exists(): # if it exist 
        order = order_qs[0] # we grab that order
    
        if order.items.filter(item__slug=item.slug).exists():# we filter the order for that specif item slug
            order_item = OrderItem.objects.filter(
                item=item,
                user= request.user,
                ordered=False # no items has been purchased
                )[0]
            order.items.remove(order_item) # then we remove it 
            messages.info(request, "This item was removed from your cart")
            return redirect("shop:order-summary-view")
        else:
            messages.info(request, "This item was not in to your cart")
            return redirect("shop:product", slug = slug)
            
    else:
        messages.info(request, "You do not havean active order")
        return redirect("shop:product", slug = slug)
    



@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)#   
    if order_qs.exists(): # if it exist 
        order = order_qs[0] # we grab that order
    
        if order.items.filter(item__slug=item.slug).exists():# we filter the order for that specif item slug
            order_item = OrderItem.objects.filter(
                item=item,
                user= request.user,
                ordered=False # no items has been purchased
                )[0]
            
            # logic for minus must be 1 no less than that 
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
                
            messages.info(request, "This item quantity was updated")
            return redirect("shop:order-summary-view")
        else:
            messages.info(request, "This item was not in to your cart")
            return redirect("shop:product", slug = slug)
            
    else:
        messages.info(request, "You do not havean active order")
        return redirect("shop:product", slug = slug)
    
