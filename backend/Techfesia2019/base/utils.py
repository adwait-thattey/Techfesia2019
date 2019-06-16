from base.decorators import run_in_background


@run_in_background
def send_account_activation_email(request, user_instance):
    # current_site = get_current_site(request)
    # email_subject = "Activate Your TechFesia2k18 Account "
    # email_message = render_to_string('data/account_activation_email_template.html',
    #                                  {'user_fullname': user_instance.get_full_name(),
    #                                   'domain': current_site.domain,
    #                                   'uid': urlsafe_base64_encode(
    #                                       force_bytes(
    #                                           user_instance.pk)).decode(),
    #                                   'token': account_activation_token.make_token(
    #                                       user_instance),
    #                                   })
    #
    # user_instance.email_user(email_subject, email_message)
    # connection.close()
    return
