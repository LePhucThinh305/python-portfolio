# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021A
# Assignment: 1
# Author: Le Phuc Thinh (s3893964)
# Created date: 12/4/2021
# Last modified date: 18/4/2021

def priority_cal(data):
    # Looping through all the keys, value of data and then checking the value, changing it to that person priority
    for key, value in data.items():
        if value[0] == 'medical':
            data[key] = 1
        elif value[0] == 'military':
            data[key] = 2
        elif value[0] == 'diplomatic':
            data[key] = 3
        elif value[0] == 'essential':
            data[key] = 4
        elif value[0] == 'teacher':
            data[key] = 5
        elif value[1] > 65:
            data[key] = 6
        elif value[2]:
            data[key] = 7
        else:
            data[key] = 8
    return data
