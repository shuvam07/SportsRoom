from login.models import UserProfileInfo
from django.contrib.auth.decorators import login_required

@login_required
def get_data(request):
	print(request.user)
	userProfile = UserProfileInfo.objects.get(user=request.user)
	return {'userProfile': userProfile }