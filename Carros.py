from tkinter import*
from tkinter import messagebox
import random

root = Tk()
root.title("SISTEMA DE ALUGUER DE VIATURAS Iyonissio Daniel Sitoe")
root.geometry('1350x650+0+0')

LeftMayFrame = Frame(root, width=1000, height=650, bd=8, relief="raise")
LeftMayFrame.pack (side=LEFT)
RightMayFrame = Frame(root, width=350, height=650, bd=8, relief="raise")
RightMayFrame.pack (side=RIGHT)

LeftMayFramel = Frame(LeftMayFrame, width=1000, height=225, bd=8, relief="raise")
LeftMayFramel.pack (side=TOP)

LeftMayFrame2 = Frame(LeftMayFrame, width=1000, height=225, bd=8, relief="raise")
LeftMayFrame2.pack (side=TOP)

LeftMayFrame3 = Frame (LeftMayFrame, width=1000, height=100, bd=8, relief="raise")
LeftMayFrame3.pack (side=TOP)

LeftMayFrame4 = Frame(LeftMayFrame, width=1000, height=100, bd=8, relief="raise")
LeftMayFrame4 .pack (side=TOP)

RightMayFramel = Frame (RightMayFrame, width=350, height=325, bd=8, relief="raise")
RightMayFramel .pack (side=TOP)

RightMayFrame2 = Frame(RightMayFrame, width =350, height=325, bd=8, relief="raise")
RightMayFrame2. pack (side=BOTTOM)

string = "3.141"

print(string)
print(type(string))

# converting string to float
Float = float(string)

print(Float)
print(type(Float))

#_____________________________________________________________
NumberofDays =StringVar()

def CarRentalcost ():
    Float = float(NumberofDays)
    NoofDays= (Float.get())
    CarDiscount = float(Discount.get())
    DailyRate = float(DaysRented.get())

    RentalCost = (((NoofDays * DailyRate)*CarDiscount)/100)
    CostofRental="£",('%.2f'%((NoofDays * DailyRate) - RentalCost))
    Total.set(CostofRental)
    ID=random.randint(51,95)
    randomID=str(ID)
    CustomerID.set ("CAR"+randomID)
    Inv=random.randint (15,112)
    InvID=str(Inv)
    InvoiceID.set("INV"+InvID)

#___________________________Variaveis_____________________________
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
CustomerID =StringVar()
DaysRented =StringVar()
Discount =StringVar()

InvoiceID =StringVar()
Total =StringVar()
Receipt_Ref =StringVar()
DateofOrder=StringVar()
EngineSize=StringVar()
Style=StringVar()
RegisteredYear=StringVar()
ClassID=StringVar()
CarDescription=StringVar()
MilesBefore=StringVar()
MilesAfter=StringVar()
Make=StringVar()
Model=StringVar()
CarColour=StringVar()
EngineMake=StringVar()
CarColour=StringVar()
CarInsurance=StringVar()
Area=StringVar()
DailyRentalRate=StringVar()
RegistrationNo=StringVar()
IssueBy=StringVar()
IssueDate=StringVar()
LicenceNo=StringVar()
NumberofDays=StringVar()
Surname=StringVar()
Street=StringVar()
Firstname=StringVar()
Title=StringVar()
Customer=StringVar()
PostCode=StringVar()

#___________________reset________________________________________________

def Reset():
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    CustomerID.set("")
    DaysRented.set("")
    Discount.set("")
    NumberofDays.set("")
    InvoiceID.set("")
    Total.set("")
    Receipt_Ref.set("")
    DateofOrder.set("")
    EngineSize.set("")
    Style.set("")
    RegisteredYear.set("")
    ClassID.set("")
    CarDescription.set("")
    MilesBefore. set ("")
    MilesAfter.set("")
    Make.set("")
    Model.set("")
    CarColour.set("")
    EngineMake.set ("")
    CarInsurance.set("")
    Area.set("")
    DailyRentalRate.set("")
    RegistrationNo.set("")
    IssueBy.set("")
    IssueDate.set("")
    LicenceNo.set("")
    Surname.set("")
    Street.set("")
    Firstname.set("")
    Title.set("")
    Customer.set("")
    PostCode.set("")
    txtReceipt.delete("1.0",END)
#__________________Receip-_______________________________
def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(106, 506)
    randomRef = str(x)
    Receipt_Ref.set ("BILL"+ randomRef)
    txtReceipt.insert (END, 'Receipt Ref:\t'+ Receipt_Ref.get() +'\n\nDate:\t'+ DateofOrder.get ()+"\n\n")
    txtReceipt.insert(END, "Car Rental Services \n\n")
    txtReceipt.insert (END, 'CustomerID: \t'+ CustomerID.get()+ "\n\n")
    txtReceipt.insert (END, 'DaysRented: \t\t'+ DaysRented.get()+ "\n\n")
    txtReceipt.insert (END, 'NumberofDays: \t\t' + NumberofDays.get()+ "\n\n")
    txtReceipt.insert (END, 'InvoiceID: \t' + InvoiceID.get()+ "\n\n")
    txtReceipt.insert (END, 'Discount: \t\t' + Discount.get()+ "\n\n")
    txtReceipt.insert(END, 'Total: \t' + Total.get())
