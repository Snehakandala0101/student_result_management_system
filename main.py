from logger_config import logger
import os
import csv
import json


def menu():
    print("\n===== STUDENT RESULT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Generate Result")
    print("7. Exit")

def add_student():
    try:
        name=input("enter name")
        roll_no=int(input(" enter his/her rollnumber"))
        marks=int(input(" enter his/her marks"))

        file_exists = os.path.exists("data.csv")
        file_empty = not file_exists or os.path.getsize("data.csv") == 0
        with open("data.csv",'a',newline='')  as file:
            writer=csv.writer(file)
            # Write header only if file is new or empty
            if file_empty:
                writer.writerow(["Name", "Roll_No", "Marks"])
            writer.writerow([name,roll_no,marks])
        print("student added successfully!")
        logger.info(f"Student added: {name}, {roll_no}, {marks}")
    except ValueError:
        print("Marks must be a number")
        logger.error("Invalid marks input")
    except Exception as e:
        logger.error(f"Error in add_student: {e}")

def view_student():
    try:
        with open("data.csv",'r')  as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                print(f"Name: {row[0]}, Roll: {row[1]}, Marks: {row[2]}")
        logger.info("dispalyed students records")
    except FileNotFoundError as fe:
        print("No student records found.")
        logger.error(f"file not found:{fe}")

def search_student():
    try:
        roll_no=int(input("enter roll number to search"))
        found=False
        with open("data.csv",'r')  as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                if int(row[1] )== roll_no:
                    print("student found: ",row)
                    found=True
                    logger.info(f"student found: {roll_no}")
                    break

        if not found:
            print("Student not found.")
            logger.warning(f"Search failed for roll: {roll_no}")

    except Exception as e:
        logger.error(f"Error in search_student: {e}")

def update_marks():
    try:
        roll_no=int(input("enter roll number to search"))
        updated=False
        rows=[]
        with open("data.csv",'r')  as file:
            reader=csv.reader(file)
            header=next(reader)
            for row in reader:
                if int(row[1]) == roll_no:
                    new_marks=int(input("enter new marks:"))
                    row[2]=new_marks
                    updated=True
                rows.append(row)
        with open("data.csv",'w',newline="")  as file:
            writer=csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)
        if updated:
            print("Marks updated.")
            logger.info(f"Marks updated for roll number: {roll_no}")
        else:
            print("Student not found.")
            logger.warning(f"update failed  for roll number: {roll_no}")
    except ValueError:
        print("Invalid input. Roll number and marks must be numbers.")
        logger.error("Invalid numeric input in update_marks")
    except Exception as e:
        logger.error(f"Error in update_marks: {e}")

def del_student():
    try:
        roll_no=int(input("enter roll number to search"))
        deletion=False
        rows=[]
        with open("data.csv",'r')  as file:
            reader=csv.reader(file)
            header=next(reader)
            for row in reader:
                if int(row[1]) != roll_no:
                    rows.append(row)
                else:
                    deletion=True
        with open("data.csv",'w',newline="")  as file:
            writer=csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)
        if deletion:
            print("student deleted")
            logger.info(f"student deleted: {roll_no}")
        else:
            print("Student not found.")
            logger.warning(f"deletion failed  for roll number: {roll_no}")

    except Exception as e:
        logger.error(f"Error in del_student: {e}")


def generate_result():
    try:
        results=[]
        with open("data.csv","r") as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                name,roll_no,marks=row   
                marks=float(marks)
                result="Pass" if marks>=35 else "Fail"  
                results.append({
                    "name":name,
                    "roll_no":roll_no,
                    "marks":marks,
                    "result":result
                 }) 

        with open("results.json","w") as file:
            json.dump(results,file,indent=4)
        print("Results generated in results.json")
        logger.info("Results generated successfully")
    except Exception as e:
        logger.error(f"Error in generate_result:{e}")
    

while True:
    menu()
    choice=input("Enter your choice: ")

    if choice=="1":
        add_student()
    elif choice=="2":
        view_student()
    elif choice=="3":
        search_student()
    elif choice=="4":
        update_marks()
    elif choice=="5":
        del_student()
    elif choice=="6":
        generate_result()
    elif choice=="7":
        logger.info("Program exited")
        print("Exiting program...")
        break
    else:
        print("Invalid choice.")