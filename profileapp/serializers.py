from rest_framework.serializers import ModelSerializer

from accountapp.serializes import UserWithoutPasswordSerializer
from profileapp.models import Profile

class ProfileSerializer(ModelSerializer):
    # owner = UserWithoutPasswordSerializer(read_only=True)
    class Meta:
        model = Profile
        # fields = ['id','nickname','image','message','owner']
        fields = ['id','nickname','image','message','owner_id']