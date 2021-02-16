from rest_framework import serializers
from users.models import LeaderProfile, Teacher, Student, StudentGroup
from django.contrib.auth.models import User


class LeaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeaderProfile
        fields = ("image", "sex", "age", "phone", "email")


class TeacherListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ("id", "image", "bio", "experience", "sex", "birthday", "phone")


class StudentListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ("id", "image", "sex", "birthday", "phone")


class TeacherCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    password = serializers.CharField(write_only=True, source="user.password")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.CharField(source="user.email")


    class Meta:
        model = Teacher
        fields = ("username", 'password', "first_name", "last_name", "email", "image", "bio", "experience", "sex", "birthday", "phone")
    
    def create(self, validated_data):
        user = validated_data.pop('user')
        user = User.objects.create(username=user['username'], first_name=user['first_name'], last_name=user['last_name'], email=user['email'])
        user.set_password('password')
        teacher = Teacher(**validated_data)
        teacher.user = user
        teacher.save()

        return teacher


    def update(self, instance, validated_data):

        user = validated_data.pop('user')

        if  user.get('password'):
            password = user.pop('password')
            instance.user.set_password(password)
            instance.user.save()

        if user.get('username'):
            username = user.pop('username')
            instance.user.username = username
            instance.user.save()

        if user.get('last_name'):
            last_name = user.pop('last_name')
            instance.user.last_name = last_name
            instance.user.save()

        if user.get('first_name'):
            first_name = user.pop('first_name')
            instance.user.first_name = first_name
            instance.user.save()    

        if user.get('email'):
            email = user.pop('email')
            instance.user.email = email
            instance.user.save()  

        if validated_data.get('bio'):
            bio = validated_data.pop('bio')
            instance.bio = bio
            instance.save()    

        if validated_data.get('experience'):
            experience = validated_data.pop('experience')
            instance.experience = experience
            instance.save() 

        if validated_data.get('sex'):
            sex = validated_data.pop('sex')
            instance.sex = sex
            instance.save() 

        if validated_data.get('sex'):
            sex = validated_data.pop('sex')
            instance.sex = sex
            instance.save() 

        if validated_data.get('birthday'):
            birthday = validated_data.pop('birthday')
            instance.birthday = birthday
            instance.save() 

        if validated_data.get('phone'):
            phone = validated_data.pop('phone')
            instance.phone = phone
            instance.save()  

        return instance

class StudentCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    password = serializers.CharField(write_only=True, source="user.password")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.CharField(source="user.email")

    class Meta:
        model = Teacher
        fields = ("username", 'password', "first_name", "last_name", "email", "image", "sex", "birthday", "phone")

    def create(self, validated_data):
        user = validated_data.pop('user')
        user = User.objects.create(username=user['username'], first_name=user['first_name'], last_name=user['last_name'], email=user['email'])
        user.set_password('password')
        student = Student(**validated_data)
        student.user = user
        student.save()

        return student

    def update(self, instance, validated_data):

        user = validated_data.pop('user')

        if  user.get('password'):
            password = user.pop('password')
            instance.user.set_password(password)
            instance.user.save()

        if user.get('username'):
            username = user.pop('username')
            instance.user.username = username
            instance.user.save()

        if user.get('last_name'):
            last_name = user.pop('last_name')
            instance.user.last_name = last_name
            instance.user.save()

        if user.get('first_name'):
            first_name = user.pop('first_name')
            instance.user.first_name = first_name
            instance.user.save()    

        if user.get('email'):
            email = user.pop('email')
            instance.user.email = email
            instance.user.save() 

        if validated_data.get('sex'):
            sex = validated_data.pop('sex')
            instance.sex = sex
            instance.save() 

        if validated_data.get('birthday'):
            birthday = validated_data.pop('birthday')
            instance.birthday = birthday
            instance.save() 

        if validated_data.get('phone'):
            phone = validated_data.pop('phone')
            instance.phone = phone
            instance.save() 

        return instance


class StudentGroupListSerializer(serializers.ModelSerializer):

    students_in_the_group = StudentCreateSerializer(many=True, read_only=True)

    class Meta:
        model = StudentGroup
        fields = ('id', 'name_of_group', 'teacher_of_group', 'students_in_the_group')



class StudentGroupCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentGroup
        fields = ('name_of_group', 'teacher_of_group', 'students_in_the_group')

    def to_representation(self, value):
        response = super().to_representation(value)
        response['Student'] = StudentListSerializer(value.students_in_the_group, many=True).data
        return response
