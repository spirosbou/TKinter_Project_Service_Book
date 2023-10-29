import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo



class windows(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Service Book")
        
        container = tk.Frame(self, height=400, width=600, bg='#808080')
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (LoginPage, SingUpPage, UserDetails, UserPage, ExitPage):
            frame = F(container, self)
            
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="news")
            
        self.show_frame(LoginPage)
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()
        
        
class LoginPage(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="User Login", font=("Arial",20))
        label.place(x=180, y=53)
        
        user_name = StringVar()
        username_label = tk.Label(self, text="Username", font=("Arial",12))
        username_entry = tk.Entry(self, textvariable=user_name)
        username_label.place(x=80, y=130)
        username_entry.place(x=200, y=130)
        password = StringVar()
        password_label = tk.Label(self, text="Password", font=("Arial",12))
        password_entry = tk.Entry(self, textvariable=password, show="*")
        password_label.place(x=80, y=180)
        password_entry.place(x=200, y=180)
        
        login_button = tk.Button(
            self, text="Login", command=lambda: controller.show_frame(UserPage))
        login_button.place(x=180, y=280)
        singup_button = tk.Button(
            self, text="SingUp", command=lambda: controller.show_frame(UserDetails))
        singup_button.place(x=280, y=280)
        
        
        
class SingUpPage(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Sing up page")
        label.pack(padx=10, pady=10)
        
        switch_window_button = tk.Button(
            self, text="User Details", command= lambda: controller.show_frame(UserDetails))
        switch_window_button.pack(side="bottom", fill=tk.X)
        
        
class UserDetails(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Create your profile", font=("Arial",20))
        label.pack(padx=10, pady=10)
        
        username = StringVar()
        username_label = tk.Label(self, text="Username", font=("Arial", 12))
        username_entry = tk.Entry(self, textvariable=username)
        username_label.place(x=80, y=130)
        username_entry.place(x=200, y=130)
        password = StringVar()
        password_label = tk.Label(self, text="Password", font=("Arial", 12))
        password_entry = tk.Entry(self, textvariable=password, show="*")
        password_label.place(x=80, y=160)
        password_entry.place(x=200, y=160)
        email = StringVar()
        email_label = tk.Label(self, text="Email", font=("Arial", 12))
        email_entry = tk.Entry(self, textvariable=email)
        email_label.place(x=80, y= 190)
        email_entry.place(x=200, y=190)
        
        
        create_button = tk.Button(
            self, text="Create", command= lambda: controller.show_frame(LoginPage))
        create_button.place(x=300, y=400)
        cancel_button = tk.Button(
            self, text="Cancel", command= lambda: controller.show_frame(LoginPage))
        cancel_button.place(x=390, y=400)
        
    
class UserPage(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Profile", font=("Arial", 20))
        label.pack(padx=10, pady=10)
        
        bike_info = tk.Label(self, text='Bike Information', font=("Arial", 14))
        bike_info.place(x=30, y=35)

        bike_company = StringVar()
        bike_model = StringVar()
        bike_company_label= tk.Label(self, text='Company', font=("Arial", 10))
        bike_company_label.place(x=30, y=60)
        bike_model_label = tk.Label(self, text='Model', font=("Arial", 10))
        bike_model_label.place(x=30, y=90)

        bike_company_entry = tk.Entry(self, textvariable=bike_company)
        bike_company_entry.place(x=110, y=60)
        bike_model_entry = tk.Entry(self, textvariable=bike_model)
        bike_model_entry.place(x=110, y=90)
        
        bike_cm3 = StringVar()
        bike_cm3_label = tk.Label(self, text='cm3', font=("Arial", 10))
        bike_cm3_label.place(x=300, y=60)
        bike_cm3_entry = tk.Entry(self, textvariable=bike_cm3)
        bike_cm3_entry.place(x=350, y=60)
        
        model_year = StringVar()
        model_year_label = tk.Label(self, text='Year', font=("Arial", 10))
        model_year_label.place(x=300, y=90)
        model_year_entry = tk.Entry(self, textvariable=model_year)
        model_year_entry.place(x=350, y=90)


        service_details = tk.Label(self, text='Service Details', font=("Arial", 14))
        service_details.place(x=30, y=130)
        
        kilometers = StringVar()
        kilometers_label = tk.Label(self, text='Kilometers', font=("Arial", 10))
        kilometers_label.place(x=30, y=155)
        kilometers_entry = tk.Entry(self, textvariable=kilometers)
        kilometers_entry.place(x=100, y=155)
        oil_change = StringVar(value="Oil Change")
        oil_change_button = tk.Checkbutton(self, text='Oil Change',font=("Arial",10),textvariable=oil_change, onvalue='Yes', offvalue='No')
        oil_change_button.place(x=30, y=180)
        filter_oil = StringVar(value="Oil Filter")
        filter_oil = tk.Checkbutton(self, text='Oil Filter',font=("Arial",10), textvariable=filter_oil, onvalue='Yes', offvalue='No')
        filter_oil.place(x=30, y=205)
        filter_gas = StringVar(value="Gas Filter")
        filter_gas = tk.Checkbutton(self, text='Gas Filter',font=("Arial",10), textvariable=filter_gas, onvalue='Yes', offvalue='No')
        filter_gas.place(x=30, y=230)
        filter_air = StringVar(value="Air Filter")
        filter_air = tk.Checkbutton(self, text='Air Filter',font=("Arial",10),textvariable=filter_air, onvalue='Yes', offvalue='No')
        filter_air.place(x=30, y=255)
        front_break = StringVar(value="Front Break")
        front_break = tk.Checkbutton(self, text='Front Breaks',font=("Arial",10),textvariable=front_break,onvalue='Yes',offvalue='No')
        front_break.place(x=150, y=180)
        rear_break = StringVar(value="Rear Break")
        rear_break = tk.Checkbutton(self, text='Rear Breaks',font=("Arial",10),textvariable=rear_break,onvalue='Yes',offvalue='No')
        rear_break.place(x=150, y=205)
        front_tire = StringVar(value="Front Tire")
        front_tire = tk.Checkbutton(self, text='Front Tire',font=("Arial",10),textvariable=front_tire,onvalue='Yes',offvalue='No')
        front_tire.place(x=150, y=230)
        rear_tire = StringVar(value="Rear Tire")
        rear_tire = tk.Checkbutton(self, text='Rear Tire',font=("Arial",10),textvariable=rear_tire,onvalue='Yes',offvalue='No')
        rear_tire.place(x=150, y=255)
        chain = StringVar(value="Transm/Chain")
        chain = tk.Checkbutton(self, text='Transmission chain',font=("Arial",10),textvariable=chain,onvalue='Yes',offvalue='No')
        chain.place(x=270, y=180)

        front_susp_oil = StringVar(value="Front/Susp/Oil")
        front_susp_oil = tk.Checkbutton(self, text="Front/Susp/Oil",font=("Arial",10),textvariable=front_susp_oil,onvalue='Yes',offvalue='No')
        front_susp_oil.place(x=270, y=205)
        front_susp_spring = StringVar(value="Front/Susp/Spring")
        front_susp_spring = tk.Checkbutton(self, text="Front/Susp/Spring",font=("Arial",10),textvariable=front_susp_spring,onvalue='Yes',offvalue='No')
        front_susp_spring.place(x=270, y=230)
        rear_susp_oil = StringVar(value="Rear/Susp/Oil")
        rear_susp_oil = tk.Checkbutton(self, text="Rear/Susp/Oil",font=("Arial",10),textvariable=rear_susp_oil,onvalue='Yes',offvalue='No')
        rear_susp_oil.place(x=410, y=180)
        rear_susp_spring = StringVar(value="Rear/Susp/Spring")
        rear_susp_spring = tk.Checkbutton(self, text="Rear/Susp/Spring",font=("Arial",10),textvariable=rear_susp_spring,onvalue='Yes',offvalue='No')
        rear_susp_spring.place(x=410, y=205)
        
        comments = StringVar()
        comments_label = tk.Label(self, text="Comments", font=("Arial", 12))
        comments_label.place(x=30, y=290)
        comments_entry = tk.Text(self, height=8, width=65, borderwidth=3 )
        comments_entry.place(x=30, y=320)
         
        exit_button = tk.Button(
            self, text="Exit", command= lambda: controller.show_frame(ExitPage))
        exit_button.place(x=390, y=500)
        
class ExitPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Thank you", font=("Arial", 30))
        label.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        

if __name__ == "__main__":
    
    testobj = windows()
    testobj.mainloop()
        
        
        
        