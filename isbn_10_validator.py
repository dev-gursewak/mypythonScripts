def valid_ISBN10(isbn):
    isbn_list = []
    for i in isbn:
        if i=='X':
            isbn_list.append(10)
        else:
            isbn_list.append(i)
    
        




#ISBN     : 1 1 1 2 2 2 3 3 3  9
#position : 1 2 3 4 5 6 7 8 9 10
#(1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0
# X repersents 10
print(valid_ISBN10('1112223339'))
print(valid_ISBN10('048665088X'))
print(valid_ISBN10('1293000000'))
print(valid_ISBN10('1234554321')) #True
valid_ISBN10('1234512345')
valid_ISBN10('1293')
valid_ISBN10('X123456788')
valid_ISBN10('ABCDEFGHIJ')
valid_ISBN10('XXXXXXXXXX')
valid_ISBN10('123456789T') #False

#check list
#The character should be int expect X
#X should be treated as digit which is 10.
#The length should be 10 digits.
#X is considerd as one digit.


