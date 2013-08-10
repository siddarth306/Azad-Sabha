from django import forms
from captcha.fields import CaptchaField

class UserLoginForm(forms.Form):
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
	
	user_name = forms.CharField(max_length=25)
	first_name = forms.CharField(max_length=25)
	last_name = forms.CharField(max_length=25)
	DOB = forms.DateField()
	state = forms.ChoiceField(choices=choice)
	password = forms.CharField(max_length=15,widget=forms.PasswordInput())
	city = forms.ChoiceField(choices=choice_city)
	locality = forms.ChoiceField(choices=choice_locality)
	Email = forms.EmailField(max_length=75)
	receive_report_card = forms.BooleanField()
	sms_alert = forms.BooleanField()
	mobile_no = forms.CharField(max_length=10)
	captcha = CaptchaField()

class PoliticianLoginForm(forms.Form):
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
	user_name = forms.CharField(max_length=25)
	first_name = forms.CharField(max_length=25)
	last_name = forms.CharField(max_length=25)
	Email = forms.EmailField(max_length=75)
	password = forms.CharField(max_length=15,widget=forms.PasswordInput())
	DOB = forms.DateField()
	mname = forms.CharField(max_length=15)
	locality = forms.ChoiceField(choices=choice_locality)
	photo = forms.ImageField()
	isPolitician= forms.BooleanField()
	qualification = forms.CharField(max_length=10)
	status = forms.CharField(max_length=10)
	pre_political_post = forms.CharField(max_length=10)

class Postform(forms.Form):
	choice_locality=(
		('KP','Koregaon Park'),
		('GN','Ganesh Nagar'),
		('UPP','Upperindira Nagar'),
		)
	locality = forms.ChoiceField(choices=choice_locality)
	subject = forms.CharField(max_length=100)
	post = forms.CharField(widget=forms.Textarea)

class FeedBackForm(forms.Form):
	text= forms.CharField(widget=forms.Textarea)

class Ecampaigning(forms.Form):
	name = forms.CharField(max_length=50)
	msg = forms.CharField(max_length=200,widget=forms.Textarea)
	future_plans = forms.CharField(max_length=200,widget=forms.Textarea)
	

class PasswordChangeForm(forms.Form):
	password = forms.CharField(max_length=15,widget=forms.PasswordInput())
	con_pass = forms.CharField(max_length=15,widget=forms.PasswordInput())

class FbSignUp(forms.Form):
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
	state = forms.ChoiceField(choices=choice)
	locality = forms.ChoiceField(choices=choice_locality)
	city = forms.ChoiceField(choices=choice_city)
	DOB = forms.DateField()
	receive_report_card = forms.BooleanField()
	sms_alert = forms.BooleanField()
	mobile_no = forms.CharField(max_length=10)
	captcha = CaptchaField()
	