from tkinter import *
from tkinter import ttk
import behind
import sqlite3


def add_data():
    behind.insert_data(examid_text.get(),name_text.get(),gender_var.get(),subject1_var.get(),subject2_var.get(),subject3_var.get(),subject4_var.get(),subject5_var.get(),subject6_var.get(),status_var.get())
    show_command()
    clear()

def show_command():
    student_table.delete(*student_table.get_children())
    for row in behind.view():
        student_table.insert('',END,values=row)    

def clear():
    examid_text.set("")
    name_text.set("")
    gender_var.set("")
    subject1_var.set("")
    subject2_var.set("")
    subject3_var.set("")
    subject4_var.set("")
    subject5_var.set("")
    subject6_var.set("")
    status_var.set("")

def get_selected_row(ev):
    global row
    cursor=student_table.focus()
    content=student_table.item(cursor)
    row=content["values"]
    examid_text.set(row[1])
    name_text.set(row[2])
    gender_var.set(row[3])
    subject1_var.set(row[4])
    subject2_var.set(row[5])
    subject3_var.set(row[6])
    subject4_var.set(row[7])
    subject5_var.set(row[8])
    subject6_var.set(row[9])
    status_var.set(row[10])


def delete_command():
    behind.remove(row[0])
    show_command()
    clear()

def search_command():
    conn=sqlite3.connect("stdetails.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM stdetail WHERE "+str(searchby_text.get())+" Like '%"+str(searchtxt_text.get())+"%'")
    rows=cur.fetchall()
    student_table.delete(*student_table.get_children())
    for row in rows: 
        student_table.insert('',END,values=row)  
        conn.commit()
    conn.close()

def update_data():
    behind.update(row[0],examid_text.get(),name_text.get(),gender_var.get(),subject1_var.get(),subject2_var.get(),subject3_var.get(),subject4_var.get(),subject5_var.get(),subject6_var.get(),status_var.get())
    show_command()

    

   


root=Tk()



root.title("STUDENT MANAGEMENT SYSTEM")
root.geometry("1350x700+0+0")

def scroll():
    global count,text
    if(count>=len("Student Mark Management")):
        count=0
        text=''
        title.config(text=text)
    else:
        text=text+"Student Mark Management"[count]
        title.config(text=text)
        count+=1
    title.after(350,scroll)

title=Label(root,text="Student Mark Management",bd=7,relief=GROOVE,font=("times new roman",30,"bold"),bg="aqua",fg="red")
title.pack(side=TOP,fill=X)
count=0
text=''
scroll()

#===========manage frames===============
manage_frame=Frame(root,bd=4,relief=RIDGE,bg="#00FF7F")
manage_frame.place(x=20,y=70,width=400,height=600)

# ============detail frames===============
detail_frame = Frame(root, bd=4, relief=RIDGE, bg="#00FF7F")
detail_frame.place(x=450, y=70, width=880, height=600)

m_title=Label(manage_frame,text="Manage student:",font=("times new roman",25,"bold"),fg="black",bg="#00FF7F")
m_title.grid(row=0,columnspan=2,pady=0)

lbl_id=Label(manage_frame,text="Exam ID :",font=("times new roman",18,"bold"),fg="darkblue",bg="#00FF7F")
lbl_id.grid(row=1,column=0,pady=8,padx=20,sticky="W")
examid_text=StringVar()
examid=Entry(manage_frame,textvariable=examid_text,font=("times new roman",12,"bold"),bd=2,relief=RIDGE)
examid.grid(row=1,column=1,pady=8,padx=20)

lbl_name=Label(manage_frame,text="Name      :",font=("times new roman",18,"bold"),fg="darkblue",bg="#00FF7F")
lbl_name.grid(row=2,column=0,padx=20,pady=8,sticky="W")

name_text=StringVar()
name=Entry(manage_frame,textvariable=name_text,bd=2,relief=RIDGE,font=("times new roman",12,"bold"))
name.grid(row=2,column=1,pady=8,padx=20)


lbl_gender = Label(manage_frame, text="Gender   :", font=("times new roman",18, "bold"), fg="darkblue", bg="#00FF7F")
lbl_gender.grid(row=3, column=0, pady=8, padx=20, sticky="W")

gender_var=StringVar()
combo_gender=ttk.Combobox(manage_frame,textvariable=gender_var,width=18,font=("times new roman",11,"bold"),state="readonly")
combo_gender['values']=("Male","Female","other")
combo_gender.grid(row=3,column=1,padx=20,pady=8)


lbl_subject1=Label(manage_frame,text="Subject 1:",font=("times new roman",18,"bold"),fg="darkblue",bg="#00FF7F")
lbl_subject1.grid(row=4,column=0,padx=20,pady=8,sticky="w")

subject1_var=StringVar()
subject1=Entry(manage_frame,textvariable=subject1_var,bd=2,relief=RIDGE,font=("times new roman",12,"bold"))
subject1.grid(row=4,column=1,pady=8,padx=20)


lbl_subject2=Label(manage_frame,text="Subject 2:",font=("times new roman",18,"bold"),fg="darkblue",bg="#00FF7F")
lbl_subject2.grid(row=5,column=0,padx=20,pady=8,sticky="w")

subject2_var=StringVar()
subject2=Entry(manage_frame,textvariable=subject2_var,bd=2,relief=RIDGE,font=("times new roman",12,"bold"))
subject2.grid(row=5,column=1,pady=8,padx=20)


lbl_subject3=Label(manage_frame,text="Subject 3:",font=("times new roman",18,"bold"),fg="darkblue",bg="#00FF7F")
lbl_subject3.grid(row=6,column=0,padx=20,pady=8,sticky="w")

