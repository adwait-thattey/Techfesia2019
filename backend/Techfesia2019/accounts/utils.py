from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.db import connection
from django.template.loader import render_to_string
from django.utils import six
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from base.decorators import run_in_background

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.email_confirmed)
        )

account_activation_token = AccountActivationTokenGenerator()

@run_in_background
def send_account_activation_email(request, user_instance):
    current_site = get_current_site(request)
    email_subject = "Activate Your TechFesia2k18 Account "
    email_message = render_to_string('accounts/email_templates/account_activation_email_template.html',
                                     {'user_fullname': user_instance.get_full_name(),
                                      'username':user_instance.username,
                                      'domain': current_site.domain,
                                      'uid': urlsafe_base64_encode(force_bytes(user_instance.pk)),
                                      'token': account_activation_token.make_token(
                                          user_instance),
                                      })

    user_instance.email_user(email_subject, email_message)
    connection.close()
    return



