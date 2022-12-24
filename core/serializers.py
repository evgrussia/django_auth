from rest_framework.serializers import ModelSerializer
from .models import User
import random
import string


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'telegram', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        validated_data['personalID'] = ''.join(random.choice(string.digits) for _ in range(10))
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'email',
                  'first_name',
                  'last_name',
                  'phone',
                  'telegram',
                  'volume_PV',
                  'volume_APV',
                  'volume_GV',
                  'volume_AGV',
                  'volume_NV',
                  'volume_ANV',
                  'volume_QV',
                  'rang',
                  'cashback',
                  'client_bonus',
                  'team_bonus',
                  'ref_link',
                  'partner_balance',
                  'personal_balance',
                  'personalID',
                  'clients_count',
                  'partners_count',
                  'clicks',
                  'telegram',
                  'partner_reward',
                  'wallet_usdt']