subject3_var=StringVar()
subject3=Entry(manage_frame,textvariable=subject3_var,bd=2,relief=RIDGE,font=("times new roman",12,"bold"))
subject3.grid(row=6,column=1,pady=8,padx=20)


lbl_subject4=Label(manage_frame,text="Subject 4:",font=("times new roman",18,"bold"),fg="darkblue",bg="#00FF7F")
lbl_subject4.grid(row=7,column=0,padx=20,pady=8,sticky="w")

subject4_var=StringVar()
subject4=Entry(manage_frame,textvariable=subject4_var,bd=2,relief=RIDGE,font=("times new roman",12,"bold"))
subject4.grid(row=7,column=1,pady=8,padx=20)


lbl_subject5=Label(manage_frame,text="Subject 5:",font=("times new roman",18,"bold"),fg="darkblue",bg="#00FF7F")
lbl_subject5.grid(row=8,column=0,padx=20,pady=8,sticky="w")

subject5_var=StringVar()
subject5=Entry(manage_frame,textvariable=subject5_var,bd=2,relief=RIDGE,font=("times new roman",12,"bold"))
subject5.grid(row=8,column=1,pady=8,padx=20)


lbl_subject6=Label(manage_frame,text="Subject 6:",font=("times new roman",18,"bold"),fg="darkblue",bg="#00FF7F")
lbl_subject6.grid(row=9,column=0,padx=20,pady=8,sticky="w")

subject6_var=StringVar()
subject6=Entry(manage_frame,textvariable=subject6_var,bd=2,relief=RIDGE,font=("times new roman",12,"bold"))
subject6.grid(row=9,column=1,pady=8,padx=20)

lbl_status=Label(manage_frame,text="Status     :",font=("times new roman",18,"bold"),fg="darkblue",bg="#00FF7F")
lbl_status.grid(row=10,column=0,padx=20,pady=8,sticky="w")


status_var=StringVar()
combo_status=ttk.Combobox(manage_frame,textvariable=status_var,width=18,font=("times new roman",12,"bold"),state="readonly")
combo_status['values']=("PASS","FAIL")
combo_status.grid(row=10,column=1,pady=8,padx=20)


frame2=Frame(manage_frame,relief=GROOVE,bd=3,bg="sandybrown")
frame2.place(x=10,y=540,width=370,height=50)

btn1 = Button(frame2, text="Add",font=("times new roman", 12, "bold"), activeforeground="white",
                      activebackground="brown",command=add_data)
btn1.grid(row=9, column=0, padx=14, pady=2, ipadx=7, ipady=3)



btn2 = Button(frame2, text="Update", font=("times new roman", 12, "bold"), activeforeground="white",activebackground="brown",command=update_data).grid(row=9, column=1, padx=7, pady=2, ipadx=7, ipady=3)

btn3 = Button(frame2, text="Delete", font=("times new roman", 12, "bold"), activeforeground="white",activebackground="brown",command=delete_command).grid(row=9,column=2, padx=13, pady=2, ipadx=7, ipady=3)

btn4 = Button(frame2, text="Clear", font=("times new roman", 12, "bold"), activeforeground="white",activebackground="brown",command=clear).grid(row=9, column=3, padx=10, pady=2, ipadx=7, ipady=3)

lbl_search=Label(detail_frame,text="Search by:",font=("times new roman",20,"bold"),fg="black",bg="#00FF7F")
lbl_search.grid(row=0,column=0,padx=10,pady=10)

searchby_text=StringVar()
combo_search=ttk.Combobox(detail_frame,textvariable=searchby_text,font=("times new roman",15,"bold"),state="readonly")
combo_search['values']=("ExamId","Name","Status")
combo_search.grid(row=0,column=1,padx=15,pady=15,ipady=3)

searchtxt_text=StringVar()
searchtxt=Entry(detail_frame,textvariable=searchtxt_text,bd=4,font=("times new roman",13,"bold"))
searchtxt.grid(row=0,column=2,padx=8)

btn_search=Button(detail_frame,text="Search",command=search_command,font=("times new roman",12,"bold"),activebackground="crimson",activeforeground="white").grid(row=0,column=4,ipadx=30,padx=10,pady=10)

btn_showall = Button(detail_frame, text="Show all",command=show_command,font=("times new roman", 12, "bold"),
                            activebackground="crimson", activeforeground="white", padx=10,).grid(row=0,column=5,padx=10,pady=10,ipadx=12)

table_frame=Frame(detail_frame,bd=3,relief=GROOVE,bg="white")
table_frame.place(x=28,y=70,height=460,width=820)


scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
scroll_y = Scrollbar(table_frame, orient=VERTICAL)
student_table=ttk.Treeview(table_frame,columns=("no","examid","name","gender","subject1","subject2","subject3","subject4","subject5","subject6","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)
student_table.heading("no", text="No")
student_table.heading("examid", text="Exam ID")
student_table.heading("name", text="Name")
student_table.heading("gender", text="Gender")
student_table.heading("subject1",text="Subject1" )
student_table.heading("subject2",text="Subject2" )
student_table.heading("subject3",text="Subject3" )
student_table.heading("subject4",text="Subject4" )
student_table.heading("subject5", text="Subject5")
student_table.heading("subject6", text="Subject6")
student_table.heading("status", text="Status")
student_table['show']='headings'
student_table.column("no",width=50)
student_table.column("examid",width=200)
student_table.column("name", width=200)
student_table.column("gender", width=100)
student_table.column("subject1", width=100)
student_table.column("subject2", width=100)
student_table.column("subject3", width=100)
student_table.column("subject4", width=100)
student_table.column("subject5", width=100)
student_table.column("subject6", width=100)
student_table.column("status", width=100)
student_table.pack(fill=BOTH,expand=1)
student_table.bind("<ButtonRelease-1>",get_selected_row)
show_command()






root.mainloop()