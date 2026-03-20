from datetime import datetime
message=input("Enter Log: ")

time=datetime.now()

with open("log.txt","a") as file:
    file.write(f"{time} - {message}\n")
    print("log saved sucessfully")
