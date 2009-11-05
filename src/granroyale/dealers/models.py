from django.db import models

# Create your models here.

class Dealer (models.Model):
    STATES = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'), 
        ('NE', 'Nebraska'), 
        ('NV', 'Nevada'), 
        ('NH', 'New Hampshire'), 
        ('NJ', 'New Jersey'), 
        ('NM', 'New Mexico'), 
        ('NY', 'New York'), 
        ('NC', 'North Carolina'), 
        ('ND', 'North Dakota'), 
        ('OH', 'Ohio'), 
        ('OK', 'Oklahoma'), 
        ('OR', 'Oregon'), 
        ('PA', 'Pennsylvania'), 
        ('RI', 'Rhode Island'), 
        ('SC', 'South Carolina'), 
        ('SD', 'South Dakota'), 
        ('TN', 'Tennessee'), 
        ('TX', 'Texas'), 
        ('UT', 'Utah'), 
        ('VT', 'Vermont'), 
        ('VA', 'Virginia'), 
        ('WA', 'Washington'), 
        ('WV', 'West Virginia'), 
        ('WI', 'Wisconsin'), 
        ('WY', 'Wyoming'),)

    name = models.CharField(max_length=100) 
    products = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    website = models.URLField(max_length=250, blank=True)

    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default='United States')
    state = models.CharField(max_length=2, choices=STATES)
    zipcode = models.CharField(max_length=5, help_text="5 digit zip code", blank=True)
    
    phone = models.CharField(max_length=15, help_text="Please use the format: <em>XXX-XXX-XXXX</em>")
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ("country", "state", "city", "name",)
