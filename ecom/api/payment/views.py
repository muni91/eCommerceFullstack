from django.contrib.auth.backends import UserModel
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

import braintree

# Create your views here.

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="krmtfkcpdz6n7wzw",
        public_key="3vtqv7b5zmj8vw42",
        private_key="d39ac4b8fd4209b5bd203b0244722d18"
    )
)

def validate_user(id, token):
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False

@csrf_exempt
def generate_token(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error':'Invalid session, please login'})
    return JsonResponse({'client':gateway.client_token.generate(), 'success':'True'})


@csrf_exempt
def process_payment(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error':'Invalid session, please login'})
    
    nonce_from_the_client = request.POST["paymentMethodNonce"]
    amount_from_the_client = request.POST["amount"]

    result = gateway.transaction.sale({
    "amount": amount_from_the_client,
    "payment_method_nonce": nonce_from_the_client,
    "options": {
      "submit_for_settlement": True
    }
    })

    if result.is_success:
        return JsonResponse({
            "success":result.is_success,
            'transaction':{
                'id': result.transaction.id,
                'amount':result.transaction.amount
            }
        })
    else:
        return JsonResponse({'error':True, 'success':False})