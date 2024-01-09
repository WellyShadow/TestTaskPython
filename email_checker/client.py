"""Client for email verification."""

import requests


class EmailVerificationClient(object):
    """Define class client ."""

    def __init__(self, base_url):
        """Initialize class."""
        self.base_url = base_url

    def verify_email(self, email):
        """Verify email."""
        endpoint = '{0}/verify_email/'.format(self.base_url)
        datatojson = {'email': email}
        response = requests.post(endpoint, json=datatojson, timeout=10)
        return response.json()

    def create_email_result(self, email):
        """Create result of email verification."""
        verify_response = self.verify_email(email)
        is_valid = verify_response['is_valid']
        endpoint = '{0}/create-email-result/'.format(self.base_url)
        datatojson = {'email': email, 'is_valid': is_valid}
        response = requests.post(endpoint, json=datatojson, timeout=10)
        return response.json()

    def get_email_result(self, email_id):
        """Get some email result."""
        endpoint = '{0}/get-email-result/{1}/'.format(self.base_url, email_id)
        response = requests.get(endpoint, timeout=10)
        return response.json()

    def get_all_email_result(self):
        """Get all emails result."""
        endpoint = '{0}/get-all-email-result/'.format(self.base_url)
        response = requests.get(endpoint, timeout=10)
        return response.json()

    def update_email_result(self, email_id, is_valid):
        """Update email result."""
        endpoint = '{0}/update-email-result/{1}/'.format(self.base_url, email_id)
        datatojson = {'is_valid': is_valid}
        response = requests.put(endpoint, json=datatojson, timeout=10)
        return response.json()

    def delete_email_result(self, email_id):
        """Delete email result."""
        endpoint = '{0}/delete-email-result/{1}/'.format(self.base_url, email_id)
        response = requests.delete(endpoint, timeout=10)
        return response.json()
