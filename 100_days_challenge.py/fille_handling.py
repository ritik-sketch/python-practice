#_____________write file operation in file handling___________

with open("new_file.txt", "w") as file:
    file.write("this is my first file.\n")
    file.write("this is very easy yeah!!")
print("file writing succesfull")



#___________read file operation in file handling__________________

with open("new_file.txt", "r") as file:
    content = file.read()
    print("file data: ")
    print(content)


#__________append operation in file hamdling _____________

with open("new_file.txt", "a") as file:
    file.write("\nye sab maine likha hai ")
print("new content add kiy gya ")




with open("new content.txt" , "w") as content:
    content.write("im a data developer")
    content.write(" till diwli i join a new company ")
print("my goal load")

with open("new content.txt", "r") as content:
    content = content.read()
    print("content data: ")
    print(content)


with open("new content.txt", "a") as content:
    content.write("\nmy priority")
print("next goal added just 2 sec before")


with open("task.txt", "w") as task:
    task.write("learning python from start to end")
    task.write(" with scrach")
print("first task")

with open("task.txt", "r") as task:
    task = task.read()
    print("task data: ")
    print(task)

with open("task.txt", "a") as task:
    task.write("\nYe mujhe diwali se pahle khatam krna hai ")
    print("be serious")


with open("database.txt", "w") as database:
    database.write("sath me sql ki preparation krni hogi ")
    database.write(" backend aur data manupulation ke liye")
print("next task")

with open("database.txt", "r") as database:
    database = database.read()
    print("database data: ")
    print(database)

with open("database.txt", "a") as database:
    database.write("\nlearn how sql command perform in database work bench ")
print("keep gain real experience")




open("myfile.txt", "a").close()

with open("myfile.txt", "r+") as myfile:
    content = myfile.read(10)
    print(f"read content: {content}")

    myfile.seek(0)
    myfile.write("python")
    
    myfile.seek(0)
    final = myfile.read()
    print(f"Final content: {final}")

# Open the file in a+ mode
with open("my_file.txt", "a+") as file:
    # The file pointer is at the end, so a read returns nothing
    start_read = file.read()
    print(f"Read at start: '{start_read}'")

    # Append new data to the end
    file.write(" and it's fun!")

    # To read, we must move the cursor to the beginning
    file.seek(0)
    final_read = file.read()
    print(f"Read after appending: {final_read}")
# Try to create a new file
try:
    with open("new_file.txt", "x") as file:
        file.write("This file was created exclusively.")
    print("File 'new_file.txt' created successfully.")
except FileExistsError:
    print("Error: The file 'new_file.txt' already exists!")
