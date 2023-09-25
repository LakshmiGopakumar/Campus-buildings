import csv

filePath = '/Users/buildings.csv'

#prompt user to select one of the three options display the details of the building to enter
def menu():
    print(" 'a' for Building/location name or part of the name")
    print(" 'b' for Reference number")
    print(" 'c' for classification")

menu()

#Open the csv file with csv reader
with open(filePath) as csvfile:
    reader = csv.DictReader(csvfile)
    option= input("Please enter your choice: ")
    #if the user want to enter the building name and find details
    if option == 'a':
        #promt the user to enter the building name
        building= input("Please enter the Building name/part of the building name that you want to enter : ")
        #create a loop to read the row which user entered
        for row in reader:
            if building == row['Building Name'] or building in row['Building Name']:
                for k,v in row.items():
                    print(k, ':' ,v)
                break
        else:
            print('Invalid input.')
    
    #if the user want to enter the reference number and find details
    elif option == 'b':
        reference= input("Enter the building reference number that you want to enter: ")
        #same as building name loop
        for row in reader:
            if reference == row['Reference']:
                for k,v in row.items():
                    print(k, ':', v)
                break
        else:
            print("Invalid input.")
    
    #if the user want to enter the classification and find the details
    elif option == 'c':
        classification= input("Please choose the classification from \n Enquiries \n Univeristy Buildings \n Science park \n Student Residence: ")
        #Each classification contains multiple buildings. So either use the reference number or building name along with classification
        enquiries = input("please enter the refernece number of the building you want to enter: ")
        for row in reader:
            if classification == row['Classification'] and enquiries == row['Reference']:
                for k,v in row.items():
                    print(k, ':', v)
                break
        else:
            print("Invalid input")

