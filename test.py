#coding=utf-8
import math
from package import program
from package.hello_world import Hello_world
print 'Hello world'
print '怎么回事？'
Hello_world()
print dir(math)
program.program_out()
print dir(program)
program.input_char()
Mystudent1=program.ClassName('oksaisai', 100)
Mystudent2=program.ClassName('oksaisai123', 99)
print program.ClassName.empCount
#del Mystudent1.record
print Mystudent1.record
print Mystudent1.record
print dir(program.ClassName)