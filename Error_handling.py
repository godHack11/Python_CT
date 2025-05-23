try:
	f = open('Introo.py')
except Exception:
    print('Sorry. This file does not exist')	



try:
	f = open('Introo.py')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)    



try:
	f = open('Intro.py')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)  
else:
    pass 



try:
	f = open('Intro.py')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)  
else:
    print(f.read())
    f.close() 
   



try:
	f = open('Intro.py')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)  
else:
    print(f.read())
    f.close() 
finally:
    print("Executing Finally...")
