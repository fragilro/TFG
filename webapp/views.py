import pyrebase
from django.contrib import auth
from django.shortcuts import render, redirect
from . import models
from django.views.decorators.csrf import csrf_exempt

config = {
    "apiKey": "AIzaSyDc2TQ_Sg81daWi9MGT7dxdo3g9z-HBwSY",
    "authDomain": "prueba-tfg-add50.firebaseapp.com",
    "databaseURL": "https://prueba-tfg-add50.firebaseio.com",
    "projectId": "prueba-tfg-add50",
    "storageBucket": "prueba-tfg-add50.appspot.com",
    "messagingSenderId": "170143729359",
    "appId": "1:170143729359:web:5b5614d5e858c02bd8d9ba",
    "measurementId": "G-QK8C8028YV"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
storage = firebase.storage()
storageRef = storage.child("TFG.pdf").get_url(None)


def singIn(request):
    return render(request, "signIn.html")


def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message = "Correo o contraseña incorrectos. Por favor, inténtelo de nuevo."
        return render(request, "signIn.html", {"msg": message})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    name = database.child('users').child(a).child('details').child('name').get().val()
    return render(request, "welcome.html", {"e": name})


def logout(request):
    auth.logout(request)
    return render(request, 'signIn.html')


def signUp(request):
    return render(request, "signup.html")


def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    if ".upv.es" not in email:
        message = "El correo no pertenece al dominio UPV"
        return render(request, "signup.html", {"msg": message})
    try:
        user = authe.create_user_with_email_and_password(email, passw)
        uid = user['localId']
    except:
        message = "No se ha podido completar el registro. Por favor, inténtelo de nuevo"
        return render(request, "signup.html", {"msg": message})

    uid = user['localId']
    data = {"name": name, "status": "1"}

    database.child("users").child(uid).child("details").set(data)
    return render(request, "signIn.html")


def mostrarguia(request):
    return render(request, "guia.html", {"url": storageRef})


def create(request):
    return render(request, 'create.html')


def post_create(request):
    import time
    from datetime import datetime, timezone
    import pytz

    tz = pytz.timezone('Europe/Madrid')
    time_now = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    work = request.POST.get('work')
    progress = request.POST.get('progress')

    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    data = {
        "work": work,
        'progress': progress
    }
    database.child('users').child(a).child('reports').child(millis).set(data)  # millis es marca temporal, como se
    # llama el padre en la ruta
    name = database.child('users').child(a).child('details').child('name').get().val()
    return render(request, 'welcome.html', {'e': name})


def check(request):
    import datetime
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']

    timestamps = database.child('users').child(a).child('reports').shallow().get().val()
    lis_time = []
    for i in timestamps:
        lis_time.append(i)

    lis_time.sort(reverse=True)

    print(lis_time)
    work = []
    prog = []

    for i in lis_time:
        wor = database.child('users').child(a).child('reports').child(i).child('work').get().val()
        work.append(wor)
    print(work)

    for i in lis_time:
        pro = database.child('users').child(a).child('reports').child(i).child('progress').get().val()
        prog.append(pro)
    print(prog)

    date = []
    for i in lis_time:
        i = float(i)
        dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
        date.append(dat)

    print(date)

    comb_lis = zip(lis_time, date, work, prog)
    name = database.child('users').child(a).child('details').child('name').get().val()

    return render(request, 'check.html', {'comb_lis': comb_lis, 'e': name})


def modificar(request):
    time = request.GET.get('z')
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    work = database.child('users').child(a).child('reports').child(time).child('work').get().val()
    progress = database.child('users').child(a).child('reports').child(time).child('progress').get().val()
    name = database.child('users').child(a).child('details').child('name').get().val()
    database.child('users').child(a).child('reports').child(time).remove()
    return render(request, 'modificar.html', {'e': name, "work": work, "prog": progress})


def eliminar(request):
    time = request.GET.get('z')
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    database.child('users').child(a).child('reports').child(time).remove()
    return check(request)

##############
# NEEEEEEEEW #
##############

def home(request):
    context = {'active' : 'Inicio'}
    return render(request, 'new/home.html', context)

def app(request):
    context = {'active' : 'Aplicación'}
    return render(request, 'new/app.html', context)

def autodiagnostico(request):
    evaluaciones = models.Evaluacion.objects.all()
    context = {'active' : 'Autodiagnostico', 'evaluaciones': evaluaciones}
    return render(request, 'new/autodiagnostico.html', context)

def formulario(request):
    context = {'active' : 'Autodiagnostico'}
    return render(request, 'new/formulario.html', context)

@csrf_exempt # NO SEGURO?, CAMBIAR EN PROD?
def resultados(request):
    if request.method == 'POST':
        datos = request.POST
        sector = [4,5,5,5,4,4,4] # Valores medios del sector
        dict = {'Muy en desacuerdo':1, 'En desacuerdo':2, 'Ligeramente  desacuerdo':3, 'Ligeramente de acuerdo':4, 'De acuerdo':5, 'Muy de acuerdo': 6}
        respuestas = [
            (dict[datos.get('1[]')] + dict[datos.get('2[]')] + dict[datos.get('3[]')] + dict[datos.get('4[]')] + dict[datos.get('5[]')])/5, #finalidadlicitudyconsentimiento
            dict[datos.get('6[]')], #limitacion
            (dict[datos.get('7[]')] + dict[datos.get('8[]')] + dict[datos.get('9[]')] + dict[datos.get('10[]')] + dict[datos.get('11[]')])/5, #transparencia
            (dict[datos.get('12[]')] + dict[datos.get('13[]')])/2, #decisionesautomatizadasperfilado
            (dict[datos.get('14[]')] + dict[datos.get('15[]')])/2, #control
            dict[datos.get('16[]')], #eipd
            (dict[datos.get('17[]')] + dict[datos.get('18[]')])/2, #otros
        ]
        evaluacion = models.Evaluacion.objects.create(respuestas=respuestas)
        finalidadlicitudyconsentimiento = respuestas[0]
        limitacion = respuestas[1]
        transparencia = respuestas[2]
        decisionesautomatizadasperfilado = respuestas[3]
        control = respuestas[4]
        eipd = respuestas[5]
        otros = respuestas[6]
        context = {
            'active' : 'Autodiagnostico',
            'sector':sector,
            'respuestas': respuestas,
            'sumrespuestas': sum(respuestas),
            'limitacion': limitacion,
            'finalidadlicitudyconsentimiento':finalidadlicitudyconsentimiento,
            'transparencia': transparencia,
            'decisionesautomatizadasperfilado':decisionesautomatizadasperfilado,
            'control':control,
            'eipd':eipd,
            'otros':otros
        }
    else:
        return redirect('/autodiagnostico/')
    return render(request, 'new/resultados.html', context)

def pasados(request, id):
    evaluacion = models.Evaluacion.objects.get(id=id)
    respuestas = evaluacion.respuestas
    for ch in [' ','[',']']:
        respuestas = respuestas.replace(ch,'')
    print(respuestas)
    respuestas = list(map(float, respuestas.split(',')))
    sector = [4,5,5,5,4,4,4] # Valores medios del sector
    finalidadlicitudyconsentimiento = respuestas[0]
    limitacion = respuestas[1]
    transparencia = respuestas[2]
    decisionesautomatizadasperfilado = respuestas[3]
    control = respuestas[4]
    eipd = respuestas[5]
    otros = respuestas[6]
    context = {
        'active' : 'Autodiagnostico',
        'sector':sector,
        'respuestas': respuestas,
        'limitacion': limitacion,
        'sumrespuestas': sum(respuestas),
        'finalidadlicitudyconsentimiento':finalidadlicitudyconsentimiento,
        'transparencia': transparencia,
        'decisionesautomatizadasperfilado':decisionesautomatizadasperfilado,
        'control':control,
        'eipd':eipd,
        'otros':otros
    }
    return render(request, 'new/resultados.html', context)
