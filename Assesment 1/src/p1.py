# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021A
# Assignment: 1
# Author: Le Phuc Thinh (s3893964)
# Created date: 12/4/2021
# Last modified date: 18/4/2021

def item_cal(house_id, no_adult, no_child, no_days, allergies, no_patient):
    # importing math to round up numbers later
    import math
    one_adult_food_portion = 3  # daily food consumption for 1 adult
    one_adult_milk_portion = 0.5  # daily milk consumption for 1 adult
    one_child_food_portion = 0.7 * 3  # daily food consumption for 1 child

    cow_milk_qty = 0
    almond_milk_qty = 0
    no_adult_with_no_medical_condition = (no_adult - no_patient)

    # calculating total food
    food_qty = (no_days * (one_adult_food_portion * no_adult + one_child_food_portion * no_child))

    # checking if the household use cow milk or almond milk
    if allergies == "nut" or allergies == "none":
        cow_milk_qty = (no_adult_with_no_medical_condition * 0.5 + no_child * 2) * no_days
    else:
        almond_milk_qty = (no_adult_with_no_medical_condition * 0.5 + no_child * 2) * no_days
    # calculating total treatment milk and toilet paper
    tm_milk_qty = (no_patient * one_adult_milk_portion) * no_days
    toilet_paper_qty = no_adult_with_no_medical_condition * (no_days / 4) + no_patient * (no_days / 2) + no_child * (
            no_days / 3)

    # printing the message
    print('Household id', house_id, 'will get', math.ceil(food_qty), 'food portions,', math.ceil(cow_milk_qty),
          'liter(s) of cow milk,', math.ceil(almond_milk_qty), 'liter(s)of almond milk,', math.ceil(tm_milk_qty),
          'liter(s) of treatment milk, and'
          , math.ceil(toilet_paper_qty), 'toilet paper rolls.')

    # returning the values and rounding up all float value using math ceiling function
    return house_id, math.ceil(food_qty), math.ceil(cow_milk_qty), math.ceil(almond_milk_qty), math.ceil(tm_milk_qty) \
        , math.ceil(toilet_paper_qty)
