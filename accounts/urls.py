from django.urls import path
from .views import SignUpView

#Accounts/urls.py : Handles only registrations URLs!!
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]

# 🔹 How They Work Together
# User requests /accounts/signup/
# → project/urls.py sees accounts/ and forwards the request to accounts/urls.py.

# accounts/urls.py handles signup/
# → Calls SignUpView.as_view(), which processes the request.

# Response is sent back to the user.

