import re
def isvalid(num):
    
    pattern=re.compile('^(\\+\\d{1,3}( )?)?((\\(\\d{3}\\))|\\d{3})[- .]?\\d{3}[- .]?\\d{4}$')
   
    return pattern.match(num)


num=input('enter the number:')
if isvalid(num):
    print('valid mobile number')
else:
    print('invalid mobile number')
