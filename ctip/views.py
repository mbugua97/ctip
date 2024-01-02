from rest_framework.decorators import APIView
from rest_framework.response import Response


from django.shortcuts import HttpResponse,render


from .serializers import PersonSerializer
from .models import Person


import jwt,datetime


class Register(APIView):
    def get(self,request):
        user=Person.objects.all()
        seri=PersonSerializer(user,many=True)
        return Response(seri.data)
    def post(self,request):
        data=request.data
        seri=PersonSerializer(data=data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)
        return Response("not saved")
    
class login(APIView):
    def post(self,request):
        user_name=request.data['user_name']
        user_password=request.data['password']
        user=Person.objects.filter(user_name=user_name).first()
        if not user :
            return Response ("no user found")
        if not user.password==user_password:
            return Response("wrong password")
        

        payload={
            'id':user.id,
            'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=30),
            'iat':datetime.datetime.utcnow()
        }
        token=jwt.encode(payload,'secret',algorithm='HS256')
        response=Response()
        response.set_cookie(key="ctip",value=token)
        response.data={
            "jwt":token
        }
        return response

        

class HomePage(APIView):
    def get(self,request):
        token=request.COOKIES.get('ctip')
        if token is None:
            return HttpResponse("you are not logged in")

        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            return HttpResponse("session expired")
    
        user=payload['id']
        User=Person.objects.filter(id=user).first()
        seri=PersonSerializer(User)

        return Response(seri.data)
    
class Logout(APIView):
    def get(self,request):
        response=Response()
        response.delete_cookie('ctip')

        response.data={"message":'successfull logout'}

        return response

