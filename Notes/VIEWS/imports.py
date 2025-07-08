from django.shortcuts import get_object_or_404, render,redirect
from ..models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Case, When, Value, IntegerField ,Q
from datetime import timedelta
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone

