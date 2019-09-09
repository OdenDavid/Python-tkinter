# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import datetime
import math
import tempfile
import os
import sqlite3
import sys

#=========================Class for Main Window=============================       
class Window2:
      
    def __init__(self, master):
        conn = sqlite3.connect(r"C:\Users\DAVID ODEN\Desktop\Restaurant Management System\database\records.db")
        c = conn.cursor()           
        self.master = master
        self.master.title("Restaurant Management System")
        self.master.geometry('1366x768')
        self.master.configure(background='green')
     
        #============================Frame for Title========================
        self.Tops = Frame(self.master,bg='green',width=1366,height=150,bd=20,pady=5, relief=RIDGE )
        self.Tops.place(x=0,y=0)
        #===========Restaurant Image===========
        self.photo = PhotoImage(file="restaurant-icon.png")
        self.icon = Label(self.Tops,image=self.photo,bg='green')
        self.icon.pack(side=LEFT)
        
        #===========Restaurant Image===========
        self.photo2 = PhotoImage(file="restaurant-icon.png")
        self.icon2 = Label(self.Tops,image=self.photo2,bg='green')
        self.icon2.pack(side=RIGHT)
        
        #==================Status Bar================
        self.Barframe = Frame(self.master,bg='green',width=866,height=26,bd=3, relief=SUNKEN)
        self.Barframe.place(x=0,y=700)
        
        #===================Receipt and Buttons Frame==============
        self.RCF = Frame(self.master,bg='pale green',width=500,height=542,bd=10, relief=RIDGE )
        self.RCF.place(x=866,y=180)
        
        self.Cart_Info = Frame(self.RCF,bg='pale green',width=480,height=420,bd=3, relief=RIDGE )
        self.Cart_Info.place(x=0,y=0)    
        
        self.Cart_Frame = Frame(self.Cart_Info,bg='white',width=480,height=420,bd=3, relief=FLAT)
        self.Cart_Frame.place(x=0,y=30)
        
        self.Buttons_Frame = Frame(self.RCF,bg='pale green',width=480,height=100,bd=3, relief=RIDGE )
        self.Buttons_Frame.place(x=0,y=420)
        #================================Menu Frame==============================
        self.MenuFrame = Frame(self.master,bg='green',width=866,height=518,bd=10,relief=RIDGE)
        self.MenuFrame.place(x=0,y=180)
        #==============Food Frame===============
        self.Food_Frame = Frame(self.MenuFrame,width=200,height=270,bg='pale green',bd=10, relief=RIDGE)
        self.Food_Frame.place(x=0,y=0)        
        #==============Picture Frame1===============
        self.pictures1 = Frame(self.MenuFrame,width=88,height=270,bg='pale green',bd=5, relief=SUNKEN)
        self.pictures1.place(x=211,y=0)        

        self.photo3 = PhotoImage(file="soup.png")
        self.icon3 = Label(self.pictures1,image=self.photo3)
        self.icon3.grid(row=0,column=0,pady=7)
        
        self.photo4 = PhotoImage(file="rice.png")
        self.icon4 = Label(self.pictures1,image=self.photo4)
        self.icon4.grid(row=1,column=0,pady=10)               
        #==============Drinks Frame=================
        self.Drinks_Frame = Frame(self.MenuFrame,width=200,height=270,bg='pale green',bd=10, relief=RIDGE)
        self.Drinks_Frame.place(x=297,y=0)        
        #==============Picture Frame2===============
        self.pictures2 = Frame(self.MenuFrame,width=88,height=270,bg='pale green',bd=5, relief=SUNKEN)
        self.pictures2.place(x=495,y=0)    
        
        self.photo6 = PhotoImage(file="steak.png")
        self.icon6 = Label(self.pictures2,image=self.photo6)
        self.icon6.grid(row=0,column=0,pady=7)
        
        self.photo7 = PhotoImage(file="drinks.png")
        self.icon7 = Label(self.pictures2,image=self.photo7)
        self.icon7.grid(row=1,column=0,pady=10)                 
        #==============Snacks Frame===============
        self.Snacks_Frame = Frame(self.MenuFrame,width=200,height=270,bg='pale green',bd=10, relief=RIDGE)
        self.Snacks_Frame.place(x=580,y=0)
        #==============Picture Frame3===============
        self.pictures3 = Frame(self.MenuFrame,width=88,height=270,bg='pale green',bd=5, relief=SUNKEN)
        self.pictures3.place(x=760,y=0)    
        
        self.photo8 = PhotoImage(file="doughnut.png")
        self.icon8 = Label(self.pictures3,image=self.photo8)
        self.icon8.grid(row=0,column=0,pady=7)
        
        self.photo9 = PhotoImage(file="cake.png")
        self.icon9 = Label(self.pictures3,image=self.photo9)
        self.icon9.grid(row=1,column=0,pady=10)                  
        #=============Others Frame===============
        self.others_frame = Frame(self.MenuFrame,width=845,height=160,bg='green',bd=5,relief=GROOVE)
        self.others_frame.place(x=0,y=250)        
        #==============Cost Frame===============
        self.Cost_Frame = Frame(self.MenuFrame,width=866,height=150,bg='pale green',bd=10,relief=RIDGE)
        self.Cost_Frame.place(x=0,y=415)        
        
        #==========================VARIABLES===========================
        #=========Checkbutton Variables=============
        var1 =IntVar()
        var2 =IntVar()
        var3 =IntVar()
        var4 =IntVar()
        var5 =IntVar()
        var6 =IntVar()
        var7 =IntVar()
        var8 =IntVar()
        var9 =IntVar()
        var10 =IntVar()
        var11 =IntVar()
        var12 =IntVar()
        var13 =IntVar()
        var14 =IntVar()
        var15 =IntVar()
        var16 =IntVar()
        var17 =IntVar()
        var18 =IntVar()
        var19 =IntVar()
        var20 =IntVar()
        var21 =IntVar()
        
        var1.set(0)
        var2.set(0) 
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)
        var17.set(0)
        var18.set(0)
        var19.set(0)
        var20.set(0)
        var21.set(0)
        #============creating lists for cart=========
        item_list = []
        price_list = []
        quantity_list = []
        item_and_quantity = []
        #=================Textvariables=============== 
        Current_date = StringVar()
        Current_time = StringVar()
        DateandTime = StringVar()
        Receipt_Ref= StringVar()
        Others = StringVar()
        Others_Qty = StringVar()
        SubTotal = StringVar()
        Total = StringVar()
        ServiceCharge = StringVar()
        
        Jollof_Rice=StringVar()
        Fried_Rice=StringVar()
        Eba=StringVar()
        Semovita=StringVar()
        Egusi_Soup=StringVar()
        Vegetable_Soup=StringVar()
        Chicken=StringVar()
        Meat=StringVar()
        
        Coke=StringVar()
        Fanta=StringVar()
        Sprite=StringVar()
        Chapman=StringVar()
        Chivita=StringVar()
        Malt=StringVar()
        Zobo=StringVar()
        Bottled_Water=StringVar()
        
        Shawarma=StringVar()
        Meat_Pie=StringVar()
        Chicken_Pie=StringVar()
        Doughnut=StringVar()
        Pop_Corn=StringVar()
        
        Jollof_Rice.set("0")
        Fried_Rice.set("0")
        Eba.set("0")
        Semovita.set("0")
        Egusi_Soup.set("0")
        Vegetable_Soup.set("0")
        Chicken.set("0")
        Meat.set("0")
        
        Coke.set("0")
        Fanta.set("0")
        Sprite.set("0")
        Chapman.set("0")
        Chivita.set("0")
        Malt.set("0")
        Zobo.set("0")
        Bottled_Water.set("0")
        
        Shawarma.set("0")
        Meat_Pie.set("0")
        Chicken_Pie.set("0") 
        Doughnut.set("0")
        Pop_Corn.set("0")
        
        now = datetime.datetime.now()
       
        Date = now.strftime("%Y-%m-%d")
        Time = now.strftime("%H:%M:%S")
        
        Current_date.set(Date)
        
        Current_time.set(Time)
        

        #==============Button exit Function===============          
        def iExit():
            iExit = tkinter.messagebox.askyesnocancel("Exit Restaurant System","Confirm if you want to Exit!")
            if iExit > 0:
                self.master.destroy()
                return
        
     
        #==============Checkbutton Function for Jollof Rice==================
        def chkJR():
            if  (var1.get()==1):
                info1 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'jollof rice'")
                for a in info1:
                    price1 = a[0] 
                    stock1 = a[1]
                txtJollof_Rice.configure(state = NORMAL)
                txtJollof_Rice.focus()
                txtJollof_Rice.delete('0',END)
                Jollof_Rice.set("")
                self.Statusbar['text'] = 'Jollof Rice Selected Price is '+price1+'...Quantity in Stock is '+stock1+'...'
            elif(var1.get()==0):
                txtJollof_Rice.configure(state = DISABLED)
                Jollof_Rice.set("0")
                self.Statusbar['text'] = ''
        #==============Checkbutton Function for Fried Rice==================
        def chkFR():
            if (var2.get()==1):
                info2 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'fried rice'")
                for b in info2:
                    price2 = b[0]
                    stock2 = b[1]                 
                txtFried_Rice.configure(state = NORMAL)
                txtFried_Rice.focus()
                txtFried_Rice.delete('0',END)
                Fried_Rice.set("")
                self.Statusbar['text'] = 'Fried Rice Selected Price is '+price2+'...Quantity in Stock is '+stock2+'...'
            elif(var2.get()==0):
                txtFried_Rice.configure(state = DISABLED)
                Fried_Rice.set("0")
                self.Statusbar['text'] = ''
        #==============Checkbutton Function for Eba==================
        def chkEBA():
            if (var3.get()==1):
                info3 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'eba'")
                for d in info3:
                    price3 = d[0]  
                    stock3 = d[1]
                txtEba.configure(state = NORMAL)
                txtEba.focus()
                txtEba.delete('0',END)
                Eba.set("")
                self.Statusbar['text'] = 'Eba Selected Price is '+price3+'...Quantity in Stock is '+stock3+'...'
            elif(var3.get()==0):
                txtEba.configure(state = DISABLED)
                Eba.set("0")
                self.Statusbar['text'] = ''
        #==============Checkbutton Function for Semovita==================
        def chkSEM():
            if (var4.get()==1):
                info4 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'semovita'")
                for e in info4:
                    price4 = e[0]  
                    stock4 = e[1]              
                txtSemovita.configure(state = NORMAL)
                txtSemovita.focus()
                txtSemovita.delete('0',END)
                Semovita.set("")
                self.Statusbar['text'] = 'Semovita Selected Price is '+price4+'...Quantity in Stock is '+stock4+'...'
            elif(var4.get()==0):
                txtSemovita.configure(state = DISABLED)
                Semovita.set("0")
                self.Statusbar['text'] = ''
        #==============Checkbutton Function for Egusi_Soup==================       
        def chkEG():
            if (var5.get()==1):
                info5 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'egusi soup'")
                for f in info5:
                    price5 = f[0]  
                    stock5 = f[1]                        
                txtEgusi_Soup.configure(state = NORMAL)
                txtEgusi_Soup.focus()
                txtEgusi_Soup.delete('0',END)
                Egusi_Soup.set("")
                self.Statusbar['text'] = 'Egusi Soup Selected Price is '+price5+'...Quantity in Stock is '+stock5+'...'
            elif(var5.get()==0):
                txtEgusi_Soup.configure(state = DISABLED)
                Egusi_Soup.set("0")
                self.Statusbar['text'] = ''
        #==============Checkbutton Function for Vegetable Soup==================
        def chkVG():
            if (var6.get()==1):
                info6 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'vegetable soup'")
                for g in info6:
                    price6 = g[0]  
                    stock6 = g[1]                  
                txtVegetable_Soup.configure(state = NORMAL)
                txtVegetable_Soup.focus()
                txtVegetable_Soup.delete('0',END)
                Vegetable_Soup.set("")
                self.Statusbar['text'] = 'Vegetable Soup Selected Price is '+price6+'...Quantity in Stock is '+stock6+'...'
            elif(var6.get()==0):
                txtVegetable_Soup.configure(state = DISABLED)
                Vegetable_Soup.set("0")
                self.Statusbar['text'] = ''
        #==============Checkbutton Function for Chicken==================
        def chkCH():
            if (var7.get()==1):
                info7 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'chicken'")
                for h in info7:
                    price7 = h[0]  
                    stock7 = h[1]                   
                txtChicken.configure(state = NORMAL)
                txtChicken.focus()
                txtChicken.delete('0',END)
                Chicken.set("")
                self.Statusbar['text'] = 'Chicken Selected Price is '+price7+'...Quantity in Stock is '+stock7+'...'
            elif(var7.get()==0):
                txtChicken.configure(state = DISABLED)
                Chicken.set("0")
                self.Statusbar['text'] = ''
        #==============Checkbutton Function for Meat==================
        def chkME():
            if (var8.get()==1):
                info8 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'meat'")
                for i in info8:
                    price8 = i[0]  
                    stock8 = i[1]                  
                txtMeat.configure(state = NORMAL)
                txtMeat.focus()
                txtMeat.delete('0',END)
                Meat.set("")
                self.Statusbar['text'] = 'Meat Selected Price is '+price8+'...Quantity in Stock is '+stock8+'...'
            elif(var8.get()==0):
                txtMeat.configure(state = DISABLED)
                Meat.set("0")
                self.Statusbar['text'] = ''
        #==============Checkbutton Function for Coke==================
        def chkCO():
            if  (var9.get()==1):
                info9 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'coke'")
                for j in info9:
                    price9 = j[0]  
                    stock9 = j[1]                  
                txtCoke.configure(state = NORMAL)
                txtCoke.focus()
                txtCoke.delete('0',END)
                Coke.set("")
                self.Statusbar['text'] = 'Coke Drink Selected Price is '+price9+'...Quantity in Stock is '+stock9+'...'
            elif(var9.get()==0):
                txtCoke.configure(state = DISABLED)
                Coke.set("0")
                self.Statusbar['text'] = ''
        #==============Checkbutton Function for Fanta==================
        def chkFA():
            if (var10.get()==1):
                info10 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'fanta'")
                for k in info10:
                    price10 = k[0]  
                    stock10 = k[1]                        
                txtFanta.configure(state = NORMAL)
                txtFanta.focus()
                txtFanta.delete('0',END)
                Fanta.set("")
                self.Statusbar['text'] = 'Fanta Drink Selected Price is '+price10+'...Quantity in Stock is '+stock10+'...'
            elif(var10.get()==0):
                txtFanta.configure(state = DISABLED)
                Fanta.set("0")
                self.Statusbar['text'] = ''
        #==============Checkbutton Function for Sprite==================
        def chkSP():
            if (var11.get()==1):
                info11 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'sprite'")
                for l in info11:
                    price11 = l[0]  
                    stock11 = l[1]                  
                txtSprite.configure(state = NORMAL)
                txtSprite.focus()
                txtSprite.delete('0',END)
                Sprite.set("")
                self.Statusbar['text'] = 'Sprite Drink Selected Price is '+price11+'...Quantity in Stock is '+stock11+'...'
            elif(var11.get()==0):
                txtSprite.configure(state = DISABLED)
                Sprite.set("0")
                self.Statusbar['text'] = ''
        #==============Checkbutton Function for Chapman==================
        def chkCHA():
            if (var12.get()==1):
                info12 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'chapman'")
                for m in info12:
                    price12 = m[0]  
                    stock12 = m[1]                     
                txtChapman.configure(state = NORMAL)
                txtChapman.focus()
                txtChapman.delete('0',END)
                Chapman.set("")
                self.Statusbar['text'] = 'Chapman Drink Selected Price is '+price12+'...Quantity in Stock is '+stock12+'...'
            elif(var12.get()==0):
                txtChapman.configure(state = DISABLED)
                Chapman.set("0")
                self.Statusbar['text'] = ''
        #==============Checkbutton Function for Chivita==================
        def chkCHI():
            if (var13.get()==1):
                info13 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'chivita'")
                for n in info13:
                    price13 = n[0]  
                    stock13 = n[1]                        
                txtChivita.configure(state = NORMAL)
                txtChivita.focus()
                txtChivita.delete('0',END)
                Chivita.set("")
                self.Statusbar['text'] = 'Chivita Juice Selected Price is '+price13+'...Quantity in Stock is '+stock13+'...'
            elif(var13.get()==0):
                txtChivita.configure(state = DISABLED)
                Chivita.set("0")
                self.Statusbar['text'] = ''
        #==============Checkbutton Function for Malt==================
        def chkMA():
            if (var14.get()==1):
                info14 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'malt'")
                for o in info14:
                    price14 = o[0]  
                    stock14 = o[1]                    
                txtMalt.configure(state = NORMAL)
                txtMalt.focus()
                txtMalt.delete('0',END)
                Malt.set("")
                self.Statusbar['text'] = 'Malt Drink Selected Price is '+price14+'...Quantity in Stock is '+stock14+'...'
            elif(var14.get()==0):
                txtMalt.configure(state = DISABLED)
                Malt.set("0")
                self.Statusbar['text'] = ''
        #==============Checkbutton Function for Zobo==================
        def chkZO():
            if (var15.get()==1):
                info15 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'zobo'")
                for p in info15:
                    price15 = p[0]  
                    stock15 = p[1]                         
                txtZobo.configure(state = NORMAL)
                txtZobo.focus()
                txtZobo.delete('0',END)
                Zobo.set("")
                self.Statusbar['text'] = 'Zobo Drink Selected Price is '+price15+'...Quantity in Stock is '+stock15+'...'
            elif(var15.get()==0):
                txtZobo.configure(state = DISABLED)
                Zobo.set("0")
                self.Statusbar['text'] = ''
        #==============Checkbutton Function for Bottled Water==================
        def chkBO():
            if (var16.get()==1):
                info16 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'bottle water'")
                for q in info16:
                    price16 = q[0]  
                    stock16 = q[1]                
                txtBottled_Water.configure(state = NORMAL)
                txtBottled_Water.focus()
                txtBottled_Water.delete('0',END)
                Bottled_Water.set("")
                self.Statusbar['text'] = 'Bottle Water Selected Price is '+price16+'...Quantity in Stock is '+stock16+'...'
            elif(var16.get()==0):
                txtBottled_Water.configure(state = DISABLED)
                Bottled_Water.set("0")
                self.Statusbar['text'] = ''
        #==============Checkbutton Function for Shawarma==================
        def chkSH():
            if  (var17.get()==1):
                info17 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'shawarma'")
                for r in info17:
                    price17 = r[0]  
                    stock17 = r[1]                   
                txtShawarma.configure(state = NORMAL)
                txtShawarma.focus()
                txtShawarma.delete('0',END)
                Shawarma.set("")
                self.Statusbar['text'] = 'Shawarma Selected Price is '+price17+'...Quantity in Stock is '+stock17+'...'
            elif(var17.get()==0):
                txtShawarma.configure(state = DISABLED)
                Shawarma.set("0")
                self.Statusbar['text'] = ''
        #==============Checkbutton Function for Meat Pie==================
        def chkMP():
            if (var18.get()==1):
                info18 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'meat pie'")
                for s in info18:
                    price18 = s[0]  
                    stock18 = s[1]                  
                txtMeat_Pie.configure(state = NORMAL)
                txtMeat_Pie.focus()
                txtMeat_Pie.delete('0',END)
                Meat_Pie.set("")
                self.Statusbar['text'] = 'Meat Pie Selected Price is '+price18+'...Quantity in Stock is '+stock18+'...'
            elif(var18.get()==0):
                txtMeat_Pie.configure(state = DISABLED)
                Meat_Pie.set("0")
                self.Statusbar['text'] = ''
        #==============Checkbutton Function for Chicken Pie==================
        def chkCP():
            if (var19.get()==1):
                info19 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'chicken pie'")
                for t in info19:
                    price19 = t[0]  
                    stock19 = t[1]                  
                txtChicken_Pie.configure(state = NORMAL)
                txtChicken_Pie.focus()
                txtChicken_Pie.delete('0',END)
                Chicken_Pie.set("")
                self.Statusbar['text'] = 'Chicken Pie Selected Price is '+price19+'...Quantity in Stock is '+stock19+'...'
            elif(var19.get()==0):
                txtChicken_Pie.configure(state = DISABLED)
                Chicken_Pie.set("0")
                self.Statusbar['text'] = ''
        #==============Checkbutton Function for Doughnut==================
        def chkDO():
            if (var20.get()==1):
                info20 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'doughnut'")
                for u in info20:
                    price20 = u[0]  
                    stock20 = u[1]                       
                txtDoughnut.configure(state = NORMAL)
                txtDoughnut.focus()
                txtDoughnut.delete('0',END)
                Doughnut.set("")
                self.Statusbar['text'] = 'Doughnut Selected Price is '+price20+'...Quantity in Stock is '+stock20+'...'
            elif(var20.get()==0):
                txtDoughnut.configure(state = DISABLED)
                Doughnut.set("0")
                self.Statusbar['text'] = ''
        #==============Checkbutton Function for Pop Corn==================
        def chkPO():
            if (var21.get()==1):
                info21 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'pop corn'")
                for v in info21:
                    price21 = v[0]  
                    stock21 = v[1]                 
                txtPop_Corn.configure(state = NORMAL)
                txtPop_Corn.focus()
                txtPop_Corn.delete('0',END)
                Pop_Corn.set("")
                self.Statusbar['text'] = 'Pop Corn Selected Price is '+price21+'...Quantity in Stock is '+stock21+'...'
            elif(var21.get()==0):
                txtPop_Corn.configure(state = DISABLED)
                Pop_Corn.set("0")
                self.Statusbar['text'] = ''
        #==========================================FOOD FRAME====================================================
        self.Jollof_Rice = Checkbutton(self.Food_Frame,text="Jollof Rice",variable=var1, onvalue=1, offvalue=0,font=('arial',11,'bold'),bg='pale green',command=chkJR)
        self.Jollof_Rice.grid(row=0,sticky=W)
        self.Fried_Rice = Checkbutton(self.Food_Frame,text="Fried Rice",variable=var2, onvalue=1, offvalue=0,font=('arial',11,'bold'),bg='pale green', command=chkFR)
        self.Fried_Rice.grid(row=1,sticky=W)
        self.Eba = Checkbutton(self.Food_Frame,text="Eba",variable=var3, onvalue=1, offvalue=0,font=('arial',11,'bold'), bg='pale green', command=chkEBA)
        self.Eba.grid(row=2,sticky=W)
        self.Semovita = Checkbutton(self.Food_Frame,text="Semovita",variable=var4, onvalue = 1, offvalue=0,font=('arial',11,'bold'),bg='pale green', command=chkSEM)
        self.Semovita.grid(row=3,sticky=W)
        self.Egusi_Soup = Checkbutton(self.Food_Frame,text="Egusi Soup",variable=var5, onvalue = 1, offvalue=0,font=('arial',11,'bold'),bg='pale green', command=chkEG)
        self.Egusi_Soup.grid(row=4,sticky=W)
        self.Vegetable_Soup = Checkbutton(self.Food_Frame,text="Vegetable soup",variable=var6, onvalue = 1, offvalue=0,font=('arial',11,'bold'),bg='pale green', command=chkVG)
        self.Vegetable_Soup.grid(row=5,sticky=W)
        self.Chicken = Checkbutton(self.Food_Frame,text="Chicken",variable=var7, onvalue = 1, offvalue=0,font=('arial',11,'bold'),bg='pale green', command=chkCH)
        self.Chicken.grid(row=6,sticky=W)
        self.Meat = Checkbutton(self.Food_Frame,text="Meat",variable=var8, onvalue = 1, offvalue=0,font=('arial',11,'bold'),bg='pale green', command=chkME)
        self.Meat.grid(row=7,sticky=W)
        #==========================ENTRY BOX FOR FOOD=======================
        txtJollof_Rice = Entry(self.Food_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Jollof_Rice)
        txtJollof_Rice.grid(row=0,column=1)
        txtFried_Rice = Entry(self.Food_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Fried_Rice)
        txtFried_Rice.grid(row=1,column=1)
        txtEba = Entry(self.Food_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Eba)
        txtEba.grid(row=2,column=1)
        txtSemovita = Entry(self.Food_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Semovita)
        txtSemovita.grid(row=3,column=1)
        txtEgusi_Soup = Entry(self.Food_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Egusi_Soup)
        txtEgusi_Soup.grid(row=4,column=1)
        txtVegetable_Soup = Entry(self.Food_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Vegetable_Soup)
        txtVegetable_Soup.grid(row=5,column=1)
        txtChicken = Entry(self.Food_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Chicken)
        txtChicken.grid(row=6,column=1)
        txtMeat = Entry(self.Food_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Meat)
        txtMeat.grid(row=7,column=1)
        #==============================DRINKS FRAME===========================
        self.Coke = Checkbutton(self.Drinks_Frame,text="Coke",variable=var9, onvalue = 1, offvalue=0,font=('arial',11,'bold'),bg='pale green',command=chkCO)
        self.Coke.grid(row=0,sticky=W)
        self.Fanta = Checkbutton(self.Drinks_Frame,text="Fanta",variable=var10, onvalue = 1, offvalue=0,font=('arial',11,'bold'),bg='pale green',command=chkFA)
        self.Fanta.grid(row=1,sticky=W)
        self.Sprite = Checkbutton(self.Drinks_Frame,text="Sprite",variable=var11, onvalue = 1, offvalue=0,font=('arial',11,'bold'),bg='pale green',command=chkSP)
        self.Sprite.grid(row=2,sticky=W)
        self.Chapman = Checkbutton(self.Drinks_Frame,text="Chapman",variable=var12, onvalue = 1, offvalue=0,font=('arial',11,'bold'),bg='pale green',command=chkCHA)
        self.Chapman.grid(row=3,sticky=W)
        self.Chivita = Checkbutton(self.Drinks_Frame,text="Chivita",variable=var13, onvalue = 1, offvalue=0,font=('arial',11,'bold'),bg='pale green',command=chkCHI)
        self.Chivita.grid(row=4,sticky=W)
        self.Malt = Checkbutton(self.Drinks_Frame,text="Malt",variable=var14, onvalue = 1, offvalue=0,font=('arial',11,'bold'),bg='pale green',command=chkMA)
        self.Malt.grid(row=5,sticky=W)
        self.Zobo = Checkbutton(self.Drinks_Frame,text="Zobo",variable=var15, onvalue = 1, offvalue=0,font=('arial',11,'bold'),bg='pale green',command=chkZO)
        self.Zobo.grid(row=6,sticky=W)
        self.Bottled_Water = Checkbutton(self.Drinks_Frame,text="Bottled Water",variable=var16, onvalue = 1, offvalue=0,font=('arial',11,'bold'),bg='pale green',command=chkBO)
        self.Bottled_Water.grid(row=7,sticky=W)
        #==========================ENTRY BOX FOR DRINKS=======================
        txtCoke = Entry(self.Drinks_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Coke)
        txtCoke.grid(row=0,column=1)
        txtFanta = Entry(self.Drinks_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Fanta)
        txtFanta.grid(row=1,column=1)
        txtSprite = Entry(self.Drinks_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Sprite)
        txtSprite.grid(row=2,column=1)
        txtChapman = Entry(self.Drinks_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Chapman)
        txtChapman.grid(row=3,column=1)
        txtChivita = Entry(self.Drinks_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Chivita)
        txtChivita.grid(row=4,column=1)
        txtMalt = Entry(self.Drinks_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Malt)
        txtMalt.grid(row=5,column=1)
        txtZobo = Entry(self.Drinks_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Zobo)
        txtZobo.grid(row=6,column=1)
        txtBottled_Water = Entry(self.Drinks_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Bottled_Water)
        txtBottled_Water.grid(row=7,column=1)
        #=============================SNACKS FRAME============================
        self.Shawarma = Checkbutton(self.Snacks_Frame,text="Shawarma",variable=var17, onvalue=1, offvalue=0,font=('arial',11,'bold'),bg='pale green',command=chkSH)
        self.Shawarma.grid(row=0,sticky=W)
        self.Meat_Pie = Checkbutton(self.Snacks_Frame,text="Meat Pie",variable=var18, onvalue=1, offvalue=0,font=('arial',11,'bold'),bg='pale green',command=chkMP)
        self.Meat_Pie.grid(row=1,sticky=W)
        self.Chicken_Pie = Checkbutton(self.Snacks_Frame,text="Chicken Pie",variable=var19, onvalue=1, offvalue=0,font=('arial',11,'bold'),bg='pale green',command=chkCP)
        self.Chicken_Pie.grid(row=2,sticky=W)
        self.Doughnut = Checkbutton(self.Snacks_Frame,text="Doughnut",variable=var20, onvalue=1, offvalue=0,font=('arial',11,'bold'),bg='pale green',command=chkDO)
        self.Doughnut.grid(row=3,sticky=W)
        self.Pop_Corn = Checkbutton(self.Snacks_Frame,text="Pop Corn",variable=var21, onvalue=1, offvalue=0,font=('arial',11,'bold'),bg='pale green',command=chkPO)
        self.Pop_Corn.grid(row=4,sticky=W)
        #==========================ENTRY BOX FOR SNACKS=======================
        txtShawarma = Entry(self.Snacks_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Shawarma)
        txtShawarma.grid(row=0,column=1)
        txtMeat_Pie = Entry(self.Snacks_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Meat_Pie)
        txtMeat_Pie.grid(row=1,column=1)
        txtChicken_Pie = Entry(self.Snacks_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Chicken_Pie)
        txtChicken_Pie.grid(row=2,column=1)
        txtDoughnut = Entry(self.Snacks_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Doughnut)
        txtDoughnut.grid(row=3,column=1)
        txtPop_Corn = Entry(self.Snacks_Frame,font=('arial',8,'bold'),bd=6,width=6, justify='right',state = DISABLED,textvariable=Pop_Corn)
        txtPop_Corn.grid(row=4,column=1)
        #======================Widgets For Others Frame=======================
        self.lblOthers = Label(self.others_frame,text="Product Name ",font=('arial',13,'bold'),bg='green',fg='light gray')
        self.lblOthers.place(x=10,y=10)
        
        self.txtOthers = Entry(self.others_frame,font=('arial',14,'bold'),width=20,bg='white',justify='left',textvariable=Others)
        self.txtOthers.place(x=135,y=10)
        self.txtOthers.focus()
        
        self.photo10 = PhotoImage(file="search.png")
        self.lblsearch = Label(self.others_frame,image=self.photo10)
        self.lblsearch.place(x=345,y=10)
        
        def search():
            try:
                self.name = (Others.get()).lower()
                query = "SELECT * FROM stock_records WHERE Product_Name=?"
                result = c.execute(query, (self.name,))
                for r in result:
                    self.item_name = r[0] #item name
                    self.stock = r[1] #quantity stock
                    self.price = r[3] #selling price
                conn.commit()   
                self.lblsearch_info = Label(self.others_frame,text="Price is "+str(self.price),font=('arial',14,'bold'),bg='green',fg='light gray')
                self.lblsearch_info.place(x=60,y=50)        
                
                self.Others_lbl = Label(self.others_frame,text="Enter Quantity ",font=('arial',14,'bold'),bg='green',fg='light gray')
                self.Others_lbl.place(x=60,y=100)
                
                self.Others_ent = Entry(self.others_frame,font=('arial',12,'bold'),bd=3,width=5, justify='right',textvariable=Others_Qty)
                self.Others_ent.place(x=310,y=100)
                self.Others_ent.focus()
                
                self.Statusbar.configure(text = ''+self.item_name+' Selected Price is '+str(self.price)+'...Quantity in Stock is '+str(self.stock)+'...')                  
                def refresh():
                    self.Others_lbl.destroy()
                    self.Others_ent.destroy()
                    self.lblsearch_info.destroy()
                    self.btnrefresh.destroy()
                    self.txtOthers.delete(0,END)
                    self.txtOthers.focus()
                self.btnrefresh = Button(self.others_frame,text="Refresh",font=('arial',12,'bold'),width=8,bd=4,bg='pale green',command=refresh)
                self.btnrefresh.place(x=520,y=98) 
            except:
                self.Statusbar.configure(text = 'No Item Match') 
                tkinter.messagebox.showerror("Name Error","Item Does Not Exist in Stock Records...")
        #================Search Button==============
        self.btnOthers = Button(self.others_frame,text="Search",font=('arial',12,'bold'),width=8,bd=4,bg='pale green',command=search)
        self.btnOthers.place(x=420,y=5)
        #================Add to Cart Function===========  
        def add_to_cart(event):
            self.lblitems = Label(self.Cart_Info,text ="Items",font=('arial',12,'bold'),bg='white')
            self.lblitems.place(x=10,y=30)
            
            self.lblqty = Label(self.Cart_Info,text ="Qty",font=('arial',12,'bold'),bg='white')
            self.lblqty.place(x=290,y=30)
            
            self.lblprice = Label(self.Cart_Info,text ="Price",font=('arial',12,'bold'),bg='white')
            self.lblprice.place(x=400,y=30)                    
            if (Others.get() != ""):
                self.quantity = Others_Qty.get()
                if  int(self.quantity) > int(self.stock):
                    tkinter.messagebox.showerror("Error","Not as Much Items in Stock")
                else:                   
                    self.final_price = int(self.price) * int(Others_Qty.get())
                    item_list.append(self.item_name)
                    price_list.append(self.final_price)
                    quantity_list.append(self.quantity)
                    
                    new_stock = int(self.stock)-int(self.quantity)
                    c.execute("UPDATE stock_records set Stock = '"+str(new_stock)+"' WHERE Product_Name = '"+self.name+"'")                    
                    item_and_quantity.append(""+self.item_name+""+self.quantity+" ")
                    
                    self.Others_lbl.place_forget()
                    self.Others_ent.delete(0,END)
                    self.Others_ent.place_forget()
                    self.lblsearch_info.place_forget()
                    self.btnrefresh.place_forget()
                    self.txtOthers.delete(0,END)
                    self.txtOthers.focus()                              
            else:
                pass 
            if (var1.get()==1):
                item1 = "Jollof Rice"+' '+Jollof_Rice.get()+' '
                price1 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'jollof rice'")
                for a in price1:
                    price1 = a[0]
                    stock1 = a[1]
                item_list.append("Jollof Rice")
                price_list.append(int(price1)*int(Jollof_Rice.get()))
                quantity_list.append(Jollof_Rice.get())
                item_and_quantity.append("jollof rice"+Jollof_Rice.get()+" ")
                new_stock1 = int(stock1)-int(Jollof_Rice.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock1)+"' WHERE Product_Name = 'jollof rice'")
            else:
                pass                
            if(var2.get()==1):
                price2 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'fried rice'")
                for b in price2:
                    price2 = b[0]  
                    stock2 = b[1]
                item_list.append("Fried Rice")
                price_list.append(int(price2)*int(Fried_Rice.get()))
                quantity_list.append(Fried_Rice.get()) 
                item_and_quantity.append("fried rice"+Fried_Rice.get()+" ")
                new_stock2 = int(stock2)-int(Fried_Rice.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock2)+"' WHERE Product_Name = 'fried rice'")                
            else:
                pass
            if(var3.get()==1):
                price3 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'eba'")
                for d in price3:
                    price3 = d[0]  
                    stock3 = d[1]
                item_list.append("Eba")
                price_list.append(int(price3)*int(Eba.get()))
                quantity_list.append(Eba.get())
                item_and_quantity.append("eba"+Eba.get()+" ")
                new_stock3 = int(stock3)-int(Eba.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock3)+"' WHERE Product_Name = 'eba'")                
            else:
                pass
            if(var4.get()==1):
                price4 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'semovita'")
                for e in price4:
                    price4 = e[0]  
                    stock4 = e[1]
                item_list.append("Semovita")
                price_list.append(int(price4)*int(Semovita.get()))
                quantity_list.append(Semovita.get())
                item_and_quantity.append("semovita"+Semovita.get()+" ")
                new_stock4 = int(stock4)-int(Semovita.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock4)+"' WHERE Product_Name = 'semovita'")                  
            else:
                pass
            if(var5.get()==1):
                price5 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'egusi soup'")
                for f in price5:
                    price5 = f[0] 
                    stock5 = f[1]
                item_list.append("Egusi Soup")
                price_list.append(int(price5)*int(Egusi_Soup.get()))
                quantity_list.append(Egusi_Soup.get())
                item_and_quantity.append("egusi soup"+Egusi_Soup.get()+" ")
                new_stock5 = int(stock5)-int(Egusi_Soup.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock5)+"' WHERE Product_Name = 'egusi soup'")                 
            else:
                pass
            if(var6.get()==1):
                price6 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'vegetable soup'")
                for g in price6:
                    price6 = g[0] 
                    stock6 = g[1]
                item_list.append("Vegetable Soup")
                price_list.append(int(price6)*int(Vegetable_Soup.get()))
                quantity_list.append(Vegetable_Soup.get())
                item_and_quantity.append("vegetable soup"+Vegetable_Soup.get()+" ")
                new_stock6 = int(stock6)-int(Vegetable_Soup.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock6)+"' WHERE Product_Name = 'vegetable soup'")                
            else:
                pass  
            if(var7.get()==1):
                price7 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'chicken'")
                for h in price7:
                    price7 = h[0] 
                    stock7 = h[1]
                item_list.append("Chicken")
                price_list.append(int(price7)*int(Chicken.get()))
                quantity_list.append(Chicken.get())
                item_and_quantity.append("chicken"+Chicken.get()+" ")
                new_stock7 = int(stock7)-int(Chicken.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock7)+"' WHERE Product_Name = 'chicken'")                 
            else:
                pass       
            if(var8.get()==1):
                price8 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'meat'")
                for i in price8:
                    price8 = i[0]   
                    stock8 = i[1]
                item_list.append("Meat")
                price_list.append(int(price8)*int(Meat.get()))
                quantity_list.append(Meat.get())
                item_and_quantity.append("meat"+Meat.get()+" ")
                new_stock8 = int(stock8)-int(Meat.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock8)+"' WHERE Product_Name = 'meat'")                 
            else:
                pass      
            if(var9.get()==1):
                price9 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'coke'")
                for j in price9:
                    price9 = j[0] 
                    stock9 = j[1]
                item_list.append("Coke")
                price_list.append(int(price9)*int(Coke.get()))
                quantity_list.append(Coke.get())
                item_and_quantity.append("coke"+Coke.get()+" ")
                new_stock9 = int(stock9)-int(Coke.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock9)+"' WHERE Product_Name = 'coke'")                   
            else:
                pass     
            if(var10.get()==1):
                price10 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'fanta'")
                for k in price10:
                    price10 = k[0]  
                    stock10 = k[1]  
                item_list.append("Fanta")
                price_list.append(int(price10)*int(Fanta.get()))
                quantity_list.append(Fanta.get())
                item_and_quantity.append("fanta"+Fanta.get()+" ")
                new_stock10 = int(stock10)-int(Fanta.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock10)+"' WHERE Product_Name = 'fanta'")                
            else:
                pass        
            if(var11.get()==1):
                price11 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'sprite'")
                for l in price11:
                    price11 = l[0]
                    stock11 = l[1]
                item_list.append("Sprite")
                price_list.append(int(price11)*int(Sprite.get()))
                quantity_list.append(Sprite.get())
                item_and_quantity.append("sprite"+Sprite.get()+" ")
                new_stock11 = int(stock11)-int(Sprite.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock11)+"' WHERE Product_Name = 'sprite'")                 
            else:
                pass       
            if(var12.get()==1):
                price12 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'chapman'")
                for m in price12:
                    price12 = m[0]
                    stock12 = m[1]
                item_list.append("Chapman")
                price_list.append(int(price12)*int(Chapman.get()))
                quantity_list.append(Chapman.get())
                item_and_quantity.append("chapman"+Chapman.get()+" ")
                new_stock12 = int(stock12)-int(Chapman.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock12)+"' WHERE Product_Name = 'chapman'")                              
            else:
                pass        
            if(var13.get()==1):
                price13 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'chivita'")
                for n in price13:
                    price13 = n[0]
                    stock13 = n[1]
                item_list.append("Chivita")
                price_list.append(int(price13)*int(Chivita.get()))
                quantity_list.append(Chivita.get())
                item_and_quantity.append("chivita"+Chivita.get()+" ")
                new_stock13 = int(stock13)-int(Chivita.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock13)+"' WHERE Product_Name = 'chivita'")                 
            else:
                pass        
            if(var14.get()==1):
                price14 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'malt'")
                for o in price14:
                    price14 = o[0]    
                    stock14 = o[1]
                item_list.append("Malt")
                price_list.append(int(price14)*int(Malt.get()))
                quantity_list.append(Malt.get())
                item_and_quantity.append("malt"+Malt.get()+" ")
                new_stock14 = int(stock14)-int(Malt.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock14)+"' WHERE Product_Name = 'malt'")                 
            else:
                pass            
            if(var15.get()==1):
                price15 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'zobo'")
                for p in price15:
                    price15 = p[0] 
                    stock15 = p[1]
                item_list.append("Zobo")
                price_list.append(int(price15)*int(Zobo.get()))
                quantity_list.append(Zobo.get())    
                item_and_quantity.append("zobo"+Zobo.get()+" ")
                new_stock15 = int(stock15)-int(Zobo.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock15)+"' WHERE Product_Name = 'zobo'")                
            else:
                pass        
            if(var16.get()==1):
                price16 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'bottle water'")
                for q in price16:
                    price16 = q[0]        
                    stock16 = q[1]
                item_list.append("Bottle Water")
                price_list.append(int(price16)*int(Bottled_Water.get()))
                quantity_list.append(Bottled_Water.get())
                item_and_quantity.append("bottle water"+Bottled_Water.get()+" ")
                new_stock16 = int(stock16)-int(Bottled_Water.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock16)+"' WHERE Product_Name = 'bottle water'")                  
            else:
                pass            
            if(var17.get()==1):
                price17 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'shawarma'")
                for r in price17:
                    price17 = r[0] 
                    stock17 = r[1]
                item_list.append("Shawarma")
                price_list.append(int(price17)*int(Shawarma.get()))
                quantity_list.append(Shawarma.get())
                item_and_quantity.append("shawarma"+Shawarma.get()+" ")
                new_stock17 = int(stock17)-int(Shawarma.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock17)+"' WHERE Product_Name = 'shawarma'")                  
            else:
                pass            
            if(var18.get()==1):
                price18 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'meat pie'")
                for s in price18:
                    price18 = s[0] 
                    stock18 = s[1]
                item_list.append("Meat Pie")
                price_list.append(int(price18)*int(Meat_Pie.get()))
                quantity_list.append(Meat_Pie.get())
                item_and_quantity.append("meat pie"+Meat_Pie.get()+" ")
                new_stock18= int(stock18)-int(Meat_Pie.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock18)+"' WHERE Product_Name = 'meat pie'")                
            else:
                pass       
            if(var19.get()==1):
                price19 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'chicken pie'")
                for t in price19:
                    price19 = t[0]       
                    stock19 = t[1]
                item_list.append("Chicken Pie")
                price_list.append(int(price19)*int(Chicken_Pie.get()))
                quantity_list.append(Chicken_Pie.get())
                item_and_quantity.append("chicken pie"+Chicken_Pie.get()+" ")
                new_stock19 = int(stock19)-int(Chicken_Pie.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock19)+"' WHERE Product_Name = 'chicken pie'")                
            else:
                pass          
            if(var20.get()==1):
                price20 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'doughnut'")
                for u in price20:
                    price20 = u[0]  
                    stock20 = u[1]
                item_list.append("Doughnut")
                price_list.append(int(price20)*int(Doughnut.get()))
                quantity_list.append(Doughnut.get())
                item_and_quantity.append("doughnut"+Doughnut.get()+" ")
                new_stock20 = int(stock20)-int(Doughnut.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock20)+"' WHERE Product_Name = 'doughnut'")                 
            else:
                pass
            if(var21.get()==1):
                price21 = c.execute("SELECT Selling_Price,Stock FROM stock_records WHERE Product_Name = 'pop corn'")
                for v in price21:
                    price21 = v[0] 
                    stock21 = v[1]
                item_list.append("Pop Corn")
                price_list.append(int(price21)*int(Pop_Corn.get()))
                quantity_list.append(Pop_Corn.get())
                item_and_quantity.append("pop corn"+Pop_Corn.get()+" ")
                new_stock21 = int(stock21)-int(Pop_Corn.get())
                c.execute("UPDATE stock_records set Stock = '"+str(new_stock21)+"' WHERE Product_Name = 'pop corn'")                
            else:
                pass
        
            self.y_axis = 25
            self.counter = 0
            for p in item_list:
                self.temp_item = Label(self.Cart_Frame,text=str(item_list[self.counter]),font=('arial',12),bg='white')
                self.temp_item.place(x=10,y=self.y_axis)
                
                self.temp_qty = Label(self.Cart_Frame,text=str(quantity_list[self.counter]),font=('arial',12),bg='white')
                self.temp_qty.place(x=290,y=self.y_axis)
                
                self.temp_price = Label(self.Cart_Frame,text=str(price_list[self.counter]),font=('arial',12),bg='white')
                self.temp_price.place(x=400,y=self.y_axis)        
                
                self.y_axis += 25
                self.counter += 1
                
                self.Statusbar.configure(text = ''+str(self.counter)+' Item(s) Added to Cart...')
                var1.set(0)
                txtJollof_Rice.configure(state = DISABLED)
                Jollof_Rice.set("0")
                var2.set(0)
                txtFried_Rice.configure(state = DISABLED)
                Fried_Rice.set("0")            
                var3.set(0)
                txtEba.configure(state = DISABLED)
                Eba.set("0")            
                var4.set(0)
                txtSemovita.configure(state = DISABLED)
                Semovita.set("0")            
                var5.set(0)
                txtEgusi_Soup.configure(state = DISABLED)
                Egusi_Soup.set("0")           
                var6.set(0)
                txtVegetable_Soup.configure(state = DISABLED)
                Vegetable_Soup.set("0")            
                var7.set(0)
                txtChicken.configure(state = DISABLED)
                Chicken.set("0")           
                var8.set(0)
                txtMeat.configure(state = DISABLED)
                Meat.set("0")            
                var9.set(0)
                txtCoke.configure(state = DISABLED) 
                Coke.set("0")            
                var10.set(0)
                txtFanta.configure(state = DISABLED)
                Fanta.set("0")
                var11.set(0)
                txtSprite.configure(state = DISABLED)
                Sprite.set("0")            
                var12.set(0)
                txtChapman.configure(state = DISABLED)
                Chapman.set("0")
                var13.set(0)
                txtChivita.configure(state = DISABLED)
                Chivita.set("0")
                var14.set(0)
                txtMalt.configure(state = DISABLED)
                Malt.set("0")                
                var15.set(0)
                txtZobo.configure(state = DISABLED)
                Zobo.set("0")
                var16.set(0)
                txtBottled_Water.configure(state = DISABLED)
                Bottled_Water.set("0")                
                var17.set(0)
                txtShawarma.configure(state = DISABLED)
                Shawarma.set("0")
                var18.set(0)
                txtMeat_Pie.configure(state = DISABLED)
                Meat_Pie.set("0")
                var19.set(0)
                txtChicken_Pie.configure(state = DISABLED)
                Chicken_Pie.set("0") 
                var20.set(0)
                txtDoughnut.configure(state = DISABLED)
                Doughnut.set("0")
                var21.set(0)
                txtPop_Corn.configure(state = DISABLED)
                Pop_Corn.set("0")                
        #==============Button Total Function=============== 
        def CostofItem():
            lbl_total = Label(self.Cart_Frame,text="Total Price : ₦"+ str(sum(price_list)),font=('arial',12,'bold'),bg='white')
            lbl_total.place(x=10,y=350)
            
            SC = 'NGN '+str('%.2f' %(0))
            ServiceCharge.set(SC)
            
            SubTotalofItems = 'NGN '+str('%.2f' %(sum(price_list)))
            SubTotal.set(SubTotalofItems)
            
            TotalCost = 'NGN '+str('%.2f' %(sum(price_list)))
            Total.set(TotalCost)
            
            self.Statusbar['text'] = 'Total Price is '+TotalCost+'...'        
        def Reset():
            var1.set(0)
            txtJollof_Rice.configure(state = DISABLED)
            Jollof_Rice.set("0")
            
            var2.set(0)
            txtFried_Rice.configure(state = DISABLED)
            Fried_Rice.set("0")
            
            var3.set(0)
            txtEba.configure(state = DISABLED)
            Eba.set("0")
            
            var4.set(0)
            txtSemovita.configure(state = DISABLED)
            Semovita.set("0")
            
            var5.set(0)
            txtEgusi_Soup.configure(state = DISABLED)
            Egusi_Soup.set("0")
            
            var6.set(0)
            txtVegetable_Soup.configure(state = DISABLED)
            Vegetable_Soup.set("0")
            
            var7.set(0)
            txtChicken.configure(state = DISABLED)
            Chicken.set("0")
            
            var8.set(0)
            txtMeat.configure(state = DISABLED)
            Meat.set("0")
            
            var9.set(0)
            txtCoke.configure(state = DISABLED) 
            Coke.set("0")
            
            var10.set(0)
            txtFanta.configure(state = DISABLED)
            Fanta.set("0")
            
            var11.set(0)
            txtSprite.configure(state = DISABLED)
            Sprite.set("0")
            
            var12.set(0)
            txtChapman.configure(state = DISABLED)
            Chapman.set("0")
            
            var13.set(0)
            txtChivita.configure(state = DISABLED)
            Chivita.set("0")
            
            var14.set(0)
            txtMalt.configure(state = DISABLED)
            Malt.set("0")
            
            var15.set(0)
            txtZobo.configure(state = DISABLED)
            Zobo.set("0")
            
            var16.set(0)
            txtBottled_Water.configure(state = DISABLED)
            Bottled_Water.set("0")
            
            var17.set(0)
            txtShawarma.configure(state = DISABLED)
            Shawarma.set("0")
            
            var18.set(0)
            txtMeat_Pie.configure(state = DISABLED)
            Meat_Pie.set("0")
            
            var19.set(0)
            txtChicken_Pie.configure(state = DISABLED)
            Chicken_Pie.set("0")
            
            var20.set(0)
            txtDoughnut.configure(state = DISABLED)
            Doughnut.set("0")
            
            var21.set(0)
            txtPop_Corn.configure(state = DISABLED)
            Pop_Corn.set("0")
            
            SubTotal.set("")
            Total.set("")
            ServiceCharge.set("")
            
            self.Statusbar['text'] = 'Restaurant Management System...'
            
            for widget in self.Cart_Frame.winfo_children():
                widget.destroy()           
            
            item_list.clear()
            price_list.clear()
            quantity_list.clear()  
            item_and_quantity.clear()  
        
        def Save():  
            self.Statusbar['text'] = 'Saving...'
            #=================================Database Connection=============================            
            def concatenate_list_data(list):
                result= ''
                for item in list:
                    result += str(item)
                return result
        
            item_qty = concatenate_list_data(item_and_quantity)            
            try: 
                c.execute("INSERT INTO sales_records (items,price,date,time) VALUES('"+str(item_qty)+"','"+str(sum(price_list))+"','"+Current_date.get()+"','"+Current_time.get()+"')")
                conn.commit()
                tkinter.messagebox.showinfo("Save","Records Saved Sucessfully!")
                self.Statusbar['text'] = 'Saved...'
                  
            except:
                tkinter.messagebox.showerror("Error","Error Saving!")
                self.Statusbar['text'] = 'Error While trying To Save...'
            
            #=============Receipt File==================
            
            directory = "C:/Users/DAVID ODEN/Desktop/Restaurant Management System/invoice/" + str(Current_date.get()) + "/"
            if not os.path.exists(directory):
                os.makedirs(directory)
            #====Templates===
            company = "\t\t\t\t\tRestaurant Managemant Ltd.\n"
            address = "\t\t\t\t\t\t  Kurudu.\n"
            phone_no = "\t\t\t\t\t       08154549452\n"
            sample = "\t\t\t\t\t     Invoice\n"
            date = "\t\t\t\t\t   "+str(Current_date.get())
       
            h_f = "\n\n\t\t\t========================================================\n\t\t\tSN.\tProducts\t\tQty\t\tAmount\n\t\t\t========================================================"
            invoice = company + address + phone_no + sample + date + "\n" + h_f
            x = random.randrange(1,500)
            #open a file to write to
            file_name = str(directory) + str(x) + ".txt"
            f = open(file_name, 'w')
            f.write(invoice)
            #fill in dynamics
            i = 1
            count = 0
            for p in item_list:
                f.write("\n\t\t\t" + str(i) + "\t" + str(item_list[count] + "      ")[:15]+"\t\t"+str(quantity_list[count])+"\t\t"+str(price_list[count])+"\t\t\t")
                count += 1
                i += 1 
            f.write("\n\n\t\t\t\t\t\t\t\tTotal N "+str(sum(price_list)))
            f.write("\n\t\t\t\t\tThanks For Coming...")
            f.close()            
                   
        #==============Button Receipt Function=============== 
        def Receipt():
            self.lblitems.place_forget()
            self.lblqty.place_forget()
            self.lblprice.place_forget()
            txtReceipt = Text(self.Cart_Frame, width=52,height=22,bg="light grey",font=('arial',12))
            txtReceipt.place(x=0,y=0)            
            txtReceipt.delete("1.0",END)
            x = random.randint(247525,568234)
            randomRef = str(x)
            Receipt_Ref.set("Bill " + randomRef)
            
            #====Templates====#
            txtReceipt.insert(END,"\t\tRestaurant Managemant Ltd.\n")
            txtReceipt.insert(END,"\t\t\t  Kurudu.\n")
            txtReceipt.insert(END,"\t\t\t08154549452\n")
            txtReceipt.insert(END,"\t\t\t    Invoice\n")                
            txtReceipt.insert(END,"Receipt Reference:\t\t"+ Receipt_Ref.get() +"\t\t"+" Date "+ Current_date.get() +'\n\n')
            txtReceipt.insert(END,"Items:\t\t\t"+ "Quantity" +"\t\t"+"Price"+'\n')
            txtReceipt.insert(END,"============================================\n")     
            count = 0
            for p in item_list:
                txtReceipt.insert(END,str(item_list[count]+"  ")[:15]+"\t\t\t"+str(quantity_list[count])+"\t\t"+str(price_list[count])+"\n") 
                count += 1
            txtReceipt.insert(END,"============================================\n")    
            txtReceipt.insert(END,"Sub Total:\t\t\t\t"+SubTotal.get()+'\n\n')
            txtReceipt.insert(END,"Total:\t\t\t\t"+Total.get()+'\n')            
            txtReceipt.insert(END,"\n\t\tThanks For Coming...")
            #==============Button Print Function=============== 
            def iPrint():
                q = txtReceipt.get("1.0","end-1c")
                filename = tempfile.mktemp(".txt")
                open (filename,"w").write(q)
                os.startfile(filename,"print")
                self.Statusbar['text'] = 'Printing Receipt...'              
            self.btnPrint = Button(self.Buttons_Frame,padx=11,pady=1,bd=6,fg="black",font=('arial',14,'bold'),width=4,text="Print",bg="pale green",command=iPrint)
            self.btnPrint.grid(row=0,column=3)                  
        #==============================PAYMENT INFORMATION=====================================
        self.lblServiceCharge = Label(self.Cost_Frame,font=('arial',14,'bold'),text = "   Service Charge",bg='pale green',fg='black')
        self.lblServiceCharge.grid(row=0,column=0)
        txtServiceCharge = Entry(self.Cost_Frame,font=('arial',12,'bold'),textvariable=ServiceCharge,bd=7,bg="white",insertwidth=2,justify='right')
        txtServiceCharge.grid(row=1,column=0,padx=20)
        
        self.lblSubTotal = Label(self.Cost_Frame,font=('arial',14,'bold'),text = "   Sub Total",bg='pale green',fg='black')
        self.lblSubTotal.grid(row=0,column=1)
        txtSubTotal = Entry(self.Cost_Frame,font=('arial',12,'bold'),textvariable=SubTotal,bd=7,bg="white",insertwidth=2,justify='right')
        txtSubTotal.grid(row=1,column=1,padx=80)
        
        self.lblTotal = Label(self.Cost_Frame,font=('arial',14,'bold'),text = "   Total",bg='pale green',fg='black')
        self.lblTotal.grid(row=0,column=2)
        txtTotal = Entry(self.Cost_Frame,font=('arial',12,'bold'),textvariable=Total,bd=7,bg="white",insertwidth=2,justify='right')
        txtTotal.grid(row=1,column=2,padx=20)
        #===========================Cart Labels============================
        self.lblcart = Label(self.Cart_Info,text ="Cart",font=('arial',16,'bold'),bg='pale green',width=36,relief=GROOVE)
        self.lblcart.place(x=0,y=0)
        
        #==================================BUTTONS============================
        self.btnTotal = Button(self.Buttons_Frame,padx=11,pady=1,bd=6,fg="black",font=('arial',14,'bold'),width=5,text="Total",bg="pale green",command=CostofItem)
        self.btnTotal.grid(row=0,column=0)
        self.btnReceipt = Button(self.Buttons_Frame,padx=11,pady=1,bd=6,fg="black",font=('arial',14,'bold'),width=4,text="Receipt",bg="pale green",command=Receipt)
        self.btnReceipt.grid(row=0,column=1)
        self.btnReset = Button(self.Buttons_Frame,padx=11,pady=1,bd=6,fg="black",font=('arial',14,'bold'),width=4,text="Reset",bg="pale green",command=Reset)
        self.btnReset.grid(row=0,column=2)
        self.btnExit = Button(self.Buttons_Frame,padx=8,pady=1,bd=6,fg="black",font=('arial',14,'bold'),width=4,text="Exit",bg="pale green",command=iExit)
        self.btnExit.grid(row=0,column=4)
        self.calculator = Button(self.Buttons_Frame,padx=11,pady=1,bd=6,fg="black",font=('arial',12,'bold'),width=6,text="Calculator",bg="pale green",command=self.Calc)     
        self.calculator.grid(row=1,column=0)
        self.btnColor1 = Button(self.Buttons_Frame, padx=6,pady=1,bd=6,fg="black",font=('arial',11,'bold'),width=9,text="Background 1",bg="pale green",command=self.color1)        
        self.btnColor1.grid(row=1,column=3) 
        self.btnColor2 = Button(self.Buttons_Frame, padx=6,pady=1,bd=6,fg="black",font=('arial',11,'bold'),width=9,text="Background 2",bg="pale green",command=self.color2)     
        self.btnColor2.grid(row=1,column=1)     
        self.btnSave = Button(self.Buttons_Frame,padx=8,pady=1,bd=6,fg="black",font=('arial',14,'bold'),width=4,text="Save",bg="pale green",command=Save)        
        self.btnSave.grid(row=1,column=4)
        #====add to Cart=====
        photo11 = PhotoImage(file="add.png")
        self.btnAdd_item = Button(self.master,image=photo11,bd=5,command=add_to_cart)
        self.btnAdd_item.place(x=590,y=400)    
        
        #===================================Status Bar===========================
        self.Statusbar = Label(self.Barframe,text="Welcome to Restaurant Management System...",bg='green',fg='light gray')
        self.Statusbar.place(x=0,y=0)
        #==========================Menu Bar======================================
        menulist = Menu(self.master)
        self.master.config(menu=menulist)
        
        subMenu = Menu(menulist)
        menulist.add_cascade(label="File",menu=subMenu)
        subMenu.add_command(label="New Customer...",command=Reset)
        subMenu.add_command(label="Calculator",command=self.Calc)
        subMenu.add_separator()
        subMenu.add_command(label="Exit",command=iExit)
        
        searchMenu = Menu(menulist)
        menulist.add_cascade(label="More",menu=searchMenu)
        searchMenu.add_command(label="Records",command=self.Rec)
        searchMenu.add_command(label="About",command=self.about_us)
        searchMenu.add_command(label="Change Color 1",command=self.color1) 
        searchMenu.add_command(label="Change Color 2",command=self.color2) 
        
        can = Canvas(self.Tops, width=1050, height=100, bg = 'green')
        can.pack(side=LEFT)
        text = can.create_text(50,50,fill="light gray",font="arial 50 bold",text="B A R C R U S E")        
        
        while True:
            for i in range(0,200):
                can.move(text, 5, 0)
                can.update() 
            for i in range(0,200):
                can.move(text, -5, 0)
                can.update()   
                
            
    #==============Function to Change Background color==============
    def color1(self):
        colors = ['red2','gray4','midnight blue','gray3','saddle brown','cyan4','forest green','bisque4','SlateBlue4',
                  'DeepSkyBlue4','RoyalBlue4','green','Orange4','RosyBrown2','navy','OliveDrab4','purple4','gold4']  
        pick = random.choice(colors)
        self.master.configure(background=pick) 
        self.canvas.configure(background=pick)
        self.lblOthers.configure(background=pick)
        self.others_frame.configure(background=pick)
        self.icon.configure(background=pick)
        self.icon2.configure(background=pick)
        self.Tops.configure(background=pick)
        self.Barframe.configure(background=pick)
        self.Statusbar.configure(background=pick)
        self.lblsearch_info.configure(background=pick)
        self.btnAdd_item.configure(background=pick)
        self.Others_lbl.configure(background=pick)
    def color2(self): 
        colors2 = ['snow','navajo white','lavender','coral1','conflower blue','cyan3','spring green','light coral','HotPink2',
                  'PeachPuff2','RoyalBlue4','yellow','orange2','RosyBrown2','SpringGreen2','AntiqueWhite2','turquoise2','plum2']    
        pick2 = random.choice(colors2)
        
        #this are buttons
        self.calculator.config(bg=pick2)
        self.btnExit.config(bg=pick2)
        self.btnReceipt.config(bg=pick2)
        self.btnSave.config(bg=pick2)
        self.btnTotal.config(bg=pick2)
        self.btnReset.config(bg=pick2)
        self.btnPrint.config(bg=pick2)
        self.btnColor1.config(bg=pick2)
        self.btnColor2.config(bg=pick2)
        self.btnOthers.config(bg=pick2)
        
        #this are labels
        self.lblServiceCharge.configure(background=pick2)
        self.lblSubTotal.configure(background=pick2)
        self.lblTotal.configure(background=pick2)
        self.lblcart.configure(background=pick2)
        
        #this are frames
        self.Buttons_Frame.configure(background=pick2)
        self.RCF.configure(background=pick2)
        self.Cart_Info.configure(background=pick2)
        self.MenuFrame.configure(background=pick2)
        self.Food_Frame.configure(background=pick2)
        self.Snacks_Frame.configure(background=pick2)
        self.Drinks_Frame.configure(background=pick2)
        self.Cost_Frame.configure(background=pick2)
        self.pictures1.config(background=pick2)
        self.pictures2.config(background=pick2)
        self.pictures3.config(background=pick2)        
        #this are check boxes
        self.Jollof_Rice.config(background=pick2)
        self.Fried_Rice.config(background=pick2)
        self.Eba.config(background=pick2)
        self.Semovita.config(background=pick2)
        self.Vegetable_Soup.config(background=pick2)
        self.Egusi_Soup.config(background=pick2)
        self.Chicken.config(background=pick2)
        self.Meat.config(background=pick2)
        self.Coke.config(background=pick2)
        self.Fanta.config(background=pick2)
        self.Sprite.config(background=pick2)
        self.Malt.config(background=pick2)
        self.Zobo.config(background=pick2)
        self.Chivita.config(background=pick2)
        self.Chapman.config(background=pick2)
        self.Bottled_Water.config(background=pick2)
        self.Shawarma.config(background=pick2)
        self.Pop_Corn.config(background=pick2)
        self.Meat_Pie.config(background=pick2)
        self.Chicken_Pie.config(background=pick2)
        self.Pop_Corn.config(background=pick2)
        self.Doughnut.config(background=pick2)
        #=========Tempoary Labels==========    
        self.btnrefresh.config(bg=pick2)              
        #=======================Function calling Calculator====================
    def Calc(self):
        self.newWindow = Toplevel(self.master)
        self.app = Calculator(self.newWindow) 
        #=======================Function calling Record Window==================
    def Rec(self):
        self.newWindow = Toplevel(self.master)
        self.app = Record(self.newWindow) 
        #=======================Function calling About Window==================
    def about_us(self):
        self.newWindow = Toplevel(self.master)
        self.app = About(self.newWindow)        
              
