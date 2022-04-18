from datetime import datetime  # for date time using
from tkinter import *  # import all tkinter
from tkinter import ttk  # import modern tkinter
import csv
from tkinter import messagebox  # import csv


# ---- GUI SETTING ---- #
GUI = Tk()  # create instance
GUI.title('ฟอร์มเพิ่มข้อมูล')  # set title
GUI.geometry('500x650+500+50')  # set windows size + position x / position y

## ---- MENU BAR ---- ##
menuBar = Menu(GUI)  # create Menu Bar for main GUI
# set menu bar by using menu bar which we've just create
GUI.config(menu=menuBar)
# ---- FILE MENU ---- #


def About():
    messagebox.showinfo('About', 'Hi There')


# create Menu Bar for sub menu in main menu, tearoff mean dash at the top can pull out to new window
menuFile = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='File', menu=menuFile)  # add sub menu to main menu
menuFile.add_command(label='Import CSV')
menuFile.add_command(label='About', command=About)

# ---- TAB ---- #
Tab = ttk.Notebook(GUI)  # create main tab in GUI
tab1 = Frame(Tab)  # create frame in Tab
tab2 = Frame(Tab)  # create frame in Tab
# x,y position expand depend on windows size ,  must use together expand=1
Tab.pack(fill=BOTH, expand=1)

# get image from pc, using .subsample(2) mean reduce image size 2 times
iconTab1 = PhotoImage(file='image/add_icon.png')
iconTab2 = PhotoImage(file='image/edit_icon.png')  # get image from pc

# add tab1 into main tab to be visible, f'{"text":^{30}}' mean lock amount of character for 30 though short or long text will be equal long
# compound is image position, there are left,top,right,bottom
Tab.add(tab1, text=f'{"เพิ่ม":^{30}}', image=iconTab1, compound='top')
# add tab2 into main tab to be visible, f'{"text":^{30}}' mean lock amount of character for 30 though short or long text will be equal long
Tab.add(tab2, text=f'{"แก้ไขค่าใช้จ่าย":^{30}}',
        image=iconTab2, compound='top')

# ---- FONT SETTING ---- #
fontPrompt = ('Prompt', 20)  # set font as prompt size 20

# ---- FRAME1 SETTING ---- #
frame1 = Frame(tab1)  # create frame in tab1
frame1.place(x=20, y=20)  # set position of frame1

# ---- VARIABLE SETTING ---- #
# create variable as string
product_name = StringVar()
product_price = StringVar()
product_quantity = StringVar()
timeNow = datetime.now()  # get time now
thaiDay = {
    'Mon': 'จันทร์',
    'Tue': 'อังคาร',
    'Wed': 'พุธ',
    'Thu': 'พฤหัส',
    'Fri': 'ศุกร์',
    'Sat': 'เสาร์',
    'Sun': 'อาทิตย์',
}  # set ditionary day for mapping to thaiday

# ---- FUNCTION SETTING ---- #


def AddData(event=None):
    # get data from input's name
    productName = product_name.get()
    productPrice = product_price.get()
    productQuantity = product_quantity.get()

    # check whether input empty or not
    if productName == '':
        messagebox.showerror('Error', 'กรุณาใส่ชื่อสินค้า')
    if productPrice == '':
        messagebox.showerror('Error', 'กรุณาใส่ราคาสินค้า')
    if productQuantity == '':
        messagebox.showerror('Error', 'กรุณาใส่จำนวน')

    # check whether price and quantity are number or not
    try:
        float(productPrice)
    except:
        messagebox.showerror('Error', 'กรุณาใส่ราคาเป็นตัวเลข')
    try:
        float(productQuantity)
    except:
        messagebox.showerror('Error', 'กรุณาใส่จำนวนเป็นตัวเลข')

    resultText = "รายการ: {}\nราคา: {}\nจำนวน: {}".format(
        productName, productPrice, productQuantity)  # set data for show as a result
    # set variable of result label that was declare at below
    resultInput.set(resultText)
    # reset data in input
    product_name.set('')
    product_price.set('')
    product_quantity.set('')

    # set time
    # get time by short day ex. Mon, Tue, Wed etc.
    shortDate = timeNow.strftime('%a')
    fullDate = timeNow.strftime('%d-%m-%Y')  # set time format
    # concatenate thaiday and full date
    thaiDayWithFullDate = thaiDay[shortDate] + " " + fullDate

    # set id foreach row
    id = timeNow.strftime("%Y%m%d%H%M%f")

    # save data to CSV file
    # savedata.csv is file name
    # a is append mode
    # as f is short name
    with open('savedata.csv', 'a', encoding='utf-8', newline='') as f:  # set csv handle as f
        fw = csv.writer(f)  # use csv writer function with f
        data = [id, thaiDayWithFullDate, productName,
                productPrice, productQuantity]  # set list
        fw.writerow(data)  # write data

    entryProductName.focus()  # set focus at product name
    updateTable()


# ---- TEXT & INPUT BOX ---- #

# image in label
frameIcon = PhotoImage(file='image/battery_icon.png')  # load image to variable
# set image to label becase there is no image tag
frameIconLabel = Label(frame1, image=frameIcon)
frameIconLabel.pack(pady=30)

