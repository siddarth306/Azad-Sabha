from django.template import Context,RequestContext
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from public.models import *
from public.forms import *
from django.template.loader import render_to_string
from django.contrib.auth import authenticate
from django_xhtml2pdf.utils import generate_pdf
import cStringIO as StringIO
from xhtml2pdf import pisa
import cgi
import os
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMessage
import datetime, random, sha
import re
import base64
import hashlib
from allaccess.clients import get_client
from allaccess.compat import smart_bytes, force_text
from allaccess.compat import get_user_model
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from urllib2 import urlopen
from allaccess.views import OAuthRedirect, OAuthCallback

#********************************************************************************************************
def fetch_resources(uri, rel):
    print "1. "+uri
    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    print "2. "+path
    return path

def render_to_pdf(template_src, context_dict):
    """Function to render html template into a pdf file"""
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")),
                                            dest=result,
                                            encoding='UTF-8',
                                            link_callback= fetch_resources)
    

    if not pdf.err:
        response = HttpResponse(result.getvalue(),mimetype='application/pdf')
        return response

    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

#********************************************************************************************************
#-----------------------------------------------------------------------------------------------
def home(request):
	if request.method=="POST":
		user=authenticate(username=request.POST["username"],password=request.POST["password"])
		if user is not None:
			login(request,user)
			return HttpResponseRedirect(reverse('public.views.profile'))		
	header=[]
	info=[]
	images=[]
	icons=[]
	serial=["1","2","3","4","5"]
	posts = PostProblems.objects.all();
	
	os.chdir(r'/home/siddharth/Downloads/janta3/janta/media/news')
	images=[]
	icons=[]
	header=[]
	info=[]
	news_file = open('news','r')
	for i in range(0,5):
		header.append(news_file.readline())
		info.append(news_file.readline())
		temp = news_file.readline()
		if temp == "None1\n":
			icons.append("None")
		else:
			icons.append(temp)
		images.append(news_file.readline())


	news_file.close()
			
			
	news=zip(header,info,images,icons,serial)
	#f.close()
	os.chdir(r'/home/siddharth/Downloads/janta3/')
	ctx={'news':news,'posts':posts}
	return  render_to_response('public/main.html',ctx,context_instance=RequestContext(request))

#-----------------------------------------------------------------------------------------------

def adduser(request):
	f = UserLoginForm(request.POST)
	if f.is_valid():
		u = User.objects.all().filter(email=request.POST['Email'])
		if len(u) == 0:
			u = User.objects.all().filter(username=request.POST['user_name'])
			if len(u) == 0:
				u = User.objects.create_user(request.POST['user_name'],email=request.POST['Email'],password=request.POST['password'])
				u.is_active=False
				u.first_name=request.POST['first_name']
				u.last_name = request.POST['last_name']
				u.save()
				salt = sha.new(str(random.random())).hexdigest()[:5]
				activation_key = sha.new(salt+u.username).hexdigest()
				key_expires = datetime.datetime.today() + datetime.timedelta(2)
				a=Customuser.objects.create(user=u,DOB=request.POST['DOB'],
				state = request.POST['state'],
				city = request.POST['city'],
				locality = request.POST['locality'],
				receive_report_card = request.POST['receive_report_card'],
				sms_alert = request.POST['sms_alert'],
				mobile_no = request.POST['mobile_no'],
				activation_key = activation_key)
				a.save()
				email_subject = 'Your new example.com account confirmation'
				email_body = r"Hello, %s, and thanks for signing up for an example.com account!\n\n\
				To activate your account, click this link within 48 hours:\n\n\
				127.0.0.1:8000/confirm/" +activation_key 
				email = EmailMessage(email_subject,email_body,
					'shashi.mishra43@gmail.com',[request.POST['Email']])
				email.send(fail_silently=False)
				return HttpResponse('Done')
			else:
				raise forms.ValidationError(u'Username Exist .. Please try a different one')
		else :
			raise forms.ValidationError(u'Email exist')
		
	return render(request,'public/UserLoginForm.html', {'form': f,})

#----------------------------------------------------------------------------------------------
def addPolitician(request):
	if request.method=="POST":
		f = PoliticianLoginForm(request.POST, request.FILES)
		if f.is_valid():
			u = User.objects.all().filter(email=request.POST['Email'])
			if len(u) == 0:
				u = User.objects.all().filter(username=request.POST['user_name'])
				if len(u) == 0:
					u = User.objects.create_user(request.POST['user_name'],email=request.POST['Email']
						,password=request.POST['password'])
					u.is_active=True
					u.first_name=request.POST['first_name']
					u.last_name = request.POST['last_name']
					u.save()
					a=Customuser.objects.create(user=u,DOB=request.POST['DOB'],
													locality = request.POST['locality'],
													)
					a.save()
					a.isPolitician=True
					a.save()
					a=PoliticianProfile.objects.create(uid=u.id,
					photo=request.FILES['photo'],
					qualification=request.POST['qualification'],
					status=request.POST['status'],
					pre_political_post=request.POST['pre_political_post']
					)
					a.save()

					return HttpResponseRedirect(reverse('public.views.profile'))
				else :
					raise forms.ValidationError(u'Username Exist .. Please try a different one')
			else :
				raise forms.ValidationError(u'Email exist')
	else:
		f = PoliticianLoginForm()
	return render(request,'public/PoliticianLoginForm.html', {'form': f,})

