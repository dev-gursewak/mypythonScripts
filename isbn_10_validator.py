def valid_ISBN10(isbn):




#ISBN     : 1 1 1 2 2 2 3 3 3  9
#position : 1 2 3 4 5 6 7 8 9 10
#(1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0
# X repersents 10
valid_ISBN10('1112223339')
valid_ISBN10('048665088X')
valid_ISBN10('1293000000')
valid_ISBN10('1234554321') #True
valid_ISBN10('1234512345')
valid_ISBN10('1293')
valid_ISBN10('X123456788')
valid_ISBN10('ABCDEFGHIJ')
valid_ISBN10('XXXXXXXXXX')
valid_ISBN10('123456789T') #False