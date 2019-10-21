from .import autoreply
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import contactForm

# Create your views here.
def contact(request):
	"""about page"""
	title = "Contact"
	form = contactForm(request.POST or None) #form handling by view.
	confirmation = None

	if form.is_valid():
		user_name = form.cleaned_data['Username']
		user_message = form.cleaned_data['Message']
		emailsub = user_name + " tried contacting you on CookMyShow."
		emailFrom = form.cleaned_data['UserEmail']
		emailmessage = '%s \nUsername: %s\nEmail: %s' %(user_message, user_name, emailFrom)
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(emailsub, emailmessage, emailFrom, list(emailTo), fail_silently=True)
		#Autoreply.
		autoreply.autoreply(emailFrom)
		title = "Thanks."
		confirmation = "We will get right back to you."
		form = None

	context = {'title':title, 'form':form, 'confirmation':confirmation,}
	template = 'contact.html'
	return render(request,template,context)