#-----------------------------------------------------------------------------------------------
def Posts(request):
	if request.user.is_authenticated():
		posts = PostProblems.objects.filter(locality=request.user.get_profile().locality)
	else :
		posts = PostProblems.objects.all();
	return render_to_response('public/Locality.html',{'posts':posts},
		context_instance=RequestContext(request))
#-----------------------------------------------------------------------------------------------

@login_required
def e_campaign(request):
	ctx={}
	if request.user.get_profile().isPolitician:
			a = PoliticianProfile.objects.get(uid=request.user.id)
			b = Issues.objects.all()
			b =	b.filter(pid=request.user.get_profile().id)
			c = b.count()
			d = 0
			e= 0
			for i in b:
				d=d+PostProblems.objects.all().filter(pk=i.issid,status=False).count()
				e=e+PostProblems.objects.all().filter(pk=i.issid,status=True).count()
			f = Ecampaigning(request.POST)
			if f.is_valid():
				ctx={'PoliticianProfile' : a ,"Issues_posted" : c,"Pending_issues":d,"Solved_issues":e,"user":request.user}
				result = render_to_string('public/Ecamp.html',ctx)
				out = StringIO.StringIO()
				pdf = pisa.pisaDocument(StringIO.StringIO(result.encode("UTF-8")), dest=out, link_callback=fetch_resources )
				recievers = Customuser.objects.all().filter(locality = request.user.get_profile().locality,isPolitician=False)
				email = EmailMessage('E-camp',request.POST['msg'],'shashi.mishra43@gmail.com',['shashi.mishra43@gmail.com','siddarth306@gmail.com'])
				email.attach('Ecamp.pdf', out.getvalue(), 'application/pdf')
				email.send(fail_silently=False)
			return render(request,'public/ecampaign.html', {'form': f,})
	return HttpResponse("Not auth")
#---------------------------------------------------------------------------------------------------
@login_required
def profile(request):
	ctx={}
	if request.user.is_authenticated():
		try :
			if request.user.get_profile().isPolitician:
				a = PoliticianProfile.objects.get(uid=request.user.id)
				b = Issues.objects.all()
				b =	b.filter(pid=request.user.get_profile().id)
				c = b.count()
				d = 0
				e= 0
				for i in b:
					d=d+PostProblems.objects.all().filter(pk=i.issid,status=False).count()
					e=e+PostProblems.objects.all().filter(pk=i.issid,status=True).count()
				print c ,d ,e	
				ctx={'PoliticianProfile' : a ,"Issues_posted" : c,"Pending_issues":d,"Solved_issues":e}
				return render_to_response('public/PoliticianProfile.html',ctx,context_instance=RequestContext(request))
			else :
				return render_to_response('public/profile.html',ctx,context_instance=RequestContext(request))
		except ObjectDoesNotExist:
			return HttpResponseRedirect('/fbsignup/');
#-----------------------------------------------------------------------------------------------

@login_required
def posting(request):
	f = Postform(request.POST)
	if f.is_valid():
		user = request.user
		pids = Customuser.objects.all().filter(locality=user.get_profile().locality,isPolitician= True)
		a=PostProblems.objects.create(pid=1,subject=request.POST['subject'],post=request.POST['post'],locality=request.POST['locality'])
		a.save()
		for p in pids:
			print p.user.first_name
			i  = Issues.objects.create(pid=p.id,issid=a.id)
			i.save();
		return HttpResponseRedirect(reverse('public.views.Posts'))
	return render_to_response('public/post.html',{'form' : f },context_instance=RequestContext(request))

#----------------------------------------------------------------------------------------------

@login_required
def feedback(request):
	f = FeedBackForm(request.POST)
	if f.is_valid():
		a=FeedBack.objects.create(uid=request.user.id,text=request.POST['text'])
		a.save()
		return HttpResponseRedirect(reverse('public.views.home'))
	return render_to_response('public/post.html',{'form' : f },context_instance=RequestContext(request))
