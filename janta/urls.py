from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout , password_reset,password_reset_done,password_reset_confirm,password_reset_complete
from janta import settings
from allaccess.views import OAuthRedirect, OAuthCallback
from public.views import OauthCustomRedirect,OauthCustomCallback
admin.autodiscover()
urlpatterns = patterns('',
	#url(r'dologin/$','public.views.loginuser'),
	 url(r'login/$',login,kwargs={'template_name':'public/login.html'},name='homepage_login'),
	 url(r'logout/$',logout,kwargs={'next_page':'/home/'},name='homepage_logout'),
	 url(r'postproblem/$','public.views.posting',name='homepage_post'),
	 url(r'^profile/$','public.views.profile',name='homepage_profile'),
	 url(r'^locality/$','public.views.Posts',name='homepage_locality'),
   	 url(r'^home/$','public.views.home',name='homepage_home'),
   	 url(r'^signup/$','public.views.adduser'),
     url(r'^ecamp/$','public.views.e_campaign'),
     url(r'^search/$','public.views.search'),
     url(r'^password_reset/$',password_reset),
     url(r'^password_reset_done/$',password_reset_done),
     url(r'^password_reset_confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',password_reset_confirm),
     url(r'^password_reset_complete/$',password_reset_complete),
     url(r'^post/(?P<post_id>\d+)/$','public.views.detail_post'),
     url(r'^confirm/(?P<activation_key>[a-zA-Z0-9_]*)/$','public.views.confirm'),
   	 url(r'^signupPolitician/$','public.views.addPolitician'),
     url(r'feedback/$','public.views.feedback',name='homepage_feedback'),
     url(r'^set/$','public.views.set'),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^accounts/login/(?P<provider>(\w|-)+)/$', OauthCustomRedirect.as_view(), name='allaccess-login'),
    url(r'^accounts/callback/(?P<provider>(\w|-)+)/$', OauthCustomCallback.as_view(), name='allaccess-callback'),
    url(r'^fbsignup/$','public.views.fbsignup'),
     #url(r'^accounts/', include('allaccess.urls')),
     url(r'^test/$','public.views.home2'),
     url(r'^$','public.views.home'),
     url(r'^aboutus/$','public.views.aboutus'),

     
     url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT}),
)

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)


