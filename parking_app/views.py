from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import *
import json
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from time import sleep
import datetime
# Create your views here.



POS1 = Position.objects.get(Rank = 1)
POS2 = Position.objects.get(Rank = 2)
POS3 = Position.objects.get(Rank = 3)
POS4 = Position.objects.get(Rank = 4)
POS5 = Position.objects.get(Rank = 5)
POS6 = Position.objects.get(Rank = 6)

POSS = [POS1, POS2, POS3, POS4, POS5, POS6]



def index(request):
	return HttpResponse("hello iheb ya3tik 3asba")



def getPosition(request):
	return int((random.random()*10)%6+1)




def addPendingRequest(request, registry):

	"""
	This method adds a new request to the system queue
	It returns a response depending on the state of the system
	Possible values for reponse code:

		value     |     Results
		---------------------------
		-1        |   Busy
		 0        |   Already Added
		 1        |   Success

	"""
	response = {}

	response['result'] = 'Request Already In Queue'
	response['code'] = 0

	if Pending_Request.objects.all().count() > 1:
		response['result'] = 'Queue is currently busy, please wait until the next car has finished'
		response['code'] = -1


	elif not Pending_Request.objects.filter(Registry = registry).exists():
		pending_request = Pending_Request(Registry = registry)
		
		pending_request.Last_Captured = datetime.datetime.now()
		pending_request.save()
		response['result'] = 'Request successfully pushed into the Queue'
		response['code'] = 1

	
	else:
		pending_request = Pending_Request.objects.get(Registry = registry)
		
		pending_request.Last_Captured = datetime.datetime.now()
		pending_request.save()


	return HttpResponse(json.dumps(response), content_type="application/json")


def generateCode():
	return int((random.random()*10)%6+1)*12345221



def register_driver(name, surname, phone,email):
	driver = Driver()
	driver.Name = name
	driver.Surname = surname
	driver.Telephone = phone
	driver.Email = email
	driver.save()
	return driver

@csrf_exempt
def testajax(request):


	return HttpResponse(
                json.dumps({
                    "result": 56,
                }),
                content_type="application/json"
            )


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"



@csrf_exempt
def match_cars(request):
	
	if request.method != "POST":
		return HttpResponse(
                json.dumps({
                    "result": -1,
					"feedback": "The request must be an AJAX POST request"
                }),
                content_type="application/json"
            )
	
	'''
	The expected format of the json object is as follows:
	{ "positiodatan1" : car_number1, "position2" : car_number2, .... , "position5":car_number5 , "anomaly" : True/False}

	Where:
		car_numberi = "-1" if position i is empty, else = car registry 


	ex: 
	{ "position1" : "2778154" , "position2": -1, "position3": "5544AZZ", "position4": "-1", "position5": "323DDDX", "anomaly" : False }
	'''
	
	data  = json.loads(request.body)

	position = 1

	Occupies.objects.all().delete()

	cars = []

	while position <= 5:
		if data["position"+str(position)] == "-1":
			cars.append(None)
		else:
			cars.append(Car.objects.get(Registry = data["position"+str(position)]))
		position+=1
	
	
	for position, car in zip(POSS, cars):
		if car == None:
			continue
		occupies = Occupies()
		occupies.Car = car
		occupies.Position = position
		occupies.save()
	
	return HttpResponse(
                json.dumps({
                    "result": 1,
					"feedback": "Parking updated successfully"
                }),
                content_type="application/json"
            )




