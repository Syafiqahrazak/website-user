from django.shortcuts import render,redirect
from django.contrib import messages
import mysql.connector 

# Create your views here.

def index(request):
    return render(request,'index.html')

import mysql.connector
from operator import itemgetter

def loginuser(request):
    con = mysql.connector.connect(
            host = "localhost",
            user='root',
            password = "",
            database = "webapp",
        )
    cursor = con.cursor()

    con2 = mysql.connector.connect(
        host = "localhost",
        user='root',
        password = "",
        database = "webapp",
    )
    cursor2 = con2.cursor()

    sql_command = "SELECT ename FROM employee"
    sql_command2 = "SELECT password FROM employee"
    cursor.execute(sql_command)
    cursor2.execute(sql_command2)
        
    ename=[]
    password=[]

    for i in cursor:
        ename.append(i)
        # list of username that registered

    for y in cursor2:
        password.append(y)
        # list of password
    print(ename)
    print(password)

    resource = list(map(itemgetter(0), ename))    
    resource2 = list(map(itemgetter(0), password))   

    print(resource) 
    
    if request.method == "POST":
        name = request.POST['ename']
        password1 = request.POST['password']
        i=0
        k=len(resource)    
        while i<k:
            if resource[i] == name and resource2[i] == password1:
                return redirect('index')
                break
            elif resource[i] != name and resource2[i] == password1:
                messages.error(request, "Username is wrong! Try again.")
                return redirect('loginuser')
                break
            elif resource[i] == name and resource2[i] != password1:
                messages.error(request, "Password is wrong! Try again.")
                return redirect('loginuser')
                break
            i+=1

        else:
            messages.error(request, 'Username and Password not validate! Try again.')
            return redirect('loginuser')
    
    return render(request, 'loginuser.html')


