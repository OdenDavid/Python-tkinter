from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect(r"C:\Users\DAVID ODEN\Desktop\Restaurant Management System\database\records.db")
c = conn.cursor() 


class add_to_database:
    def __init__(self,master):
        
        self.master = master
        self.master.title("Update Database")
        self.master.resizable(False,False)
        self.master.configure(background='dark slate gray')
        self.master.geometry('1000x600')
        #====================Top Frame=================================
        self.photo1 = PhotoImage(file="settings.png")
        self.set1 = Label(self.master,image=self.photo1,bg='dark slate gray')
        self.set1.place(x=50,y=5)
        
        self.top_frame = Frame(self.master,bd=5,width=500,height=100,relief=GROOVE,bg='dark green')
        self.top_frame.place(x=250,y=0)
        
        self.title = Label(self.master,text="Update Records",font=('onyx',40,'bold'),bg='dark green')
        self.title.place(x=400,y=20)
        
        self.photo2 = PhotoImage(file="settings.png")
        self.set2 = Label(self.master,image=self.photo2,bg='dark slate gray')
        self.set2.place(x=850,y=5)        
        
        #=======================Middle Frame==============================
        self.middle_frame = Frame(self.master,bd=5,width=1000,height=100,relief=GROOVE,bg='dark slate gray')
        self.middle_frame.place(x=0,y=100)
        
        self.item_lbl = Label(self.master,text="Enter Product Name",font=('onyx',25,'bold'),bg='dark slate gray')
        self.item_lbl.place(x=15,y=120)
        
        self.item_ent = Entry(self.master,font=('arial',20,'bold'),bd=3,width=30)
        self.item_ent.place(x=250,y=120)
        self.item_ent.focus()
        
        self.search = Button(self.master,text="Search",font=('onyx',15,'bold'),bg='dark green',width=15,command=self.search_item)
        self.search.place(x=760,y=120)
        
        #=======================Bottom Frame==============================
        self.down_frame = Frame(self.master,bd=5,width=930,height=400,relief=GROOVE,bg='dark green')
        self.down_frame.place(x=30,y=200)
        #============Stocks================
        self.stocks_lbl = Label(self.master,text="Stocks",font=('onyx',25,'bold'),bg='dark green')
        self.stocks_lbl.place(x=70,y=250)
        self.stocks_imp = Label(self.master,text="*",font=('arial',20,'bold'),bg='dark green',fg='red')
        self.stocks_imp.place(x=140,y=250)        
        self.stocks_ent = Entry(self.master,font=('arial',20,'bold'),bd=3,width=10)
        self.stocks_ent.place(x=240,y=250) 
        #============Cost Price================
        self.cp_lbl = Label(self.master,text="Cost Price",font=('onyx',25,'bold'),bg='dark green')
        self.cp_lbl.place(x=70,y=350)
        self.cp_imp = Label(self.master,text="*",font=('arial',20,'bold'),bg='dark green',fg='red')
        self.cp_imp.place(x=170,y=350)        
        self.cp_ent = Entry(self.master,font=('arial',20,'bold'),bd=3,width=10)
        self.cp_ent.place(x=240,y=350) 
        
        #============Vendor Name================
        self.vn_lbl = Label(self.master,text="Category Name",font=('onyx',25,'bold'),bg='dark green')
        self.vn_lbl.place(x=550,y=250)
        self.vn_ent = Entry(self.master,font=('arial',20,'bold'),bd=3,width=10)
        self.vn_ent.place(x=770,y=250) 
        #============Selling Price================
        self.sp_lbl = Label(self.master,text="Selling Price",font=('onyx',25,'bold'),bg='dark green')
        self.sp_lbl.place(x=550,y=350)
        self.sp_imp = Label(self.master,text="*",font=('arial',20,'bold'),bg='dark green',fg='red')
        self.sp_imp.place(x=670,y=350)          
        self.sp_ent = Entry(self.master,font=('arial',20,'bold'),bd=3,width=10)
        self.sp_ent.place(x=770,y=350) 
        #=============Button to Clear Entries================ 
        self.clear_btn = Button(self.master,text="Reset",font=('onyx',15,'bold'),bg='dark slate gray',width=18,command=self.clear)
        self.clear_btn.place(x=70,y=530)         
        #=============Button to Add to Database================  
        self.save_btn = Button(self.master,text="Save",font=('onyx',15,'bold'),bg='dark slate gray',width=18,command=self.save)
        self.save_btn.place(x=770,y=530) 
         
        
    def save(self):
        self.item = (str(self.item_ent.get())).lower() #Product Name
        self.stocks = self.stocks_ent.get() #Stock
        self.cp = self.cp_ent.get() #Cost Price
        self.vn = self.vn_ent.get() #Vendors Name
        self.sp = self.sp_ent.get() #Selling Price
        #=======Dynamic Entries=========
        self.tcp = float(self.cp) * float(self.stocks) #Total Cost Price
        self.tsp = float(self.sp) * float(self.stocks) #Total Selling Price
        if self.item == '' or self.stocks == '' or self.cp == '' or self.sp == '':
            tkinter.messagebox.showerror("Error","Couldn't Save\n Specify Stock, Cost Price and Selling Price")
        else:             
            sql = "INSERT INTO stock_records (Product_Name, Stock, Cost_Price, Selling_Price, Total_Cost_Price, Total_Selling_Price, Vendors_Name) VALUES(?,?,?,?,?,?,?)"
            c.execute(sql, (self.item, self.stocks, self.cp, self.sp, self.tcp, self.tsp, self.vn))
            conn.commit()
            tkinter.messagebox.showinfo("Successfull","Saved Successfully")
    
    def update(self):
        self.u0 = (str(self.item_ent.get())).lower() #Product Name
        self.u1 = self.stocks_ent.get() #Stock
        self.u2 = self.cp_ent.get() #Cost Price
        self.u3 = self.sp_ent.get() #Selling Price
        self.u4 = self.tcp_ent.get() #Total Cost Price
        self.u5 = self.tsp_ent.get() #Total Selling Price
        self.u6 = self.vn_ent.get() #Vendors Name
             
        sql = "UPDATE stock_records SET Stock=?, Cost_Price=?, Selling_Price=?,Total_Cost_Price=?, Total_Selling_Price=?, Vendors_Name=? WHERE Product_Name=?"
        c.execute(sql, (self.u1, self.u2, self.u3, self.u4, self.u5, self.u6,self.u0))
        conn.commit()
        tkinter.messagebox.showinfo("Successfull","Records Updated Successfully")
        
    def search_item(self):
        try:
            self.r0 = (str(self.item_ent.get())).lower() #Product Name
                     
            sql = "SELECT * FROM stock_records WHERE Product_Name=?"
            result = c.execute(sql, (self.r0, ))
            for i in result:
                self.r1 = i[1] #Stock
                self.r2 = i[2] #Cost Price
                self.r3 = i[3] #Selling Price
                self.r4 = i[4] #Total Cost Price
                self.r5 = i[5] #Total Selling Price
                self.r6 = i[6] #Vendors Name
            conn.commit()
            #============Total Cost Price================
            self.tcp_lbl = Label(self.master,text="Total Cost Price",font=('onyx',25,'bold'),bg='dark green')
            self.tcp_lbl.place(x=70,y=450)
            self.tcp_ent = Entry(self.master,font=('arial',20,'bold'),bd=3,width=10)
            self.tcp_ent.place(x=240,y=450)         
            #============Total Selling Price================
            self.tsp_lbl = Label(self.master,text="Total Selling Price",font=('onyx',25,'bold'),bg='dark green')
            self.tsp_lbl.place(x=550,y=450)
            self.tsp_ent = Entry(self.master,font=('arial',20,'bold'),bd=3,width=10)
            self.tsp_ent.place(x=770,y=450)         
            #===========Insert Results Into Entries============
            #Stock
            self.stocks_ent.delete(0, END)
            self.stocks_ent.insert(0, str(self.r1))
            #Cost Price
            self.cp_ent.delete(0, END)
            self.cp_ent.insert(0, str(self.r2))
            #Selling Price
            self.sp_ent.delete(0, END)
            self.sp_ent.insert(0, str(self.r3))
            #Total Cost Price
            self.tcp_ent.delete(0, END)
            self.tcp_ent.insert(0, str(self.r4))
            #Total Selling Price
            self.tsp_ent.delete(0, END)
            self.tsp_ent.insert(0, str(self.r5))
            #Vendors Name
            self.vn_ent.delete(0, END)
            self.vn_ent.insert(0, str(self.r6))
            #=============Button to Update to Database================  
            self.save_btn.place_forget()
            self.update_btn = Button(self.master,text="Update",font=('onyx',15,'bold'),bg='dark slate gray',width=18,command=self.update)
            self.update_btn.place(x=770,y=530)                    
        except:
            tkinter.messagebox.showinfo("Error","No Such Item in the Items List")
                
    def clear(self):
        self.item_ent.delete(0, END)
        self.item_ent.focus() 
        self.stocks_ent.delete(0, END)
        self.cp_ent.delete(0, END)
        self.vn_ent.delete(0, END)
        self.sp_ent.delete(0, END)
        self.tcp_ent.delete(0, END)
        self.tsp_ent.delete(0, END)
        self.tcp_ent.place_forget()
        self.tsp_ent.place_forget()       
        self.tcp_lbl.place_forget()
        self.tsp_lbl.place_forget()
        self.update_btn.place_forget()
        self.save_btn.place(x=770,y=530)
            
if __name__=='__main__':
    root = Tk()  
    app = add_to_database(root)
    root.mainloop()