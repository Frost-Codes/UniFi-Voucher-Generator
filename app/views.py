from django.shortcuts import render
from pymongo.mongo_client import MongoClient
from django.http import JsonResponse
from django.contrib import messages
from .models import Image
import datetime
import re


uri = "YOUR_MONGO_DB_URI"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


database = client['YOUR_MONGO_DB_DATABASE']
collection = database['YOUR_MONGO_DB_COLLECTION']


def get_ip_address(request):
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
        print('Request', user_ip_address)
    else:
        ip = request.META.get('REMOTE_ADDR')
        print('Request', ip)
    return ip


def delete_many(delete_items={}):
    """

    :param delete_items:
    :return:
    """
    result = collection.delete_many(delete_items)
    return f'{result.deleted_count} Item(s) in the database have been deleted successfully'


def find(find_value={}):
    """

    :param find_value: Dictionary where key is column name and value is search item
    :return: a list of the values that match the find_value
    """
    result = collection.find(find_value)
    data = []
    for item in result:
        data.append(item)
    return data

# Create your views here.


def home(request):
    entries = find()
    vouchers = []
    image = Image.objects.get(image_description='Logo')
    print(image.image.url)
    for voucher in entries:
        vouchers.append((voucher['_id'], voucher['hours']))
    return render(request, 'app/home.html', locals())


def twenty_four(request):
    entries = find(find_value={'hours': 24})
    image = Image.objects.get(image_description='Logo')
    vouchers = []
    for voucher in entries:
        vouchers.append((voucher['_id'], voucher['hours']))
    return render(request, 'app/twenty_four.html', locals())


def seventy_two(request):
    entries = find(find_value={'hours': 72})
    image = Image.objects.get(image_description='Logo')
    vouchers = []
    for voucher in entries:
        vouchers.append((voucher['_id'], voucher['hours']))
    return render(request, 'app/seventy_two.html', locals())


def ninety_six(request):
    entries = find(find_value={'hours': 96})
    image = Image.objects.get(image_description='Logo')
    vouchers = []
    for voucher in entries:
        vouchers.append((voucher['_id'], voucher['hours']))
    return render(request, 'app/ninety_six.html', locals())


def search(request):
    query = request.GET['search']
    pattern = '^'+query
    pattern = re.compile(pattern)
    entries = find(find_value={'_id': pattern})
    image = Image.objects.get(image_description='Logo')
    vouchers = []
    for voucher in entries:
        vouchers.append((voucher['_id'], voucher['hours']))
    return render(request, 'app/search.html', locals())


def write_log(ip, used_id):
    with open('logs/mark_used.log', 'a'):
        file.write('\n' + 'Date Time:\t' + str(datetime.datetime.now()) + '\n')
        file.write(f'IP Address:\t {ip}\n')
        file.write(f'Action:\t\t Marked Voucher ID : {used_id}: As Used\n')
        file.write(str('=' * 56) + '\n')


def mark_used(request):
    if request.method == 'GET':
        used_id = request.GET['used_id']
        result = collection.delete_one({'_id': used_id})
        ip = get_ip_address(request)
        # write_log(ip=ip, used_id=used_id)
        messages.success(request, f'Voucher ID {used_id} Marked As Used')
        data = {}
        return JsonResponse(data)


