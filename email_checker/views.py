from . import models
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .email_service import EmailValidationService

import os
from dotenv import load_dotenv


@api_view(['POST'])
def verify_email(request):
    email = request.data.get('email')
    if EmailValidationService.validate_email(email):
        load_dotenv()
        api_key = os.getenv('ACCESS_TOKEN')
        url = f'https://api.hunter.io/v2/email-verifier?email={email}&api_key={api_key}'   
        response = requests.get(url)
        verification_result = response.json()    
        if verification_result.get('data', {}).get('result') == 'deliverable':
            result = models.EmailVerificationResult.objects.create(email=email, is_valid=True)
            return Response({'status': 'success', 'message': 'Email verified successfully'})
        else:
            return Response({'status': 'error', 'message': 'Email verification failed'})



@api_view(['POST'])
def create_email_result(request):
    email = request.data.get('email')
    is_valid = request.data.get('is_valid')
    result = models.EmailVerificationResult.objects.create(email=email, is_valid=is_valid)
    return Response({'status': 'success', 'message': 'Email result created successfully'})

@api_view(['GET'])
def get_email_result(request, email_id):
    try:
        result = models.EmailVerificationResult.objects.get(pk=email_id)
        return Response({'email': result.email, 'is_valid': result.is_valid})
    except models.EmailVerificationResult.DoesNotExist:
        return Response({'status': 'error', 'message': 'Email result not found'}, status=404)
@api_view(['PUT'])
def update_email_result(request, email_id):
    try:
        result = models.EmailVerificationResult.objects.get(pk=email_id)
        result.is_valid = request.data.get('is_valid')
        result.save()
        return Response({'status': 'success', 'message': 'Email result updated successfully'})
    except models.EmailVerificationResult.DoesNotExist:
        return Response({'status': 'error', 'message': 'Email result not found'}, status=404)
@api_view(['DELETE'])
def delete_email_result(request, email_id):
    try:
        result = models.EmailVerificationResult.objects.get(pk=email_id)
        result.delete()
        return Response({'status': 'success', 'message': 'Email result deleted successfully'})
    except models.EmailVerificationResult.DoesNotExist:
        return Response({'status': 'error', 'message': 'Email result not found'}, status=404)

@api_view(['GET'])
def get_all_email_result(request):
    try:
        results = models.EmailVerificationResult.objects.all()
        serialized_results = []
        for result in results:
            serialized_results.append({'email': result.email, 'is_valid': result.is_valid})
        return Response(serialized_results)
    except models.EmailVerificationResult.DoesNotExist:
        return Response({'status': 'error', 'message': 'Email result not found'}, status=404)
