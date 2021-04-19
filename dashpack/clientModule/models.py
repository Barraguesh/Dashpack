from django.db import models

class Log(models.Model):
    log = models.CharField(
        max_length=1000,
        verbose_name='Log',
        primary_key=True
    )
    date = models.DateField(
        max_length=1000,
        verbose_name='Date'
    )
    def __str__(self):
        return str(self.log)

class Client(models.Model):
    client_id = models.CharField(
        max_length=1000,
        verbose_name='Client ID',
        primary_key=True
    )
    name = models.CharField(
        max_length=1000,
        verbose_name='Name'
    )
    def __str__(self):
        return str(self.client_id)

class Device(models.Model):
    device_id = models.CharField(
        max_length=100,
        verbose_name='Device ID',
        primary_key=True
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Name'
    )   
    client = models.ForeignKey(
        'Client',
        on_delete=models.PROTECT,
        verbose_name='Client'
    )
    category = models.CharField(
        max_length=100,
        verbose_name='Category'
    )
    entry_date = models.DateField(
        verbose_name='Entry date'
    )
    def __str__(self):
        return str(self.device_id)

class Ticket(models.Model):
    ticket_id = models.CharField(
        max_length=1000,
        verbose_name='Ticket ID',
        primary_key=True
    )
    description = models.CharField(
        max_length=1000,
        verbose_name='Description'
    )
    log = models.TextField(
        verbose_name='Log'
    )
    comment = models.TextField(
        verbose_name='Comment'
    )
    priority = models.IntegerField(
        verbose_name='Priority'
    )
    client = models.ForeignKey(
        'Client',
        on_delete=models.PROTECT,
        verbose_name='Client'
    )
    device = models.ForeignKey(
        'Device',
        on_delete=models.PROTECT,
        verbose_name='Device'
    )
    date = models.DateField(
        max_length=1000,
        verbose_name='Date'
    )
    def __str__(self):
        return str(self.ticket_id)