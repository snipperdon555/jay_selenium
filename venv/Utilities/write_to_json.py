import json
import random

# write the created user id to file
def write_user_id_to_text(user_id):
    with open("../TestData/testdata.txt", 'a') as f:
        f.write(user_id+"\n")

# read the existing user ids from file and return one
def read_userid_from_textfile():
    with open("../TestData/testdata.txt", 'r') as f:
        data_into_list = [line.rstrip() for line in f]
        print(data_into_list)
        return (random.choice(data_into_list))
