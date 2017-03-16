"""
Created on Tue Mar 14 15:25:59 2017
@author: Gabriel Aptekar

I decided to write some test cases using python.
You're welcome
"""


#test cases that I came up with
manual_tests=(
"""
-1+1+0+0+0+(0)*0*(10-1)
0*0
(-1-(-2-(-3-(-4-(-5)))))
((((((((((1))))))))))*(((((((((((5)))))))))))
+1-+1
-1+-1
(1)-1
9-8-7-6-5-4-3-2-1
(9-(8-(7-(6-(5-(4-(3-(2-(1)))))))))
3+(-3-11)*2*4*(54-46*1*(1))-(4*4*(4+(4*6)))
5-1
1-5
1--5
5--1
1+-5
5+-1
-1--5
-5--1
-1+5
-5+1
5+1
1+5
-5-+1
-1-+1
+5-1
+1-5
(0+1)*(-1+0+0+1)
(((((((((((((((((((((((1+(4234*(5*323+(6*(56*(132*(3123*(212*(1-(1))))))))))))))))))))))))))))))))
-1+-2+-3+-4+-5+-6+-7+-8+-9+-10+-11
""".split()
)           


#test cases that would be a pain to write out
generated_tests=[]
generated_tests.append("".join("1+" for i in range(100))+"1")
generated_tests.append("".join("1-1+" for i in range(100))+"0")


#combine all the tests
tests=manual_tests+generated_tests
answers=[test+"="+str(eval(test)) for test in tests]
#write out the tests
with open("tests/tests.txt","w") as file:
    file.write('\n'.join(tests))
with open("answers/tests.ans","w") as file:
    file.write('\n'.join(answers))


#this section is to create some random test cases...
#it's kinda of hackish but it works
from random import randint, choice
def random_test(max_exponent):
    #avoid lines longer than 256 chars
    numbers=256//(2*max_exponent+2)
    rand_number=lambda: str(randint(-(10**max_exponent),10**max_exponent))
    
    parts=[]
    for i in range(numbers):
        parts.append(choice( ["(","(",""] )+rand_number()+ (choice([")",")",""])if parts.count("(")>parts.count(")") else "") +choice("+*-"))
    line=''.join(parts)
    line+=rand_number()
    
    if line.count("(")>line.count(")"):
        line+=")"*(line.count("(")-line.count(")"))
    elif line.count("(")<line.count(")"):
        line="("*(line.count(")")-line.count("(")) +line
    return line

random_tests=[]
for i in range(2,19):
    for _ in range(1000):
        random_tests.append(random_test(i))

random_answers=[test+"="+str(eval(test)) for test in random_tests]        

with open("tests/random_tests.txt","w") as file:
    file.write('\n'.join(random_tests))
with open("answers/random_tests.ans","w") as file:
    file.write('\n'.join(random_answers))










