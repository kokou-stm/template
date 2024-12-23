from django.shortcuts import render, redirect

# Create your views here.

from .api import *
from django.shortcuts import render
from gtts import gTTS
import os, io, json
from io import BytesIO
import requests
from openai import AzureOpenAI
from PIL import Image
#import langdetect
import shutil
from .api import *
from django.http import  JsonResponse
import time
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .agora.RtcTokenBuilder import RtcTokenBuilder, Role_Attendee
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from django.db.models import Q
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from .models import *
# Create your views here.

@csrf_exempt
def generate_agora_token(request):
    app_id = 'f2891190d713482dbed4c3fd804ec233'
    app_certificate = 'ec7803663ae640658b2a5afe5dc0894e'
    channel_name = 'channel1'
    uid = 0  # Utilisez 0 pour des utilisateurs anonymes ou un UID spécifique
    #role = RtcTokenBuilder.Role_Attendee  # Utilisateur participant à la réunion
    expiration_time_in_seconds = 3600  # Durée de validité du token en secondes

    current_timestamp = int(time.time())
    privilege_expired_ts = current_timestamp + expiration_time_in_seconds

    token = RtcTokenBuilder.buildTokenWithUid(app_id, app_certificate, channel_name, uid, Role_Attendee, privilege_expired_ts)
    print("="*10, "token", "="*10)
    print(token)
    print("="*10, "token", "="*10)
    return JsonResponse({'token': token})


def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")



from .forms import *

def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user  # Assigner l'utilisateur connecté comme hôte
            room.save()
            return redirect('room_detail', room_id=room.id)  # Rediriger vers la page de la salle
    else:
        form = RoomForm()
    return render(request, 'create_room.html', {'form': form})
