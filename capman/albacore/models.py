from django.db import models

# Create your models here.

class Provider(models.Model):
  name = models.CharField(max_length=100)
  def __unicode__(self):
    return self.name
  
class Switch(models.Model):
  name = models.CharField(max_length=50)
  model = models.CharField(max_length=50)
  num_ports = models.IntegerField()
  def __unicode__(self):
    return self.name

class SwitchPort(models.Model):
  name = models.CharField(max_length=2)
  switch = models.ForeignKey(Switch, related_name='switch')
  speed = models.IntegerField()
  def __unicode__(self):
    return self.name

class Circuit(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=500)
  vlan_id = models.IntegerField()
  direct_provider = models.ForeignKey(Provider, related_name='direct_prov')
  cdr = models.IntegerField()
  bearer = models.IntegerField()
  pbdemuxport = models.ForeignKey(SwitchPort, related_name='pbdmuxport')
  metroeport = models.ForeignKey(SwitchPort, related_name='metroeport') 
  def __unicode__(self):
    return self.name
  
class Datacentre(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=500)
  def __unicode__(self):
    return self.name

class Interconnect(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=500)  
  pbdemuxport = models.ForeignKey(SwitchPort)
  provider = models.ForeignKey(Provider, related_name='int_direct_prov')
  dc = models.ForeignKey(Datacentre, related_name='int_dc')
  is_open = models.BooleanField()
  capacity = models.IntegerField()
  def __unicode__(self):
    return self.name

class Site(models.Model):
  name = models.CharField(max_length=100)
  operator = models.ForeignKey(Switch, related_name='op')
  primary = models.ForeignKey(Circuit, related_name='pri_cct')
  backup = models.ForeignKey(Circuit, related_name='sec_cct')
  def __unicode__(self):
    return self.name

class Operator(models.Model):
  name = models.CharField(max_length=100)  
  def __unicode__(self):
    return self.name
    