def processQueue(request):
	occupations = []

	for item in list(Occupies.objects.all()):
		occupations.append(item.Position.Rank)


	number_of_requests = int(Pending_Request.objects.all().count())

	if number_of_requests > 0:
		pending_request = Pending_Request.objects.all()[0]
		if pending_request.Status == "verified" and int((datetime.datetime.now().replace(tzinfo=None) - pending_request.Last_Captured.replace(tzinfo=None)).total_seconds()) > 20 and Door.objects.all()[0].State == "open":

			pending_request.delete()


			
	if request.method == "GET":

		if is_ajax(request):
			if number_of_requests==0:
				return HttpResponse(
	                json.dumps({
	                    "result": "empty",
						"occupations": occupations,
	                }),
	                content_type="application/json"
	            )
			else:
				pending_request = Pending_Request.objects.all()[0]
				registry = pending_request.Registry
				return HttpResponse(
	                json.dumps({
	                    "result": "waiting",
	                    "registry":registry,
	                    "status":pending_request.Status,
						"occupations": occupations,
	                }),
	                content_type="application/json"
	            )
		else:

			status = "empty"

			if number_of_requests > 0:
				pending_request = Pending_Request.objects.all()[0]
				status = pending_request.Status

			return render(request,"index.html",{'status':status})
			
	if request.method == "POST":

		if Pending_Request.objects.all().count():
			# There is a pending request
			pending_request = Pending_Request.objects.all()[0]
			registry = pending_request.Registry

			if pending_request.Status == 'pending':
				## email must be sent
				gen_code = str(generateCode())
				
				is_registered = Car.objects.filter(Registry = registry).exists()

				if not is_registered:
					pending_request.Status = 'in progress'
					pending_request.Verification_Code = gen_code
					pending_request.save()
					driver = Driver()
					driver = register_driver(request.POST.get("name"), request.POST.get("surname"),request.POST.get("telephone"),request.POST.get("email"))
					send_mail(
				    'Verification Code - Mines Paris',
				    'Here is your verification code: '+gen_code,
				    'adel_hajhasan@example.com',
				    [request.POST.get("email")],
				    fail_silently=False,
				)

					return render(request,'index.html',{'state':'emailed','registry':registry, 'status': pending_request.Status, 'driver':driver.pk})

				else:
					pending_request.Status = 'verified'
					pending_request.save()
					driver = Driver()
					driver = register_driver(request.POST.get("name"), request.POST.get("surname"),request.POST.get("telephone"),request.POST.get("email"))
					drives_car = Drives_Car()
					drives_car.Driver = driver

					car = Car.objects.get(Registry = registry)

					drives_car.Car = car

					drives_car.save()

					return render(request,"index.html",{'state':'success',})




			else:
				## verification
				if request.POST.get("verification_code") == pending_request.Verification_Code:
					pending_request.Status = "verified"
					pending_request.save()



					if not Car.objects.filter(Registry = registry).exists():
						car = Car()
						car.Registry = pending_request.Registry
						car.save()

					drives_car = Drives_Car()

					driver = Driver.objects.get(pk = request.POST.get("driver"))
					drives_car.Driver = driver

					car = Car.objects.get(Registry = registry)

					drives_car.Car = car

					drives_car.save()


					return render(request,"index.html",{'state':'success',})

				else:
					return render(request,"index.html",{'state':'failed','registry':registry, 'status': pending_request.Status , 'driver':request.POST.get("driver")})

	else:
		pass


@csrf_exempt
def administration(request):

	door = Door.objects.all()[0].State
	
	occupations = []

	drivers = []

	cars = []

	for item in list(Occupies.objects.all()):
		occupations.append(item.Position.Rank)
		car = item.Car
		cars.append(car.Registry)
		
		driver = list(Drives_Car.objects.filter(Car = car).order_by('-Pub_Time'))[0].Driver
		drivers.append({'name':driver.Name, 'surname':driver.Surname, 'email':driver.Email, 'telephone':driver.Telephone})

	number_of_requests = int(Pending_Request.objects.all().count())

	if is_ajax(request):
			if request.method == "POST":
				door = Door.objects.all()[0]
				if door.State == "open":
					door.State = "closed"
				else:
					 door.State = "open"
				door.save()
				return HttpResponse(
					json.dumps({
	                    
	                }),
	                content_type="application/json"
	            )
			if number_of_requests==0:
				return HttpResponse(
	                json.dumps({
	                    "result": "empty",
						"occupations": occupations,
						"door": door,
						"drivers": drivers,
						"cars":cars
	                }),
	                content_type="application/json"
	            )
			else:
				pending_request = Pending_Request.objects.all()[0]
				registry = pending_request.Registry
				return HttpResponse(
	                json.dumps({
	                    "result": "waiting",
	                    "registry":registry,
	                    "status":pending_request.Status,
						"occupations": occupations,
						"door":door,
						"drivers": drivers,
						"cars":cars
	                }),
	                content_type="application/json"
	            )
	else:

		status = "empty"

		if number_of_requests > 0:
			pending_request = Pending_Request.objects.all()[0]
			status = pending_request.Status

		return render(request,"administration.html",{'status':status})