#==================Class Window for Calculator=======================        
class Calculator:   
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry('480x380')
        self.master.resizable(False,False)
        self.frame3 = Frame(self.master)
        self.frame3.configure(background='pale green')
        self.frame3.pack()
        
        self.title = Frame(self.frame3,bd=10,pady=5,bg='green',relief=SUNKEN)
        self.title.pack(side=TOP,fill=X)
        
        self.cal = Frame(self.frame3,bd=10,pady=5,bg='pale green',relief=GROOVE)
        self.cal.pack(side=BOTTOM,fill=BOTH)       
        
        self.info = Label(self.title,text="Calculator",font=('arial',25,'bold'),bg='green',fg='black',bd=20)
        self.info.pack(fill=X)
        #============================CALCULATOR DISPLAY==================================       
        
        def btnClick(numbers):
            global operator
            operator = operator + str(numbers)
            text_Input.set(operator)
    
        def btnClearDisplay():
            global operator
            operator = ""
            text_Input.set("")
    
        def btnEquals():
            global operator
            sum_up = str(eval(operator))
            text_Input.set(sum_up)
            operator = ""                     
             
        txtDisplay = Entry(self.cal,font=('arial',12,'bold'),textvariable=text_Input,width=45, bg="light gray",bd=4,justify='right')
        txtDisplay.grid(row=0, column=0,columnspan=4)
        txtDisplay.insert(0,"0")
        #=============================CALCULATOR BUTTONS============================
        #-----------------------------------ROW 2--------------------------------------
        btn7 =  Button(self.cal,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),
                       width=4,text="7",bg="white",command=lambda:btnClick(7)).grid(row=2,column=0)
        btn8 =  Button(self.cal,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),
                       width=4,text="8",bg="white",command=lambda:btnClick(8)).grid(row=2,column=1)
        btn9 =  Button(self.cal,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),
                       width=4,text="9",bg="white",command=lambda:btnClick(9)).grid(row=2,column=2)
        btnAdd =  Button(self.cal,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),
                       width=4,text="+",bg="white",command=lambda:btnClick("+")).grid(row=2,column=3)
        #-----------------------------------ROW 3----------------------------------------
        btn4 =  Button(self.cal,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),
                      width=4,text="4",command=lambda:btnClick(4)).grid(row=3,column=0)
        btn5 =  Button(self.cal,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),
                      width=4,text="5",command=lambda:btnClick(5)).grid(row=3,column=1)
        btn6 =  Button(self.cal,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),
                       width=4,text="6",command=lambda:btnClick(6)).grid(row=3,column=2)
        btnSub =  Button(self.cal,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),
                       width=4,text="-",bg="white",command=lambda:btnClick("-")).grid(row=3,column=3)
        #-----------------------------------ROW 4----------------------------------------
        btn1 =  Button(self.cal,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),
                       width=4,text="1",bg="white",command=lambda:btnClick(1)).grid(row=4,column=0)
        btn2 =  Button(self.cal,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),
                       width=4,text="2",bg="white",command=lambda:btnClick(2)).grid(row=4,column=1)
        btn3 =  Button(self.cal,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),
                       width=4,text="3",bg="white",command=lambda:btnClick(3)).grid(row=4,column=2)
        btnMult =  Button(self.cal,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),
                      width=4,text="x",bg="white",command=lambda:btnClick("*")).grid(row=4,column=3)
        #-----------------------------------ROW 5---------------------------------------
        btn0 =  Button(self.cal,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),
                       width=4,text="0",command=lambda:btnClick(0)).grid(row=5,column=0)
        btnClear =  Button(self.cal,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),
                       width=4,text="C",command=btnClearDisplay).grid(row=5,column=1)
        btnEquals =  Button(self.cal,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),
                       width=4,text="=",command=btnEquals).grid(row=5,column=2)
        btnDiv =  Button(self.cal,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),
                       width=4,text="/",bg="white",command=lambda:btnClick("/")).grid(row=5,column=3)      

                
