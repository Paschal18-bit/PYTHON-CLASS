# begining = 13
# end = 36
# while(begining < end):
#     print(begining)
#     begining = begining + 1



mylist = ["football", "tennis",  "basketball","golf", "hockey", "hunting"]

counter = 0
for item in mylist:

    
    if item == "golf":
        print("yes this is golf")
        print(counter)
        break
    else:
        counter += 1
        continue  




name = "Paschal"
for item in name:
    print(item)





for number in range(1,10):
    print(number)
else:
    print("this is the end of the loop")
