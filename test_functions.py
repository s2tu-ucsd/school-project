import project_code
from project_code import *

def test_Course():
    assert Course
    assert Course("code", "name", "year", 
                 "weekday", "start_time", "end_time")
    class_1 = Course("LIFR1b", "french conversation 1b", 2019, 
                 "tuesday and thursday", "0900", "1000")
    assert isinstance(class_1, Course)
    
def test_date():
    class_1 = Course("LIFR1b", "french conversation 1b", 2019, 
                 "tuesday and thursday", "0900", "1000")
    dates = class_1.date()
    assert isinstance(dates, list)
    assert dates == ['20190108','20190110', '20190115', '20190117','20190122','20190124',
                            '20190129','20190131', '20190205', '20190207','20190212', '20190214',
                            '20190219','20190221','20190226','20190228','20190305','20190307']
                            
def test_start_time():
    class_1 = Course("LIFR1b", "french conversation 1b", 2019, 
                 "tuesday and thursday", "0900", "1000")
    assert isinstance(class_1.start_time, str)
    assert class_1.start_time == "0900"
    