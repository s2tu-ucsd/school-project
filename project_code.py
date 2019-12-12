

from datetime import datetime
from datetime import date
from datetime import timedelta
import time
from icalendar import Calendar, Event

"the following two function were quoted with slight modification from answer by Ben James on https://stackoverflow.com/questions/304256/whats-the-best-way-to-find-the-inverse-of-datetime-isocalendar"
def iso_year_start(iso_year):
    "The gregorian calendar date of the first day of the given ISO year"
    fourth_jan = date(iso_year, 1, 4)
    delta = timedelta(fourth_jan.isoweekday()-1)
    return fourth_jan - delta 

def iso_to_gregorian(iso_year, iso_week, iso_day):
    "Gregorian calendar date for the given ISO year, week and day"
    year_start = iso_year_start(iso_year)
    return year_start + timedelta(days=iso_day-1, weeks=iso_week-1)

class Course():
    """this class classes the courses with appropriate formula"""
    def __init__(self, code, name, year, 
                 weekday, start_time, end_time):
        self.code = code
        self.name = name
        self.year = year
        self.weekday = weekday
        self.start_time = start_time
        self.end_time = end_time
        
        
    
    
    def date(self):
        """ this function identifies keywords in input of weekday and returns dates of class
        """
   
        
        weekday_numb = []
       
        if "monday" in self.weekday:
            weekday_numb.append(1)
        if "tuesday" in self.weekday:
            weekday_numb.append(2)
        if "wednsday" in self.weekday:
            weekday_numb.append(3)
        if "thursday" in self.weekday:
            weekday_numb.append(4)
        if "friday" in self.weekday:
            weekday_numb.append(5)
        
        
        #instruction_begin = (2020, 2, 1)
        
        date_of_class = []
        
        total_week = 10
        week_num = 1
        while week_num < total_week:
            for num in weekday_numb:
                date = (self.year, week_num + 1, num)
                date_of_class.append(iso_to_gregorian(*date))
            week_num +=1
            continue
        
        str_form_date = []
        for date in date_of_class:
            str_date = date.strftime("%Y %m %d")
            str_form_date.append(str_date.replace(" ", ""))
        return str_form_date
    
    def start_time(self):
        "this function converts input into appropraite formula for ics file"
        start_time = "T" + self.start_time
        
        return start_time
   
    def end_time(self):
        "this function converts input into appropraite formula for ics file"
        end_time = "T" + self.end_time
        
        return end_time



def ics_generator(new_class):
    """ this function converts input of courses into ics file and export into the same directory
    """
    total_dates = new_class.date()
    new_cal = Calendar()
    new_cal.add('summary', new_class.code + " " + new_class.name)
    counter = 1
    for date in total_dates:
        event = Event()
        event["dtstart"] = date + "T" + new_class.start_time + "00"
        event["dtend"] = date + "T" + new_class.end_time + "00" 
        event["summary"] = new_class.code + " " + new_class.name + " lesson " + str(counter)
        new_cal.add_component(event)
        counter += 1
    f = open('course_schedule.ics', 'wb')
    f.write(new_cal.to_ical())
    f.close()