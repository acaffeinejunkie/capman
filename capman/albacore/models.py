from django.db import models

# Create your models here.

class Provider(models.Model):
  name = models.CharField(max_length=100)
  
class Switch(models.Model):
  name = models.CharField(max_length=50)
  model = models.CharField(max_length=50)
  num_ports = models.IntegerField()

class SwitchPort(models.Model):
  name = models.CharField(max_length=2)
  switch = models.ForeignKey(Switch, related_name='switch')
  speed = models.IntegerField()

class Circuit(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=500)
  vlan_id = models.IntegerField()
  direct_provider = models.ForeignKey(Provider, related_name='direct_prov')
  cdr = models.IntegerField()
  bearer = models.IntegerField()
  pbdemuxport = models.ForeignKey(SwitchPort, related_name='pbdmuxport')
  metroeport = models.ForeignKey(SwitchPort, related_name='metroeport') 
  
class Datacentre(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=500)

class Interconnect(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=500)  
  pbdemuxport = models.ForeignKey(SwitchPort)
  provider = models.ForeignKey(Provider, related_name='int_direct_prov')
  dc = models.ForeignKey(Datacentre, related_name='int_dc')
  is_open = models.BooleanField()
  capacity = models.IntegerField()

class Site(models.Model):
  name = models.CharField(max_length=100)
  operator = models.ForeignKey(Switch, related_name='op')
  primary = models.ForeignKey(Circuit, related_name='pri_cct')
  backup = models.ForeignKey(Circuit, related_name='sec_cct')

class Operator(models.Model):
  name = models.CharField(max_length=100)  

