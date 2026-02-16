# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021A
# Assignment: 1
# Author: Le Phuc Thinh (s3893964)
# Created date: 12/4/2021
# Last modified date: 18/4/2021

def data_check(house_id, no_adult, no_child, no_days, allergies, no_patient):
    error_type = []  # Creating a list of error types that occurred
    if no_adult < no_patient:
        print('Error type 1 in the data of Household id ' + str(house_id) + ': more patients than adults')
        error_type += 1
    if no_adult == 0 and no_child >= 1:
        print('Error type 2 in the data of Household id ' + str(house_id) + ': no adult but', no_child, 'children')
        error_type += 2
    if no_days < 14:
        print('Error type 3 in the data of Household id ' + str(house_id) + ': less than 14 days of quarantine')
        error_type += 3
    for data in [house_id, no_adult, no_child, no_days, no_patient]:  # Looping to check if any data is a float
        if type(data) == float:
            print('Error type 4 in the data of Household id ' + str(house_id) + ': ' + str(data) + ' is a float')
            error_type += 4
    return house_id, error_type
