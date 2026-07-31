from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import AnonRateThrottle
from django.core.mail import send_mail
from django.conf import settings
from ..models import Contact
from ..serializers.contact import ContactSerializer

class ContactCreateView(APIView):
    throttle_classes = [AnonRateThrottle]

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()
            
            # Send Email
            subject = f"New Contact Message from {contact.nom}"
            message = f"You have a new message from {contact.nom} ({contact.email}):\n\n{contact.message}"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.ADMIN_EMAIL]
            
            try:
                send_mail(subject, message, from_email, recipient_list)
            except Exception as e:
                # Log the error or handle it as needed
                print(f"Error sending email: {e}")
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
