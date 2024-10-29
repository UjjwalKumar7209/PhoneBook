import mysql.connector

from tkinter import *

import tkinter.messagebox as tmsg



root = Tk()
root.geometry("400x229")
root.title("PhoneBook")

def show():
    con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='phone'
    )
    cursor = con.cursor()
    cursor.execute('SELECT * FROM specification')
    data = cursor.fetchall()
    for i in data:
        if i[0] == phoneEntry.get():
            specification = f"Name : {i[0]}\nBrand : {i[1]}\nProcessor : {i[2]}\nRAM : {i[3]}\nStorage {i[4]}\nScreen Size : {i[5]}\nCamera Resolution : {i[6]}\nBattery Capacity : {i[7]}\nOperating System : {i[8]}"

            showValue = StringVar()
            show = Label(root, textvariable=showValue, font="Aerial 10 italic")
            show.grid(row=2, column=1)
            showValue.set(specification)

def addData():
    root2 = Tk()
    root2.geometry("250x150")
    root2.title("Add Data")
    def login():
        if usernameEntry.get() == "user" and passwordEntry.get() == "1234":
            root3 = Tk()
            root3.geometry("600x400")
            root3.title("Add Data")
            def finalAdd():
                conn  = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='phone'
                )
                cursor = conn.cursor()
                phoneNameFinal = phoneNameEntry.get()
                brandNameFinal = brandNameEntry.get()
                processorFinal = processorEntry.get()
                ramFinal = ramEntry.get()
                storageFinal = storageEntry.get()
                screenFinal = screenEntry.get()
                cameraFinal = cameraEntry.get()
                batteryFinal = batteryEntry.get()
                osFinal = osEntry.get()

                query ="INSERT INTO specification(name, brand, processor, ram, storage, screen_size, camera_resolution, battery_capacity, os) VALUES('{}', '{}', '{}', {}, {}, '{}', '{}', '{}', '{}')".format(phoneNameFinal, brandNameFinal, processorFinal, ramFinal, storageFinal, screenFinal, cameraFinal, batteryFinal, osFinal)
                cursor.execute(query)
                conn.commit()
                tmsg.showinfo("Thanks.", "Your Data Inserted Successfully")


            Label(root3, text="Add Data to the Database.", font="Aerial 15 bold", bg="grey", relief=SUNKEN).grid(row=0, column=1, padx=5)
            Label(root3, text="Phone Name", font="Aerial").grid(row=1, column=0, padx=2, pady=2)
            Label(root3, text="Brand Name", font="Aerial").grid(row=2, column=0, padx=2, pady=2)
            Label(root3, text="Processor", font="Aerial").grid(row=3, column=0, padx=2, pady=2)
            Label(root3, text="RAM", font="Aerial").grid(row=4, column=0, padx=2, pady=2)
            Label(root3, text="Storage", font="Aerial").grid(row=5, column=0, padx=2, pady=2)
            Label(root3, text="Screen Size", font="Aerial").grid(row=6, column=0, padx=2, pady=2)
            Label(root3, text="Camera Resolution", font="Aerial").grid(row=7, column=0, padx=2, pady=2)
            Label(root3, text="Battery Capacity", font="Aerial").grid(row=8, column=0, padx=2, pady=2)
            Label(root3, text="OS", font="Aerial").grid(row=9, column=0, padx=2, pady=2)

            phoneNameValue = StringVar()
            brandNameValue = StringVar()
            processorValue = StringVar()
            ramValue = StringVar()
            storageValue = StringVar()
            screenValue = StringVar()
            cameraValue = StringVar()
            batteryValue = StringVar()
            osValue = StringVar()

            phoneNameEntry = Entry(root3, textvariable=phoneNameValue)
            phoneNameEntry.grid(row=1, column=1, padx=4)
            brandNameEntry = Entry(root3, textvariable=brandNameValue)
            brandNameEntry.grid(row=2, column=1, padx=4)
            processorEntry = Entry(root3, textvariable=processorValue)
            processorEntry.grid(row=3, column=1, padx=4)
            ramEntry = Entry(root3, textvariable=ramValue)
            ramEntry.grid(row=4, column=1, padx=4)
            storageEntry = Entry(root3, textvariable=storageValue)
            storageEntry.grid(row=5, column=1, padx=4)
            screenEntry = Entry(root3, textvariable=screenValue)
            screenEntry.grid(row=6, column=1, padx=4)
            cameraEntry = Entry(root3, textvariable=cameraValue)
            cameraEntry.grid(row=7, column=1, padx=4)
            batteryEntry = Entry(root3, textvariable=batteryValue)
            batteryEntry.grid(row=8, column=1, padx=4)
            osEntry = Entry(root3, textvariable=osValue)
            osEntry.grid(row=9, column=1, padx=4)
            Button(root3, text="Add Data", font="Aerial", bg="grey", relief=SUNKEN, command=finalAdd).grid(row=10, column=1, pady=8)


            root3.mainloop()
        else:
            tmsg.showerror("Error", "Username/Password is incorrect. Please check it and try again.")

    Label(root2, text="LogIn", font="Aerial 10 bold", bg="grey", padx=5, relief=SUNKEN).grid(row=0, column=1, pady=8)
    username = Label(root2, text="Username")
    username.grid(row=1, column=0)
    password = Label(root2, text="Password")
    password.grid(row=2, column=0)

    usernameValue = StringVar()
    passwordValue = StringVar()
    usernameEntry = Entry(root2, textvariable=usernameValue)
    usernameEntry.grid(row=1, column=1, padx=2, pady=4)
    passwordEntry = Entry(root2, textvariable=passwordValue)
    passwordEntry.grid(row=2, column=1, padx=2, pady=4)
    Button(root2, text="Login", bg="grey", padx=2, pady=2, command=login).grid(row=3, column=1, pady=5)

    root2.mainloop()


myMenu = Menu(root)
myMenu.add_command(label="Add Data", command=addData)
root.config(menu=myMenu)

Label(root, text="Welcome to this PhoneBook", font="Aerial 10 bold", bg="grey", fg="white", pady=5, relief=SUNKEN).grid(row=0, column=1, pady=8)
Label(root, text="Enter Phone Name", font="Aerial 10").grid(row=1, column=0)
phoneValue = StringVar()
phoneEntry = Entry(root, textvariable=phoneValue)
phoneEntry.grid(row=1, column=1)
Button(root, text="Show Specs", padx=5, pady=4, command=show).grid(row=1, column=2)
root.mainloop()