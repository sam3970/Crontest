#!/usr/bin/python3
#-*- coding: utf-8 -*-

class Person(object):
    
    my_class_var = 'sklee02'
    
    def __init__(self, year, month, day, sex):
        self.year = year
        self.month = month
        self.day = day
        self.sex = sex
        
    def __str__(self):
        return '{}년 {}월 {}일생 {}입니다.'.format(self.year, self.month, self.day, self.sex)
    
    @classmethod
    def ssn_constructor(cls, ssn):
        front, back = ssn.split('-')
        sex = back[0]
        
        if sex == '1' or sex == '2':
            year = '19' + front[:2]
        else:
            year = '20' + front[:2]
            
        if (int(sex) % 2) == 0:
            sex = '여성'
        else:
            sex = '남성'
            
        month = front[2:4]
        day = front[4:6]
        
        return cls(year, month, day, sex)
    
    @staticmethod
    def is_work_day(day):
        # weekday() 함수의 리턴값은
        # 월: 0, 화: 1, 수: 2, 목: 3, 금: 4, 토: 5, 일: 6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
ssn_1 = '900829-1034356'
ssn_2 = '051224-4061569'

person_1 = Person.ssn_constructor(ssn_1)
print(person_1)

person_2 = Person.ssn_constructor(ssn_2)
print(person_2)

import datetime
# 일요일 날짜 오브젝트 생성
my_date = datetime.date(2016, 10, 9)

# 클래스를 통하여 스태틱 메소드 호출
print(Person.is_work_day(my_date))
# 인스턴스를 통하여 스태틱 메소드 호출
print(person_1.is_work_day(my_date))	