#________________________Funcoes__________________________
def qExit():
    qExit=messagebox.askyesno("Sair do sistema","Você quer sair do Sistema ?")
    if qExit > 0:
        root.destroy()
        return


#___________________________________________________________________________________
Style = Checkbutton (RightMayFramel, text="Style \t", onvalue = 1, offvalue = 0,
font=('arial',14, 'bold')).grid(row=0, sticky=W)

ClassID = Checkbutton(RightMayFramel, text="Class ID \t\t", onvalue = 1, offvalue = 0,
font=('arial',14, 'bold')).grid(row=1, sticky=W)

InvoiceID = Checkbutton(RightMayFramel, text="Invoice ID \t\t", onvalue = 1, offvalue = 0,
font=('arial',14, 'bold')).grid(row=1, sticky=W)

DailyRate = Checkbutton(RightMayFramel, text="Daily Rate \t\t", onvalue = 1, offvalue = 0,
font=('arial',14, 'bold')).grid(row=3, sticky=W)

Automatic = Checkbutton(RightMayFramel, text="Automatic \t\t", onvalue = 1, offvalue = 0,
font=('arial',14, 'bold')).grid(row=4, sticky=W)

AirCondition = Checkbutton(RightMayFramel, text="AirCondition \t\t", onvalue = 1, offvalue = 0,
font=('arial',14, 'bold')).grid(row=5, sticky=W)

InsuranceSold = Checkbutton(RightMayFramel, text="Insurance Sold \t\t", onvalue = 1, offvalue = 0,
font=('arial',14, 'bold')).grid(row=6, sticky=W)

CustomerDetails = Checkbutton(RightMayFramel, text="Customer Details \t\t", onvalue = 1, offvalue = 0,
font=('arial',14, 'bold')) .grid(row=7, sticky=W)
#____________________________________________________________________________________
txtReceipt=Text(RightMayFrame2, height=15, width=32, bd= 8, font=('arial', 12, 'bold')).grid(row=0,column=0)

#____________________________________________________________________________________________________________
lblCustomerID = Label (LeftMayFramel, font=('arial', 10,'bold'), text="Cliente", bd=8)
lblCustomerID.grid(row=0,column=0, sticky=W)
txtCustomerID = Entry (LeftMayFramel, font=('arial',10,'bold'), bd=8,
width=31, justify='left')
txtCustomerID.grid (row=0, column=1)

lblDaysRented = Label (LeftMayFramel, font=('arial',10,'bold'), text="Titulo", bd=8)
lblDaysRented.grid(row=0,column=2, sticky=W)
txtDaysRented = Entry(LeftMayFramel, font=('arial',10,'bold'), bd=8,
width=31, justify='left')
txtDaysRented. grid (row=0, column=3)
lblDiscount = Label (LeftMayFramel, font=('arial',10,'bold'), text="Nome", bd=8)
lblDiscount .grid (row=0,column=4, sticky=W)
txtDiscount = Entry(LeftMayFramel, font=('arial',10,'bold'), bd=8, width=31,
justify='left')
txtDiscount .grid(row=0,column=5)
lblNumberofDays = Label (LeftMayFramel, font=('arial',10,'bold'), text="Sobrenome", bd=8)
lblNumberofDays.grid(row=1,column=0, sticky=W)
txtNumberofDays= Entry (LeftMayFramel, font=('arial',10,'bold'), bd=8,
width=31, justify='left')
txtNumberofDays .grid(row=1, column=1)
lblinvoiceID = Label (LeftMayFramel, font=('arial',10,'bold'), text="Rua", bd=8)
lblinvoiceID .grid(row=1,column=2, sticky=W)
txtInvoiceID = Entry (LeftMayFramel,font=('arial',10,'bold'), bd=8, width=31,
justify='left')
txtInvoiceID .grid(row=1,column=3)
lblTotal = Label (LeftMayFramel, font=('arial',10,'bold'), text="Bairo", bd=8)
lblTotal .grid(row=1,column=4, sticky=W)
txtTotal = Entry (LeftMayFramel, font=('arial',10,'bold'), bd=8, width=31,
justify="left")
txtTotal .grid(row=1,column=5)

