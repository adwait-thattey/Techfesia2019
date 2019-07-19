import requests
import json
from payments.models import Transaction
from .Checksum import generate_checksum, verify_checksum
from accounts.models import User, Profile
from events.models import Event, TeamEvent, SoloEvent
from event_registrations.models import TeamEventRegistration, SoloEventRegistration
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.


@login_required
def initiate_payment(request):
    merchant_key = settings.PAYTM_SECRET_KEY
    transaction = Transaction.objects.create(created_by=request.user.profile, amount=40)
    transaction.generate_order_id()
    paytm_params = {
        'MID': settings.PAYTM_MERCHANT_ID,
        'ORDER_ID': str(transaction.order_id),
        'CUST_ID': str(transaction.created_by.user.email),
        'TXN_AMOUNT': str(transaction.amount),
        'CHANNEL_ID': settings.PAYTM_CHANNEL_ID,
        'WEBSITE': settings.PAYTM_WEBSITE,
        'INDUSTRY_TYPE_ID': settings.PAYTM_INDUSTRY_TYPE_ID,
        'CALLBACK_URL': 'http://localhost:8000/payment/callback/',
        # 'EMAIL': request.user.email,
        # 'MOBILE_N0': '9911223388',
        # 'PAYMENT_MODE_ONLY': 'NO',
    }
    checksum = generate_checksum(paytm_params, merchant_key)
    transaction.checksum = checksum
    transaction.save()
    paytm_params['CHECKSUMHASH'] = checksum

    response = render_to_string(request, 'payments/pay.html',
                                {**paytm_params, 'payment_url': settings.PAYTM_PAYMENT_URL}
                                )
    return HttpResponse(response)
    # return render(request, 'payments/pay.html', context={**paytm_params, 'payment_url': payment_url})


class PaymentInitiateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        print(request.data)
        data = dict(request.data)
        try:
            event_public_id = data['eventPublicId']
            registration_id = data['registrationId']
        except KeyError as key:
            return Response({'error': 'Missing field {0}'.format(key)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)        
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            return Response({'error': 'Profile Does Not Exist'}, status=status.HTTP_404_NOT_FOUND)
        try:
            base_event = Event.objects.get(public_id=event_public_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event Does Not exist'})
        if base_event.team_event:
            event = base_event.teamevent
            registration = TeamEventRegistration.objects.get(public_id=registration_id)
        else:
            event = base_event.soloevent
            registration = SoloEventRegistration.objects.get(public_id=registration_id)
        if base_event.team_event:
            # Confirming Registration
            if registration in event.teameventregistration_set.all():
                # Checking if payment is already complete
                if registration.is_complete or \
                Transaction.objects.filter(team_registration=registration, status='Successful').count() is not 0:
                    return Response({'message': 'Already Paid'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

                transaction = Transaction.objects.create(created_by=profile, amount=event.fee,
                                                         team_registration=registration, is_team_registration=True)
                transaction.generate_order_id()
                paytm_params = {
                    'MID': settings.PAYTM_MERCHANT_ID,
                    'ORDER_ID': str(transaction.order_id),
                    'CUST_ID': str(transaction.created_by.user.email),
                    'TXN_AMOUNT': str(transaction.amount),
                    'CHANNEL_ID': settings.PAYTM_CHANNEL_ID,
                    'WEBSITE': settings.PAYTM_WEBSITE,
                    'INDUSTRY_TYPE_ID': settings.PAYTM_INDUSTRY_TYPE_ID,
                    'CALLBACK_URL': 'http://localhost:8000/payment/callback/',
                    # 'EMAIL': request.user.email,
                    # 'MOBILE_N0': '9911223388',
                    # 'PAYMENT_MODE_ONLY': 'NO',
                }
                checksum = generate_checksum(paytm_params, settings.PAYTM_SECRET_KEY)
                transaction.checksum = checksum
                transaction.save()
                paytm_params['CHECKSUMHASH'] = checksum
                response = render_to_string('payments/pay.html',
                                            {**paytm_params, 'payment_url': settings.PAYTM_PAYMENT_URL}
                                            )
                return HttpResponse(response)
            else:
                return Response({'error': 'Registration Does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        else:
            if registration in event.soloeventregistration_set.all():

                # Checking if payment is already complete

                if registration.is_complete or Transaction.objects.filter(solo_registration=registration, status='Successful').count() is not 0:
                    return Response({'message': 'Already Paid'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

                transaction = Transaction.objects.create(created_by=profile, amount=event.fee,
                                                         solo_registration=registration)
                transaction.generate_order_id()
                paytm_params = {
                    'MID': settings.PAYTM_MERCHANT_ID,
                    'ORDER_ID': str(transaction.order_id),
                    'CUST_ID': str(transaction.created_by.user.email),
                    'TXN_AMOUNT': str(transaction.amount),
                    'CHANNEL_ID': settings.PAYTM_CHANNEL_ID,
                    'WEBSITE': settings.PAYTM_WEBSITE,
                    'INDUSTRY_TYPE_ID': settings.PAYTM_INDUSTRY_TYPE_ID,
                    'CALLBACK_URL': 'http://localhost:8000/payment/callback/',
                    # 'EMAIL': request.user.email,
                    # 'MOBILE_N0': '9911223388',
                    # 'PAYMENT_MODE_ONLY': 'NO',
                }

                checksum = generate_checksum(paytm_params, settings.PAYTM_SECRET_KEY)
                transaction.checksum = checksum
                transaction.save()
                paytm_params['CHECKSUMHASH'] = checksum
                response = render_to_string('payments/pay.html',
                                            {**paytm_params, 'payment_url': settings.PAYTM_PAYMENT_URL}
                                            )
                print(response)
                return HttpResponse(response)
            else:
                return Response({'error': 'Registration Does not exist'}, status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        # print('Request:', request)
        # print('Request Method:', request.method)
        # print('Request body:', request.body)
        print('Request POST:', request.POST)

        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key is not 'CHECKSUMHASH':
                paytm_params[key] = str(value[0])
        # Verify checksum
        try:
            is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, paytm_checksum)
        except ValueError:
            return Response({'error': 'ERROR:IVCKSUM Contact site admin'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if is_valid_checksum:
            # print("Checksum Matched")
            received_data['message'] = "Checksum Matched"
        else:
            # print("Checksum Mismatched")
            received_data['message'] = "Checksum Mismatched"
            # return Response({'error': 'Invalid Transaction'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            transaction = Transaction.objects.get(order_id=paytm_params['ORDERID'])
        except Transaction.DoesNotExist:
            return Response({'error': 'Invalid Transaction'}, status=status.HTTP_404_NOT_FOUND)

        if check_with_paytm(transaction.order_id, paytm_params) is False:
            return HttpResponse('Forged Transaction')

        transaction.response_checksum = paytm_checksum

        if paytm_params['RESPCODE'] == '01':
            transaction.status = 'Successful'
            if transaction.is_team_registration:
                registration = transaction.team_registration
            else:
                registration = transaction.solo_registration

            registration.is_complete = True
            registration.save()
            registration.event.refresh_participants()
        else:
            transaction.status = 'Failed'

        transaction.save()

        return render(request, 'payments/callback.html', context=received_data)


def check_with_paytm(order_id, received_params):
    paytm_params = dict()

    paytm_params["MID"] = settings.PAYTM_MERCHANT_ID
    paytm_params["ORDERID"] = order_id

    checksum = generate_checksum(paytm_params, settings.PAYTM_SECRET_KEY)
    paytm_params["CHECKSUMHASH"] = checksum
    post_data = json.dumps(paytm_params)

    # for Staging
    url = "https://securegw-stage.paytm.in/order/status"

    # for Production
    if settings.PAYTM_PRODUCTION:
        url = "https://securegw.paytm.in/order/status"

    response = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()
    print(response)
    print(received_params)
    is_valid = response['TXNID'] == received_params['TXNID'] \
        and response['BANKTXNID'] == received_params['BANKTXNID'] \
        and response['TXNAMOUNT'] == received_params['TXNAMOUNT'] \
        and response['STATUS'] == received_params['STATUS']
    print(is_valid)
    return is_valid


# In case of Pending/Late Transactions
def refresh_payment_status(transaction):
    paytm_params = dict()

    paytm_params["MID"] = settings.PAYTM_MERCHANT_ID
    paytm_params["ORDERID"] = transaction.order_id

    checksum = generate_checksum(paytm_params, settings.PAYTM_SECRET_KEY)
    paytm_params["CHECKSUMHASH"] = checksum
    post_data = json.dumps(paytm_params)

    # for Staging
    url = "https://securegw-stage.paytm.in/order/status"

    # for Production
    if settings.PAYTM_PRODUCTION:
        url = "https://securegw.paytm.in/order/status"

    response = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()

    transaction.response_checksum = response['CHECKSUMHASH']

    if response['RESPCODE'] == '01':
        transaction.status = 'Successful'
        if transaction.is_team_registration:
            registration = transaction.team_registration
        else:
            registration = transaction.solo_registration

        registration.is_complete = True
        registration.save()
        registration.event.refresh_participants()
    else:
        transaction.status = 'Failed'

    transaction.save()

    return