#----------------------------------------------------------------------------------------------------
def confirm(request,activation_key):
	if request.user.is_authenticated():
		return render_to_response('confirm.html', {'has_account': True})
	user_profile = get_object_or_404(Customuser,
                                     activation_key=activation_key)
	user_account = user_profile.user
	user_account.is_active = True
	user_account.save()
	return render_to_response('confirm.html', {'success': True})

#------------------------------------------------------------------------------------------------------



def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
	return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
	query = None 
	terms = normalize_query(query_string)
	for term in terms:
		or_query = None 
		for field_name in search_fields:
			q = Q(**{"%s__icontains" % field_name: term})
			if or_query is None:
				or_query = q
			else:
				or_query = or_query | q
		if query is None:
			query = or_query
		else:
			query = query & or_query
		return query


#------------------------------------------------------------------------------------------------------

def search(request):

	q = request.POST['search']
	search_in = request.POST['cars']
	ctx ={}
	if search_in == "Issue" :	
		entry_query = get_query(q,['subject','post'])
		found_entries = PostProblems.objects.all().filter(entry_query)
		
	elif search_in == "Politician" :
		entry_query = get_query(q,['first_name','last_name'])
		#users = Customuser.objects.all().filter(isPolitician=True)
		found_entries = User.objects.all().filter(entry_query)
		
	else :
		found_entries = None
	ctx = {'query':q,'results' : found_entries,'search':search_in}
	print search_in , q ,found_entries
	return render_to_response('public/search.html',ctx,context_instance=RequestContext(request))

#------------------------------------------------------------------------------------------------------

def forgot_password(request):
	email = request.POST['email']
	user = User.objects.get(email=email)
	if not user:
		print "NO such email"
	else :
		f=PasswordChangeForm(request.POST)
		if f.is_valid():
			user.set_password(request.POST['password'])
			user.save()
			
#-----------------------------------------------------------------------------------------
def detail_post(request,post_id):
	if request.method == "POST":
		comment = Comment.objects.create(uid=request.user.id,comment=request.POST['comment'],post_id=post_id)
		comment.save()
	c = Comment.objects.all().filter(post_id=post_id)
	p = PostProblems.objects.get(pk=post_id)
	ctx ={"p":p,"comments":c}
	return render_to_response('public/detail_issue.html',ctx,context_instance=RequestContext(request))

#-----------------------------------------------------------------------------------------

def aboutus(request):
	ctx ={}
	return render_to_response('public/aboutus.html',ctx,context_instance=RequestContext(request))

#-----------------------------------------------------------------------------------------

def feedback(request):
	ctx ={}
	return render_to_response('public/feedback.html',ctx,context_instance=RequestContext(request))
#------------------------------------------------------------------------------------------------

def home2(request):
	"Simple homepage view."
	context = {}
	if request.user.is_authenticated():
		try:
			access = request.user.accountaccess_set.all()[0]
		except IndexError:
			access = None
		else:
			client = access.api_client
			context['info'] = client.get_profile_info(raw_token=access.access_token)
	return render(request, 'public/home.html', context)

#-----------------------------------------------------------------
def fbsignup(request):
	if request.method=="POST":
		f = FbSignUp(request.POST)
		if f.is_valid():
			a=Customuser.objects.create(user=request.user,DOB=request.POST['DOB'],
				state = request.POST['state'],
				city = request.POST['city'],
				locality = request.POST['locality'],
				receive_report_card = request.POST['receive_report_card'],
				sms_alert = request.POST['sms_alert'],
				mobile_no = request.POST['mobile_no'],
				)
			a.save()
			return HttpResponseRedirect('/profile/')
	else:
		f = FbSignUp()
	ctx={'form':f}
	return render_to_response('public/fbsignup.html',ctx,context_instance=RequestContext(request))


#-----------------------------------------------------------------------------------------------------
class OauthCustomCallback(OAuthCallback):

	def get_or_create_user(self,provider,access,info):
		digest = hashlib.sha1(smart_bytes(access)).digest()
		username = force_text(base64.urlsafe_b64encode(digest)).replace('=', '')
		User = get_user_model()
		try:
  			user = User.objects.get(email=info.get('email'))
  			return user
		except ObjectDoesNotExist:
  			pass
		user = User.objects.create(username=username,email=info.get('email'),first_name=info.get('first_name'),
			last_name=info.get('last_name')) 
		user.save()
		return user

	def get_login_redirect(self, provider, user, access, new=False):
		return settings.LOGIN_REDIRECT_URL
#-------------------------------------------------------------

class OauthCustomRedirect(OAuthRedirect):
	def get_additional_parameters(self,provider):
		if provider.name == 'facebook':
			return {'scope': 'email'}

#-----------------------------------------------------------------------------------------------------

def set(request):
	ctx ={}
	return render_to_response('public/set.html',ctx,context_instance=RequestContext(request))