lblNumberofDays = Label (LeftMayFramel, font=('arial',10,'bold'), text="Endereco", bd=8)
lblNumberofDays.grid(row=2,column=0, sticky=W)
txtNumberofDays= Entry (LeftMayFramel, font=('arial',10,'bold'), bd=8,
width=31, justify='left')
txtNumberofDays .grid(row=2, column=1)
lblinvoiceID = Label (LeftMayFramel, font=('arial',10,'bold'), text="Licensa N*", bd=8)
lblinvoiceID .grid(row=2,column=2, sticky=W)
txtInvoiceID = Entry (LeftMayFramel,font=('arial',10,'bold'), bd=8, width=31,
justify='left')
txtInvoiceID .grid(row=2,column=3)
lblTotal = Label (LeftMayFramel, font=('arial',10,'bold'), text="Data Emissao", bd=8)
lblTotal .grid(row=2,column=4, sticky=W)
txtTotal = Entry (LeftMayFramel, font=('arial',10,'bold'), bd=8, width=31,
justify="left")
txtTotal .grid(row=2,column=5)

lblNumberofDays = Label (LeftMayFramel, font=('arial',10,'bold'), text="Emitido Por", bd=8)
lblNumberofDays.grid(row=3,column=0, sticky=W)
txtNumberofDays= Entry (LeftMayFramel, font=('arial',10,'bold'), bd=8,
width=31, justify='left')
txtNumberofDays .grid(row=3, column=1)
lblinvoiceID = Label (LeftMayFramel, font=('arial',10,'bold'), text="Reg. N*", bd=8)
lblinvoiceID .grid(row=3,column=2, sticky=W)
txtInvoiceID = Entry (LeftMayFramel,font=('arial',10,'bold'), bd=8, width=31,
justify='left')
txtInvoiceID .grid(row=3,column=3)
lblTotal = Label (LeftMayFramel, font=('arial',10,'bold'), text="Taxa Aluguel", bd=8)
lblTotal .grid(row=3,column=4, sticky=W)
txtTotal = Entry (LeftMayFramel, font=('arial',10,'bold'), bd=8, width=31,
justify="left")
txtTotal .grid(row=3,column=5)
#____________________________________________________________________________________________________________
lblCustomerID = Label (LeftMayFrame2, font=('arial', 10,'bold'), text="Motor", bd=8)
lblCustomerID.grid(row=0,column=0, sticky=W)
txtCustomerID = Entry (LeftMayFrame2, font=('arial',10,'bold'), bd=8,
width=31, justify='left')
txtCustomerID.grid (row=0, column=1)

lblDaysRented = Label (LeftMayFrame2, font=('arial',10,'bold'), text="Estilo", bd=8)
lblDaysRented.grid(row=0,column=2, sticky=W)
txtDaysRented = Entry(LeftMayFrame2, font=('arial',10,'bold'), bd=8,
width=31, justify='left')
txtDaysRented. grid (row=0, column=3)
lblDiscount = Label (LeftMayFrame2, font=('arial',10,'bold'), text="Ano Reg", bd=8)
lblDiscount .grid (row=0,column=4, sticky=W)
txtDiscount = Entry(LeftMayFrame2, font=('arial',10,'bold'), bd=8, width=31,
justify='left')
txtDiscount .grid(row=0,column=5)
lblNumberofDays = Label (LeftMayFrame2, font=('arial',10,'bold'), text="Class Id", bd=8)
lblNumberofDays.grid(row=1,column=0, sticky=W)
txtNumberofDays= Entry (LeftMayFrame2, font=('arial',10,'bold'), bd=8,
width=31, justify='left')
txtNumberofDays .grid(row=1, column=1)
lblinvoiceID = Label (LeftMayFrame2, font=('arial',10,'bold'), text="Descr. Carro", bd=8)
lblinvoiceID .grid(row=1,column=2, sticky=W)
txtInvoiceID = Entry (LeftMayFrame2,font=('arial',10,'bold'), bd=8, width=31,
justify='left')
txtInvoiceID .grid(row=1,column=3)
lblTotal = Label (LeftMayFrame2, font=('arial',10,'bold'), text="Km/h antes", bd=8)
lblTotal .grid(row=1,column=4, sticky=W)
txtTotal = Entry (LeftMayFrame2, font=('arial',10,'bold'), bd=8, width=31,
justify="left")
txtTotal .grid(row=1,column=5)

lblNumberofDays = Label (LeftMayFrame2, font=('arial',10,'bold'), text="Km/h antes", bd=8)
lblNumberofDays.grid(row=2,column=0, sticky=W)
txtNumberofDays= Entry (LeftMayFrame2, font=('arial',10,'bold'), bd=8,
width=31, justify='left')
txtNumberofDays .grid(row=2, column=1)
lblinvoiceID = Label (LeftMayFrame2, font=('arial',10,'bold'), text="Marca", bd=8)
lblinvoiceID .grid(row=2,column=2, sticky=W)
txtInvoiceID = Entry (LeftMayFrame2,font=('arial',10,'bold'), bd=8, width=31,
justify='left')
txtInvoiceID .grid(row=2,column=3)
lblTotal = Label (LeftMayFrame2, font=('arial',10,'bold'), text="Modelo", bd=8)
lblTotal .grid(row=2,column=4, sticky=W)
txtTotal = Entry (LeftMayFrame2, font=('arial',10,'bold'), bd=8, width=31,
justify="left")
txtTotal .grid(row=2,column=5)

