import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from music_teacher_booking_app.models import *



def admin_home(request):
    return render(request,'admin/admin_index.html')

def login_get(request):
    return render(request,'login_index.html')

def  login_post(request):
    username1 = request.POST['usname']
    password1 = request.POST['pword']

    lobj = login.objects.filter(username = username1,password = password1)
    if lobj.exists():
        request.session['login'] = 1
        lobj = lobj[0]
        if lobj.usertype == "admin":
            request.session['lid']=lobj.id
            return HttpResponse("<script>alert('login successfully');window.location='/admin_home'</script>")
        elif lobj.usertype == "musicteacher":
            request.session['lid'] = lobj.id
            request.session['mid'] = music_teacher.objects.get(LOGIN=lobj.id).id
            return HttpResponse("<script>alert('login successfully');window.location='/musicteacher_home'</script>")

        elif lobj.usertype == "user":
            request.session['lid'] = lobj.id
            request.session['sid'] = user.objects.get(LOGIN=lobj.id).id
            request.session['name'] = user.objects.get(LOGIN=lobj.id).name
            return HttpResponse("<script>alert('login successfully');window.location='/user_index'</script>")

        else:
            return HttpResponse("<script>alert('user not found');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('invalid user');window.location='/'</script>")


def logout(request):
    request.session['login'] = 0
    return HttpResponse("<script>alert('logig out..');window.location='/'</script>")


###################################admin###########################################

def add_category_get(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request,'admin/add_category.html')


def add_category_post(request):


    category1 = request.POST['catg']

    c = category.objects.filter(category_name = category1)
    if c.exists():
        return HttpResponse("<script>alert('category already exist');window.location='/add_category_get#module1'</script>")
    else:

        obj = category()
        obj.category_name = category1
        obj.save()
        return HttpResponse("<script>alert('category add successfully');window.location='/view_category_admin#module1'</script>")


