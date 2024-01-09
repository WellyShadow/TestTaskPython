"""Module with views for email verification."""

import os

import requests
from dotenv import load_dotenv
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models
from .email_service import EmailValidationService
from .utils.constant import NOT_FOUND_STATUS


@api_view(['POST'])
def verify_email(request):
    """Verify email."""
    email = request.data.get('email')
    if EmailValidationService.validate_email(email):
        load_dotenv()
        api_key = os.getenv('ACCESS_TOKEN')
        url = 'https://api.hunter.io/v2/email-verifier?email={0}&api_key={1}'.format(email, api_key)
        response = requests.get(url, timeout=10)
        verification_result = response.json()
        if verification_result.get('data', {}).get('result') == 'deliverable':
            return Response({'is_valid': 'True', 'message': 'Email verified successfully'})
        return Response({'is_valid': 'False', 'message': 'Email verification failed'})


@api_view(['POST'])
def create_email_result(request):
    """Create result."""
    email = request.data.get('email')
    is_valid = request.data.get('is_valid')
    request_results = models.EmailVerificationResult.objects.create(email=email, is_valid=is_valid)
    return Response({'status': 'success', 'message': 'Email result created successfully'})


@api_view(['GET'])
def get_email_result(request, email_id):
    """Read some result."""
    try:
        request_results = models.EmailVerificationResult.objects.get(pk=email_id)
        return Response({'email': request_results.email, 'is_valid': request_results.is_valid})
    except models.EmailVerificationResult.DoesNotExist:
        return Response({'status': 'error', 'message': 'Email result not found'}, status=NOT_FOUND_STATUS)


@api_view(['PUT'])
def update_email_result(request, email_id):
    """Update result."""
    try:
        request_results = models.EmailVerificationResult.objects.get(pk=email_id)
        request_results.is_valid = request.data.get('is_valid')
        request_results.save()
        return Response({'status': 'success', 'message': 'Email result updated successfully'})
    except models.EmailVerificationResult.DoesNotExist:
        return Response({'status': 'error', 'message': 'Email result not found'}, status=NOT_FOUND_STATUS)


@api_view(['DELETE'])
def delete_email_result(request, email_id):
    """Delete result."""
    try:
        request_results = models.EmailVerificationResult.objects.get(pk=email_id)
        request_results.delete()
        return Response({'status': 'success', 'message': 'Email result deleted successfully'})
    except models.EmailVerificationResult.DoesNotExist:
        return Response({'status': 'error', 'message': 'Email result not found'}, status=NOT_FOUND_STATUS)


@api_view(['GET'])
def get_all_email_result(request):
    """Read all result."""
    try:
        request_results = models.EmailVerificationResult.objects.all()
        serialized_results = []
        for request_result in request_results:
            serialized_results.append({'email': request_result.email, 'is_valid': request_result.is_valid})
        return Response(serialized_results)
    except models.EmailVerificationResult.DoesNotExist:
        return Response({'status': 'error', 'message': 'Email result not found'}, status=NOT_FOUND_STATUS)
