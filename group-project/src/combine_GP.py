# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021A
# Assignment: 3 Group project
# Group:Dang Hoang Anh Khoa (s3836606),Le Phuc Thinh(s3893964), Ho Tran Minh Khoi(s3877653)
# Created date: 10/05/2021
# Last modified date: 28/05/2021

import sys #import these packs to run this program
import math#to calculate and round up some values
import os.path #use this to create file txt in the same directory
import random #randomly estimated health condition of spaceship and astronaut
import datefinder #to find datetime in text content
import keyboard #use this to create hoy key for each sub-program
from datetime import datetime, timedelta # import datetime pack for putting out time

######### This program is based on real time, you can change values below to check by yourselves #########

welcome_text = '''Welcome professor. What do you want ?
        +Press Ctrl + 1 : Set day of departure is today(it means data will reset)
        +Press Ctrl + 2 : Condition of spaceship
        +Press Ctrl + 3 : Add more information into diary
        +Press Ctrl + 4 : Read diary
        +Press Ctrl + 5 : Check storage'''
#### Create welcome sentence
date_time_now = datetime.now() # to get true time
days_to_mars_from_earth = math.ceil((330000000 / 39600) / 24) # estimated days need to reach Mars from the Earth unit is days
number_of_member = 4 #According to NASA, just only 4 astronauts for each launching

def main_screen(welcome_content):
    """
    :param welcome_content: Input welcome quote
    :return: nothing because this function is just used to control sub-program
    """
    print(welcome_content)
    reset_date_time, mars_journey, diary_write_key, diary_read_key, storage_key = 'ctrl + 1', 'ctrl + 2', 'ctrl + 3', 'ctrl + 4', 'ctrl + 5'
    while True:
        try:
            if keyboard.is_pressed(reset_date_time):
                day_from_departure(days_to_mars_from_earth)
                break
            if keyboard.is_pressed(mars_journey):
                mars_journey_status(pending_time)
                break
            if keyboard.is_pressed(diary_write_key):
                write_diary()
                break
            if keyboard.is_pressed(diary_read_key):
                read_diary()
                break
            if keyboard.is_pressed(storage_key):
                crew_consumption(days_to_mars_from_earth, math.floor((pending_time/60)/24), pending_time, number_of_member)
                break
        except:
            break

def mars_journey_status(minutes):
    """
    :param minutes: Total passed minutes on spaceship
    :return:
    """
    distance_from_earth_to_mars = 330000000  # the distance unit is kilometer
    current_velocity = 39600/60  # velocity unit is kilometer per minute
    total_fuel = 1390000  # unit for fuel is liter, the fuel is exactly enough for 1 round trip from earth to mars
    current_fuel_burn_rate = 2.77  # unit for burn rate is liter per minute
    time_to_mars_from_earth = math.ceil((330000000 / 39600) * 60) #unit is minute
    if 0 <= minutes <= time_to_mars_from_earth:
        distance_from_earth = minutes * current_velocity
        distance_from_mars = distance_from_earth_to_mars - distance_from_earth
        estimated_time_of_arrival = math.ceil((time_to_mars_from_earth - minutes)/60)#unit is hour
        current_fuel_level = total_fuel - (current_fuel_burn_rate * minutes)
    else:
        distance_from_earth = distance_from_earth_to_mars
        distance_from_mars = 0
        estimated_time_of_arrival = 0
        current_fuel_level = total_fuel / 2
    # We assume that the crew and spaceship health are measured in integer number percentage and cannot be equal to zero
    current_general_health_of_spaceship = random.randint(60, 100)
    current_general_health_of_crew_member = random.randint(50, 100)
    print("""
        Mars journey status:
        Current velocity =""", current_velocity, """kilometers per minute
        Distance from Earth =""", distance_from_earth, """kilometers
        Distance from Mars =""", distance_from_mars, """kilometers
        Estimated time of arrival =""", estimated_time_of_arrival, """hours
        Current fuel level =""", current_fuel_level, """liters
        Current fuel burn rate =""", current_fuel_burn_rate, """liters per minute
        Current general health of the space ship =""", current_general_health_of_spaceship, """%
        Current general health of the crew members =""", current_general_health_of_crew_member, """%""")

#file readind place
def day_from_departure(days):#set departure time and estimate arrive day
    #It will write present time into file txt in order to use later for some calculation with real time
    """
    :param days: number of days that was estimated based on NASA website
    :return:
    """
    estimated_arrive_time = (date_time_now + timedelta(days)).strftime('%Y-%m-%d %H:%M:%S')
    with open(os.path.join(sys.path[0], 'saving-day.txt'), 'w+')as departure:#read file in the same directory of project_file.py
        departure.write(str(date_time_now.strftime('%Y-%m-%d %H:%M:%S')))
        departure.seek(0)
        read = departure.readlines()
    print('Time of departure: ' + ''.join(read) + '\n')
    print('[Estimated] Arrive time: ', estimated_arrive_time)