labelProductName = ttk.Label(
    frame1, text="ชื่อสินค้า", font=fontPrompt)
labelProductName.pack()  # label product name

entryProductName = ttk.Entry(
    frame1, textvariable=product_name, font=fontPrompt)
entryProductName.pack()  # input product name

labelProductPrice = ttk.Label(
    frame1, text="ราคา", font=fontPrompt)
labelProductPrice.pack()  # label product price

entryProductPrice = ttk.Entry(
    frame1, textvariable=product_price, font=fontPrompt)
entryProductPrice.pack()  # input product price

labelProductQuantity = ttk.Label(
    frame1, text="จำนวน", font=fontPrompt)
labelProductQuantity.pack()  # label product quantity

entryProductQuantity = ttk.Entry(
    frame1, textvariable=product_quantity, font=fontPrompt)
entryProductQuantity.pack()  # input product quantity


# ---- BUTTON ---- #
iconButton1 = PhotoImage(file='image/edit_icon.png')  # get image from pc
# create button in frame1, when click will activate AddData function
button1 = ttk.Button(frame1, text="Save", image=iconButton1,
                     compound='top', command=AddData)
# set button at center of frame1, ipadx,y is padding for button and pady is margin
button1.pack(ipadx=50, ipady=20, pady=20)

# ---- SHOW RECENT INPUT ---- #
resultInput = StringVar()  # create input variable
resultInput.set('----ผลลัพธ์----')  # set first value
resultInputLabel = ttk.Label(
    frame1, textvariable=resultInput, font=fontPrompt)  # set label with variable
resultInputLabel.pack()  # set at center

# ---- SET STATE ---- #
entryProductName.focus()  # set product name focus

## -------- TAB2 --------##

# ---- FUNCTION READ DATA ----#


def read_csv():
    with open('savedata.csv', newline='', encoding='utf-8') as f:
        fileReader = csv.reader(f)
        data = list(fileReader)
        return data


# ---- TABLE SHOW DATA ----#
header = ['ID', 'วัน-เวลา', 'รายการ', 'ค่าใช้จ่าย', 'จำนวน']
# column mean set header for table
# 'show' mean do a regular table not tree table
# height is shown line in table
resultTable = ttk.Treeview(tab2, column=header, show='headings', height=10)
resultTable.pack()

for h in header:  # foreach each header
    resultTable.heading(h, text=h)  # map each header to table header

headerWidth = [50, 150, 170, 80, 80, 80]  # set header width as list
for h, w in zip(header, headerWidth):  # zip is mapping 2 list together to header and width
    resultTable.column(h, width=w)  # map header to width to set column width

# ---- CREATE TRANSACTION DICTIONARY ---- #
# we need to create dictionary from all row to delete each one that we want to delete it
allTransaction = {}  # create enpty dictionary


def updateCsv():
    check = messagebox.askyesno('Confirm', 'ต้องการลบใช่หรือไม่')
    if check == True:
        with open('savedata.csv', 'w', newline='', encoding='utf-8') as f:
            fw = csv.writer(f)
            # set allTransaction as list because write data into csv file need to be list
            valueAllTransaction = allTransaction.values()  # get only value of object
            print('valueAllTransaction : ', valueAllTransaction)

            # set imported data as list
            listAllTransaction = list(valueAllTransaction)
            # write multiple line [ [],[],[] ]
            fw.writerows(listAllTransaction)
            print('Write done')
    else:
        pass


def updateTable():  # function for updating table in tab2
    # (Alternative) for loop to delete all data in old data
    # for oldData in resultTable.get_children():
    #     resultTable.delete(oldData)
    # Shorthand delete all of old data before insret new data
    resultTable.delete(*resultTable.get_children())
    try:
        data = read_csv()  # call read csv function
        for d in data:  # foreach data in array
            # create transaction data as object
            # d[0] = transactionid , d[1] = date time, d[2] = item , d[3] = price , d[4] = quantity
            # This is example off allTransaction
            #  { 'id1' : {'id1','2022-4-18','นมเปรี้ยว,......}}
            allTransaction[d[0]] = d

            # insert data to index 0 to table
            resultTable.insert('', 0, value=d)
    except Exception as e:
        pass


updateTable()

# ---- DELETED DATA ----#


def deleteData(event=None):
    # get id from selection record ,Return as special ascii
    selectedId = resultTable.selection()
    data = resultTable.item(selectedId)  # get row by id, Return as object
    id = data['values'][0]  # get key 'values' from object
    transactionId = str(id)
    # delete selected key, value that we get from selected is int
    del allTransaction[transactionId]
    updateCsv()
    updateTable()


# create deleted button
deleteButton = ttk.Button(tab2, text='Delete', command=deleteData)
deleteButton.place(x=50, y=250)

# ---- SHORTCUT ---- #
GUI.bind('<Return>', AddData)  # set Enter button to start AddData function
resultTable.bind('<Delete>',deleteData)

GUI.mainloop()  # set gui still show, not automaticcally shutdown itself
