from time import sleep
import vaccine_tracker
# pip install win10toast
from win10toast import ToastNotifier
toaster = ToastNotifier()

pincode =  [each.strip() for each in input("Enter comma separated pincodes: ").split(",")]  # ["823001", "824221"]
date = input("Enter Date in the format DD-MM-YYYY: ")
print(pincode)
while True:
    if len(pincode)==0:
        break
    for each in pincode:
        data = vaccine_tracker.find_vaccines(each, date)
        print("searching", each)
        if data:
            print(data)
            toast_message = "hospital-"+data[0]+", Date-"+data[1]+", Pin Code: "+data[2]
            toaster.show_toast("Vaccine Available",toast_message)
            sleep(10)
            pincode.remove(each)
    sleep(60)