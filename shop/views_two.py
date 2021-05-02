# import  stripe
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



# stripe.api_key = settings.STRIPE_SECRET_KEY 





class PaymentView(View):
    
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        context={"order": order}
        return render(self.request, "shop/payment.html", context)
    
    # def post(self, *args, **kwargs):
    #     order = Order.objects.get(user=self.request.user, ordered=False)
    #     token = self.request.POST.get('stripeToken') #got from js 
    #     amount = int(order.get_total() * 100)
        
    #     try:
                
    #         charge = stripe.charge.create(
    #             amount =  amount,
    #             currency ="usd",
    #             source= token,
                
    #         )
            
    #         # create the payment 
    #         payment = Payment()
    #         payment.stripe_charge_id = charge['id']
    #         payment.user = self.request.user
    #         payment.amount = amount
    #         payment.save()
            
    #         # now we have payment we must assign it to the order
    #         order.ordered = True
    #         order.payment = payment
    #         order.save()
            
    #         messages.success(self.request, "Your order was successful")
    #         return redirect("/")
            
    #     except stripe.error.CardError as e:
    #         body = e.Json_body
    #         err = body.get('error', {})
    #         messages.error(self.request, f"{err.get('message')}")
    #         return redirect("/")
            
    #     except stripe.error.RateLimitError as e:
    #         messages.error(self.request, "Rate limit error ")
    #         return redirect("/")
        
    #     except stripe.error.InvalidRequestError as e:
    #         messages.error(self.request, " Invalid parameters")
    #         return redirect("/")
        
    #     except stripe.error.AuthenticationError as e:
    #         messages.error(self.request, "Not Authenticate")
    #         return redirect("/")
        
    #     except stripe.error.APIConnectionError as e:
    #         messages.error(self.request, "Network Error ")
    #         return redirect("/")
        
    #     except stripe.error.StripeError as e:
    #         messages.error(self.request, "You were not Charge Please Try again ")
    #         return redirect("/")
        
    #     except Exception as e:
    #         messages.error(self.request, "You habeen notify for this error  ")
    #         return redirect("/")
    