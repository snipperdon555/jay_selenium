from faker import Faker
import phonenumbers
import random,string

user_id =''.join(random.choices(string.ascii_letters + string.digits, k=16))
print(user_id)