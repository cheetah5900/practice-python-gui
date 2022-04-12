from datetime import datetime # for date time using
from tkinter import * # import all tkinter
from tkinter import ttk # import modern tkinter
import csv # import csv


# ---- GUI SETTING ---- #
GUI = Tk() # create instance
GUI.title('ฟอร์มเพิ่มข้อมูล') # set title
GUI.geometry('400x350+500+50') # set windows size + position x / position y

# ---- FONT SETTING ---- #
fontPrompt = ('Prompt', 20) # set font as prompt size 20

# ---- FRAME SETTING ---- #
frame1 = Frame(GUI) # set frame1 in GUI
frame1.place(x=20, y=20) # set position of frame1 

# ---- TAB ---- #
Tab = ttk.Notebook(GUI)  # set tab for GUI
tab1 = Frame(Tab) # set Tab in frame
tab2 = Frame(Tab) # set Tab in frame
Tab.pack(fill=BOTH, expand=1)

# ---- VARIABLE SETTING ---- #
# create variable as string
product_name = StringVar() 
product_price = StringVar() 
product_quantity = StringVar()
timeNow = datetime.now() # get time now
thaiDay = {
    'Mon': 'จันทร์',
    'Tue': 'อังคาร',
    'Wed': 'พุธ',
    'Thu': 'พฤหัส',
    'Fri': 'ศุกร์',
    'Sat': 'เสาร์',
    'Sun': 'อาทิตย์',
} # set ditionary day for mapping to thaiday

# ---- FUNCTION SETTING ---- #
def AddData(event=None):
    # get data from input's name
    productName = product_name.get()
    productPrice = product_price.get()
    productQuantity = product_quantity.get()

    # reset data in input
    product_name.set('')
    product_price.set('')
    product_quantity.set('')

    # set time
    shortDate = timeNow.strftime('%a') # get time by short day ex. Mon, Tue, Wed etc.
    fullDate = timeNow.strftime('d-M-y') # set time format
    thaiDayWithFullDate = thaiDay[shortDate] + fullDate # concatenate thaiday and full date

    # save data to CSV file
    # savedata.csv is file name
    # a is append mode
    # as f is short name
    with open('savedata.csv', 'a', encoding='utf-8', newline='') as f:  # set csv handle as f
        fw = csv.writer(f)  # use csv writer function with f
        data = [productName, productPrice, productQuantity,
                thaiDayWithFullDate]  # set list
        fw.writerow(data)  # write data

    entryProductName.focus()  # set focus at product name


# ---- SHORTCUT ---- #
GUI.bind('<Return>', AddData) # set Enter button to start AddData function

# ---- TEXT & INPUT BOX ---- #
labelProductName = ttk.Label(
    frame1, text="ชื่อสินค้า", font=fontPrompt)
labelProductName.pack() # label product name

entryProductName = ttk.Entry(
    frame1, textvariable=product_name, font=fontPrompt)
entryProductName.pack() # input product name

labelProductPrice = ttk.Label(
    frame1, text="ราคา", font=fontPrompt)
labelProductPrice.pack()# label product price

entryProductPrice = ttk.Entry(
    frame1, textvariable=product_price, font=fontPrompt)
entryProductPrice.pack()# input product price

labelProductQuantity = ttk.Label(
    frame1, text="จำนวน", font=fontPrompt)
labelProductQuantity.pack()# label product quantity

entryProductQuantity = ttk.Entry(
    frame1, textvariable=product_quantity, font=fontPrompt)
entryProductQuantity.pack()# input product quantity


# ---- BUTTON ---- #
button1 = ttk.Button(frame1, text="Add data", command=AddData) # create button in frame1, when click will activate AddData function
button1.pack() # set button at center of frame1

# ---- SET STATE ---- #
entryProductName.focus() # set product name focus

GUI.mainloop() # set gui still show, not automaticcally shutdown itself
