# Ex.04 Design a Website for Server Side Processing
## Date:29-12-2025

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```
<html>
    <head>
        <title>Mileage</title>
    </head>
    <style>
        .box
        {
            margin-top: 15%;
            margin-left: 30%;
            margin-right:30%;
            border: 4px doted black; 
            background-color: blue;
            text-align: center; 
            width: 450px;
            height:  400px;
        }
    </style>
    <body>
        <div class="box">
        <h1>Mileage Calculator</h1>
        <h3>Aashik.A</h3>
        <h3>25012808</h3>
        <br>
        <form method="POST">
            {% csrf_token %}
            <label><i>Distance Travelled: </label><i/>
            <input type="text" name="distance" value="{{d}}" required> Km
            <br><br>
            <br>
            <label>fuel Consumed: </label>
            <input type="text" name="fuel" value="{{f}}" required> L
            <br>
            <br>

            <br>
            <input type="submit" value="Calculate">
            <br>
            <br><br>
            <label>Mileage: </label>
            <input type="text" name="efficiency" value="{{efficiency}}"> Km/L
        </form>
        </div>
    </body>
</html>

from django.shortcuts import render
def fueleff(request):
    d = int(request.POST.get('distance', 0))
    f = int(request.POST.get('fuel', 0))
    efficiency = d/f if request.method == 'POST' else 0
    print("Distance=",d)
    print("Fuel=",f)
    print("Efficiency=",efficiency)
    return render(request, 'mathserverapp/math.html', {'d': d, 'f': f, 'efficiency': efficiency})

    from django.urls import path
from mathserverapp import views
urlpatterns = [
    path('', views.fueleff, name='fuelefff'),
]  


```

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot 2025-12-15 081655.png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot 2025-12-15 081334.png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
