import webbrowser, sys, pyperclip
sys.argv #for passing command line argument to it
if len(sys.argv) > 1 : # ["mapit.py", "ghanaur khurd", "street"]
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

#for opening website

webbrowser.open('https://www.google.com/maps/place/' + address)
    
print(address)
