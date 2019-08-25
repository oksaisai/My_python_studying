#coding=utf-8
def program_out():
    print 'This is a program'
    #print globals()
def input_char():
    str=raw_input('请输入您想输入的字符串：')
    print str
class ClassName:
    '所有学生的基类'
    empCount=0
    def __init__(self,name,record):
        self.name=name
        self.record=record
        ClassName.empCount+=1
    def displaycount(self):
        print 'Total student %d' %ClassName.empCount
    def displaystudent(self):
        print 'Name:', self.name,',record:',self.record

