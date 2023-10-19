print("\__||'__'||__/ - This Tool Made By Wctos")
print(" > Age challenge")


Question = int(input(' > How old are you? :  '))
if Question == 0:
    print(" > Invalid  input")
elif 0 <= Question <= 2:
    print(" > Baby")
elif 3 <= Question <= 12:
    print(" > Children ")
elif 13 <= Question <= 19:
    print(" > Teen ")
elif 20 <= Question <= 64:
    print(" > Adult ")
elif 65 <= Question <= 200:
    print(" > Elderly")
else:
    print(" > Invalid input")
