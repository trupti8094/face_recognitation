from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x780+0+0")
        self.root.title("Face Recognition System")

#1st Image

        img=Image.open(r"C:\Users\shreyas yadav\OneDrive\Desktop\Facial_Recognition_System-main\Images\Stanford.jpg")
        img=img.resize((550,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=516.66,height=130)

#2nd Image

        img1=Image.open(r"C:\Users\shreyas yadav\OneDrive\Desktop\Facial_Recognition_System-main\Images\facialrecognition.png")
        img1=img1.resize((515,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=515,height=130)

#3rd Image

        img2=Image.open(r"C:\Users\shreyas yadav\OneDrive\Desktop\Facial_Recognition_System-main\Images\u.jpg")
        img2=img2.resize((550,130),Image.LANCZOS)
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

        title_lbl=Label(bg_img,text="FACE  RECOGNITION  ATTENDANCE  SYSTEM", font=("coolvetica",35,"bold"),
                        bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        

#Student Button
        
        img4=Image.open(r"C:\Users\shreyas yadav\OneDrive\Desktop\Facial_Recognition_System-main\Images\gettyimages-1022573162.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.Student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.Student_details,cursor="hand2",font=("coolvetica",15,"bold"),
                        bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


#Detect Face Button
        
        img5=Image.open(r"C:\Users\shreyas yadav\OneDrive\Desktop\Facial_Recognition_System-main\Images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b2.place(x=500,y=100,width=220,height=220)

        b2_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("coolvetica",15,"bold"),
                        bg="darkblue",fg="white")
        b2_1.place(x=500,y=300,width=220,height=40)


 #Attendance Button
        
        img6=Image.open(r"C:\Users\shreyas yadav\OneDrive\Desktop\Facial_Recognition_System-main\Images\report.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b3.place(x=800,y=100,width=220,height=220)

        b3_1=Button(bg_img,text="Attendance",cursor="hand2",font=("coolvetica",15,"bold"),
                        bg="darkblue",fg="white")
        b3_1.place(x=800,y=300,width=220,height=40)


#Help Button
        
        img7=Image.open(r"C:\Users\shreyas yadav\OneDrive\Desktop\Facial_Recognition_System-main\Images\help.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b4.place(x=1100,y=100,width=220,height=220)

        b4_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("coolvetica",15,"bold"),
                        bg="darkblue",fg="white")
        b4_1.place(x=1100,y=300,width=220,height=40)


 #Train Button
        
        img8=Image.open(r"C:\Users\shreyas yadav\OneDrive\Desktop\Facial_Recognition_System-main\Images\Train.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b5.place(x=200,y=380,width=220,height=220)

        b5_1=Button(bg_img,text="Train Data",cursor="hand2",font=("coolvetica",15,"bold"),
                        bg="darkblue",fg="white")
        b5_1.place(x=200,y=580,width=220,height=40)


#Photos Button
        
        img9=Image.open(r"C:\Users\shreyas yadav\OneDrive\Desktop\Facial_Recognition_System-main\Images\opencv_face_reco_more_data.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b6.place(x=500,y=380,width=220,height=220)

        b6_1=Button(bg_img,text="Photos",cursor="hand2",font=("coolvetica",15,"bold"),
                        bg="darkblue",fg="white")
        b6_1.place(x=500,y=580,width=220,height=40)

#Developer Button
        
        img10=Image.open(r"C:\Users\shreyas yadav\OneDrive\Desktop\Facial_Recognition_System-main\Images\Team-Management-Software-Development.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b7.place(x=800,y=380,width=220,height=220)

        b7_1=Button(bg_img,text="Developer",cursor="hand2",font=("coolvetica",15,"bold"),
                        bg="darkblue",fg="white")
        b7_1.place(x=800,y=580,width=220,height=40)

#Exit Button
        
        img11=Image.open(r"C:\Users\shreyas yadav\OneDrive\Desktop\Facial_Recognition_System-main\Images\exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b8.place(x=1100,y=380,width=220,height=220)

        b8_1=Button(bg_img,text="Exit",cursor="hand2",font=("coolvetica",15,"bold"),
                        bg="darkblue",fg="white")
        b8_1.place(x=1100,y=580,width=220,height=40)


#=====================================Functions buttons====================================================
def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()