lblNumberofDays = Label (LeftMayFrame2, font=('arial',10,'bold'), text="Number of Days", bd=8)
lblNumberofDays.grid(row=3,column=0, sticky=W)
txtNumberofDays= Entry (LeftMayFrame2, font=('arial',10,'bold'), bd=8,
width=31, justify='left')
txtNumberofDays.grid(row=3, column=1)
lblinvoiceID = Label (LeftMayFrame2, font=('arial',10,'bold'), text="Carro Cor", bd=8)
lblinvoiceID .grid(row=3,column=2, sticky=W)
txtInvoiceID = Entry (LeftMayFrame2,font=('arial',10,'bold'), bd=8, width=31,
justify='left')
txtInvoiceID .grid(row=3,column=3)
lblTotal = Label (LeftMayFrame2, font=('arial',10,'bold'), text="Seguro Auto", bd=8)
lblTotal .grid(row=3,column=4, sticky=W)
txtTotal = Entry (LeftMayFrame2, font=('arial',10,'bold'), bd=8, width=31,
justify="left")
txtTotal .grid(row=3,column=5)

#------------------------------------------------------------------------------------------------------------
lblCustomerID = Label (LeftMayFrame3, font=('arial', 10,'bold'), text="Customer ID", bd=8)
lblCustomerID.grid(row=0,column=0, sticky=W)
txtCustomerID = Entry (LeftMayFrame3, font=('arial',10,'bold'), bd=8,
width=31, justify='left')
txtCustomerID.grid (row=0, column=1)

lblDaysRented = Label (LeftMayFrame3, font=('arial',10,'bold'), text="Dias Alugados", bd=8)
lblDaysRented.grid(row=0,column=2, sticky=W)
txtDaysRented = Entry(LeftMayFrame3, font=('arial',10,'bold'), bd=8,
width=31, justify='left')
txtDaysRented.grid (row=0, column=3)
lblDiscount = Label (LeftMayFrame3, font=('arial',10,'bold'), text="Desconto", bd=8)
lblDiscount.grid(row=0,column=4, sticky=W)
txtDiscount = Entry(LeftMayFrame3, font=('arial',10,'bold'), bd=8, width=31,
justify='left')
txtDiscount.grid(row=0,column=5)
lblNumberofDays = Label (LeftMayFrame3, font=('arial',10,'bold'), text="Number of Days", bd=8)
lblNumberofDays.grid(row=1,column=0, sticky=W)
txtNumberofDays= Entry (LeftMayFrame3, font=('arial',10,'bold'), bd=8,
width=31, justify='left')
txtNumberofDays.grid(row=1, column=1)
lblinvoiceID = Label (LeftMayFrame3, font=('arial',10,'bold'), text="Invoice ID", bd=8)
lblinvoiceID.grid(row=1,column=2, sticky=W)
txtInvoiceID = Entry (LeftMayFrame3,font=('arial',10,'bold'), bd=8, width=31,
justify='left')
txtInvoiceID.grid(row=1,column=3)
lblTotal = Label (LeftMayFrame3, font=('arial',10,'bold'), text="Total", bd=8)
lblTotal.grid(row=1,column=4, sticky=W)
txtTotal = Entry (LeftMayFrame3, font=('arial',10,'bold'), bd=8, width=31,
justify="left")
txtTotal .grid(row=1,column=5)

#____________________________________________________________________________________________________________
btnTotal = Button(LeftMayFrame4, text='Total', padx=8, pady=8, bd=8, fg="black",
font=('arial', 13, 'bold'), width=21, height=2,command=CarRentalcost).grid(row=0,column=0)
btnReceipt = Button(LeftMayFrame4, text='Recibo', padx=8, pady=8, bd=8, fg="black",
font=('arial', 13, 'bold'), width= 21, height=2,command=Receipt).grid(row=0,column=1)
btnReset = Button(LeftMayFrame4, text='Resetar', padx=8, pady=8, bd=8, fg="black",
font=('arial', 13, 'bold'), width= 21, height=2,command=Reset).grid(row=0,column=2)
btnExit = Button(LeftMayFrame4, text='Sair', padx=8, pady=8, bd=8, fg="black",
font=('arial', 13, 'bold'), width= 21, height=2,command=qExit) .grid(row=0,column=3)

root.mainloop()