def convert_strtime_into_datetime(file_day='saving-day.txt'):#convert string time in file into datetime type
    """
    :param file_day: open file with time that was saved in day_from_departure
    :return: return time that was found by datefinder pack
    """
    try:
        with open(os.path.join(sys.path[0], file_day), 'r+')as elapsed_time:
            date_match = datefinder.find_dates(elapsed_time.readline()) #using datefinder to identify date and time in file and change it to datetime type
            for time_match in date_match:
                return time_match #return this time for real time calculation
    except:
        day_from_departure(days_to_mars_from_earth)

def calculate_time_minutes(day_from_earth=convert_strtime_into_datetime(), date_now=date_time_now):#calculate elapsed minutes from departure day.
    """
    :param day_from_earth: This parameter based on (real)datetime(str) in file
    :param date_now: To get real date time
    :return: elapsed minutes on spaceship to Mars
    """
    try:
        minutes_from_earth = math.ceil((date_now - day_from_earth).total_seconds() / 60)#calculate exactly how many passed minutes from departure day
        return minutes_from_earth
    except:
        print('Automatically set departure day is to day. Please restart program !!!')
        sys.exit(1)

pending_time = calculate_time_minutes()
print('Minutes passed', pending_time)
print('Hours passed', math.floor(pending_time/60))

def read_diary(diary_read_file='Diary.txt'):
    """
    :param diary_read_file: using this file to read history contents of astronaut instead of using database
    :return: history content of diary
    """
    with open(os.path.join(sys.path[0], diary_read_file), 'r')as open_diary: #open file for just reading
            for line in open_diary:
                history = line.split()
                print(' '.join(history))

def write_diary(diary_write_file='Diary.txt'):
    """
    :param diary_write_file: using this file to save journal of astronaut instead of using database
    :return: this function will not return anything. Just using it to add more information into txt file
    """
    with open(os.path.join(sys.path[0], diary_write_file), 'a')as open_diary_day:#open file to write new things. If the file does not exist, 'a' function in file will automatically create the file.
        your_name = input(str('Author: '))
        print('Welcome ', your_name)
        findings = '#Findings: ' + input('Please enter daily findings: ')
        ideas = '#Idea: ' + input('Please enter new plants: ')
        mission ='#Duty: ' + input('Current mission: ')
        add_information = '#Addional information: ' + input('If you have any information please let us know: ')
        write_in_diary = [findings, ideas, mission, add_information]
        open_diary_day.write('Date and time : ')
        open_diary_day.write(date_time_now.strftime('%Y-%m-%d %H:%M:%S\n'))# print time
        for infor in write_in_diary:#using loop function to write contents itself.
                open_diary_day.write(infor + '\n')
        open_diary_day.write('\n')
        print('Thank you! Your information was saved')

def crew_consumption(total_days, days_passed, minutes_passed, crew_num):  # time = day  crew_num = number of the crew on broad
    """
    :param minutes_passed: total minutes passed on spaceship
    :param total_days: number of days that are estimated from real journey (NASA)
    :param days_passed: passed days from departure day
    :param crew_num: number of member on spaceship
    :return:
    """
    # total crew necessities available on broad
    total_oxygen = (11500 * crew_num * 2) * total_days # unit is liter, each people needs 11500 liters of oxygen per day * 2 because they need double to return
    total_food = (3 * crew_num * 2) * total_days# unit is portion
    total_water = (3 * crew_num * 2) * total_days #unit is liter
    total_toilet_paper = math.ceil(0.5 * crew_num * 2) * total_days
    # total crew necessities the crew have consumed
    oxygen_consumed = math.ceil(8 * minutes_passed) * crew_num #every people need 8 liters of oxygen per minute
    food_consumed = math.ceil(3 * days_passed) * crew_num
    water_consumed = math.ceil(3 * days_passed) * crew_num
    toilet_paper_consumed = math.ceil(0.5 * days_passed) * crew_num
    # total necessities left on board
    oxygen_left = math.ceil(total_oxygen - oxygen_consumed)
    food_left = math.ceil(total_food - food_consumed)
    water_left = math.ceil(total_water - water_consumed)
    toilet_paper_left = math.ceil(total_toilet_paper - toilet_paper_consumed)
    # create from for format function
    print('''***Totally based resources: %d oxygen(liters), %d food(portion), %d water(liters), %d toilet paper(rolls).
Totally remaining resources: %d oxygen(liters), %d food(portion), %d water(liters), %d toilet paper(rolls).
Totally consumed resources: %d oxygen(liters), %d food(portion), %d water(liters), %d toilet paper(rolls).'''%(total_oxygen, total_food, total_water, total_toilet_paper, oxygen_left,
                                                                                                                               food_left, water_left, toilet_paper_left, oxygen_consumed, food_consumed, water_consumed, toilet_paper_consumed))

main_screen(welcome_text)