class Record: 
    def __init__(self, master):
        self.master = master
        self.master.title("Sales Record")
        self.master.geometry('800x700')
        self.master.resizable(False,False)
        self.master.configure(background='green')
        
        date = StringVar()
        date.set("")
        item = []
        prices = []
        times = []
        
        self.tops = Frame(self.master,bd=5,width=800,height=110,bg='green',relief=SUNKEN)
        self.tops.place(x=150,y=0)
        
        lblinfo = Label(self.tops,text="Enter a Date To Check Records",font=('arial',12,'bold'),bg='green',fg='black')
        lblinfo.grid(row=0,column=0,sticky=W)
        
        txtdate = Entry(self.tops,font=('arial',10),bg='white',justify=RIGHT,textvariable=date,bd=8)
        txtdate.grid(row=0,column=1)
        txtdate.focus()    
        
        self.bottom = Frame(self.master,bd=5,width=800,height=700,bg='white',relief=RAISED)
        self.bottom.place(x=0,y=50)
                
        def search():
          
            try:
                form_at = datetime.datetime.strptime(date.get(), "%Y-%m-%d")
            
                try:
                    conn = sqlite3.connect(r"C:\Users\DAVID ODEN\Desktop\Restaurant Management System\database\records.db")
                    c = conn.cursor()              
                     
                    c.execute("SELECT `items` FROM `sales_records` WHERE `date` = '"+date.get()+"';")
                    result1 = c.fetchall()
                    for a in result1:
                        item.append(a[0])
                    
                    c.execute("SELECT `price` FROM `sales_records` WHERE `date` = '"+date.get()+"';")
                    result2 = c.fetchall()
                    for b in result2:
                        prices.append(b[0])
                    
                    c.execute("SELECT `time` FROM `sales_records` WHERE `date` = '"+date.get()+"';")
                    result3 = c.fetchall()
                    for d in result3:
                        times.append(d[0])
                 
                    self.y_axis = 20
                    self.counter = 0
                    self.index = 1
                    for p in item:
                        self.lblitems = Label(self.bottom,text ="Items",font=('arial',12,'bold'),bg='white')
                        self.lblitems.place(x=100,y=0)
                        
                        self.lblqty = Label(self.bottom,text ="Price",font=('arial',12,'bold'),bg='white')
                        self.lblqty.place(x=600,y=0)
                        
                        self.lblprice = Label(self.bottom,text ="Time",font=('arial',12,'bold'),bg='white')
                        self.lblprice.place(x=700,y=0) 
                        
                        self.temp_item = Label(self.bottom,text=""+str(self.index)+"."+str(item[self.counter]),font=('arial',11),bg='white')
                        self.temp_item.place(x=5,y=self.y_axis)
                        
                        self.temp_qty = Label(self.bottom,text=str(prices[self.counter]),font=('arial',11),bg='white')
                        self.temp_qty.place(x=600,y=self.y_axis)
                        
                        self.temp_price = Label(self.bottom,text=str(times[self.counter]),font=('arial',11),bg='white')
                        self.temp_price.place(x=700,y=self.y_axis)        
                        
                        self.y_axis += 20
                        self.counter += 1
                        self.index += 1
                    db.commit()
                    db.close()     
                except:
                    tkinter.messagebox.showerror("Error","Error in Connection!")                 
            except:
                tkinter.messagebox.showerror("Error","Wrong Date Format!\n Date Format Should Be year-month-day \n For Example 2019-04-12 ")                  
                      
    

        def clear():
            date.set("")
            txtRecords.delete('1.0',END)

        btnsearch = Button(self.tops,bd=3,fg="black",font=('arial',10,'bold'),
                          width=5,text="Search",padx=3,bg="pale green",command=search).grid(row=0,column=2,sticky=E)
        btnclear = Button(self.tops,bd=3,fg="black",font=('arial',10,'bold'),
                          width=5,text="Clear",padx=3,bg="pale green",command=clear).grid(row=0,column=3,sticky=E)        
        
