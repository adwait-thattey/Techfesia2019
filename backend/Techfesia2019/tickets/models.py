from django.db import models
from base.utils import generate_random_string, generate_public_id

# Create your models here.


class Ticket(models.Model):

    # Fields Regarding User/ Query
    public_id = models.CharField(max_length=100,
                                 unique=True,
                                 blank=True,
                                 db_index=True
                                 )

    title = models.CharField(max_length=100)

    description = models.CharField(max_length=2000)

    opened_by = models.ForeignKey(to='accounts.Profile',
                                  on_delete=models.CASCADE
                                  )

    opening_date = models.DateField(auto_now=True)

    event = models.ForeignKey(to='events.Event',
                              on_delete=models.CASCADE,
                              null=True,
                              blank=True
                              )

    is_public = models.BooleanField(default=True)

    subscribers = models.ManyToManyField(to='accounts.Profile', related_name='subscribed_tickets')

    # Fields regarding Solution
    status = models.CharField(max_length=20,
                              choices=(('Opened', 'Opened'), ('In Progress', 'In Progress'), ('Solved', 'Solved')),
                              default='Opened'
                              )

    solved_by = models.ForeignKey(to='accounts.Profile',
                                  on_delete=models.CASCADE,
                                  null=True,
                                  blank=True,
                                  related_name='solved_tickets'
                                  )

    solving_date = models.DateField(null=True, blank=True)

    content = models.CharField(max_length=2000)

    @property
    def owner(self):
        return self.opened_by.user

    def save(self, *args, **kwargs):
        if self.id:
            if self.opened_by not in self.subscribers.all():
                self.subscribers.add(self.opened_by)

        if not self.public_id:
            self.public_id = generate_public_id(self)

        super().save(*args, **kwargs)


class TicketComment(models.Model):

    public_id = models.CharField(max_length=100,
                                 unique=True,
                                 blank=True,
                                 db_index=True
                                 )

    ticket = models.ForeignKey(to=Ticket,
                               on_delete=models.CASCADE,
                               related_name='comments'
                               )

    commenter = models.ForeignKey(to='accounts.Profile',
                                  on_delete=models.CASCADE,
                                  related_name='opened_tickets'
                                  )

    text = models.CharField(max_length=1000)

    posting_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.public_id:
            self.public_id = generate_public_id(self)

        super().save(*args, **kwargs)



