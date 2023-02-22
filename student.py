from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x780+0+0")
        self.root.title("Face Recognition System")



        #=============variables=============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        #1st Image

        img=Image.open(r"C:\Users\shreyas yadav\OneDrive\Desktop\Facial_Recognition_System-main\Images\face-recognition.png")
        img=img.resize((550,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=516.66,height=130)

#2nd Image

        img1=Image.open(r"C:\Users\shreyas yadav\OneDrive\Desktop\Facial_Recognition_System-main\Images\smart-attendance.jpg")
        img1=img1.resize((515,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=515,height=130)

#3rd Image

        img2=Image.open(r"C:\Users\shreyas yadav\OneDrive\Desktop\Facial_Recognition_System-main\Images\iStock-182059956_18390_t12.jpg")
        img2=img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

#BG Image

        img3=Image.open(r"C:\Users\shreyas yadav\OneDrive\Desktop\Facial_Recognition_System-main\Images\wp2551980.jpg")
        img3=img3.resize((1550,680),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1550,height=680)

#Title

        title_lbl=Label(bg_img,text="STUDENT  MANAGEMENT  SYSTEM", font=("coolvetica",35,"bold"),
                        bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)


#Frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=50,width=1520,height=620)
        
#Left Label Frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",
                              font=("coolvetica",12,"bold"))
        Left_frame.place(x=15,y=5,width=740,height=600)


        img_left=Image.open(r"C:\Users\shreyas yadav\OneDrive\Desktop\Facial_Recognition_System-main\Images\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((730,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=3,y=0,width=730,height=130) 


#Current Course Frame

        CC_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",
                              font=("coolvetica",12,"bold"))
        CC_frame.place(x=3,y=135,width=730,height=110)

#Departhment
        
        dep_label=Label(CC_frame,text="Department :",font=("coolvetica",12,"bold"),bg="white",justify=LEFT)
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(CC_frame,textvariable=self.var_dep,font=("Times New Roman",10,"bold"),width=20,state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

#Course
        
        course_label=Label(CC_frame,text="Course :",font=("coolvetica",12,"bold"),bg="white",justify=LEFT)
        course_label.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(CC_frame,textvariable=self.var_course,font=("Times New Roman",10,"bold"),width=20,state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


#Year
        
        year_label=Label(CC_frame,text="Year :",font=("coolvetica",12,"bold"),bg="white",justify=LEFT)
        year_label.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(CC_frame,textvariable=self.var_year,font=("Times New Roman",10,"bold"),width=20,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

#Semester
        
        semester_label=Label(CC_frame,text="Semester :",font=("coolvetica",12,"bold"),bg="white",justify=LEFT)
        semester_label.grid(row=1,column=2,padx=10)

        semester_combo=ttk.Combobox(CC_frame,textvariable=self.var_semester,font=("Times New Roman",10,"bold"),width=20,state="readonly")
        semester_combo["values"]=("Select Semester","Semester 1","Semester 2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


#Class Student Information Frame

        CS_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",
                              font=("coolvetica",12,"bold"))
        CS_frame.place(x=3,y=250,width=730,height=325)

#Student ID

        studentID_label=Label(CS_frame,text="Student ID :",font=("coolvetica",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        
        studentID_entry=ttk.Entry(CS_frame,textvariable=self.var_std_id,width=20,font=("coolvetica",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

#Student Name

        studentName_label=Label(CS_frame,text="Student Name :",font=("coolvetica",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentName_entry=ttk.Entry(CS_frame,textvariable=self.var_std_name,width=20,font=("coolvetica",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


#Class Division

        class_div_label=Label(CS_frame,text="Class Division :",font=("coolvetica",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        #class_div_entry=ttk.Entry(CS_frame,textvariable=self.var_div,width=20,font=("coolvetica",12,"bold"))
        #class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(CS_frame,textvariable=self.var_div,font=("Times New Roman",10,"bold"),width=20,state="readonly")
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


#Roll No.

        roll_no_label=Label(CS_frame,text="Roll No :",font=("coolvetica",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(CS_frame,textvariable=self.var_roll,width=20,font=("coolvetica",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


#Gender

        gender_div_label=Label(CS_frame,text="Gender :",font=("coolvetica",12,"bold"),bg="white")
        gender_div_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        #gender_div_entry=ttk.Entry(CS_frame,textvariable=self.var_gender,width=20,font=("coolvetica",12,"bold"))
        #gender_div_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        gender_combo=ttk.Combobox(CS_frame,textvariable=self.var_gender,font=("Times New Roman",13,"bold"),width=18,state="readonly")
        gender_combo["values"]=("Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


#Date Of Birth

        dob_label=Label(CS_frame,text="DOB :",font=("coolvetica",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(CS_frame,textvariable=self.var_dob,dwidth=20,font=("coolvetica",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)


#Email

        email_label=Label(CS_frame,text="Email :",font=("coolvetica",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(CS_frame,textvariable=self.var_email,width=20,font=("coolvetica",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

#Phone No.

        phone_no_label=Label(CS_frame,text="Phone No :",font=("coolvetica",12,"bold"),bg="white")
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_no_entry=ttk.Entry(CS_frame,textvariable=self.var_phone,width=20,font=("coolvetica",12,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

#Address

        address_label=Label(CS_frame,text="Address :",font=("coolvetica",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(CS_frame,textvariable=self.var_address,width=20,font=("coolvetica",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=10,sticky=W)

#Teacher's Name

        teacher_label=Label(CS_frame,text="Teacher's Name :",font=("coolvetica",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(CS_frame,textvariable=self.var_teacher,width=20,font=("coolvetica",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=10,sticky=W)

#Radio Buttons
        
        radiobtn1=ttk.Radiobutton(CS_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(CS_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

#Button Frame
        
        btn_frame=Frame(CS_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=230,width=725,height=35)

#Save Button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("coolvetica",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

#Update Button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("coolvetica",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

#Delete Button
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("coolvetica",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

#Reset Button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("coolvetica",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

#Button Frame 2
        
        btn_frame2=Frame(CS_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame2.place(x=0,y=267,width=725,height=35)

#Take Photo Sample Button
        take_photo_btn=Button(btn_frame2,text="Take Photo Sample",width=35,font=("coolvetica",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

#Update Photo Sample Button
        update_photo_btn=Button(btn_frame2,text="Update Photo Sample",width=35,font=("coolvetica",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)




#Right Label Frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",
                              font=("coolvetica",12,"bold"))
        Right_frame.place(x=760,y=5,width=740,height=600)


        img_right=Image.open(r"C:\Users\shreyas yadav\OneDrive\Desktop\Facial_Recognition_System-main\Images\gettyimages-1022573162.jpg")
        img_right=img_right.resize((730,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)


        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=3,y=0,width=730,height=130) 


# >>>>>>>>>>>Search System<<<<<<<<<<<<<

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",
                              font=("coolvetica",12,"bold"))
        Search_frame.place(x=3,y=135,width=730,height=70)

        search_label=Label(Search_frame,text="Search By :",font=("coolvetica",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("Times New Roman",10,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","Roll Number","Phone Number")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        search_entry=ttk.Entry(Search_frame,width=15,font=("coolvetica",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        
        search_btn=Button(Search_frame,text="Search",width=12,font=("coolvetica",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(Search_frame,text="Show All",width=12,font=("coolvetica",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)
        

#Table Frame
    
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=3,y=210,width=730,height=365)



        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender",
                                                            "dob","email","phone","address","teacher","photo"),
                                                            xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teaccher")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=120)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

     #================function decaration===================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required", parent=self.root)
        else:
            try:  
                conn=mysql.connector.connect(host="localhost",userame="root",password="Admin@123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                                self.var_dep.get(), 
                                                                                                                                self.var_course.get(),
                                                                                                                                self.var_year.get(),
                                                                                                                                self.var_semester.get(),
                                                                                                                                self.var_std_id.get(),
                                                                                                                                self.var_std_name.get(),
                                                                                                                                self.var_div.get(),
                                                                                                                                self.var_roll.get(),
                                                                                                                                self.var_gender.get(),
                                                                                                                                self.var_dob.get(),
                                                                                                                                self.var_email.get(),
                                                                                                                                self.var_phone.get(),
                                                                                                                                self.var_address.get(),
                                                                                                                                self.var_teacher.get(),
                                                                                                                                self.var_radio1.get()
                                                                                                                     ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been addedSuccessfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due T : {str(es)}",parent=self.root)                                                                                        
                

      #=================fetch data=============================== 
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",userame="root",password="Admin@123",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END, values=i)  
            conn.commit()
        conn.close()                 

#===========================get cursor=========================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus) 
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root) 
                if Update>0:
                   conn=mysql.connector.connect(host="localhost",userame="root",password="Admin@123",database="face_recognizer")
                   my_cursor=conn.cursor()
                   my_cursor.execute("Update student set Dep=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                         
                                                                                                                                                                          self.var_dep.get(),
                                                                                                                                                                          self.var_course.get(),
                                                                                                                                                                          self.var_year.get(),
                                                                                                                                                                          self.var_semester.get(),
                                                                                                                                                                          self.var_std_name.get(),
                                                                                                                                                                          self.var_div.get(),
                                                                                                                                                                          self.var_roll.get(),
                                                                                                                                                                          self.var_gender.get(),
                                                                                                                                                                          self.var_dob.get(),
                                                                                                                                                                          self.var_email.get(),
                                                                                                                                                                          self.var_phone.get(),
                                                                                                                                                                          self.var_address.get(),
                                                                                                                                                                          self.var_teacher.get(),
                                                                                                                                                                          self.var_radio1.get(),
                                                                                                                                                                          self.var_std_id.get()                              
                                                                                                                                                                                                                  
                                                                                                                                      
                                                                                                                     
                                                                                                       ))
                else:
                    if not Update:
                        return
                messagebox.howinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close() 
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)      

        #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
                messagebox.showerror("Error","Student id must be required", parent=self.root)
        else:
                try:
                        delete=messagebox.askyesno("Student Delete Page", "Do you want to delete this Student",parent=self.root)
                        if delete>0:
                            conn=mysql.connector.connect(host="localhost",userame="root",password="Admin@123",database="face_recognizer")
                            my_cursor=conn.cursor() 
                            sql="delete from where student_id=%s"
                            val=(self.var_std_id.get(),) 
                            my_cursor.execute(sql,val)
                        else:
                                if not delete:
                                        return
                        conn.commit()
                        self.fetch_data()
                        conn.close() 
                        messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)  
                except Exception as es:
                        messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)            


    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course"),
        self.var_year.set("Selecy Year"),
        self.var_semester.set("Select Semister"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")


    # ============Generate data set Take photo samples=================================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",userame="root",password="Admin@123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                        id+=1
                my_cursor.execute("Update student set Dep=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                         
                                                                                                                                                                          self.var_dep.get(),
                                                                                                                                                                          self.var_course.get(),
                                                                                                                                                                          self.var_year.get(),
                                                                                                                                                                          self.var_semester.get(),
                                                                                                                                                                          self.var_std_name.get(),
                                                                                                                                                                          self.var_div.get(),
                                                                                                                                                                          self.var_roll.get(),
                                                                                                                                                                          self.var_gender.get(),
                                                                                                                                                                          self.var_dob.get(),
                                                                                                                                                                          self.var_email.get(),
                                                                                                                                                                          self.var_phone.get(),
                                                                                                                                                                          self.var_address.get(),
                                                                                                                                                                          self.var_teacher.get(),
                                                                                                                                                                          self.var_radio1.get(),
                                                                                                                                                                          self.var_std_id.get()                              
                                                                                                                                                                                                                  
                                                                                                                                      
                                                                                                                     
                                                                                                       ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()                                                                                            








           











if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()