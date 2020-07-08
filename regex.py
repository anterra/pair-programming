# PART 1

import re

def check_email(string):
    matched = re.match('[\w+.]*\@[a-z0-9.]+\.[a-z]+', string)
    return bool(matched)


#print(check_email('wo9.rd@department.example.com'))

test_cases_fail = ['hfij#kjdfvkl','Abc.example.com','this is not true','<invalid>@foo.com',
              'A@b@c@example.com','asterisk_domain@foo.*','just"not"right@example.com',
              'this is"not\allowed@example.com',
              'a"b(c)d,e:f;g<h>i[j\\k]l@example.com','this\ still\"not\\allowed@example.com']

test_cases_pass = ['b@d.net','1@d.net','b@domain.net','bob123@alice123.com',
              'very.common@example.com','niceandsimple@example.com',
              'a.little.lengthy.but.fine@dept.example.com','disposable.style.email.with+156@example.com',
              'disposable.style.email.with+symbol@example.com']


lst=[]
#for test_case in test_cases_pass:
#    lst.append(check_email(test_case))

#print(lst)


# PART 2

def check_email2(string):
    if '@' in string:
        atindex = string.index('@')
    else:
        return False
    str1 = string[:atindex]
    str2 = string[(atindex+1):]
    if '+' in str1:
        str1 = str1.replace('+','')
    if '.' in str1:
        str1 = str1.replace('.','')
    if '.' in str2:
        str2 = str2.replace('.','')
    if str1.isalnum() and str2.isalnum():
        return True
    else:
        return False



lst=[]
for test_case in test_cases_fail:
    lst.append(check_email2(test_case))

print(lst)