#=================About Window==================        
class About:
    def __init__(self, about):
        self.about = about
        self.about.title("About us")
        self.about.geometry('650x480')
        self.about.resizable(False,False)
        
        self.frame1 = Frame(self.about,bd=5,relief=SUNKEN)
        self.frame1.pack(side=TOP)
        
        self.photo = PhotoImage(file="RMS.png")
        self.lblAbout = Label(self.frame1,image = self.photo)
        self.lblAbout.pack()
        
        self.frame2 = Frame(self.about,bd=5,bg='green',relief=RAISED)
        self.frame2.pack(side=BOTTOM,fill=X)
        
        self.info = Label(self.frame2,text="Product: Restaurant Management System\n\
                                            Version: 1.0.1\n\
                                            Release Type: Limited Edition\n\
                                            Release Date: July 1, 2019\n\
                                            OS: Cross Platform\n\
                                            GUI Toolkit: Tkinter\n\
                                            Retained Updates: None\n\
                                            Phone number: 08154549452",font=('arial',11),fg='white',bg='green',justify=CENTER)
        self.info.grid(row=0,column=1)
        
        
        
        
if __name__=='__main__':
    root = Tk() 
    
    text_Input = StringVar()
    operator="" 
    
    app = Window2(root)
    root.mainloop()
           