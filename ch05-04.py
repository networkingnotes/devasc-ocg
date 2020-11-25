import csv

print("Please add a new router to the list")
hostname = input("What is the hostname? ")
ip = input("What is the IP address? ")
location = input("What is the location? ")

router = [hostname, ip, location]

with open("routerlist.csv", "a") as data:
    csv_writer = csv.writer(data, quoting=csv.QUOTE_ALL)
    csv_writer.writerow(router)
