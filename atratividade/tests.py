from django.http.response import HttpResponse
from django.test import TestCase

# Create your tests here.

import datetime

data = '2021-11-05'
if int(str(datetime.date.today()).replace('-', '')) > int(str(data).replace('-', '')):
    print(datetime.date.today())
else:
    print(data)