def view_category_admin(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data = category.objects.all()
    return render(request,'admin/view_category.html',{'data':data})

def edit_category_get(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data1 = category.objects.get(id=id)
    return render(request,'admin/update_category.html',{'data1':data1})

def edit_category_post(request,id):
    category1 = request.POST['catg']
    category.objects.filter(id=id).update(category_name = category1)
    return HttpResponse("<script>alert('category update successfully');window.location='/view_category_admin#module1'</script>")

def delete_category(request,id):
    category.objects.get(id=id).delete()
    return HttpResponse("<script>alert('delete successfully');window.location='/view_category_admin#module1'</script>")

def view_musicteacher_verifie(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data2 = music_teacher.objects.filter(LOGIN__usertype = "pending")
    return render(request,'admin/accept_treacher.html',{'data2':data2})

def accept_teacher(request,id):
    login.objects.filter(id=id).update(usertype = "musicteacher")
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("riss.abhijith@gmail.com", "sdvy imwc tgcb crkb")
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = "riss.abhijith@gmail.com"
    msg['To'] = login.objects.get(id=id).username
    msg['Subject'] = "registration request"
    body = "your registration request approved sucessfully.."
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    return HttpResponse("<script>alert('accept successfully');window.location='/view_verified_teacher#module1'</script>")

def reject_teacher(request,id):
    login.objects.filter(id=id).update(usertype = "rejected")
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("riss.abhijith@gmail.com", "sdvy imwc tgcb crkb")
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = "riss.abhijith@gmail.com"
    msg['To'] = login.objects.get(id=id).username
    msg['Subject'] = "registration request"
    body = "Sorry for the inconvenience. Your registration request was rejected. Please try again later."
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    return HttpResponse("<script>alert('reject successfully');window.location='/admin_home'</script>")


def view_verified_teacher(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data3 = music_teacher.objects.filter(LOGIN__usertype = "musicteacher")
    return render(request,'admin/view_accepted_teacher.html',{'data3':data3})


def view_rating_admin(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data4 = rating.objects.all()
    return render(request,'admin/view_rating.html',{'data4':data4})

def view_user(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data5 = user.objects.all()
    return render(request,'admin/view_user.html',{'data5':data5})

def view_feedback(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data6 = feedback.objects.all()
    return render(request,'admin/view_feedback.html',{'data6':data6})

def change_password_get(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request,'change_password.html')

def change_password_post(request):
    current_password1 = request.POST['current_password']
    new_password1 = request.POST['new_password']
    conform_password1 = request.POST['conform_password']

    password = login.objects.filter(password=current_password1, id = request.session['lid'] )
    if password.exists():
        if new_password1 == conform_password1:
            login.objects.filter(id = request.session['lid']).update(password = new_password1)
            return HttpResponse("<script>alert('password changed successfully');window.location='/'</script>")
        else:
            return HttpResponse("<script>alert('wrong password');window.location='/change_password_get'</script>")

    else:
        return HttpResponse("<script>alert('invalid password');window.location='/change_password_get'</script>")

############################music teacher ################################

def musicteacher_home(request):
    return render(request,'music_teacher/musicteacher_index.html')

def musicteacher_register_get(request):
    # if request.session['login'] == "0":
    #     return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request,'music_teacher/music_teacher_register.html')

def musicteacher_register_post(request):
    name1 = request.POST['name']
    email1 = request.POST['email']
    phone1 = request.POST['phone']
    pin1 = request.POST['pin']
    post1 = request.POST['post']
    place1 = request.POST['place']
    password1 = request.POST['password']
    conf_password1 = request.POST['cnf_password']
    photo1 = request.FILES['photo']
    d=datetime.datetime.now().strftime('%y%m%d-%H%M%S')
    fs = FileSystemStorage()
    fs.save(r"C:\Users\abhij\PycharmProjects\music_teacher_booking\music_teacher_booking_app\static\\"+ d + '.jpg', photo1)
    photo2 = '/static/'+ d + '.jpg'
    latitude1 = request.POST['latitude']
    longitude1 = request.POST['longitude']
    x = music_teacher.objects.filter(email = email1)
    if x.exists():
        return HttpResponse("<script>alert('email already exist');window.location='/musicteacher_register_get'</script>")

    elif conf_password1 == password1:

        obj2 = login()
        obj2.username = email1
        obj2.password = password1
        obj2.usertype = 'pending'
        obj2.save()

        obj1 = music_teacher()
        obj1.name = name1
        obj1.email = email1
        obj1.phone = phone1
        obj1.pin = pin1
        obj1.post = post1
        obj1.place = place1
        obj1.image = photo2
        obj1.latitude = latitude1
        obj1.longitude = longitude1
        obj1.LOGIN = obj2
        obj1.save()
        return HttpResponse("<script>alert('Register successfully');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('password missmatching');window.location='/musicteacher_register_get'</script>")






def view_category(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data7 = category.objects.all()
    for i in data7:
        if own_category.objects.filter(CATEGORY_id=i.id,MUSIC_TEACHER= request.session['mid']).exists():
            i.status = '0'
        else:
            i.status = '1'
    return render(request,'music_teacher/view_category.html',{'data7':data7})

def add_own_category_get(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request,'music_teacher/add_own_category.html',{'id':id})

def add_own_category_post(request,id):
    fees1 = request.POST['fees']

    obj3 = own_category()
    obj3.fees = fees1
    obj3.MUSIC_TEACHER_id = request.session['mid']
    obj3.CATEGORY_id = id
    obj3.save()
    return HttpResponse("<script>alert('added successfully');window.location='/view_category#module2'</script>")


def view_own_category(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data8 = own_category.objects.filter(MUSIC_TEACHER=request.session['mid'])
    for i in data8:
        if class_new.objects.filter(OWN_CATEGORY=i.id).exists():
            i.r = '1'
        else:
            i.r = '0'


    return render(request,'music_teacher/view_own_category.html',{'data8':data8})



def edit_own_category_get(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data9 = own_category.objects.get(id=id)
    return render(request,'music_teacher/edit_own_category.html',{'data9':data9})

def edit_own_category_post(request,id):
    fees1 = request.POST['fees']

    own_category.objects.filter(id=id).update(fees = fees1)
    return HttpResponse("<script>alert('Update successfully');window.location='/view_own_category#module2''</script>")


def delete_own_category(request,id):
    own_category.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Delete successfully');window.location='/view_own_category#module2''</script>")



def add_class_time_get(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request,'music_teacher/allote_time_post.html',{'id':id})

def add_class_time_post(request,id):
    day1 = request.POST['days']
    star1 = request.POST['strtime']
    end1 = request.POST['endtime']

    obj4 = class_new()
    obj4.day = day1
    obj4.starttime = star1
    obj4.endtime = end1
    obj4.MUSIC_TEACHER_id = request.session['mid']
    obj4.OWN_CATEGORY_id = id
    obj4.save()
    return HttpResponse("<script>alert('add successfully');window.location='/view_own_category#module2'</script>")


def view_timesloats(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data10 = class_new.objects.filter(MUSIC_TEACHER = request.session['mid'] )
    return render(request,'music_teacher/view_time sloats.html',{'data10':data10})

def edit_time_sloat_get(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data11 = class_new.objects.get(id=id)
    return render(request,'music_teacher/edit_timesloat.html',{'data11':data11})

def edi_time_sloat_post(request,id):
    day1 = request.POST['days']
    star1 = request.POST['strtime']
    end1 = request.POST['endtime']

    class_new.objects.filter(id=id).update(day = day1,starttime = star1,endtime = end1)
    return HttpResponse("<script>alert('update successfully');window.location='/view_timesloats#module2'</script>")

def delete_time_slot(request,id):
    class_new.objects.get(id=id).delete()
    return HttpResponse("<script>alert('delete successfully');window.location='/view_timesloats#module2'</script>")


def view_request(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data12 = requests.objects.filter(OWN_CATEGORY__MUSIC_TEACHER = request.session['mid'],status="pending")
    return render(request,'music_teacher/view_request.html',{'data12':data12})


def accept_request(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    requests.objects.filter(id=id).update(status = "approved")
    return HttpResponse("<script>alert('approve successfully');window.location='/view_request#module2'</script>")

def rejet_request(request,id):
    requests.objects.filter(id=id).update(status = "rejected")
    return HttpResponse("<script>alert('rejected successfully');window.location='/view_request#module2'</script>")

def request_allote_time(request):
    data13=requests.objects.filter(status = "approved")
    for i in data13:
        if allocate_time.objects.filter(REQUESTS = i.id).exists():
            i.r = "0"
        else:
            i.r ="1"

    return render(request,'music_teacher/request_allote_time.html',{'data13':data13})


def view_alote_time(request,id,rid):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data14 = class_new.objects.filter(OWN_CATEGORY = id)
    print("data14",data14)
    return render(request,'music_teacher/view_allot_time.html',{'data14':data14,"rid":rid})

def allocate_times(request,rid,id):
    d = datetime.datetime.now()
    obj = allocate_time()
    obj.REQUESTS_id = rid
    obj.CLASS_NEW_id = id
    obj.date = d
    obj.save()

    return HttpResponse("<script>alert('selected');window.location='/view_verified_request#module2'</script>")




def view_payment_history(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data15 = payment.objects.filter(REQUESTS__OWN_CATEGORY__MUSIC_TEACHER = request.session['sid'])
    return render(request,'music_teacher/view_payment_history.html',{'data15':data15})

def view_rating(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data16 = rating.objects.all()
    return render(request,'music_teacher/view_rating.html',{'data16':data16})


def view_verified_request(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data23 = allocate_time.objects.filter(REQUESTS__OWN_CATEGORY__MUSIC_TEACHER = request.session['sid'],REQUESTS__status = 'approved')
    return render(request,'music_teacher/view_verified_request.html',{'data23':data23})

##############################USER################################################################

def user_index(request):
    return render(request,'user/user_index.html')


def user_register(request):
    # if request.session['login'] == "0":
    #     return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request,'user/user_register.html')

def user_register_post(request):
    name1 = request.POST['name']
    phone1 = request.POST['phone']
    emai1 = request.POST['email']
    pin1 = request.POST['pin']
    post1 = request.POST['post']
    place1 = request.POST['place']
    password1 = request.POST['password']
    conf_password1 = request.POST['conf_password']

    y = user.objects.filter(email = emai1)
    if y.exists():
        return HttpResponse("<script>alert('email already exist');window.location='/user_register'</script>")

    elif password1 == conf_password1:
        obj5 = login()
        obj5.username = emai1
        obj5.password = conf_password1
        obj5.usertype = "user"
        obj5.save()

        obj6 = user()
        obj6.name = name1
        obj6.phone = phone1
        obj6.email = emai1
        obj6.pin = pin1
        obj6.post = post1
        obj6.place = place1
        obj6.LOGIN_id = obj5.id
        obj6.save()

        return HttpResponse("<script>alert('Register successfully');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('password is incorrect');window.location='/user_register'</script>")



def user_home(request):
    return render(request,'user/User_home.html')

def view_all_category(request):
    # if request.session['login'] == "0":
    #     return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data17 = category.objects.all()
    return render(request,'user/view_all_category.html',{'data17':data17})

# def view_all_category_post(request):
#     if request.session['login'] == "0":
#         return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
#     data17 = category.objects.filter(category_name__contains=request.POST['s'])
#     return render(request,'user/view_all_category.html',{'data17':data17})

def view_teacher_from_category(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data18 = own_category.objects.filter(CATEGORY=id)
    for i in data18:
        if requests.objects.filter(OWN_CATEGORY=i.id).exists():
            i.rr = '0'
        else:
            i.rr = '1'

        rating_new =  rating.objects.filter(MUSIC_TEACHER = i.MUSIC_TEACHER_id).aggregate(rating = Avg('rating'))
        print(rating_new)
        if rating_new['rating'] is None:
            i.rating = "0"
        else:
            i.rating = str(int(rating_new['rating']))
        print(rating_new)

    return render(request,'user/view_teacher_from_category.html',{'data18':data18})

def send_request(request,id):
    d= datetime.datetime.now()

    obj = requests()
    obj.request_date = d
    obj.status = "pending"
    obj.USER_id = request.session['sid']
    obj.OWN_CATEGORY_id = id
    obj.save()
    return HttpResponse("<script>alert('request send sucessfully');window.location='/view_all_category#module3'</script>")


def user_view_rating(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data19 = rating.objects.filter(MUSIC_TEACHER=id)
    return render(request, 'user/user_view_rating.html',{'data19':data19})

def view_user_request(request):
    data = requests.objects.filter(USER=request.session['sid'],status= "pending",)
    return render(request,'user/view_requests.html',{'data':data})


def view_approved_request(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data20 = allocate_time.objects.filter(REQUESTS__USER=request.session['sid'],REQUESTS__status= "approved")
    for i in data20:
        if rating.objects.filter(MUSIC_TEACHER = i.CLASS_NEW.MUSIC_TEACHER).exists():
            i.ff = "0"
        else:
            i.ff = "1"
    return render(request, 'user/View_approved_request.html',{'data20':data20})

def view_rejected_request(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data21 = requests.objects.filter(USER=request.session['sid'],status= "rejected")
    return render(request, 'user/view_rejected_request.html', {'data21': data21})



def send_rating_get(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request, 'user/send_rating.html',{'id':id})


def send_rating_post(request,id):
    rating1 = request.POST['star']
    d= datetime.datetime.now()

    obj = rating()
    obj.rating = rating1
    obj.date = d
    obj.USER_id = request.session['sid']
    obj.MUSIC_TEACHER_id  = id
    obj.save()
    return HttpResponse("<script>alert('send successfully');window.location='/view_approved_request#module3'</script>")


def send_feedback_get(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request,'user/send_feedback.html')


def send_feedback_post(request):
    feedback1 = request.POST['feed']
    d= datetime.datetime.now()

    obj = feedback()
    obj.feedback = feedback1
    obj.date = d
    obj.USER_id = request.session['sid']
    obj.save()
    return HttpResponse("<script>alert('send successfully');window.location='/user_index'</script>")


def make_payment(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data22 = requests.objects.filter(USER = request.session['sid'],status = 'approved')

    for i in data22:
        x = payment.objects.filter(REQUESTS=i.id,date__month = datetime.datetime.now().strftime('%m'),date__year = datetime.datetime.now().strftime('%Y'))
        if x.exists():

            i.payment_status = 'paid'
            i.payment_month = str(x[0].date.month) +"/"+ str(x[0].date.year)
        else:
            i.payment_status = 'not paid'
            i.payment_month = datetime.datetime.now().strftime('%m') +"/"+datetime.datetime.now().strftime('%Y')
    print(data22)
    return render(request,'user/make_payment.html',{'data22':data22})


def user_payment(request,id,fee):
    request.session['pid'] =  id
    import razorpay

    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

    razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    amount = int(fee) *100
    # amount = float(amount)

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }

    # Create an order
    order = razorpay_client.order.create(data=order_data)

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }

    return render(request,'user/payment.html', {'razorpay_api_key': razorpay_api_key,
                                            'amount': order_data['amount'],
                                            'currency': order_data['currency'],
                                            'order_id': order['id'], "id":id})


def payment_complete(request,id):
    obj = payment()
    obj.payment_status='paid'
    obj.payment_method='online'
    obj.REQUESTS_id=   request.session['pid']
    obj.date=datetime.datetime.now().strftime("%Y-%m-%d")
    obj.save()

    return redirect('/make_payment')





