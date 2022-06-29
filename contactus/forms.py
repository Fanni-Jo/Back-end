from django import forms
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.Form):

    name = forms.CharField(max_length=120,label='Full Name')
    email = forms.EmailField(required=True, label=' Email')
    subject = forms.CharField(max_length=70, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='We are listening!')

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('subject')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):

        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS],
            fail_silently=False
        )
