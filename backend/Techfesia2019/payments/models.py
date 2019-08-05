from django.db import models

# Create your models here.


class Transaction(models.Model):
    created_by = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, related_name='transactions')
    created_on = models.DateTimeField(auto_now_add=True)
    is_team_registration = models.BooleanField(default=False)
    team_registration = models.ForeignKey('event_registrations.TeamEventRegistration', on_delete=models.CASCADE,
                                          related_name='payments', null=True, blank=True
                                          )
    solo_registration = models.ForeignKey('event_registrations.SoloEventRegistration', on_delete=models.CASCADE,
                                          related_name='payments', null=True, blank=True
                                          )
    order_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    request_checksum = models.CharField(max_length=200)

    response_checksum = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=(('Pending', 'Pending'),
                                                      ('Failed', 'Failed'),
                                                      ('Successful', 'Successful')),
                              )

    transaction_id = models.CharField(max_length=100, null=True, blank=True)

    def generate_order_id(self):
        self.order_id = self.created_on.strftime('TCHFS%Y%m%dODR') + '{0:04d}Test'.format(self.id)
        self.save()
        return self.order_id
