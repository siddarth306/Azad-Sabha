from django.db import models
from django.contrib.auth.models import User, UserManager
from functools import partial

#-----------------------------------------------------------------------------------------------------
class Customuser(models.Model):
	
	choice=(
			('UP','UTTAR PRADESH'),
			('MH','MAHARASHTRA'),
			('BI','BIHAR'),
			('WB','WEST BENGAL'),
			('AP','ANDHRA PRADESH'),
			('MP','MADHYA PRADESH'),
		)
	choice_locality=(
		('KP','Koregaon Park'),
		('GN','Ganesh Nagar'),
		('UPP','Upperindira Nagar'),
		)
	choice_city=(
		('PUNE','PUNE'),
		('MUMBAI','MUMBAI'),
		('NAGPUR','NAGPUR'),
			)
	def __unicode__(self) :
		return self.user.first_name

	user=models.OneToOneField(User,related_name="public")
	DOB = models.DateField('Date of Birth')
	state = models.CharField(max_length=25,choices=choice)
	city=models.CharField(max_length=15,choices=choice_city)
	locality = models.CharField(max_length=25,choices=choice_locality)
	receive_report_card = models.BooleanField(default=False)
	sms_alert = models.BooleanField(default=False)
	activation_key = models.CharField(max_length=50)
	mobile_no = models.CharField(max_length=10)
	isPolitician = models.BooleanField(default=False)
#----------------------------------------------------------------------------------------------------
class PoliticianProfile(models.Model):
	def make_filepath(field_name, instance, filename):
		new_filename = "%s.%s" % (User.objects.make_random_password(10),
                             filename.split('.')[-1])
		return '/'.join([instance.__class__.__name__.lower(),
                     field_name, new_filename])

	uid = models.IntegerField()
	photo = models.ImageField(upload_to=partial(make_filepath, 'image'))
	qualification = models.CharField(max_length=10)
	status = models.CharField(max_length=10)
	pre_political_post = models.CharField(max_length=10)

#----------------------------------------------------------------------------------------------------
class PostProblems(models.Model):

	choice_locality=(
		('KP','Koregaon Park'),
		('GN','Ganesh Nagar'),
		('UPP','Upperindira Nagar'),
		)
	pid = models.IntegerField()
	status = models.BooleanField(default=False)
	subject = models.CharField(max_length=100,null=False)
	pts = models.IntegerField(blank=True,default=0)
	post = models.TextField()
	Date = models.DateTimeField('Date of Posting',auto_now_add=True)
	locality = models.CharField(max_length=25,choices=choice_locality,null=False,blank=False)
	spam = models.IntegerField(blank=True,default=0)

#----------------------------------------------------------------------------------------------

class FeedBack(models.Model):
	uid = models.IntegerField()
	text = models.CharField(max_length=200,null=False)
	Date = models.DateTimeField('Date of Posting',auto_now_add=True)

#---------------------------------------------------------------------------------------------

class States(models.Model):
	state = models.CharField(max_length=50)

class Cities(models.Model):
	sid = models.IntegerField()
	city = models.CharField(max_length=50)

#------------------------------------------------------------------------------------------------

class Issues(models.Model):
	issid = models.IntegerField()
	pid = models.IntegerField()

#------------------------------------------------------------------------------------------------

class Comment(models.Model):
	uid = models.IntegerField()
	post_id = models.IntegerField()
	comment = models.CharField(max_length=200)
	Date = models.DateTimeField('Date of Posting',auto_now_add=True)