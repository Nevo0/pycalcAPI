from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from box.models import Box, MaxHubsSideAB, MaxHubsSideCD, Termina, Order
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings


class SideABSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaxHubsSideAB
        fields = '__all__'


class TerminaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Termina
        fields = '__all__'


class SideCDSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaxHubsSideCD
        fields = '__all__'


class BoxSerializers(ModelSerializer):
    max_hubs_side_a_b = SideABSerializer(many=False, read_only=True)
    max_hubs_side_c_d = SideABSerializer(many=False, read_only=True)
    termina = TerminaSerializer(many=False, read_only=True)
    # max_hubs_side_c_d = serializers.StringRelatedField(many=False)
    # max_hubs_side_a_b = serializers.PrimaryKeyRelatedField(many=False)
    # max_hubs_side_c_d = serializers.SlugRelatedField(
    #     many=False,
    #     read_only=True,
    #     slug_field='code'
    # )
    # team = serializers.RelatedField(read_only=True)
    # max_hubs_side_a_b = serializers.RelatedField(many=False, read_only='True')
    ab = SideABSerializer(read_only=True)
    cd = SideCDSerializer(read_only=True)

    class Meta:
        model = Box
        # all = '__all__'
        # fields = ('name', "ab", "cd")
        fields = '__all__'


class TerminaSerializers(ModelSerializer):
    terminals = TerminaSerializer(many=False, read_only=True)

    term = TerminaSerializer(read_only=True)

    class Meta:
        model = Box
        # all = '__all__'
        # fields = ('name', "ab", "cd")
        fields = '__all__'


class OrderSerializers(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        pass

    def create(self, validated_data):
        email = validated_data.get('email')
        name = validated_data.get('name')
        # message1 = ('Subject here', 'Here is the message',
        #             'piecyk.wolff@gmail.com', ['piecyk.wolff@gmail.com'])
        # message2 = ('Another Subject', 'Here is another message',
        #             'piecyk.wolff@gmail.com', ['piecyk.wolff@gmail.com'])
        # send_mass_mail((message1, message2), fail_silently=False)
        subject = 'Hardo TECH'
        message = f'Hi {name},\n\n  Dzięki za zgłoszenie :)'
        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        try:
            send_mail(subject, message, email_from, recipient_list)
        except Exception as e:
            return Order(**validated_data)
        return Order(**validated_data)
