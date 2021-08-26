from tkinter import *
from tkinter import ttk
from tkinter.constants import DISABLED, NORMAL  
import tkinter.messagebox
import time
import mysql.connector

#! /usr/bin/env python3

class BuildDB:
	def __init__(self, root):
		self.root = root
		titlespace = " "
		self.root.title("Collector MySQL Database Builder")
		self.root.geometry("1380x865+40+0")
		self.root.resizable(width=False, height=False)

		#----------------------------------------------------------------------#
		############################# Build Frames #############################
		#----------------------------------------------------------------------#		
		#=================== Build Main Frames =============================
		MainFrame1 = Frame(self.root, bd=12, width=1350, height=865, relief=RIDGE, bg='gold')
		MainFrame1.grid()

		#====== Database Creation Steps 1 to 3 & Process Completion Frame =====
		TopFrame1 = Frame(MainFrame1, bd=5, width=1350, height=300, relief=RIDGE)
		TopFrame1.grid(row=1, column=0)

		LeftTopFrame = Frame(TopFrame1, bd=5, width=322, height=360, bg="cyan2", relief=RIDGE)
		LeftTopFrame.place(x=1, y=1)

		CenterTopFrame1 = Frame(TopFrame1, bd=5, width=322, height=360, bg="cyan2", relief=RIDGE)
		CenterTopFrame1.place(x=323, y=1)

		CenterTopFrame2 = Frame(TopFrame1, bd=5, width=322, height=360, bg="cyan2", relief=RIDGE)
		CenterTopFrame2.place(x=643, y=1)

		RightTopFrame = Frame(TopFrame1, bd=5, width=395, height=360, bg="wheat1", relief=RIDGE)
		RightTopFrame.place(x=944, y=1)

		#============== Database Creation Step 4 ==========================
		TopFrame2 = Frame(MainFrame1, bd=5, width=1350, height=360, relief=RIDGE)
		TopFrame2.grid(row=2, column=0)

		MidLeftFrame = Frame(TopFrame2, bd=5, width=340, height=349, bg="cyan2", relief=RIDGE)
		MidLeftFrame.place(x=1, y=1)

		MidCenterFrame1 = Frame(TopFrame2, bd=5, width=340, height=349, bg="cyan2", relief=RIDGE)
		MidCenterFrame1.place(x=340, y=1)

		MidCenterFrame2 = Frame(TopFrame2, bd=5, width=340, height=349, bg="cyan2", relief=RIDGE)
		MidCenterFrame2.place(x=680, y=1)

		MidRightFrame = Frame(TopFrame2, bd=5, width=340, height=349, bg="cyan2", relief=RIDGE)
		MidRightFrame.place(x=1000, y=1)

		#============== Message & Process Area ==========================
		TopFrame3 = Frame(MainFrame1, bd=5, width=1350, height=180, relief=RIDGE)
		TopFrame3.grid(row=3, column=0)

		LeftBottomFrame = Frame(TopFrame3, bd=5, width=1340, height=190, bg="lightgreen", relief=RIDGE)
		LeftBottomFrame.place(x=1, y=1)

		lblTopFrame3 = Label(TopFrame3, fg="black", bg="lightgreen", font=("ariel", 25, "bold", "underline"), text="<<< SQL Summary >>>", bd=5)
		lblTopFrame3.place(x=520, y=6)


		#================= Build Frame Labels =============================
		lbl1LeftTopFrame = Label(LeftTopFrame, fg="black", bg="cyan2", font=("ariel", 25, "bold", "underline"), text="Step 1 - DB Name", bd=7)
		lbl1LeftTopFrame.place(x=25, y=1)

		lbl1CenterTopFrame = Label(CenterTopFrame1, fg="black", bg="cyan2", font=("ariel", 25, "bold", "underline"), text="Step 2 - Table Det.", bd=7)
		lbl1CenterTopFrame.place(x=25, y=1)
			
		lbl1CenterTopFrame = Label(CenterTopFrame2, fg="black", bg="cyan2", font=("ariel", 25, "bold", "underline"), text="Step 3 - Col. Det.", bd=7)
		lbl1CenterTopFrame.place(x=25, y=1)

		lbl1RightTopFrame = Label(RightTopFrame, fg="black", bg="wheat1", font=("ariel", 25, "bold", "underline"), text="<< Edit Actions >>", bd=1)
		lbl1RightTopFrame.place(x=75, y=1)

		#--------------------------------------------------------------#
		########################## Set Variables #######################
		#--------------------------------------------------------------#
		ctr = 0

		self.dbName = ""

		# self.tblChkList = ['A', 'B', 'C', 'D']

		self.tblPosList = []

		self.tblName1 = ""
		self.tblName2 = ""
		self.tblName3 = ""
		self.tblName4 = ""
		self.tables = []
		self.procCtr = 0

		self.tbl1Status = ""
		self.tbl2Status = ""
		self.tbl3Status = ""
		self.tbl4Status = ""

		self.colListTbl1 = []
		self.colListTbl2 = []
		self.colListTbl3 = []
		self.colListTbl4 = []

		# Set Storage Dictionary for Column Names in Tables
		self.my_entries1 = []
		self.my_entries2 = []
		self.my_entries3 = []
		self.my_entries4 = []

		self.chars_to_check = ["y", "Y", "n", "N"]

		def Process():
		#----------------------------------------------------------------------#
		######################### 1. Create the Database Name ##################
		#----------------------------------------------------------------------#
			if v.get() == 1:
				# print("This is the Database Name Creation Process")

				a = Tk()
				a.geometry("300x200+400+100")
				a.title("User Database Creation")
				a.configure(bg="lightblue")


				def dbStep2():					
					v.set(3)  # change the choice, i.e. Add Table Name Process

					# Destroy the Database Creation Frame
					a.destroy()
					actionMenu()

				def dbSubmitName():
					self.dbName = (self.txtdbName.get())

					nameCharCount = 0
					for i in self.dbName:
						nameCharCount += 1

					if nameCharCount > 0:

						self.dbbtnSubmit = Button(a, text="Submit", width=5, height=1, font=("ariel", 14, "bold"), fg="red2", bg="white", state="disabled", command=dbSubmitName)
						self.dbbtnSubmit.place(x=10, y=150)

						self.steplbl1 = Label(TopFrame1, text="Database Name Set To:", font=("ariel", 16, "bold"), fg="red2", bg="white", state="normal")
						self.steplbl1.place(x=80, y=120)

						self.steplbl2 = Label(TopFrame1, text=self.dbName, font=("ariel", 16, "bold"), fg="red2", bg="white")
						self.steplbl2.place(x=130, y=160)

						self.nameLbl = Label(TopFrame3, text="Database Name Set To: " + self.dbName + "+ db", font=("ariel", 16, "bold"),height=1, fg="red2", bg="white")
						self.nameLbl.place(x=20, y=15)

					else:
						tkinter.messagebox.askyesno("Name Not Accepted", "Return to Main", parent=CenterTopFrame2)

					self.dbbtnSubmit = Button(a, text="Submit", width=5, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", state="disabled", command=dbSubmitName)
					self.dbbtnSubmit.place(x=10, y=150)

					self.dbbtnNext = Button(a, text="Next", width=5, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=dbStep2, state="normal")
					self.dbbtnNext.place(x=100, y=150)	

				self.lbldbName = Label(a, text="Enter Database Name", bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
				self.lbldbName.place(x=50, y=50)

				self.txtdbName = Entry(a, width=15, bd=1, relief="raised", font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
				self.txtdbName.place(x=50, y=90)

				self.dbbtnSubmit = Button(a, text="Submit", width=5, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", state="normal", command=dbSubmitName)
				self.dbbtnSubmit.place(x=10, y=150)

				self.dbbtnNext = Button(a, text="Next", width=5, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=dbStep2, state="disabled")
				self.dbbtnNext.place(x=100, y=150)

				self.dbbtnExit = Button(a, text="Exit", width=5, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=exit, state="normal")
				self.dbbtnExit.place(x=190, y=150)
			#--------------------------------------------------------------#
			################# 1. End Create the Database Name ##############
			#--------------------------------------------------------------#

			#--------------------------------------------------------------#
			################## 2. Begin Edit Database Name #################
			#--------------------------------------------------------------#
			if v.get() == 2:
				# print("This is the Edit Database Name Process")

				b = Tk()
				b.geometry("500x200+400+100")
				b.title("Edit Database Name")
				b.configure(bg="lightblue")

				chgLabel = Label(RightTopFrame, fg="dodger blue", bg="wheat1", font=("ariel", 18, "bold", "underline"), text="All Changes in 'Dodger Blue' ", bd=1)
				chgLabel.place(x=2, y=300)

				self.dbName = ""

				def dbActionB():
					self.nameLbl = Label(TopFrame3, text="",height=1, width=20,fg="green3")
					self.nameLbl.place(x=20, y=60)

					# Display new name in Step-1 Box
					self.nameLbl1 = Label(TopFrame1, text="DB Name Chgd to: " + self.dbName + "+ db", font=("ariel", 16, "bold"), width=25, height=1, fg="darkblue", bg="white")
					self.nameLbl1.place(x=20, y=200)

					# Display new name in Summary Box
					self.nameLbl2 = Label(TopFrame3, text="Database Name Changed to: " + self.dbName + "+ db", font=("ariel", 16, "bold"),height=1, fg="darkblue", bg="white")
					self.nameLbl2.place(x=20, y=60)

					v.set(4)  # change the choice, i.e. Add Table Name Process

					# Destroy the Database Edit Frame
					b.destroy()

				def newName():
					self.dbName = (name_entry.get())

					button1 = Button(b, text="Submit Change", width=8, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=newName, state="disabled")
					button1.place(x=20, y=150)

					button2 = Button(b, text="Return", width=8, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=dbActionB, state="normal")
					button2.place(x=170, y=150)

					button3 = Button(b, text="Exit", width=8, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=exit, state="normal")
					button3.place(x=350, y=150)
	
				if len (self.dbName) <= 0:
					tkinter.messagebox.askyesno("Database Name Not Present", "Return to Main", parent=CenterTopFrame2)
					v.set(0)
					b.destroy()
					actionMenu()	

				lbla1 = Label(b, font=("ariel", 16, "bold", "underline"), text="<<< Edit Database Name >>>", bd=1)
				lbla1.place(x=150, y=20)

				lbla2 = Label(b, font=("ariel", 16, "bold", "underline"), text="<<< Current Name >>>", bd=1)
				lbla2.place(x=50, y=60)

				lbla3 = Label(b, font=("ariel", 16, "bold", "underline"), text="<<< Revised Name >>>", bd=1)
				lbla3.place(x=250, y=60)

				lbla4 = Label(b, font=("ariel", 16, "bold", "underline"), text=self.dbName, bd=1)
				lbla4.place(x=100, y=100)

				name_entry = Entry(b, width=10, bd=1, relief=RIDGE, font=("ariel", 16), fg="red2", bg="wheat1")
				name_entry.place(x=280, y=100)
 
				btna1 = Button(b, text="Submit Change", width=8, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=newName, state="normal")
				btna1.place(x=20, y=150)

				btna2 = Button(b, text="Return", width=8, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=dbActionA, state="disabled")
				btna2.place(x=170, y=150)

				btna = Button(b, text="Exit", width=8, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=exit, state="normal")
				btna.place(x=350, y=150)
			#------------------------------------------------------------------#
			################### 2. End Edit Database Name ######################
			#------------------------------------------------------------------#

			#------------------------------------------------------------------#
			################# 3. Begin Table Name(s) Process ###################
			#------------------------------------------------------------------#
			if v.get() == 3:
				# print("This is the Table Name(s) Process")
				# if self.proc == 'A':  # Add Table Names
				self.tables = []

				def dbStep3():
					v.set(5)
					self.tblBtnNext.destroy()
					self.tblBtnExit.destroy()
					self.tblbtnSubmit.destroy()
					self.tblSubmit.destroy()
					actionMenu()				

				def summaryDisplay():
					# print("The number of tables = ", int(self.nbrTbls))
					self.tblBtnNext = Button(CenterTopFrame1, text="Next", width=10, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=dbStep3, state="normal")
					self.tblBtnNext.place(x=20, y=178)

					if int(self.nbrTbls) == 1:
						self.tbl1aLbl = Label(TopFrame3, text="1: " + str(self.tblName1), font=("ariel", 16, "bold"), height=1, fg="red2", bg="white")
						self.tbl1aLbl.place(x=20, y=50)

					if int(self.nbrTbls) == 2:
						self.tbl1aLbl = Label(TopFrame3, text="1: " + str(self.tblName1), font=("ariel", 16, "bold"), height=1, fg="red2", bg="white")
						self.tbl1aLbl.place(x=20, y=50)

						self.tbl2aLbl = Label(TopFrame3, text="2: " + str(self.tblName2), font=("ariel", 16, "bold"), height=1, fg="red2", bg="white")
						self.tbl2aLbl.place(x=20, y=80)

					if int(self.nbrTbls) == 3:
						self.tbl1aLbl = Label(TopFrame3, text="1: " + str(self.tblName1), font=("ariel", 16, "bold"), height=1, fg="red2", bg="white")
						self.tbl1aLbl.place(x=20, y=50)

						self.tbl2aLbl = Label(TopFrame3, text="2: " + str(self.tblName2), font=("ariel", 16, "bold"), height=1, fg="red2", bg="white")
						self.tbl2aLbl.place(x=20, y=80)

						self.tbl3aLbl = Label(TopFrame3, text="3: " + str(self.tblName3), font=("ariel", 16, "bold"), height=1, fg="red2", bg="white")
						self.tbl3aLbl.place(x=20, y=110)

					if int(self.nbrTbls) == 4:
						self.tbl1aLbl = Label(TopFrame3, text="1: " + str(self.tblName1), font=("ariel", 16, "bold"), height=1, fg="red2", bg="white")
						self.tbl1aLbl.place(x=20, y=50)

						self.tbl2aLbl = Label(TopFrame3, text="2: " + str(self.tblName2), font=("ariel", 16, "bold"), height=1, fg="red2", bg="white")
						self.tbl2aLbl.place(x=20, y=80)

						self.tbl3aLbl = Label(TopFrame3, text="3: " + str(self.tblName3), font=("ariel", 16, "bold"), height=1, fg="red2", bg="white")
						self.tbl3aLbl.place(x=20, y=110)

						self.tbl4aLbl = Label(TopFrame3, text="4: " + str(self.tblName4), font=("ariel", 16, "bold"), height=1, fg="red2", bg="white")
						self.tbl4aLbl.place(x=20, y=140)

				def lenTest1():
					if len(self.tblName1) > 14:
						tkinter.messagebox.askretrycancel(title="Alert", message="Table 1 Length Exceeded\nKeep Names Under\n14 Characters", parent=CenterTopFrame2)

						self.tbl1txt.delete(0, END)
						tblName1 = ""

						setAddTbl()
					return

				def lenTest2():
					if len(self.tblName2) > 14:
						tkinter.messagebox.askretrycancel(title="Alert", message="Table 2 Length Exceeded\nKeep Names Under\n14 Characters", parent=CenterTopFrame2)

						self.tbl2txt.delete(0, END)
						tblName2 = ""

						setAddTbl()
					return

				def lenTest3():
					if len(self.tblName3) > 14:
						tkinter.messagebox.askretrycancel(title="Alert", message="Table 3 Length Exceeded\nKeep Names Under\n14 Characters", parent=CenterTopFrame2)

						self.tbl3txt.delete(0, END)
						tblName3 = ""

						setAddTbl()
					return

				def lenTest4():
					if len(self.tblName4) > 14:
						tkinter.messagebox.askretrycancel(title="Alert", message="Table 4 Length Exceeded\nKeep Names Under\n14 Characters", parent=CenterTopFrame2)

						self.tbl4txt.delete(0, END)
						tblName4 = ""

						setAddTbl()
					return

				def addTblNames():
					# print("Table 1 input = ", self.tbl1txt.get())
					# print("Table Qty = ", self.nbrTbls)
				
					if int(self.nbrTbls) == 1:
						self.tblName1 = self.tbl1txt.get()
						# print("self.tblName1 (addTblNames()) = ", self.tblName1)
						lenTest1()
						self.tables = [self.tblName1]
						self.tblStr = ','.join((self.tables))
						self.tblPos = ("A", "", "", "")
						# print("Tables assigned are = ", self.tables)
						# print("Table positions are = ", self.tblPos)

						# Show Table Names created in the Summary Section
						summaryDisplay()

					if int(self.nbrTbls) == 2:
						self.tblName1 = self.tbl1txt.get()
						lenTest1()
						self.tblName2 = self.tbl2txt.get()
						lenTest2()
						self.tables = (self.tblName1, self.tblName2)
						self.tblStr = ','.join((self.tables))
						self.tblPos = ("A", "B", "", "")
						# print("Tables assigned are = ", self.tables)

						# Show Table Names created in the Summary Section
						summaryDisplay()

					if int(self.nbrTbls) == 3:
						self.tblName1 = self.tbl1txt.get()
						lenTest1()
						self.tblName2 = self.tbl2txt.get()
						lenTest2()
						self.tblName3 = self.tbl3txt.get()
						lenTest3()
						self.tables = (self.tblName1, self.tblName2, self.tblName3)
						self.tblStr = ','.join((self.tables))
						self.tblPos = ("A", "B", "C", "")
						# print("Tables assigned are = ", self.tables)

						# Show Table Names created in the Summary Section
						summaryDisplay()

					if int(self.nbrTbls) == 4:
						self.tblName1 = self.tbl1txt.get()
						lenTest1()
						self.tblName2 = self.tbl2txt.get()
						lenTest2()
						self.tblName3 = self.tbl3txt.get()
						lenTest3()
						self.tblName4 = self.tbl4txt.get()
						lenTest4()
						self.tables = (self.tblName1, self.tblName2, self.tblName3, self.tblName4)
						self.tblStr = ','.join((self.tables))
						self.tblPos = ("A", "B", "C", "D")
						# print("Tables assigned are = ", self.tables)

						# Show Table Names created in the Summary Section
						summaryDisplay()

					

				def setAddTbl():
					# Get user input - Number of Tabes to Add
					self.nbrTbls = self.txtNbr.get()
					# print("Number of Tables to Add = ", self.nbrTbls)

					# Clear data input area of frame
					self.tblLbl.destroy()
					self.txtNbr.destroy()

					self.tblSubmit = Button(CenterTopFrame1, text="Submit", width=10, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=addTblNames, state="normal")
					self.tblSubmit.place(x=20, y=178)

					if int(self.nbrTbls) == 1:
						self.tbl1Label = Label(CenterTopFrame1,text="Table 1 Name:", bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
						self.tbl1Label.place(x=5 ,y=52)

						self.tbl1txt = Entry(CenterTopFrame1, width=15, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
						self.tbl1txt.place(x=130, y=50)

					if int(self.nbrTbls) == 2:
						# Detail input for table 1
						self.tbl1Label = Label(CenterTopFrame1,text="Table 1 Name:", bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
						self.tbl1Label.place(x=5 ,y=52)

						self.tbl1txt = Entry(CenterTopFrame1, width=15, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
						self.tbl1txt.place(x=130, y=50)

						# Detail input for table 2
						self.tbl2Label = Label(CenterTopFrame1,text="Table 2 Name:", bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
						self.tbl2Label.place(x=5 ,y=82)

						self.tbl2txt = Entry(CenterTopFrame1, width=15, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
						self.tbl2txt.place(x=130, y=80)

					if int(self.nbrTbls) == 3:
						# Detail input for table 1
						self.tbl1Label = Label(CenterTopFrame1,text="Table 1 Name:", bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
						self.tbl1Label.place(x=5 ,y=52)

						self.tbl1txt = Entry(CenterTopFrame1, width=15, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
						self.tbl1txt.place(x=130, y=50)

						# Detail input for table 2
						self.tbl2Label = Label(CenterTopFrame1,text="Table 2 Name:", bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
						self.tbl2Label.place(x=5 ,y=82)

						self.tbl2txt = Entry(CenterTopFrame1, width=15, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
						self.tbl2txt.place(x=130, y=80)

						# Detail input for table 3
						self.tbl3Label = Label(CenterTopFrame1,text="Table 3 Name:", bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
						self.tbl3Label.place(x=5 ,y=112)

						self.tbl3txt = Entry(CenterTopFrame1, width=15, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
						self.tbl3txt.place(x=130, y=110)

					if int(self.nbrTbls) == 4:
						# Detail input for table 1
						self.tbl1Label = Label(CenterTopFrame1,text="Table 1 Name:", bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
						self.tbl1Label.place(x=5 ,y=52)

						self.tbl1txt = Entry(CenterTopFrame1, width=15, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
						self.tbl1txt.place(x=130, y=50)

						# Detail input for table 2
						self.tbl2Label = Label(CenterTopFrame1,text="Table 2 Name:", bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
						self.tbl2Label.place(x=5 ,y=82)

						self.tbl2txt = Entry(CenterTopFrame1, width=15, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
						self.tbl2txt.place(x=130, y=80)

						# Detail input for table 3
						self.tbl3Label = Label(CenterTopFrame1,text="Table 3 Name:", bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
						self.tbl3Label.place(x=5 ,y=112)

						self.tbl3txt = Entry(CenterTopFrame1, width=15, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
						self.tbl3txt.place(x=130, y=110)

						# Detail input for table 4
						self.tbl4Label = Label(CenterTopFrame1,text="Table 4 Name:", bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
						self.tbl4Label.place(x=5 ,y=142)

						self.tbl4txt = Entry(CenterTopFrame1, width=15, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
						self.tbl4txt.place(x=130, y=140)

				if len(self.dbName) == 0:
					v.set(3)
					actionMenu()

				# Set Frame labels, buttons and entries
				self.tblbtnSubmit = Button(CenterTopFrame1, text="Submit Nbr", width=10, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=setAddTbl, state="normal")
				self.tblbtnSubmit.place(x=20, y=178)

				self.tblBtnExit = Button(CenterTopFrame1, text="Exit", width=7, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=exit, state="normal")
				self.tblBtnExit.place(x=180, y=178)

				# Get Number of Tables to add
				self.tblLbl = Label(CenterTopFrame1,text="Enter Number of Tables(Max 4)", bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
				self.tblLbl.place(x=10 ,y=100)

				self.txtNbr = Entry(CenterTopFrame1, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
				self.txtNbr.place(x=265, y=100)

			#--------------------------------------------------------------#
			############### 3. End Table Name(s) Process ###################
			#--------------------------------------------------------------#

			#--------------------------------------------------------------#
			############### 4. Begin Change Table Name(s) Process ##########
			#--------------------------------------------------------------#
			if v.get() == 4:
				if len(self.tables) == 0:
					tkinter.messagebox.showinfo(title="Incomplete Information", message="No Tables Available to Change\nReturn to Main")
					v.set(0)
					actionMenu()
				else:
		########################################################################
					c = Tk()
					c.geometry("800x400+300+200")
					c.title("Table Name Change")
					c.configure(bg="beige")

					def chgNext():
						v.set(5)
						c.destroy()
						actionMenu()

					def nameChgDisp():
						# print("Length of var1 = ", len(self.var1))
						# print("Length of var2 = ", len(self.var2))
						# print("Length of var3 = ", len(self.var3))
						# print("Length of var4 = ", len(self.var4))

						if int(self.nbrTbls) == 1:
							if len(self.var1) > 0:
								self.tbl1txt.destroy()
								self.tbl1aLbl.destroy()

								# Table Detail Windows
								self.tbl1ChgLbl = Label(CenterTopFrame1, text=self.tblName1, width=15, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="darkblue", bg="wheat1")
								self.tbl1ChgLbl.place(x=130, y=50)

								self.tbl1aChgLbl = Label(TopFrame3, text="Table 1: " + str(self.tblName1), font=("ariel", 16, "bold"), height=1, fg="darkblue", bg="white")
								self.tbl1aChgLbl.place(x=20, y=90)

								self.newName1Label = Label(c, bd=1, relief=RIDGE, text=self.tblName1, width=12, font=("ariel", 22, "bold"), fg="green", bg="wheat1")
								self.newName1Label.place(x=550, y=100)

							# Display the NEW Table List
							self.newTblList = Label(c, bd=5, relief=SUNKEN, text="The 'NEW' Table List is: " + str(self.tables), font=("ariel", 17, "bold"), fg="darkblue", bg="beige")
							self.newTblList.place(x=5, y=300)


						if int(self.nbrTbls) == 2:
							if len(self.var1) > 0:
								self.tbl1txt.destroy()
								self.tbl1aLbl.destroy()

								# Step 2 Table Detail Window
								self.tbl1ChgLbl = Label(CenterTopFrame1, text=self.tblName1, width=15, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="darkblue", bg="wheat1")
								self.tbl1ChgLbl.place(x=130, y=50)

								self.tbl1aChgLbl = Label(TopFrame3, text="Table 1: " + str(self.tblName1), font=("ariel", 16, "bold"), height=1, fg="darkblue", bg="white")
								self.tbl1aChgLbl.place(x=20, y=90)

								self.newName1Label = Label(c, bd=1, relief=RIDGE, text=self.tblName1, width=12, font=("ariel", 22, "bold"), fg="green", bg="wheat1")
								self.newName1Label.place(x=550, y=100)

							if len(self.var2) > 0:
								self.tbl2txt.destroy()
								self.tbl2aLbl.destroy()

								self.tbl2ChgLbl = Label(CenterTopFrame1, text=self.tblName2, width=15, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="darkblue", bg="wheat1")
								self.tbl2ChgLbl.place(x=130, y=80)

								self.tbl2aChgLbl = Label(TopFrame3, text="Table 2: " + str(self.tblName2), font=("ariel", 16, "bold"), height=1, fg="darkblue", bg="white")
								self.tbl2aChgLbl.place(x=20, y=120)

								self.newName2Label = Label(c, bd=1, relief=RIDGE, text=self.tblName2, width=12, font=("ariel", 22, "bold"), fg="green", bg="wheat1")
								self.newName2Label.place(x=550, y=140)

							# Display the NEW Table List
							self.newTblList = Label(c, bd=5, relief=SUNKEN, text="The 'NEW' Table List is: " + str(self.tables), font=("ariel", 17, "bold"), fg="darkblue", bg="beige")
							self.newTblList.place(x=5, y=300)


						if int(self.nbrTbls) == 3:
							if len(self.var1) > 0:
								self.tbl1txt.destroy()
								self.tbl1aLbl.destroy()

								# Step 2 Table Detail Window
								self.tbl1ChgLbl = Label(CenterTopFrame1, text=self.tblName1, width=15, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="darkblue", bg="wheat1")
								self.tbl1ChgLbl.place(x=130, y=50)

								self.tbl1aChgLbl = Label(TopFrame3, text="Table 1: " + str(self.tblName1), font=("ariel", 16, "bold"), height=1, fg="darkblue", bg="white")
								self.tbl1aChgLbl.place(x=20, y=90)

								self.newName1Label = Label(c, bd=1, relief=RIDGE, text=self.tblName1, width=12, font=("ariel", 22, "bold"), fg="green", bg="wheat1")
								self.newName1Label.place(x=550, y=100)

							if len(self.var2) > 0:
								self.tbl2txt.destroy()
								self.tbl2aLbl.destroy()

								self.tbl2ChgLbl = Label(CenterTopFrame1, text=self.tblName2, width=15, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="darkblue", bg="wheat1")
								self.tbl2ChgLbl.place(x=130, y=80)

								self.tbl2aChgLbl = Label(TopFrame3, text="Table 2: " + str(self.tblName2), font=("ariel", 16, "bold"), height=1, fg="darkblue", bg="white")
								self.tbl2aChgLbl.place(x=20, y=120)

								self.newName2Label = Label(c, bd=1, relief=RIDGE, text=self.tblName2, width=12, font=("ariel", 22, "bold"), fg="green", bg="wheat1")
								self.newName2Label.place(x=550, y=140)

							if len(self.var3) > 0:
								self.tbl3txt.destroy()
								self.tbl3aLbl.destroy()

								self.tbl3ChgLbl = Label(CenterTopFrame1, text=self.tblName3, width=15, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="darkblue", bg="wheat1")
								self.tbl3ChgLbl.place(x=130, y=110)

								self.tbl3aChgLbl = Label(TopFrame3, text="Table 3: " + str(self.tblName3), font=("ariel", 16, "bold"), height=1, fg="darkblue", bg="white")
								self.tbl3aChgLbl.place(x=250, y=90)

								self.newName3Label = Label(c, bd=1, relief=RIDGE, text=self.tblName3, width=12, font=("ariel", 22, "bold"), fg="green", bg="wheat1")
								self.newName3Label.place(x=550, y=180)

							# Display the NEW Table List	
							self.newTblList = Label(c, bd=5, relief=SUNKEN, text="The 'NEW' Table List is: " + str(self.tables), font=("ariel", 17, "bold"), fg="darkblue", bg="beige")
							self.newTblList.place(x=5, y=300)

						if int(self.nbrTbls) == 4:						
							if len(self.var1) > 0:
								self.tbl1txt.destroy()
								self.tbl1aLbl.destroy()

								# Step 2 Table Detail Window
								self.tbl1ChgLbl = Label(CenterTopFrame1, text=self.tblName1, width=15, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="darkblue", bg="wheat1")
								self.tbl1ChgLbl.place(x=130, y=50)

								self.tbl1aChgLbl = Label(TopFrame3, text="Table 1: " + str(self.tblName1), font=("ariel", 16, "bold"), height=1, fg="darkblue", bg="white")
								self.tbl1aChgLbl.place(x=20, y=90)

								self.newName1Label = Label(c, bd=1, relief=RIDGE, text=self.tblName1, width=12, font=("ariel", 22, "bold"), fg="green", bg="wheat1")
								self.newName1Label.place(x=550, y=100)

							if len(self.var2) > 0:
								self.tbl2txt.destroy()
								self.tbl2aLbl.destroy()

								self.tbl2ChgLbl = Label(CenterTopFrame1, text=self.tblName2, width=15, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="darkblue", bg="wheat1")
								self.tbl2ChgLbl.place(x=130, y=80)

								self.tbl2aChgLbl = Label(TopFrame3, text="Table 2: " + str(self.tblName2), font=("ariel", 16, "bold"), height=1, fg="darkblue", bg="white")
								self.tbl2aChgLbl.place(x=20, y=120)

								self.newName2Label = Label(c, bd=1, relief=RIDGE, text=self.tblName2, width=12, font=("ariel", 22, "bold"), fg="green", bg="wheat1")
								self.newName2Label.place(x=550, y=140)

							if len(self.var3) > 0:
								self.tbl3txt.destroy()
								self.tbl3aLbl.destroy()

								self.tbl3ChgLbl = Label(CenterTopFrame1, text=self.tblName3, width=15, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="darkblue", bg="wheat1")
								self.tbl3ChgLbl.place(x=130, y=110)

								self.tbl3aChgLbl = Label(TopFrame3, text="Table 3: " + str(self.tblName3), font=("ariel", 16, "bold"), height=1, fg="darkblue", bg="white")
								self.tbl3aChgLbl.place(x=250, y=90)

								self.newName3Label = Label(c, bd=1, relief=RIDGE, text=self.tblName3, width=12, font=("ariel", 22, "bold"), fg="green", bg="wheat1")
								self.newName3Label.place(x=550, y=180)

							if len(self.var4) > 0:
								self.tbl4txt.destroy()
								self.tbl4aLbl.destroy()

								self.tbl4ChgLbl = Label(CenterTopFrame1, text=self.tblName4, width=15, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="darkblue", bg="wheat1")
								self.tbl4ChgLbl.place(x=130, y=140)

								self.tbl4aChgLbl = Label(TopFrame3, text="Table 4: " + str(self.tblName4), font=("ariel", 16, "bold"), height=1, fg="darkblue", bg="white")
								self.tbl4aChgLbl.place(x=250, y=120)

								self.newName4Label = Label(c, bd=1, relief=RIDGE, text=self.tblName4, width=12, font=("ariel", 22, "bold"), fg="green", bg="wheat1")
								self.newName4Label.place(x=550, y=220)

							# Display the NEW Table List
							self.newTblList = Label(c, bd=5, relief=SUNKEN, text="The 'NEW' Table List is: " + str(self.tables), font=("ariel", 17, "bold"), fg="darkblue", bg="beige")
							self.newTblList.place(x=5, y=300)
					
					def submit():
					# def tblChgSubmit():
						self.var1 = ""
						self.var2 = "" 
						self.var3 = ""
						self.var4 = ""
						# self.var1 = ent1.get()
						# print("self.var1 = ", self.var1)
						# self.var2 = ent2.get()
						# print("self.var2 = ", self.var2)
						# self.var3 = ent3.get()
						# print("self.var3 = ", self.var3)
						# self.var4 = ent4.get()
						# print("self.var4 = ", self.var4)


						if int(self.nbrTbls) == 1:
							self.var1 = ent1.get()
							if len(self.var1) == 0:
								self.tblName1 == self.tables[0]
							else:
								self.tblName1 = self.var1
							# print("Table Name 1 = ", self.tblName1)

							# Replace entire Tables List
							self.tables = []
							self.tables = [self.tblName1]
							# print("The 1 Tabels in the list are now: ", self.tables)

						if int(self.nbrTbls) == 2:
							self.var1 = ent1.get()
							if len(self.var1) == 0:
								self.tblName1 == self.tables[0]
							else:
								self.tblName1 = self.var1
							# print("Table Name 1 = ", self.tblName1)

							self.var2 = ent2.get()
							if len(self.var2) == 0:
								self.tblName2 == self.tables[1]		
							else:
								self.tblName2 = self.var2
							# print("Table Name 2 = ", self.tblName2)

							# Replace entire Tables List
							self.tables = []
							self.tables = [self.tblName1, self.tblName2]
							# print("The 2 Tabels in the list are now: ", self.tables)

						if int(self.nbrTbls) == 3:
							self.var1 = ent1.get()
							if len(self.var1) == 0:
								self.tblName1 == self.tables[0]
							else:
								self.tblName1 = self.var1
							# print("Table Name 1 = ", self.tblName1)

							self.var2 = ent2.get()
							if len(self.var2) == 0:
								self.tblName2 == self.tables[1]		
							else:
								self.tblName2 = self.var2
							# print("Table Name 2 = ", self.tblName2)

							self.var3 = ent3.get()
							self.var3 = ent3.get()
							if len(self.var3) == 0:
								self.tblName3 == self.tables[2]
							else:
								self.tblName3 = self.var3
							# print("Table Name 3 = ", self.tblName3)

							# Replace entire Tables List
							self.tables = []
							self.tables = [self.tblName1, self.tblName2, self.tblName3]
							# print("The 3 Tabels in the list are now: ", self.tables)


						if int(self.nbrTbls) == 4:
							self.var1 = ent1.get()
							if len(self.var1) == 0:
								self.tblName1 == self.tables[0]
							else:
								self.tblName1 = self.var1
							# print("Table Name 1 = ", self.tblName1)

							self.var2 = ent2.get()
							if len(self.var2) == 0:
								self.tblName2 == self.tables[1]		
							else:
								self.tblName2 = self.var2
							# print("Table Name 2 = ", self.tblName2)

							self.var3 = ent3.get()
							if len(self.var3) == 0:
								self.tblName3 == self.tables[2]
							else:
								self.tblName3 = self.var3
							# print("Table Name 3 = ", self.tblName3)

							self.var4 = ent4.get()
							if len(self.var4) == 0:
								self.tblName4 == self.tables[3]
							else:
								self.tblName4 = self.var4
							# print("Table Name 4 = ", self.tblName4)

							# Replace entire Tables List
							self.tables = []
							self.tables = [self.tblName1, self.tblName2, self.tblName3, self.tblName4]
							# print("The 4 Tabels are now: ", self.tables)

						nameChgDisp()

					self.tblChgHdr = Label(c, text="<<<< Record Table Name Changes >>>>", font=("ariel", 20, "bold", "underline"), fg="black", bg="beige")
					self.tblChgHdr.place(x=210, y=20)

					self.tblCurLbl = Label(c, text="Current Table Name", font=("ariel", 20, "bold", "underline"), fg="black", bg="beige")
					self.tblCurLbl.place(x=40, y=60)

					self.tblFutLbl = Label(c, text="New Table Name", font=("ariel", 20, "bold", "underline"), fg="black", bg="beige")
					self.tblFutLbl.place(x=330, y=60)

					self.newNameLabel = Label(c, text="Confimed Name", font=("ariel", 20, "bold", "underline"), fg="black", bg="beige")
					self.newNameLabel.place(x=565, y=60)

					self.tblChgSubmit = Button(c, text="Submit", width=5, height=1, font=("ariel", 20, "bold"), fg="black", bg="white", command=submit, state="normal")
					self.tblChgSubmit.place(x=100, y=360)

					self.tblChgNext = Button(c, text="Next", width=5, height=1, font=("ariel", 20, "bold"), fg="black", bg="white", command=chgNext, state="normal")
					self.tblChgNext.place(x=325, y=360)

					self.tblChgExit = Button(c, text="Exit", width=5, height=1, font=("ariel", 20, "bold"), fg="black", bg="white", command=exit, state="normal")
					self.tblChgExit.place(x=550, y=360)

					# Display the Original Table List
					self.originalTblList = Label(c, bd=5, relief=SUNKEN, text="The 'ORIGINAL' Table List is: " + str(self.tables), font=("ariel", 17, "bold"), fg="red3", bg="beige")
					self.originalTblList.place(x=5, y=260)

					# print("The number of Tables (ln 793) = ", self.nbrTbls)

					if int(self.nbrTbls) == 1:
						self.tbl1Label = Label(c, text=self.tblName1, width=12, font=("ariel", 22, "bold"), fg="black", bg="wheat1")
						self.tbl1Label.place(x=45, y=100)

						ent1 = Entry(c, width=12, bd=1, relief=RIDGE, font=("ariel", 22, "bold"), fg="red2", bg="wheat1")
						ent1.place(x=315, y=100)

						self.newName1Label = Label(c, text=" ", width=12, font=("ariel", 22, "bold"), fg="darkblue", bg="wheat1")
						self.newName1Label.place(x=550, y=100)

					if int(self.nbrTbls) == 2:
						self.tbl1Label = Label(c, text=self.tables[0], width=12, font=("ariel", 22, "bold"), fg="black", bg="wheat1")
						self.tbl1Label.place(x=45, y=100)

						ent1 = Entry(c, width=12, bd=1, relief=RIDGE, font=("ariel", 22, "bold"), fg="red2", bg="wheat1")
						ent1.place(x=315, y=100)

						self.newName1Label = Label(c, text=" ", width=12, font=("ariel", 22, "bold"), fg="darkblue", bg="wheat1")
						self.newName1Label.place(x=550, y=100)

						self.tbl2Label = Label(c, text=self.tables[1], width=12, font=("ariel", 22, "bold"), fg="black", bg="wheat1")
						self.tbl2Label.place(x=45, y=140)

						ent2 = Entry(c, width=12, bd=1, relief=RIDGE, font=("ariel", 22, "bold"), fg="red2", bg="wheat1")
						ent2.place(x=315, y=140)

						self.newName2Label = Label(c, text=" ", width=12, font=("ariel", 22, "bold"), fg="darkblue", bg="wheat1")
						self.newName2Label.place(x=550, y=140)
			
					if int(self.nbrTbls) == 3:
						self.tbl1Label = Label(c, text=self.tables[0], width=12, font=("ariel", 22, "bold"), fg="black", bg="wheat1")
						self.tbl1Label.place(x=45, y=100)

						ent1 = Entry(c, width=12, bd=1, relief=RIDGE, font=("ariel", 22, "bold"), fg="red2", bg="wheat1")
						ent1.place(x=315, y=100)

						self.newName1Label = Label(c, text=" ", width=12, font=("ariel", 23, "bold", "underline"), fg="black", bg="wheat1")
						self.newName1Label.place(x=550, y=100)

						self.tbl2Label = Label(c, text=self.tables[1], width=12, font=("ariel", 22, "bold"), fg="black", bg="wheat1")
						self.tbl2Label.place(x=45, y=140)

						ent2 = Entry(c, width=12, bd=1, relief=RIDGE, font=("ariel", 22, "bold"), fg="red2", bg="wheat1")
						ent2.place(x=315, y=140)

						self.newName2Label = Label(c, text=" ", width=12, font=("ariel", 22, "bold"), fg="darkblue", bg="wheat1")
						self.newName2Label.place(x=550, y=140)

						self.tbl3Label = Label(c, text=self.tables[2], width=12, font=("ariel", 22, "bold"), fg="black", bg="wheat1")
						self.tbl3Label.place(x=45, y=180)

						ent3 = Entry(c, width=12, bd=1, relief=RIDGE, font=("ariel", 22, "bold"), fg="red2", bg="wheat1")
						ent3.place(x=315, y=180)

						self.newName3Label = Label(c, text=" ", width=12, font=("ariel", 22, "bold"), fg="darkblue", bg="wheat1")
						self.newName3Label.place(x=550, y=180)

					if int(self.nbrTbls) == 4:
						self.tbl1Label = Label(c, bd=1, relief=RIDGE, text=self.tblName1, width=12, font=("ariel", 22, "bold"), fg="black", bg="wheat1")
						self.tbl1Label.place(x=45, y=100)

						ent1 = Entry(c, width=12, bd=1, relief=RIDGE, font=("ariel", 22, "bold"), fg="red2", bg="wheat1")
						ent1.place(x=315, y=100)

						self.newName1Label = Label(c, bd=1, relief=RIDGE, text=" ", width=12, font=("ariel", 23, "bold"), fg="darkblue", bg="wheat1")
						self.newName1Label.place(x=550, y=100)

						self.tbl2Label = Label(c, bd=1, relief=RIDGE, text=self.tblName2, width=12, font=("ariel", 22, "bold"), fg="black", bg="wheat1")
						self.tbl2Label.place(x=45, y=140)

						ent2 = Entry(c, width=12, bd=1, relief=RIDGE, font=("ariel", 22, "bold"), fg="red2", bg="wheat1")
						ent2.place(x=315, y=140)

						self.newName2Label = Label(c, bd=1, relief=RIDGE, text=" ", width=12, font=("ariel", 23, "bold"), fg="darkblue", bg="wheat1")
						self.newName2Label.place(x=550, y=140)

						self.tbl3Label = Label(c, bd=1, relief=RIDGE, text=self.tblName3, width=12, font=("ariel", 22, "bold"), fg="black", bg="wheat1")
						self.tbl3Label.place(x=45, y=180)

						ent3 = Entry(c, width=12, bd=1, relief=RIDGE, font=("ariel", 22, "bold"), fg="red2", bg="wheat1")
						ent3.place(x=315, y=180)

						self.newName3Label = Label(c, bd=1, relief=RIDGE, text=" ", width=12, font=("ariel", 23, "bold"), fg="darkblue", bg="wheat1")
						self.newName3Label.place(x=550, y=180)

						self.tbl4Label = Label(c, bd=1, relief=RIDGE, text=self.tblName4, width=12, font=("ariel", 22, "bold"), fg="black", bg="wheat1")
						self.tbl4Label.place(x=45, y=220)

						ent4 = Entry(c, width=12, bd=1, relief=RIDGE, font=("ariel", 22, "bold"), fg="red2", bg="wheat1")
						ent4.place(x=315, y=220)

						self.newName4Label = Label(c, bd=1, relief=RIDGE, text=" ", width=12, font=("ariel", 23, "bold"), fg="darkblue", bg="wheat1")
						self.newName4Label.place(x=550, y=220)

			#--------------------------------------------------------------#
			################ 4. End Change Table Name(s) Process ###########
			#--------------------------------------------------------------#

			#--------------------------------------------------------------#
			################ 5. Start - Add Column Quantity Process ########
			#--------------------------------------------------------------#
			if v.get() == 5:
				def nextItem():
					# self.addColBtnNext.destroy()
					v.set(6)
					actionMenu()

				def sumColDisplay():
					self.addColBtnNext.destroy()					
					# Display Information in the Summary Section
					def colSum1():
						self.tbl1ColNbr = Label(TopFrame3, text="Cols. = " + self.txtColNbr1.get(), font=("ariel", 16, "bold"), height=1, fg="red2", bg="white")
						self.tbl1ColNbr.place(x=195, y=50)

					def colSum2():
						self.tbl2ColNbr = Label(TopFrame3, text="Cols. = " + self.txtColNbr2.get(), font=("ariel", 16, "bold"), height=1, fg="red2", bg="white")
						self.tbl2ColNbr.place(x=195, y=80)

					def colSum3():
						self.tbl3ColNbr = Label(TopFrame3, text="Cols. = " + self.txtColNbr3.get(), font=("ariel", 16, "bold"), height=1, fg="red2", bg="white")
						self.tbl3ColNbr.place(x=195, y=110)

					def colSum4():
						self.tbl4ColNbr = Label(TopFrame3, text="Cols. = " + self.txtColNbr4.get(), font=("ariel", 16, "bold"), height=1, fg="red2", bg="white")
						self.tbl4ColNbr.place(x=195, y=140)

					if int(self.nbrTbls) == 1:
						colSum1()
						nextItem()
					if int(self.nbrTbls) == 2:
						colSum1()
						colSum2()
						nextItem()
					if int(self.nbrTbls) == 3:
						colSum1()
						colSum2()
						colSum3()
						nextItem()
					if int(self.nbrTbls) == 4:
						colSum1()
						colSum2()
						colSum3()
						colSum4()
						nextItem()


				def colNbr():
					self.addColBtnSubmit.destroy()
					self.addColBtnExit.destroy()

					self.addColBtnNext = Button(CenterTopFrame2, text="Next", width=6, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=sumColDisplay, state="normal")
					self.addColBtnNext.place(x=125, y=178)

					if int(self.nbrTbls) == 1:
						self.NbrColsTbl1 = int(self.txtColNbr1.get())
						# print("Number Columns in Table 1 = ", self.NbrColsTbl1)

					if int(self.nbrTbls) == 2:
						self.NbrColsTbl1 = int(self.txtColNbr1.get())
						self.NbrColsTbl2 = int(self.txtColNbr2.get())
						# print("Number Columns in Table 1 = ", self.NbrColsTbl1)
						# print("Number Columns in Table 2 = ", self.NbrColsTbl2)

					if int(self.nbrTbls) == 3:
						self.NbrColsTbl1 = int(self.txtColNbr1.get())
						self.NbrColsTbl2 = int(self.txtColNbr2.get())
						self.NbrColsTbl3 = int(self.txtColNbr3.get())
						# print("Number Columns in Table 1 = ", self.NbrColsTbl1)
						# print("Number Columns in Table 2 = ", self.NbrColsTbl2)
						# print("Number Columns in Table 3 = ", self.NbrColsTbl3)

					if int(self.nbrTbls) == 4:
						self.NbrColsTbl1 = int(self.txtColNbr1.get())
						self.NbrColsTbl2 = int(self.txtColNbr2.get())
						self.NbrColsTbl3 = int(self.txtColNbr3.get())
						self.NbrColsTbl4 = int(self.txtColNbr4.get())
						# print("Number Columns in Table 1 = ", self.NbrColsTbl1)
						# print("Number Columns in Table 2 = ", self.NbrColsTbl2)
						# print("Number Columns in Table 3 = ", self.NbrColsTbl3)
						# print("Number Columns in Table 4 = ", self.NbrColsTbl4)

					# sumColDisplay()

				def tbl1Col():
					self.lblColNbr1 = Label(CenterTopFrame2, text="Number Columns - Tabel 1", bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
					self.lblColNbr1.place(x=5, y=52)

					self.txtColNbr1 = Entry(CenterTopFrame2, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
					self.txtColNbr1.place(x=250, y=50)

				def tbl2Col():
					self.lblColNbr2 = Label(CenterTopFrame2, text="Number Columns - Tabel 2", bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
					self.lblColNbr2.place(x=5, y=82)

					self.txtColNbr2 = Entry(CenterTopFrame2, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
					self.txtColNbr2.place(x=250, y=80)

				def tbl3Col():
					self.lblColNbr3 = Label(CenterTopFrame2, text="Number Columns - Tabel 3", bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
					self.lblColNbr3.place(x=5, y=112)

					self.txtColNbr3 = Entry(CenterTopFrame2, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
					self.txtColNbr3.place(x=250, y=110)

				def tbl4Col():
					self.lblColNbr4 = Label(CenterTopFrame2, text="Number Columns - Tabel 3", bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
					self.lblColNbr4.place(x=5, y=142)

					self.txtColNbr4 = Entry(CenterTopFrame2, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
					self.txtColNbr4.place(x=250, y=140)

				tkinter.messagebox.showinfo(title="Show Info", message="Max 14 Columns per Table", icon="info")

				self.addColBtnSubmit = Button(CenterTopFrame2, text="Add Nbr(s)", width=10, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=colNbr, state="normal")
				self.addColBtnSubmit.place(x=5, y=178)

				self.addColBtnNext = Button(CenterTopFrame2, text="Next", width=6, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=sumColDisplay, state="disabled")
				self.addColBtnNext.place(x=125, y=178)

				self.addColBtnExit = Button(CenterTopFrame2, text="Exit", width=5, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=exit)
				self.addColBtnExit.place(x=205, y=178)

				if int(self.nbrTbls) == 1:
					tbl1Col()
				if int(self.nbrTbls) == 2:
					tbl1Col()
					tbl2Col()
				if int(self.nbrTbls) == 3:
					tbl1Col()
					tbl2Col()
					tbl3Col()
				if int(self.nbrTbls) == 4:
					tbl1Col()
					tbl2Col()
					tbl3Col()
					tbl4Col()

			#--------------------------------------------------------------#
			################ 5. End - Add Column Quantity Process ##########
			#--------------------------------------------------------------#
			#--------------------------------------------------------------#
			############## 6. Start - Add Column Names to Table(s) #########
			#--------------------------------------------------------------#
			if v.get() == 6:
				self.addColBtnSubmit.destroy()
				# self.addColBtnNext.destroy()
				# self.colbtnExit.destroy()

				# self.colbtnNext = Button(CenterTopFrame2, text="Next", width=6, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command="", state="disabled")
				# self.colbtnNext.place(x=125, y=178)

				tkinter.messagebox.showinfo(title="Show Info", message="Keep Column Names As Small As Possible", parent=MidCenterFrame2)

				def colSubmit1():
					# Create the Column List for Table 1
					ctrNbr = 1				
					self.colListTbl1 = ""

					for entry in self.my_entries1:
						if ctrNbr <= int(self.txtColNbr1.get()):
							self.colListTbl1 = self.colListTbl1 + str(entry.get()) + ','
							ctrNbr += 1
						else:
							self.colListTbl1 = self.colListTbl1 + str(entry.get())
					# Split the string based on comma delimiter
					self.colListTbl1 = self.colListTbl1.split(',')

					# Remove the last null item
					self.colListTbl1.pop()

					# Test string for Alpha-Numeric characters only
					for item in self.colListTbl1:
						ctr = 0
						isalnum = item.isalnum()
						# print("Is String Alphanumeric : ", isalnum)
						if isalnum == False:
							tkinter.messagebox.showinfo(title="Show Info", message="Error in Column List For Table 1\n non-Alpha-Numeric Characters Are Removed", parent=CenterTopFrame2)
							s = ''.join(ch for ch in item if ch.isalnum())
							self.colListTbl1[ctr] = s


					# Display list in Summary Area
					self.lblColListTbl1 = Label(TopFrame3, text="Names = " + str(self.colListTbl1) , font=("ariel", 16, "bold"), height=1, fg="red2", bg="white")
					self.lblColListTbl1.place(x=300, y=50)

					self.colbtnSubmit1.destroy()


				def colSubmit2():
					# Create the Column List for Table 2
					ctrNbr = 1				
					self.colListTbl2 = ""

					for entry in self.my_entries2:
						if ctrNbr <= int(self.txtColNbr2.get()):
							self.colListTbl2 = self.colListTbl2 + str(entry.get()) + ','
							ctrNbr += 1
						else:
							self.colListTbl2 = self.colListTbl2 + str(entry.get())
					# Split the string based on comma delimiter
					self.colListTbl2 = self.colListTbl2.split(',')

					# Remove the last null item
					self.colListTbl2.pop()

					# Test string for Alpha-Numeric characters only
					for item in self.colListTbl2:
						ctr = 0
						isalnum = item.isalnum()
						# print("Is String Alphanumeric : ", isalnum)
						if isalnum == False:
							tkinter.messagebox.showinfo(title="Show Info", message="Error in Column List For Table 2\n non-Alpha-Numeric Characters Are Removed", parent=CenterTopFrame2)
							s = ''.join(ch for ch in item if ch.isalnum())
							self.colListTbl2[ctr] = s

					# Display list in Summary Area
					self.lblColListTbl2 = Label(TopFrame3, text="Names = " + str(self.colListTbl2) , font=("ariel", 16, "bold"), height=1, fg="red2", bg="white")
					self.lblColListTbl2.place(x=300, y=80)

					self.colbtnSubmit2.destroy()

				def colSubmit3():
					# Create the Column List for Table 3
					ctrNbr = 1				
					self.colListTbl3 = ""

					for entry in self.my_entries3:
						if ctrNbr <= int(self.txtColNbr3.get()):
							self.colListTbl3 = self.colListTbl3 + str(entry.get()) + ','
							ctrNbr += 1
						else:
							self.colListTbl3 = self.colListTbl3 + str(entry.get())
					# Split the string based on comma delimiter
					self.colListTbl3 = self.colListTbl3.split(',')

					# Remove the last null item
					self.colListTbl3.pop()

					# Print test the column name list for completion
					# print("Column List for Table 3 is: ", self.colListTbl3)

					# Test string for Alpha-Numeric characters only
					for item in self.colListTbl3:
						ctr = 0
						isalnum = item.isalnum()
						# print("Is String Alphanumeric : ", isalnum)
						if isalnum == False:
							tkinter.messagebox.showinfo(title="Show Info", message="Error in Column List For Table 3\n non-Alpha-Numeric Characters Are Removed", parent=CenterTopFrame2)
							s = ''.join(ch for ch in item if ch.isalnum())
							self.colListTbl3[ctr] = s

					# Display list in Summary Area
					self.lblColListTbl3 = Label(TopFrame3, text="Names = " + str(self.colListTbl3) , font=("ariel", 16, "bold"), height=1, fg="red2", bg="white")
					self.lblColListTbl3.place(x=300, y=110)

					self.colbtnSubmit3.destroy()

				def colSubmit4():
					# Create the Column List for Table 4
					ctrNbr = 1				
					self.colListTbl4 = ""

					for entry in self.my_entries4:
						if ctrNbr <= int(self.txtColNbr4.get()):
							self.colListTbl4 = self.colListTbl4 + str(entry.get()) + ','
							ctrNbr += 1
						else:
							self.colListTbl4 = self.colListTbl4 + str(entry.get())
					# Split the string based on comma delimiter
					self.colListTbl4 = self.colListTbl4.split(',')

					# Remove the last null item
					self.colListTbl4.pop()

					# Test string for Alpha-Numeric characters only
					for item in self.colListTbl4:
						ctr = 0
						isalnum = item.isalnum()
						# print("Is String Alphanumeric : ", isalnum)
						if isalnum == False:
							tkinter.messagebox.showinfo(title="Show Info", message="Error in Column List For Table 4\n non-Alpha-Numeric Characters Are Removed", parent=MainFrame1)
							s = ''.join(ch for ch in item if ch.isalnum())
							self.colListTbl4[ctr] = s

					# Display list in Summary Area
					self.lblColListTbl4 = Label(TopFrame3, text="Names = " + str(self.colListTbl4) , font=("ariel", 16, "bold"), height=1, fg="red2", bg="white")
					self.lblColListTbl4.place(x=300 , y=140)

					self.colbtnSubmit4.destroy()			

				def tbl1ColNames():
					# Button Setup
					self.colbtnSubmit1 = Button(MidLeftFrame, text="Submit", width=6, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=colSubmit1, state="normal")
					self.colbtnSubmit1.place(x=10, y=310)

					# Set string for Column Header Presentation
					self.tblStr1 = "Columns in >>> " + str(self.tblName1)
					# print("self.tblStr1 = ", self.tblStr1)

					# 	#=========== Header for Data Block ==========
					self.lblColTbl1 = Label(MidLeftFrame,text=self.tblStr1, font=("ariel", 20, "bold", "underline"), fg="black", bg="cyan2")
					self.lblColTbl1.place(x=20, y=10)

					# Set Starting Location Axis Parameters
					Loc_x = 4
					Loc_y = 55
					z = 1

					while (z <= int(self.txtColNbr1.get())) and (z <= 7):
						self.lnNbrBox1 = Label(MidLeftFrame,text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
						self.lnNbrBox1.place(x=(Loc_x), y=Loc_y)

						ent1 = Entry(MidLeftFrame, width=11, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
						ent1.place(x=(Loc_x + 18), y=Loc_y)

						self.my_entries1.append(ent1)

						Loc_y += 36
						z += 1
					next

					# Reset Starting Location Axis Parameters
					Loc_x = 165
					Loc_y = 55

					while (z <= int(self.txtColNbr1.get())):
						self.lnNbrBox1 = Label(MidLeftFrame,text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
						self.lnNbrBox1.place(x=(Loc_x), y=Loc_y)

						ent1 = Entry(MidLeftFrame, width=11, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
						ent1.place(x=(Loc_x + 25), y=Loc_y)

						self.my_entries1.append(ent1)

						Loc_y += 36
						z += 1
					next

				def tbl2ColNames():
					# Button Setup
					self.colbtnSubmit2 = Button(MidCenterFrame1, text="Submit", width=6, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=colSubmit2, state="normal")
					self.colbtnSubmit2.place(x=10, y=310)

					# Set string for Column Header Presentation
					self.tblStr2 = "Columns in >>> " + str(self.tblName2)
					# print("self.tblStr2 = ", self.tblStr2)

					# 	#=========== Header for Data Block ==========
					self.lblColTbl2 = Label(MidCenterFrame1,text=self.tblStr2,font=("ariel", 20, "bold", "underline"), fg="black", bg="cyan2")
					self.lblColTbl2.place(x=20, y=10)

					# Set Starting Location Axis Parameters
					Loc_x = 4
					Loc_y = 55
					z = 1

					while (z <= int(self.txtColNbr2.get())) and (z <= 7):
						self.lnNbrBox2 = Label(MidCenterFrame1,text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
						self.lnNbrBox2.place(x=(Loc_x), y=Loc_y)

						ent2 = Entry(MidCenterFrame1, width=11, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
						ent2.place(x=(Loc_x + 18), y=Loc_y)

						self.my_entries2.append(ent2)

						Loc_y += 36
						z += 1
					next

					# Reset Starting Location Axis Parameters
					Loc_x = 165
					Loc_y = 55

					while (z <= int(self.txtColNbr2.get())):
						self.lnNbrBox2 = Label(MidCenterFrame1,text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
						self.lnNbrBox2.place(x=(Loc_x), y=Loc_y)

						ent2 = Entry(MidCenterFrame1, width=11, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
						ent2.place(x=(Loc_x + 25), y=Loc_y)

						self.my_entries2.append(ent2)

						Loc_y += 36
						z += 1
					next

				def tbl3ColNames():
					# Button Setup
					self.colbtnSubmit3 = Button(MidCenterFrame2, text="Submit", width=6, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=colSubmit3, state="normal")
					self.colbtnSubmit3.place(x=10, y=310)

					# Set string for Column Header Presentation
					self.tblStr3 = "Columns in >>> " + str(self.tblName3)
					# print("self.tblStr3 = ", self.tblStr3)

					# 	#=========== Header for Data Block ==========
					self.lblColTbl3 = Label(MidCenterFrame2,text=self.tblStr3,font=("ariel", 20, "bold", "underline"), fg="black", bg="cyan2")
					self.lblColTbl3.place(x=20, y=10)

					# Set Starting Location Axis Parameters
					Loc_x = 4
					Loc_y = 55
					z = 1

					while (z <= int(self.txtColNbr3.get())) and (z <= 7):
						self.lnNbrBox3 = Label(MidCenterFrame2,text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
						self.lnNbrBox3.place(x=(Loc_x), y=Loc_y)

						ent3 = Entry(MidCenterFrame2, width=11, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
						ent3.place(x=(Loc_x + 18), y=Loc_y)

						self.my_entries3.append(ent3)

						Loc_y += 36
						z += 1
					next

					# Reset Starting Location Axis Parameters
					Loc_x = 157
					Loc_y = 55

					while (z <= int(self.txtColNbr3.get())):
						self.lnNbrBox3 = Label(MidCenterFrame2,text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
						self.lnNbrBox3.place(x=(Loc_x), y=Loc_y)

						ent3 = Entry(MidCenterFrame2, width=11, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
						ent3.place(x=(Loc_x + 25), y=Loc_y)

						self.my_entries3.append(ent3)

						Loc_y += 36
						z += 1
					next

				def tbl4ColNames():
					# Button Setup
					self.colbtnSubmit4 = Button(MidRightFrame, text="Submit", width=6, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=colSubmit4, state="normal")
					self.colbtnSubmit4.place(x=10, y=310)

					# Set string for Column Header Presentation
					self.tblStr4 = "Columns in >>> " + str(self.tblName4)
					# print("self.tblStr4 = ", self.tblStr4)

					# 	#=========== Header for Data Block ==========
					self.lblColTbl4 = Label(MidRightFrame,text=self.tblStr4,font=("ariel", 20, "bold", "underline"), fg="black", bg="cyan2")
					self.lblColTbl4.place(x=20, y=10)

					# Set Starting Location Axis Parameters
					Loc_x = 4
					Loc_y = 55
					z = 1

					while (z <= int(self.txtColNbr4.get())) and (z <= 7):
						self.lnNbrBox4 = Label(MidRightFrame,text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
						self.lnNbrBox4.place(x=(Loc_x), y=Loc_y)

						ent4 = Entry(MidRightFrame, width=11, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
						ent4.place(x=(Loc_x + 18), y=Loc_y)

						self.my_entries4.append(ent4)

						Loc_y += 36
						z += 1
					next

					# Reset Starting Location Axis Parameters
					Loc_x = 157
					Loc_y = 55

					while (z <= int(self.txtColNbr4.get())):
						self.lnNbrBox4 = Label(MidRightFrame,text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="white")
						self.lnNbrBox4.place(x=(Loc_x), y=Loc_y)

						ent4 = Entry(MidRightFrame, width=11, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="red2", bg="wheat1")
						ent4.place(x=(Loc_x + 25), y=Loc_y)

						self.my_entries4.append(ent4)

						Loc_y += 36
						z += 1
					next

				if int(self.nbrTbls) == 1:
					tbl1ColNames()
				if int(self.nbrTbls) == 2:
					tbl1ColNames()
					tbl2ColNames()
				if int(self.nbrTbls) == 3:
					tbl1ColNames()
					tbl2ColNames()
					tbl3ColNames()
				if int(self.nbrTbls) == 4:
					tbl1ColNames()
					tbl2ColNames()
					tbl3ColNames()
					tbl4ColNames()

			#--------------------------------------------------------------#
			############## 6. End - Add Column Names to Table(s) ###########
			#--------------------------------------------------------------#

			#--------------------------------------------------------------#
			################## 7. Start - Delete Columns ###################
			#--------------------------------------------------------------#	
			if v.get() == 7:
				# self.chars_to_check = ["y", "Y", "n", "N"]

				def closeChoice():
					if self.nbrTbls == 1:
						self.Frame_d.destroy()
					elif self.nbrTbls == 2:
						self.Frame_e.destroy()
						self.Frame_d.destroy()
					elif self.nbrTbls == 3:
						self.Frame_f.destroy()	
						self.Frame_e.destroy()
						self.Frame_d.destroy()
					elif self.nbrTbls == 4:
						self.Frame_g.destroy()
						self.Frame_f.destroy()	
						self.Frame_e.destroy()
						self.Frame_d.destroy()

					self.TopFrame4.destroy()

					v.set(0)
					actionMenu()

				def submitChg1():
					if self.mkr1 == "Changes":
						# Destroy original elements to be changed in this section	
						self.txtColNbr1.destroy()
						self.lblColListTbl1.destroy()

						# Display the Number of Columns in Summary Section - TopFrame3					
						self.colNbr1 = int(len(self.colListTbl1))
						# print("New Column Quantity for Table 1 = ", self.colNbr1)

						self.lblColNbr1 = Label(CenterTopFrame2,text="Number Columns - Table 1", bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
						self.lblColNbr1.place(x=5, y=52)

						self.txtColNbr1 = Label(CenterTopFrame2, text=self.colNbr1, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
						self.txtColNbr1.place(x=250, y=50)	
						
						# Display the Column List in BottomRightFrame
						# print("New Column List for Table 1 = ", self.colListTbl1)

						# Display the Column Quantity in Summary Section - TopFrame3
						self.tbl1ColNbr = Label(TopFrame3, text="Cols. = " + str(self.colNbr1) , font=("ariel", 16, "bold"), height=1, fg="dodger blue", bg="white")
						self.tbl1ColNbr.place(x=195, y=50)

						# Display the Column Names in Summary Section - TopFrame3
						self.lblColListTbl1 = Label(TopFrame3, text="Names = " + str(self.colListTbl1) , font=("ariel", 16, "bold"), height=1, fg="dodger blue", bg="white")
						self.lblColListTbl1.place(x=300, y=50)

						# Change the Column Name Listing in the MidLeftFrame (2 Steps)
						# Step 1 -  delete the current presentation
						for widgets in MidLeftFrame.winfo_children():
							# print("widget = ", widgets)
							widgets.destroy()

						# Step 2 - Populate the new information 
						# Button Setup
						self.colBtnSubmit1 = Button(self.Frame_d, text="Next", width=4, height=1, font=("ariel", 16, "bold"), fg="black", bg="white", command="", state="disabled")
						self.colBtnSubmit1.place(x=10, y=650)

						self.delColBtn1a = Button(self.Frame_d, text="Submit", width=4, font=("ariel", 16, "bold"), command=submitChg1, fg="black", bg="PaleGreen2", state='disabled')
						self.delColBtn1a.place(x=110, y=650)

						self.delColBtn1b = Button(self.Frame_d, text="Close", width=4, font=("ariel", 16, "bold"), command=closeChoice, fg="black", bg="PaleGreen2", state='normal')
						self.delColBtn1b.place(x=205, y=650)

						# Set string for Column Header Presentation
						self.tblStr1 = "Columns in >>> " + str(self.tblName1)
						# print("self.tblStr1 = ", self.tblStr1)

						# 	#=========== Header for Data Block ==========
						self.lblColTbl1 = Label(MidLeftFrame,text=self.tblStr1, font=("ariel", 20, "bold", "underline"), fg="black", bg="cyan2")
						self.lblColTbl1.place(x=20, y=10)

						# Set Starting Location Axis Parameters
						Loc_x = 4
						Loc_y = 55
						z = 1

						while (z <= int(len(self.colListTbl1))) and (z <= 7):
							self.lnNbrBox1 = Label(MidLeftFrame,text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							self.lnNbrBox1.place(x=(Loc_x), y=Loc_y)

							colName1 = self.colListTbl1[z-1]
							# print("colName1 = ", colName1)

							newColName1 = Label(MidLeftFrame, text=colName1, width=11, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							newColName1.place(x=(Loc_x + 18), y=Loc_y)

							Loc_y += 36
							z += 1
						next

						# Reset Starting Location Axis Parameters
						Loc_x = 155
						Loc_y = 55

						while (z <= int(len(self.colListTbl1))):
							self.lnNbrBox1 = Label(MidLeftFrame,text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							self.lnNbrBox1.place(x=(Loc_x), y=Loc_y)

							colName1 = self.colListTbl1[z-1]

							newColName1 = Label(MidLeftFrame, text=colName1, width=11, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							newColName1.place(x=(Loc_x + 25), y=Loc_y)
			
							Loc_y += 36
							z += 1
						next

					else:
						self.addColBtnSubmit.destroy()
						self.addColBtnExit.destroy()

				def submitChg2():
					if self.mkr2 == "Changes":
						# Destroy original elements to be changed in this section	
						self.txtColNbr2.destroy()
						self.lblColListTbl2.destroy()

						# Display the Number of Columns in Summary Section - TopFrame3					
						self.colNbr2 = int(len(self.colListTbl2))
						# print("New Column Quantity for Table 2 = ", self.colNbr2)

						self.lblColNbr2 = Label(CenterTopFrame2,text="Number Columns - Table 2", bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
						self.lblColNbr2.place(x=5, y=82)

						self.txtColNbr2 = Label(CenterTopFrame2, text=self.colNbr2, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
						self.txtColNbr2.place(x=250, y=80)	
						

						# Display the Column List in BottomRightFrame
						# print("New Column List for Table 2 = ", self.colListTbl2)

						# Display the Column Quantity in Summary Section - TopFrame3
						self.tbl2ColNbr = Label(TopFrame3, text="Cols. = " + str(self.colNbr2) , font=("ariel", 16, "bold"), height=1, fg="dodger blue", bg="white")
						self.tbl2ColNbr.place(x=195, y=80)

						# Display the Column Names in Summary Section - TopFrame3
						self.lblColListTbl2 = Label(TopFrame3, text="Names = " + str(self.colListTbl2) , font=("ariel", 16, "bold"), height=1, fg="dodger blue", bg="white")
						self.lblColListTbl2.place(x=300, y=80)

						# Change the Column Name Listing in the MidLeftFrame (2 Steps)
						# Step 1 -  delete the current presentation
						for widgets in MidCenterFrame1.winfo_children():
							# print("widget = ", widgets)
							widgets.destroy()

						self.colBtnSubmit2 = Button(self.Frame_e, text="Next", width=4, font=("ariel", 16, "bold"), command=colTbl1Chg, fg="black", bg="PaleGreen2", state='disabled')
						self.colBtnSubmit2.place(x=10, y=650)

						self.delColBtn2a = Button(self.Frame_e, text="Submit", width=4, font=("ariel", 16, "bold"), command=submitChg1, fg="black", bg="PaleGreen2", state='disabled')
						self.delColBtn2a.place(x=110, y=650)

						self.delColBtn2b = Button(self.Frame_e, text="Close", width=4, font=("ariel", 16, "bold"), command=closeChoice, fg="black", bg="PaleGreen2", state='normal')
						self.delColBtn2b.place(x=205, y=650)

						# Set string for Column Header Presentation
						self.tblStr2 = "Columns in >>> " + str(self.tblName2)
						# print("self.tblStr1 = ", self.tblStr1)

						# 	#=========== Header for Data Block ==========
						self.lblColTbl2 = Label(MidCenterFrame1,text=self.tblStr2, font=("ariel", 20, "bold", "underline"), fg="black", bg="cyan2")
						self.lblColTbl2.place(x=20, y=10)

						# Set Starting Location Axis Parameters
						Loc_x = 4
						Loc_y = 55
						z = 1

						while (z <= int(len(self.colListTbl2))) and (z <= 7):
							self.lnNbrBox2 = Label(MidCenterFrame1,text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							self.lnNbrBox2.place(x=(Loc_x), y=Loc_y)

							colName2 = self.colListTbl2[z-1]
							# print("colName1 = ", colName1)

							newColName2 = Label(MidCenterFrame1, text=colName2, width=11, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							newColName2.place(x=(Loc_x + 18), y=Loc_y)

							Loc_y += 36
							z += 1
						next

						# Reset Starting Location Axis Parameters
						Loc_x = 155
						Loc_y = 55

						while (z <= int(len(self.colListTbl2))):

							self.lnNbrBox2 = Label(MidCertenFrame1,text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							self.lnNbrBox2.place(x=(Loc_x), y=Loc_y)

							colName2 = self.colListTbl1[z-1]

							newColName2 = Label(MidCenterFrame1, text=colName2, width=11, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							newColName2.place(x=(Loc_x + 25), y=Loc_y)
					
							Loc_y += 36
							z += 1
						next

					else:
						self.colBtnSubmit2.destroy()
						self.colbtnExit2.destroy()

				def submitChg3():
					if self.mkr3 == "Changes":
						# Destroy original elements to be changed in this section	
						self.txtColNbr3.destroy()
						self.lblColListTbl3.destroy()

						# Display the Number of Columns in Summary Section - TopFrame3					
						self.colNbr3 = int(len(self.colListTbl3))
						# print("New Column Quantity for Table 3 = ", self.colNbr3)

						self.lblColNbr3 = Label(CenterTopFrame2,text="Number Columns - Table 3", bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
						self.lblColNbr3.place(x=5, y=112)

						self.txtColNbr3 = Label(CenterTopFrame2, text=self.colNbr3, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
						self.txtColNbr3.place(x=250, y=110)	
						

						# Display the Column List in BottomRightFrame
						# print("New Column List for Table 3 = ", self.colListTbl3)

						# Display the Column Quantity in Summary Section - TopFrame3
						self.tbl3ColNbr = Label(TopFrame3, text="Cols. = " + str(self.colNbr3) , font=("ariel", 16, "bold"), height=1, fg="dodger blue", bg="white")
						self.tbl3ColNbr.place(x=195, y=110)

						# Display the Column Names in Summary Section - TopFrame3
						self.lblColListTbl3 = Label(TopFrame3, text="Names = " + str(self.colListTbl3) , font=("ariel", 16, "bold"), height=1, fg="dodger blue", bg="white")
						self.lblColListTbl3.place(x=300, y=110)

						# Change the Column Name Listing in the MidLeftFrame (2 Steps)
						# Step 1 -  delete the current presentation
						for widgets in MidCenterFrame2.winfo_children():
							# print("widget = ", widgets)
							widgets.destroy()

						self.colBtnSubmit3 = Button(self.Frame_f, text="Next", width=4, font=("ariel", 16, "bold"), command=colTbl3Chg, fg="black", bg="PaleGreen2", state='disabled')
						self.colBtnSubmit3.place(x=10, y=650)

						self.delColBtn3a = Button(self.Frame_f, text="Submit", width=4, font=("ariel", 16, "bold"), command=submitChg3, fg="black", bg="PaleGreen2", state='disabled')
						self.delColBtn3a.place(x=110, y=650)

						self.delColBtn3b = Button(self.Frame_f, text="Close", width=4, font=("ariel", 16, "bold"), command=closeChoice, fg="black", bg="PaleGreen2", state='normal')
						self.delColBtn3b.place(x=205, y=650)

						# Set string for Column Header Presentation
						self.tblStr3 = "Columns in >>> " + str(self.tblName3)
						# print("self.tblStr1 = ", self.tblStr1)

						# 	#=========== Header for Data Block ==========
						self.lblColTbl3 = Label(MidCenterFrame2,text=self.tblStr3, font=("ariel", 20, "bold", "underline"), fg="black", bg="cyan2")
						self.lblColTbl3.place(x=20, y=10)

						# Set Starting Location Axis Parameters
						Loc_x = 4
						Loc_y = 55
						z = 1

						while (z <= int(len(self.colListTbl3))) and (z <= 7):
							self.lnNbrBox3 = Label(MidCenterFrame2,text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							self.lnNbrBox3.place(x=(Loc_x), y=Loc_y)

							colName3 = self.colListTbl3[z-1]
							# print("colName1 = ", colName1)

							newColName3 = Label(MidCenterFrame2, text=colName3, width=11, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							newColName3.place(x=(Loc_x + 18), y=Loc_y)

							Loc_y += 36
							z += 1
						next

						# Reset Starting Location Axis Parameters
						Loc_x = 155
						Loc_y = 55

						while (z <= int(len(self.colListTbl3))):
							self.lnNbrBox3 = Label(MidCenterFrame2,text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							self.lnNbrBox3.place(x=(Loc_x), y=Loc_y)

							colName3 = self.colListTbl3[z-1]

							newColName3 = Label(MidCenterFrame2, text=colName3, width=11, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							newColName3.place(x=(Loc_x + 25), y=Loc_y)
					
							Loc_y += 36
							z += 1
						next

					else:
						self.colBtnSubmit3.destroy()
						self.colbtnExit3.destroy()					

				def submitChg4():
					if self.mkr4 == "Changes":
						# Destroy original elements to be changed in this section	
						self.txtColNbr4.destroy()
						self.lblColListTbl4.destroy()

						# Display the Number of Columns in Summary Section - TopFrame3					
						self.colNbr4 = int(len(self.colListTbl4))
						# print("New Column Quantity for Table 4 = ", self.colNbr4)

						self.lblColNbr4 = Label(CenterTopFrame2,text="Number Columns - Table 4", bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
						self.lblColNbr4.place(x=5, y=142)

						self.txtColNbr4 = Label(CenterTopFrame2, text=self.colNbr4, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
						self.txtColNbr4.place(x=250, y=140)	
						

						# Display the Column List in BottomRightFrame
						# print("New Column List for Table 4 = ", self.colListTbl4)

						# Display the Column Quantity in Summary Section - TopFrame3
						self.tbl4ColNbr = Label(TopFrame3, text="Cols. = " + str(self.colNbr4) , font=("ariel", 16, "bold"), height=1, fg="dodger blue", bg="white")
						self.tbl4ColNbr.place(x=195, y=140)

						# Display the Column Names in Summary Section - TopFrame3
						self.lblColListTbl4 = Label(TopFrame3, text="Names = " + str(self.colListTbl4) , font=("ariel", 16, "bold"), height=1, fg="dodger blue", bg="white")
						self.lblColListTbl4.place(x=300, y=140)

						# Change the Column Name Listing in the MidLeftFrame (2 Steps)
						# Step 1 -  delete the current presentation
						for widgets in MidRightFrame.winfo_children():
							# print("widget = ", widgets)
							widgets.destroy()

						self.colBtnSubmit4 = Button(self.Frame_g, text="Next", width=4, font=("ariel", 16, "bold"), command=colTbl4Chg, fg="black", bg="pale goldenrod", state='disabled')
						self.colBtnSubmit4.place(x=10, y=650)

						self.delColBtn4a = Button(self.Frame_g, text="Submit", width=4, font=("ariel", 16, "bold"), command=submitChg4, fg="black", bg="pale goldenrod", state='disabled')
						self.delColBtn4a.place(x=110, y=650)

						self.delColBtn4b = Button(self.Frame_g, text="Close", width=4, font=("ariel", 16, "bold"), command=closeChoice, fg="black", bg="pale goldenrod", state='normal')
						self.delColBtn4b.place(x=205, y=650)

						# Set string for Column Header Presentation
						self.tblStr4 = "Columns in >>> " + str(self.tblName4)
						# print("self.tblStr1 = ", self.tblStr1)

						# 	#=========== Header for Data Block ==========
						self.lblColTbl4 = Label(MidRightFrame,text=self.tblStr4, font=("ariel", 20, "bold", "underline"), fg="black", bg="cyan2")
						self.lblColTbl4.place(x=20, y=10)

						# Set Starting Location Axis Parameters
						Loc_x = 4
						Loc_y = 55
						z = 1

						while (z <= int(len(self.colListTbl4))) and (z <= 7):
							self.lnNbrBox4 = Label(MidRightFrame,text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							self.lnNbrBox4.place(x=(Loc_x), y=Loc_y)

							colName4 = self.colListTbl4[z-1]
							# print("colName4 = ", colName4)

							newColName4 = Label(MidRightFrame, text=colName4, width=11, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							newColName4.place(x=(Loc_x + 18), y=Loc_y)

							Loc_y += 36
							z += 1
						next

						# Reset Starting Location Axis Parameters
						Loc_x = 155
						Loc_y = 55

						while (z <= int(len(self.colListTbl4))):
							self.lnNbrBox4 = Label(MidRightFrame,text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							self.lnNbrBox4.place(x=(Loc_x), y=Loc_y)

							colName4 = self.colListTbl4[z-1]

							newColName4 = Label(MidRightFrame, text=colName4, width=11, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							newColName4.place(x=(Loc_x + 25), y=Loc_y)					
							Loc_y += 36
							z += 1
						next

					else:
						self.colbtnSubmit4.destroy()
						self.colbtnExit4.destroy()					

				def colTbl1Chg():
					# Set variables for this section
					entry_list1 = ""
					self.mkr1 = "Changes"
					self.newColListTbl1 = []

					# Create a Yes / No retention list
					for entries in self.my_entries1:
						entry_list1 = entry_list1 + str(entries.get())

					# print("entry_list1 = ", entry_list1)
					# print("self.colListTbl1 = ", self.colListTbl1)
	
					# Cycle through the entry list to retain or deleted selected items
					ctr = 0
					Loc_y = 87
					for entry in entry_list1:
						ctr = 0
						var1 = " "
						# print("entry  = ", entry)
						# print("self.colListTbl1 = ", self.colListTbl1)
						for char in self.chars_to_check:
							if entry == char:
								if entry == 'n' or entry == 'N':
									# print("ctr = ", ctr)
									# print("self.colListTbl1[ctr] = ", self.colListTbl1[ctr])
									var1 = self.colListTbl1[ctr]
									# print("var1 = ", var1)

									delColLbl1d = Label(self.Frame_d, text="Retained", font=("ariel", 16, "bold"), fg="dark slate blue", bg="PaleGreen2")
									delColLbl1d.place(x=200, y=(Loc_y))

									self.newColListTbl1.append(var1)

									var1 = " "
									ctr += 1

									break	

								elif entry == 'y' or entry == 'Y':
									delColLbl1d = Label(self.Frame_d, text="Deleted", font=("ariel", 16, "bold"), fg="indian red", bg="PaleGreen2")
									delColLbl1d.place(x=200, y=(Loc_y))

									self.newColListTbl1.append(var1)
									ctr += 1

									break

								else:
									tkinter.messagebox.showinfo(title="Incorrect Entry Choices", message="'Y, y, N, n' \n Only Characters Allowed\n A Correct Choice is\n Required in Every Block", parent=CenterTopFrame2)			

						Loc_y += 40

					# Remove all items in the Table 1 Column List
					self.colListTbl1 = []

					# Re-populate the Table 1 Column List after changes
					for item in self.newColListTbl1:
						if item != " ":
							self.colListTbl1.append(str(item))

					# print("self.colListTbl1(ln 1712) = ", self.colListTbl1)

					self.Nbr1 = 0
					for entry in entry_list1:
						if entry == 'y' or entry == 'Y':
							self.Nbr1 += 1
					
					if self.Nbr1 <= 0:		
						tkinter.messagebox.showinfo(title="Table 1 Column Delete", message="There Are No Recorded Changes\n In Table 1", parent=CenterTopFrame2)
						self.mkr1 = "No Changes"

					self.colBtnSubmit1 = Button(self.Frame_d, text="Next", width=4, font=("ariel", 16, "bold"), command=colTbl1Chg, fg="black", bg="PaleGreen2", state='disabled')
					self.colBtnSubmit1.place(x=10, y=650)

					self.delColBtn1a = Button(self.Frame_d, text="Submit", width=4, font=("ariel", 16, "bold"), command=submitChg1, fg="black", bg="PaleGreen2", state='normal')
					self.delColBtn1a.place(x=110, y=650)

					self.delColBtn1b = Button(self.Frame_d, text="Close", width=4, font=("ariel", 16, "bold"), command=closeChoice, fg="black", bg="PaleGreen2", state='normal')
					self.delColBtn1b.place(x=205, y=650)


				def colTbl2Chg():
					# Set variables for this section
					entry_list2 = ""
					self.mkr2 = "Changes"
					self.newColListTbl2 = []

					# Create a Yes / No retention list
					for entries in self.my_entries2:
						entry_list2 = entry_list2 + str(entries.get())

					# print("entry_list2 = ", entry_list2)
					# print("self.colListTbl2 = ", self.colListTbl2)
	
					# Cycle through the entry list to retain or deleted selected items
					ctr = 0
					Loc_y = 87
					for entry in entry_list2:
						# ctr = 0
						var2 = " "
						# print("entry  = ", entry)
						# print("self.colListTbl2 = ", self.colListTbl2)
						for char in self.chars_to_check:
							if entry == char:
								if entry == 'n' or entry == 'N':
									# print("ctr = ", ctr)
									# print("self.colListTbl2[ctr] = ", self.colListTbl2[ctr])
									var2 = self.colListTbl2[ctr]
									# print("var2 = ", var2)

									delColLbl2d = Label(self.Frame_e, text="Retained", font=("ariel", 16, "bold"), fg="dark slate blue", bg="pale goldenrod")
									delColLbl2d.place(x=200, y=(Loc_y))

									self.newColListTbl2.append(var2)

									var2 = " "
									ctr += 1

									break	

								elif entry == 'y' or entry == 'Y':
									delColLbl2d = Label(self.Frame_e, text="Deleted", font=("ariel", 16, "bold"), fg="indian red", bg="pale goldenrod")
									delColLbl2d.place(x=200, y=(Loc_y))

									self.newColListTbl2.append(var2)
									ctr += 1

									break

								else:
									tkinter.messagebox.showinfo(title="Incorrect Entry Choices", message="'Y, y, N, n' \n Only Characters Allowed\n A Correct Choice is\n Required in Every Block", parent=CenterTopFrame2)			

						Loc_y += 40

					# Remove all items in the Table 1 Column List
					self.colListTbl2 = []

					# Re-populate the Table 1 Column List after changes
					for item in self.newColListTbl2:
						if item != " ":
							self.colListTbl2.append(str(item))

					# print("self.colListTbl2(ln 1795) = ", self.colListTbl2)

					self.Nbr2 = 0
					for entry in entry_list2:
						if entry == 'y' or entry == 'Y':
							self.Nbr2 += 1
					
					if self.Nbr2 <= 0:		
						tkinter.messagebox.showinfo(title="Table 2 Column Delete", message="There Are No Recorded Changes\n In Table 2", parent=CenterTopFrame2)
						self.mkr2 = "No Changes"

					self.colBtnSubmit2 = Button(self.Frame_e, text="Next", width=4, font=("ariel", 16, "bold"), command=colTbl2Chg, fg="black", bg="PaleGreen2", state='disabled')
					self.colBtnSubmit2.place(x=10, y=650)

					self.delColBtn2a = Button(self.Frame_e, text="Submit", width=4, font=("ariel", 16, "bold"), command=submitChg2, fg="black", bg="PaleGreen2", state='normal')
					self.delColBtn2a.place(x=110, y=650)

					self.delColBtn2b = Button(self.Frame_e, text="Close", width=4, font=("ariel", 16, "bold"), command=closeChoice, fg="black", bg="PaleGreen2", state='normal')
					self.delColBtn2b.place(x=205, y=650)

				def colTbl3Chg():
					# Set variables for this section
					entry_list3 = ""
					self.mkr3 = "Changes"
					self.newColListTbl3 = []

					# Create a Yes / No retention list
					for entries in self.my_entries3:
						entry_list3 = entry_list3 + str(entries.get())

					# print("entry_list3 = ", entry_list3)
					# print("self.colListTbl2 = ", self.colListTbl2)
	
					# Cycle through the entry list to retain or deleted selected items
					ctr = 0
					Loc_y = 87
					for entry in entry_list3:
						# ctr = 0
						var3 = " "
						# print("entry  = ", entry)
						# print("self.colListTbl2 = ", self.colListTbl2)
						for char in self.chars_to_check:
							if entry == char:
								if entry == 'n' or entry == 'N':
									# print("ctr = ", ctr)
									# print("self.colListTbl2[ctr] = ", self.colListTbl2[ctr])
									var3 = self.colListTbl3[ctr]
									# print("var2 = ", var2)

									delColLbl3d = Label(self.Frame_f, text="Retained", font=("ariel", 16, "bold"), fg="dark slate blue", bg="PaleGreen2")
									delColLbl3d.place(x=200, y=(Loc_y))

									self.newColListTbl3.append(var3)

									var3 = " "
									ctr += 1

									break	

								elif entry == 'y' or entry == 'Y':
									delColLbl3d = Label(self.Frame_f, text="Deleted", font=("ariel", 16, "bold"), fg="indian red", bg="PaleGreen2")
									delColLbl3d.place(x=200, y=(Loc_y))

									self.newColListTbl3.append(var3)
									ctr += 1

									break

								else:
									tkinter.messagebox.showinfo(title="Incorrect Entry Choices", message="'Y, y, N, n' \n Only Characters Allowed\n A Correct Choice is\n Required in Every Block", parent=CenterTopFrame2)			

						Loc_y += 40

					# Remove all items in the Table 1 Column List
					self.colListTbl3 = []

					# Re-populate the Table 1 Column List after changes
					for item in self.newColListTbl3:
						if item != " ":
							self.colListTbl3.append(str(item))

					# print("self.colListTbl3(ln 2045) = ", self.colListTbl3)

					self.Nbr3 = 0
					for entry in entry_list3:
						if entry == 'y' or entry == 'Y':
							self.Nbr3 += 1
					
					if self.Nbr3 <= 0:		
						tkinter.messagebox.showinfo(title="Table 3 Column Delete", message="There Are No Recorded Changes\n In Table 3", parent=CenterTopFrame2)
						self.mkr3 = "No Changes"

					self.colBtnSubmit3 = Button(self.Frame_f, text="Next", width=4, font=("ariel", 16, "bold"), command=colTbl3Chg, fg="black", bg="PaleGreen2", state='disabled')
					self.colBtnSubmit3.place(x=10, y=650)

					self.delColBtn3a = Button(self.Frame_f, text="Submit", width=4, font=("ariel", 16, "bold"), command=submitChg3, fg="black", bg="PaleGreen2", state='normal')
					self.delColBtn3a.place(x=110, y=650)

					self.delColBtn3b = Button(self.Frame_f, text="Close", width=4, font=("ariel", 16, "bold"), command=closeChoice, fg="black", bg="PaleGreen2", state='normal')
					self.delColBtn3b.place(x=205, y=650)


				def colTbl4Chg():
					# Set variables for this section
					entry_list4 = ""
					self.mkr4 = "Changes"
					self.newColListTbl4 = []

					# Create a Yes / No retention list
					for entries in self.my_entries4:
						entry_list4 = entry_list4 + str(entries.get())

					# print("entry_list4 = ", entry_list4)
					# print("self.colListTbl4 = ", self.colListTbl4)
	
					# Cycle through the entry list to retain or deleted selected items
					ctr = 0
					Loc_y = 87
					for entry in entry_list4:
						# ctr = 0
						var4 = " "
						# print("entry  = ", entry)
						# print("self.colListTbl4 = ", self.colListTbl4)
						for char in self.chars_to_check:
							if entry == char:
								if entry == 'n' or entry == 'N':
									# print("ctr = ", ctr)
									# print("self.colListTbl4[ctr] = ", self.colListTbl4[ctr])
									var4 = self.colListTbl4[ctr]
									# print("var4 = ", var4)

									delColLbl4d = Label(self.Frame_g, text="Retained", font=("ariel", 16, "bold"), fg="dark slate blue", bg="pale goldenrod")
									delColLbl4d.place(x=200, y=(Loc_y))

									self.newColListTbl4.append(var4)

									var4 = " "
									ctr += 1

									break	

								elif entry == 'y' or entry == 'Y':
									delColLbl4d = Label(self.Frame_g, text="Deleted", font=("ariel", 16, "bold"), fg="indian red", bg="pale goldenrod")
									delColLbl4d.place(x=200, y=(Loc_y))

									self.newColListTbl4.append(var4)
									ctr += 1

									break

								else:
									tkinter.messagebox.showinfo(title="Incorrect Entry Choices", message="'Y, y, N, n' \n Only Characters Allowed\n A Correct Choice is\n Required in Every Block", parent=CenterTopFrame2)			

						Loc_y += 40

					# Remove all items in the Table 1 Column List
					self.colListTbl4 = []

					# Re-populate the Table 1 Column List after changes
					for item in self.newColListTbl4:
						if item != " ":
							self.colListTbl4.append(str(item))

					# print("self.colListTbl4(ln 2053) = ", self.colListTbl4)

					self.Nbr4 = 0
					for entry in entry_list4:
						if entry == 'y' or entry == 'Y':
							self.Nbr4 += 1
					
					if self.Nbr4 <= 0:		
						tkinter.messagebox.showinfo(title="Table 4 Column Delete", message="There Are No Recorded Changes\n In Table 4", parent=CenterTopFrame2)
						self.mkr4 = "No Changes"

					self.colBtnSubmit4 = Button(self.Frame_g, text="Next", width=4, font=("ariel", 16, "bold"), command=colTbl4Chg, fg="black", bg="pale goldenrod", state='disabled')
					self.colBtnSubmit4.place(x=10, y=650)

					self.delColBtn4a = Button(self.Frame_g, text="Submit", width=4, font=("ariel", 16, "bold"), command=submitChg4, fg="black", bg="pale goldenrod", state='normal')
					self.delColBtn4a.place(x=110, y=650)

					self.delColBtn4b = Button(self.Frame_g, text="Close", width=4, font=("ariel", 16, "bold"), command=closeChoice, fg="black", bg="pale goldenrod", state='normal')
					self.delColBtn4b.place(x=205, y=650)


				def drawFrame1():
					delColLbl1 = Label(self.Frame_d, text="Table 1: " + str(self.tblName1),font=("ariel", 16, "bold", "underline"), fg="black", bg="PaleGreen2")
					delColLbl1.place(x=50, y=27)

					delColLbl1a = Label(self.Frame_d, text="Column", font=("ariel", 16, "bold", "underline"), fg="black", bg="PaleGreen2")
					delColLbl1a.place(x=20, y=52)

					delColLbl1b = Label(self.Frame_d, text="Delete(Y/N) - Reqd.", font=("ariel", 16, "bold", "underline"), fg="black", bg="PaleGreen2")
					delColLbl1b.place(x=120, y=52)

					self.my_entries1 = []
					# z = 1
					Loc_y = 87
					# print("self.colListTbl1 (Ln 1451) = ", self.colListTbl1)

					for x in range(int(self.txtColNbr1.get())):
						# print(self.colListTbl1[x]),
						# while (z <= int(self.NbrColsTbl1)):
						delColLbl1c = Label(self.Frame_d, text=self.colListTbl1[x], font=("ariel", 16, "bold"), fg="black", bg="PaleGreen2")
						delColLbl1c.place(x=25, y=(Loc_y))

						self.my_entry1 = Entry(self.Frame_d, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="black", bg="PaleGreen2")
						self.my_entry1.place(x=147, y=(Loc_y))

						self.my_entries1.append(self.my_entry1)

						Loc_y += 40
						
					next

					self.colBtnSubmit1 = Button(self.Frame_d, text="Next", width=4, font=("ariel", 16, "bold"), command=colTbl1Chg, fg="black", bg="PaleGreen2", state="normal")
					self.colBtnSubmit1.place(x=10, y=650)

					self.delColBtn1a = Button(self.Frame_d, text="Submit", width=4, font=("ariel", 16, "bold"), command=submitChg1, fg="black", bg="PaleGreen2", state='disabled')
					self.delColBtn1a.place(x=110, y=650)

					self.delColBtn1b = Button(self.Frame_d, text="Close", width=4, font=("ariel", 16, "bold"), command=closeChoice, fg="black", bg="PaleGreen2", state='normal')
					self.delColBtn1b.place(x=205, y=650)
			
					tkinter.messagebox.showinfo(title="Acceptable Entry Choices", message="Y, y, N, n \n Only Characters Allowed\n A Choice is Required in Every Block", parent=CenterTopFrame2)

				def drawFrame2():
					drawFrame1()

					delColLbl2 = Label(self.Frame_e, text="Table 2: " + str(self.tblName2),font=("ariel", 16, "bold", "underline"), fg="black", bg="pale goldenrod")
					delColLbl2.place(x=50, y=27)

					delColLbl2a = Label(self.Frame_e, text="Column", font=("ariel", 16, "bold", "underline"), fg="black", bg="pale goldenrod")
					delColLbl2a.place(x=20, y=52)

					delColLbl2b = Label(self.Frame_e, text="Delete(Y/N) - Reqd.", font=("ariel", 16, "bold", "underline"), fg="black", bg="pale goldenrod")
					delColLbl2b.place(x=120, y=52)

					self.my_entries2 = []
					# z = 1
					Loc_y = 87
					# print("self.colListTbl1 (Ln 1451) = ", self.colListTbl1)

					for x in range(int(self.txtColNbr2.get())):
						# print(self.colListTbl2[x]),
						# while (z <= int(self.NbrColsTbl2)):
						delColLbl2c = Label(self.Frame_e, text=self.colListTbl2[x], font=("ariel", 16, "bold"), fg="black", bg="pale goldenrod")
						delColLbl2c.place(x=25, y=(Loc_y))

						self.my_entry2 = Entry(self.Frame_e, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="black", bg="pale goldenrod")
						self.my_entry2.place(x=147, y=(Loc_y))

						self.my_entries2.append(self.my_entry2)

						Loc_y += 40
						
					next

					self.colBtnSubmit2 = Button(self.Frame_e, text="Next", width=4, font=("ariel", 16, "bold"), command=colTbl2Chg, fg="black", bg="pale goldenrod", state='normal')
					self.colBtnSubmit2.place(x=10, y=650)

					self.delColBtn2a = Button(self.Frame_e, text="Submit", width=4, font=("ariel", 16, "bold"), command=submitChg2, fg="black", bg="pale goldenrod", state='disabled')
					self.delColBtn2a.place(x=110, y=650)

					self.delColBtn2b = Button(self.Frame_e, text="Close", width=4, font=("ariel", 16, "bold"), command=closeChoice, fg="black", bg="pale goldenrod", state='normal')
					self.delColBtn2b.place(x=205, y=650)

					if self.nbrTbls == 2:
						tkinter.messagebox.showinfo(title="Acceptable Entry Choices", message="Y, y, N, n \n Only Characters Allowed\n A Choice is Required in Every Block", parent=CenterTopFrame2)

						tkinter.messagebox.showinfo(title="Multiple Table Entry Choices", message="Where There Are Multiple Tables Shown\n You Need Only Choose Impacted Table(s) ", parent=CenterTopFrame2)

				def drawFrame3():
					drawFrame2()

					delColLbl3 = Label(self.Frame_f, text="Table 3: " + str(self.tblName3),font=("ariel", 16, "bold", "underline"), fg="black", bg="PaleGreen2")
					delColLbl3.place(x=50, y=27)

					delColLbl3a = Label(self.Frame_f, text="Column", font=("ariel", 16, "bold", "underline"), fg="black", bg="PaleGreen2")
					delColLbl3a.place(x=20, y=52)

					delColLbl3b = Label(self.Frame_f, text="Delete(Y/N) - Reqd.", font=("ariel", 16, "bold", "underline"), fg="black", bg="PaleGreen2")
					delColLbl3b.place(x=120, y=52)

					self.my_entries3 = []
					# z = 1
					Loc_y = 87
					# print("self.colListTbl1 (Ln 1451) = ", self.colListTbl1)

					for x in range(int(self.txtColNbr3.get())):
						# print(self.colListTbl2[x]),
						# while (z <= int(self.NbrColsTbl2)):
						delColLbl3c = Label(self.Frame_f, text=self.colListTbl3[x], font=("ariel", 16, "bold"), fg="black", bg="PaleGreen2")
						delColLbl3c.place(x=25, y=(Loc_y))

						self.my_entry3 = Entry(self.Frame_f, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="black", bg="PaleGreen2")
						self.my_entry3.place(x=147, y=(Loc_y))

						self.my_entries3.append(self.my_entry3)

						Loc_y += 40
						
					next

					self.colBtnSubmit3 = Button(self.Frame_f, text="Next", width=4, font=("ariel", 16, "bold"), command=colTbl3Chg, fg="black", bg="PaleGreen2", state='normal')
					self.colBtnSubmit3.place(x=10, y=650)

					self.delColBtn3a = Button(self.Frame_f, text="Submit", width=4, font=("ariel", 16, "bold"), command=submitChg3, fg="black", bg="PaleGreen2", state='disabled')
					self.delColBtn3a.place(x=110, y=650)

					self.delColBtn3b = Button(self.Frame_f, text="Close", width=4, font=("ariel", 16, "bold"), command=closeChoice, fg="black", bg="PaleGreen2", state='normal')
					self.delColBtn3b.place(x=205, y=650)

					if self.nbrTbls == 3:
						tkinter.messagebox.showinfo(title="Acceptable Entry Choices", message="Y, y, N, n \n Only Characters Allowed\n A Choice is Required in Every Block", parent=CenterTopFrame2)

						tkinter.messagebox.showinfo(title="Multiple Table Entry Choices", message="Where There Are Multiple Tables Shown\n You Need Only Choose Impacted Table(s) ", parent=CenterTopFrame2)

				def drawFrame4():
					drawFrame3()

					delColLbl4 = Label(self.Frame_g, text="Table 4: " + str(self.tblName4),font=("ariel", 16, "bold", "underline"), fg="black", bg="Pale goldenrod")
					delColLbl4.place(x=50, y=27)

					delColLbl4a = Label(self.Frame_g, text="Column", font=("ariel", 16, "bold", "underline"), fg="black", bg="Pale goldenrod")
					delColLbl4a.place(x=20, y=52)

					delColLbl4b = Label(self.Frame_g, text="Delete(Y/N) - Reqd.", font=("ariel", 16, "bold", "underline"), fg="black", bg="Pale goldenrod")
					delColLbl4b.place(x=120, y=52)

					self.my_entries4 = []
					# z = 1
					Loc_y = 87
					# print("self.colListTbl4 (Ln 2216) = ", self.colListTbl4)

					for x in range(int(self.txtColNbr4.get())):
						# print(self.colListTbl4[x]),
						# while (z <= int(self.NbrColsTbl4)):
						delColLbl4c = Label(self.Frame_g, text=self.colListTbl4[x], font=("ariel", 16, "bold"), fg="black", bg="Pale goldenrod")
						delColLbl4c.place(x=25, y=(Loc_y))

						self.my_entry4 = Entry(self.Frame_g, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="black", bg="Pale goldenrod")
						self.my_entry4.place(x=147, y=(Loc_y))

						self.my_entries4.append(self.my_entry4)

						Loc_y += 40
						
					next

					self.colBtnSubmit4 = Button(self.Frame_g, text="Next", width=4, font=("ariel", 16, "bold"), command=colTbl4Chg, fg="black", bg="Pale goldenrod", state='normal')
					self.colBtnSubmit4.place(x=10, y=650)

					self.delColBtn4a = Button(self.Frame_g, text="Submit", width=4, font=("ariel", 16, "bold"), command=submitChg4, fg="black", bg="Pale goldenrod", state='disabled')
					self.delColBtn4a.place(x=110, y=650)

					self.delColBtn4b = Button(self.Frame_g, text="Close", width=4, font=("ariel", 16, "bold"), command=closeChoice, fg="black", bg="Pale goldenrod", state='normal')
					self.delColBtn4b.place(x=205, y=650)

					if self.nbrTbls == 4:
						tkinter.messagebox.showinfo(title="Acceptable Entry Choices", message="Y, y, N, n \n Only Characters Allowed\n A Choice is Required in Every Block", parent=CenterTopFrame2)

						tkinter.messagebox.showinfo(title="Multiple Table Entry Choices", message="Where There Are Multiple Tables Shown\n You Need Only Choose Impacted Table(s) ", parent=CenterTopFrame2)

				if int(self.nbrTbls) == 1:
					self.TopFrame4 = Frame(MainFrame1, bd=10, width=320, height=720, relief=RIDGE, bg="light grey")
					self.TopFrame4.place(x=20,y=20)

					self.Frame_d = Frame(self.TopFrame4, bd=5, width=300, height=700, bg="PaleGreen2", relief=RIDGE)
					self.Frame_d.place(x=1, y=1)	
				
					self.lbl1FrameD = Label(self.Frame_d, text="Select Columns to Retain or Delete", font=("ariel", 16, "bold", "underline"), fg="black", bg="PaleGreen2") 
					self.lbl1FrameD.place(x=5, y=4)

					drawFrame1()

				elif int(self.nbrTbls) == 2:
					self.TopFrame4 = Frame(MainFrame1, bd=10, width=625, height=720, relief=RIDGE, bg="light grey")
					self.TopFrame4.place(x=20,y=20)

					self.Frame_d = Frame(self.TopFrame4, bd=5, width=300, height=700, bg="PaleGreen2", relief=RIDGE)
					self.Frame_d.place(x=1, y=1)

					self.lbl1FrameD = Label(self.Frame_d, text="Select Columns to Retain or Delete", font=("ariel", 16, "bold", "underline"), fg="black", bg
						="PaleGreen2") 
					self.lbl1FrameD.place(x=5, y=4)		

					self.Frame_e = Frame(self.TopFrame4, bd=5, width=300, height=700, bg="Pale goldenrod", relief=RIDGE)
					self.Frame_e.place(x=301, y=1)

					self.lbl1FrameE = Label(self.Frame_e, text="Select Columns to Retain or Delete", font=("ariel", 16, "bold", "underline"), fg="black", bg="Pale goldenrod") 
					self.lbl1FrameE.place(x=5, y=4)

					drawFrame2()

				elif int(self.nbrTbls) == 3:
					self.TopFrame4 = Frame(MainFrame1, bd=10, width=925, height=720, relief=RIDGE, bg="light grey")
					self.TopFrame4.place(x=20,y=20)

					self.Frame_d = Frame(self.TopFrame4, bd=5, width=300, height=700, bg="PaleGreen2", relief=RIDGE)
					self.Frame_d.place(x=1, y=1)

					self.lbl1FrameD = Label(self.Frame_d, text="Select Columns to Retain or Delete", font=("ariel", 16, "bold", "underline"), fg="black", bg
						="PaleGreen2") 
					self.lbl1FrameD.place(x=5, y=4)		

					self.Frame_e = Frame(self.TopFrame4, bd=5, width=300, height=700, bg="Pale goldenrod", relief=RIDGE)
					self.Frame_e.place(x=301, y=1)

					self.lbl1FrameE = Label(self.Frame_e, text="Select Columns to Retain or Delete", font=("ariel", 16, "bold", "underline"), fg="black", bg="Pale goldenrod") 
					self.lbl1FrameE.place(x=5, y=4)

					self.Frame_f = Frame(self.TopFrame4, bd=5, width=300, height=700, bg="PaleGreen2", relief=RIDGE)
					self.Frame_f.place(x=602, y=1)

					self.lbl1FrameF = Label(self.Frame_f, text="Select Columns to Retain or Delete", font=("ariel", 16, "bold", "underline"), fg="black", bg="PaleGreen2") 
					self.lbl1FrameF.place(x=5, y=4)

					drawFrame3()

				else:
					self.TopFrame4 = Frame(MainFrame1, bd=10, width=1225, height=720, relief=RIDGE, bg="light grey")
					self.TopFrame4.place(x=20,y=20)

					self.Frame_d = Frame(self.TopFrame4, bd=5, width=300, height=700, bg="PaleGreen2", relief=RIDGE)
					self.Frame_d.place(x=1, y=1)

					self.lbl1FrameD = Label(self.Frame_d, text="Select Columns to Retain or Delete", font=("ariel", 16, "bold", "underline"), fg="black", bg
						="PaleGreen2") 
					self.lbl1FrameD.place(x=5, y=4)		

					self.Frame_e = Frame(self.TopFrame4, bd=5, width=300, height=700, bg="Pale goldenrod", relief=RIDGE)
					self.Frame_e.place(x=301, y=1)

					self.lbl1FrameE = Label(self.Frame_e, text="Select Columns to Retain or Delete", font=("ariel", 16, "bold", "underline"), fg="black", bg="Pale goldenrod") 
					self.lbl1FrameE.place(x=5, y=4)

					self.Frame_f = Frame(self.TopFrame4, bd=5, width=300, height=700, bg="PaleGreen2", relief=RIDGE)
					self.Frame_f.place(x=602, y=1)

					self.lbl1FrameF = Label(self.Frame_f, text="Select Columns to Retain or Delete", font=("ariel", 16, "bold", "underline"), fg="black", bg="PaleGreen2") 
					self.lbl1FrameF.place(x=5, y=4)

					self.Frame_g = Frame(self.TopFrame4, bd=5, width=300, height=700, bg="Pale goldenrod", relief=RIDGE)
					self.Frame_g.place(x=902, y=1)

					self.lbl1FrameG = Label(self.Frame_g, text="Select Columns to Retain or Delete", font=("ariel", 16, "bold", "underline"), fg="black", bg="Pale goldenrod") 
					self.lbl1FrameG.place(x=5, y=4)

					drawFrame4()

		#--------------------------------------------------------------#
		################## 7. End - Delete Columns ###################
		#--------------------------------------------------------------#

		#--------------------------------------------------------------#
		############# 8. Start - Delete Tables & Columns ###############
		#--------------------------------------------------------------#
			if v.get() == 8:
				# print(" Item 8 has started")

				def closeChoice8():
					self.Frame_h.destroy()
					self.TopFrame5.destroy()
					v.set(0)
					actionMenu()

				def reorgInfo():
					# print("Here at reorgInfo....")
					# Split the remain list into separate variables for processing

					# self.item1, self.item2, self.item3, self.item4 = [self.remainTblNo[i] for i in (0, 1, 2, 3)]					

					if len(self.remainTblNo) == 1:
						self.item1 = [self.remainTblNo[i] for i in (0)]
						# print("int(self.item1:) ", int(self.item1))
					if len(self.remainTblNo) == 2:
						self.item1, self.item2 = [self.remainTblNo[i] for i in (0, 1)]
						# print("int(self.item1) = ", int(self.item1))
						# print("int(self.item2) = ", int(self.item2))
					if len(self.remainTblNo) == 3:
						self.item1, self.item2, self.item3 = [self.remainTblNo[i] for i in (0, 1, 2)]
						# print("int(self.item1) = ", int(self.item1))
						# print("int(self.item2) = ", int(self.item2))
						# print("int(self.item3) = ", int(self.item3))
					if len(self.remainTblNo) == 4:
						self.item1, self.item2, self.item3, self.item4 = [self.remainTblNo[i] for i in (0, 1, 2, 3)]
						# print("int(self.item1) = ", int(self.item1))
						# print("int(self.item2) = ", int(self.item2))
						# print("int(self.item3) = ", int(self.item3))
						# print("int(self.item4) = ", int(self.item4))

					# print("self.remainTblNo: ", self.remainTblNo)
					if int(self.item1) <= 0 and int(self.item2) > 0:
						# print("self.remainTblNo item 1 is NULL and item 2 is populated")
						# Table Name Move Position 2 to Position 1
						self.tblName1 = self.tblName2
						self.tblName2 = ""
						# print("self.tblName1 =", self.tblName1)
						# print("self.tblName2 =", self.tblName2)

						# Modify data under Step 2 - Table Detail
						self.label1 = Label(CenterTopFrame1, text="Table 1 Name:", font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
						self.label1.place(x=5, y=50)

						self.label1a = Label(CenterTopFrame1, text=self.tblName1, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
						self.label1a.place(x=130, y=50)

						self.tbl2Label.destroy()
						self.tbl2txt.destroy()

						# Modify data under Step 3 - Col. Detail
						self.NbrColsTbl1 = int(self.txtColNbr2.get())

						self.label2 = Label(CenterTopFrame2, text="Number Columns - Table 1", font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
						self.label2.place(x=5, y=50)

						self.label2a = Label(CenterTopFrame2, text=self.NbrColsTbl1, font=("ariel", 16, "bold"), height=1, fg="dodger blue", bg="white")
						self.label2a.place(x=250, y=50)

						self.lblColNbr2.destroy()
						self.txtColNbr2.destroy()

						# Modify data in Table Column lists - Center Frames
						# print("self.colListTbl2: ", self.colListTbl2)

						# Button Setup
						self.colbtnSubmit = Button(MidLeftFrame, text="Submit", width=6, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command="", state="disabled")
						self.colbtnSubmit.place(x=10, y=310)

						self.colbtnExit = Button(MidLeftFrame, text="Exit", width=6, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=exit, state="normal")
						self.colbtnExit.place(x=220, y=310)

						# Set string for Column Header Presentation
						self.tblStr1 = "Columns in >>> " + str(self.tblName1)
						# print("self.tblStr1 = ", self.tblStr1)

						# 	#=========== Header for Data Block ==========
						self.lblColTbl1 = Label(MidLeftFrame,text=self.tblStr1, font=("ariel", 20, "bold", "underline"), fg="black", bg="cyan2")
						self.lblColTbl1.place(x=20, y=10)

						# Set Starting Location Axis Parameters
						Loc_x = 4
						Loc_y = 55
						z = 1

						while (z <= len(self.colListTbl2)) and (z <= 7):
							self.lnNbrBox1 = Label(MidLeftFrame,text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							self.lnNbrBox1.place(x=(Loc_x), y=Loc_y)

							label2 = Label(MidLeftFrame, width=11, bd=1, relief=RIDGE, text=self.colListTbl2[z-1], font=("ariel", 16, "bold"), fg="dodger blue", bg="wheat1")
							label2.place(x=(Loc_x + 18), y=Loc_y)

							Loc_y += 36
							z += 1
						next

						# Reset Starting Location Axis Parameters
						Loc_x = 165
						Loc_y = 55

						while (z <= len(self.colListTbl2)):
							self.lnNbrBox1 = Label(MidLeftFrame, text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							self.lnNbrBox1.place(x=(Loc_x), y=Loc_y)

							label2 = Label(MidLeftFrame, width=11, bd=1, relief=RIDGE, text=self.colListTbl2[z-1], font=("ariel", 16, "bold"), fg="dodger blue", bg="wheat1")
							label2.place(x=(Loc_x + 25), y=Loc_y)

							Loc_y += 36
							z += 1
						next

						for widget in MidCenterFrame1.winfo_children():
									widget.destroy()

						# Modify SQL Summary Data from 2 10 1
						# Table Information
						self.tbl1aLbl = Label(TopFrame3, text="1: " + str(self.tblName1), font=("ariel", 16, "bold"), height=1, fg="dodger blue", bg="white")
						self.tbl1aLbl.place(x=20, y=50)

						self.tbl2aLbl.destroy()

						# Column Quantity Information
						self.tbl1ColNbr = Label(TopFrame3, text="Cols. = " + str(self.NbrColsTbl1), font=("ariel", 16, "bold"), height=1, fg="dodger blue", bg="white")
						self.tbl1ColNbr.place(x=195, y=50)

						self.tbl2ColNbr.destroy()

						# Column Name Information
						self.colListTbl1 = self.colListTbl2

						self.lblColListTbl1 = Label(TopFrame3, text="Names = " + str(self.colListTbl1) , font=("ariel", 16, "bold"), height=1, fg="dodger blue", bg="white")
						self.lblColListTbl1.place(x=300, y=50)

						self.lblColListTbl2.destroy()

						# Reset 'remainTblNbr' list
						self.remainTblNo[0] = 1
						self.remainTblNo[1] = ""
						# print("Ending remainTblNo: ", self.remainTblNo)

					closeChoice8()

					# print("self.remainTblNo: ", self.remainTblNo)
					if int(self.item2) <= 0 and int(self.item3) > 0:
						# print("self.remainTblNo item 2 is NULL and item 3 is populated")
						# Table Name Move Position 2 to Position 1
						self.tblName2 = self.tblName3
						self.tblName3 = ""
						# print("self.tblName2 =", self.tblName2)
						# print("self.tblName3 =", self.tblName3)

						# Modify data under Step 2 - Table Detail
						self.label2 = Label(CenterTopFrame1, text="Table 2 Name:", font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
						self.label2.place(x=5, y=80)

						self.label2a = Label(CenterTopFrame1, text=self.tblName2, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
						self.label2a.place(x=130, y=80)

						self.tbl3Label.destroy()
						self.tbl3txt.destroy()

						# Modify data under Step 3 - Col. Detail
						self.NbrColsTbl2 = int(self.txtColNbr3.get())

						self.label3 = Label(CenterTopFrame2, text="Number Columns - Table 2", font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
						self.label3.place(x=5, y=80)

						self.label2a = Label(CenterTopFrame2, text=self.NbrColsTbl2, font=("ariel", 16, "bold"), height=1, width=2, fg="dodger blue", bg="white")
						self.label2a.place(x=250, y=80)

						self.lblColNbr3.destroy()
						self.txtColNbr3.destroy()

						# Modify data in Table Column lists - Center Frames
						# print("self.colListTbl2: ", self.colListTbl2)

						# Button Setup
						self.colbtnSubmit = Button(MidCenterFrame1, text="Submit", width=6, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command="", state="disabled")
						self.colbtnSubmit.place(x=10, y=310)

						self.colbtnExit = Button(MidCenterFrame1, text="Exit", width=6, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=exit, state="normal")
						self.colbtnExit.place(x=220, y=310)

						# Set string for Column Header Presentation
						self.tblStr2 = "Columns in >>> " + str(self.tblName2)
						# print("self.tblStr1 = ", self.tblStr1)

						# 	#=========== Header for Data Block ==========
						self.lblColTbl2 = Label(MidCenterFrame1,text=self.tblStr2, font=("ariel", 20, "bold", "underline"), fg="black", bg="cyan2")
						self.lblColTbl2.place(x=20, y=10)

						# Set Starting Location Axis Parameters
						Loc_x = 4
						Loc_y = 55
						z = 1

						while (z <= len(self.colListTbl3)) and (z <= 7):
							self.lnNbrBox1 = Label(MidCenterFrame1,text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							self.lnNbrBox1.place(x=(Loc_x), y=Loc_y)

							label2 = Label(MidCenterFrame1, width=11, bd=1, relief=RIDGE, text=self.colListTbl3[z-1], font=("ariel", 16, "bold"), fg="dodger blue", bg="wheat1")
							label2.place(x=(Loc_x + 18), y=Loc_y)

							Loc_y += 36
							z += 1
						next

						# Reset Starting Location Axis Parameters
						Loc_x = 165
						Loc_y = 55

						while (z <= len(self.colListTbl3)):
							self.lnNbrBox2 = Label(MidCenterFrame1, text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							self.lnNbrBox2.place(x=(Loc_x), y=Loc_y)

							label2 = Label(MidCenterFrame1, width=11, bd=1, relief=RIDGE, text=self.colListTbl3[z-1], font=("ariel", 16, "bold"), fg="dodger blue", bg="wheat1")
							label2.place(x=(Loc_x + 25), y=Loc_y)

							Loc_y += 36
							z += 1
						next

						for widget in MidCenterFrame2.winfo_children():
									widget.destroy()

						# Modify SQL Summary Data from 2 10 1
						# Table Information
						self.tbl2aLbl = Label(TopFrame3, text="2: " + str(self.tblName2), font=("ariel", 16, "bold"), height=1, fg="dodger blue", bg="white")
						self.tbl2aLbl.place(x=20, y=80)

						self.tbl3aLbl.destroy()

						# Column Quantity Information
						self.tbl1ColNbr = Label(TopFrame3, text="Cols. = " + str(self.NbrColsTbl2), font=("ariel", 16, "bold"), height=1, fg="dodger blue", bg="white")
						self.tbl1ColNbr.place(x=195, y=80)

						self.tbl3ColNbr.destroy()

						# Column Name Information
						self.colListTbl2 = self.colListTbl3

						self.lblColListTbl2 = Label(TopFrame3, text="Names = " + str(self.colListTbl2) , font=("ariel", 16, "bold"), height=1, fg="dodger blue", bg="white")
						self.lblColListTbl2.place(x=300, y=80)

						self.lblColListTbl3.destroy()

						# Reset 'remainTblNbr' list
						self.remainTblNo[0] = 1
						self.remainTblNo[1] = 2
						self.remainTblNo[2] = ""
						# print("Ending remainTblNo: ", self.remainTblNo)

					closeChoice8()

					# print("self.remainTblNo: ", self.remainTblNo)
					if int(self.item3) <= 0 and int(self.item4) > 0:
						# print("self.remainTblNo item 3 is NULL and item 4 is populated")
						# Table Name Move Position 2 to Position 1
						self.tblName3 = self.tblName4
						self.tblName4 = ""
						# print("self.tblName3 =", self.tblName3)
						# print("self.tblName4 =", self.tblName4)

						# Modify data under Step 2 - Table Detail
						self.label3 = Label(CenterTopFrame1, text="Table 3 Name:", font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
						self.label3.place(x=5, y=110)

						self.label3a = Label(CenterTopFrame1, text=self.tblName3, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
						self.label3a.place(x=130, y=110)

						self.tbl4Label.destroy()
						self.tbl4txt.destroy()

						# Modify data under Step 3 - Col. Detail
						self.NbrColsTbl3 = int(self.txtColNbr4.get())

						self.label4 = Label(CenterTopFrame2, text="Number Columns - Table 3", font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
						self.label4.place(x=5, y=110)

						self.label2a = Label(CenterTopFrame2, text=self.NbrColsTbl3, font=("ariel", 16, "bold"), height=1, width=2, fg="dodger blue", bg="white")
						self.label2a.place(x=250, y=110)

						self.lblColNbr4.destroy()
						self.txtColNbr4.destroy()

						# Modify data in Table Column lists - Center Frames
						# print("self.colListTbl3: ", self.colListTbl3)

						# Button Setup
						self.colbtnSubmit = Button(MidCenterFrame2, text="Submit", width=6, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command="", state="disabled")
						self.colbtnSubmit.place(x=10, y=310)

						self.colbtnExit = Button(MidCenterFrame2, text="Exit", width=6, height=1, font=("ariel", 14, "bold"), fg="black", bg="white", command=exit, state="normal")
						self.colbtnExit.place(x=220, y=310)

						# Set string for Column Header Presentation
						self.tblStr3 = "Columns in >>> " + str(self.tblName3)
						# print("self.tblStr1 = ", self.tblStr1)

						# 	#=========== Header for Data Block ==========
						self.lblColTbl2 = Label(MidCenterFrame2,text=self.tblStr3, font=("ariel", 20, "bold", "underline"), fg="black", bg="cyan2")
						self.lblColTbl2.place(x=20, y=10)

						# Set Starting Location Axis Parameters
						Loc_x = 4
						Loc_y = 55
						z = 1

						while (z <= len(self.colListTbl4)) and (z <= 7):
							self.lnNbrBox1 = Label(MidCenterFrame2,text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							self.lnNbrBox1.place(x=(Loc_x), y=Loc_y)

							label2 = Label(MidCenterFrame2, width=11, bd=1, relief=RIDGE, text=self.colListTbl4[z-1], font=("ariel", 16, "bold"), fg="dodger blue", bg="wheat1")
							label2.place(x=(Loc_x + 18), y=Loc_y)

							Loc_y += 36
							z += 1
						next

						# Reset Starting Location Axis Parameters
						Loc_x = 165
						Loc_y = 55

						while (z <= len(self.colListTbl3)):
							self.lnNbrBox2 = Label(MidLCenterFrame2, text=str(z), bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="dodger blue", bg="white")
							self.lnNbrBox2.place(x=(Loc_x), y=Loc_y)

							label2 = Label(MidCenterFrame2, width=11, bd=1, relief=RIDGE, text=self.colListTbl4[z-1], font=("ariel", 16, "bold"), fg="dodger blue", bg="wheat1")
							label2.place(x=(Loc_x + 25), y=Loc_y)

							Loc_y += 36
							z += 1
						next

						for widget in MidRightFrame.winfo_children():
									widget.destroy()

						# Modify SQL Summary Data from 2 10 1
						# Table Information
						self.tbl3aLbl = Label(TopFrame3, text="3: " + str(self.tblName3), font=("ariel", 16, "bold"), height=1, fg="dodger blue", bg="white")
						self.tbl3aLbl.place(x=20, y=110)

						self.tbl4aLbl.destroy()

						# Column Quantity Information
						self.tbl3ColNbr = Label(TopFrame3, text="Cols. = " + str(self.NbrColsTbl3), font=("ariel", 16, "bold"), height=1, fg="dodger blue", bg="white")
						self.tbl3ColNbr.place(x=195, y=110)

						self.tbl4ColNbr.destroy()

						# Column Name Information
						self.colListTbl3 = self.colListTbl4

						self.lblColListTbl3 = Label(TopFrame3, text="Names = " + str(self.colListTbl3) , font=("ariel", 16, "bold"), height=1, fg="dodger blue", bg="white")
						self.lblColListTbl3.place(x=300, y=110)

						self.lblColListTbl4.destroy()

						# Reset 'remainTblNbr' list
						self.remainTblNo[0] = 1
						self.remainTblNo[1] = 2
						self.remainTblNo[2] = 3
						self.remainTblNo[3] = ""
						# print("Ending remainTblNo: ", self.remainTblNo)

					closeChoice8()

				def tblSubmit():
					# print("self.delete_list: ", self.delete_list)
					# Determine the Table and Associated Columns to Delete
					self.delPos = ""
					self.remainTblNo = []

					ctr = 1
					for entry in self.delete_list:
						if entry == "y" or entry == "Y":
							
							self.remainTblNo.append(0)
							
							if ctr == 1:
								# print("Number of Tables = ", self.nbrTbls)
								# print("Table Name = ", self.tblName1)
								# print()
								# Adjust Table Details
								numberTables = int(self.nbrTbls)
								self.nbrTbls = str(numberTables - ctr)
								self.tblName1 = ""
								# print("Number of Tables = ", self.nbrTbls)
								# print("Table Name = ", self.tblName1)

								# Adjust Recorded Table Details
								self.tbl1aLbl.destroy() 
								self.tbl1txt.destroy() # CenterTopFrame1
								self.tbl1Label.destroy() # CenterTopFrame1

								# Adjust Recorded Column Details
								self.tbl1ColNbr.destroy()
								self.txtColNbr1.destroy()
								self.lblColListTbl1.destroy()
								self.lblColNbr1.destroy() # TopCenterFrame2

								#Reset the Column lists
								self.lblColListTbl1 = []
								self.my_entries1 = []

								for widget in MidLeftFrame.winfo_children():
									widget.destroy()

							if ctr == 2:
								# print("Number of Tables = ", self.nbrTbls)
								# print("Table Name = ", self.tblName1)
								# print()
								# Adjust Table Details
								numberTables = int(self.nbrTbls)
								self.nbrTbls = str(numberTables - ctr)
								self.tblName2 = ""
								# print("Number of Tables = ", self.nbrTbls)
								# print("Table Name = ", self.tblName1)

								# Adjust Recorded Table Details
								self.tbl2aLbl.destroy() 
								self.tbl2txt.destroy() # CenterTopFrame1

								# Adjust Recorded Column Details
								self.tbl2ColNbr.destroy()
								self.txtColNbr2.destroy()
								self.lblColListTbl2.destroy()

								#Reset the Column lists
								self.lblColListTbl2 = []
								self.my_entries2 = []

								for widget in MidCenterFrame1.winfo_children():
									widget.destroy()
								
								

							if ctr == 3:
								# print("Number of Tables = ", self.nbrTbls)
								# print("Table Name = ", self.tblName1)
								# print()
								# Adjust Table Details
								numberTables = int(self.nbrTbls)
								self.nbrTbls = str(numberTables - ctr)
								self.tblName3 = ""
								# print("Number of Tables = ", self.nbrTbls)
								# print("Table Name = ", self.tblName1)

								# Adjust Recorded Table Details
								self.tbl3aLbl.destroy() 
								self.tbl3txt.destroy() # CenterTopFrame1

								# Adjust Recorded Column Details
								self.tbl3ColNbr.destroy()
								self.txtColNbr3.destroy()
								self.lblColListTbl3.destroy()

								#Reset the Column lists
								self.lblColListTbl3 = []
								self.my_entries3 = []

								for widget in MidCenterFrame2.winfo_children():
									widget.destroy()

							if ctr == 4:
								# print("Number of Tables = ", self.nbrTbls)
								# print("Table Name = ", self.tblName1)
								# print()
								# Adjust Table Details
								numberTables = int(self.nbrTbls)
								self.nbrTbls = str(numberTables - ctr)
								self.tblName4 = ""
								# print("Number of Tables = ", self.nbrTbls)
								# print("Table Name = ", self.tblName1)

								# Adjust Recorded Table Details
								self.tbl4aLbl.destroy() 
								self.tbl4txt.destroy() # CenterTopFrame1
								self.tbl4Label.destroy()

								# Adjust Recorded Column Details
								self.tbl4ColNbr.destroy()
								self.txtColNbr4.destroy()
								self.lblColListTbl4.destroy()
								self.lblColNbr4.destroy()

								#Reset the Column lists
								self.lblColListTbl4 = []
								self.my_entries4 = []

								for widget in MidRightFrame.winfo_children():
									widget.destroy()

						else:
							self.remainTblNo.append(ctr)

						ctr += 1

					reorgInfo()

				def tblAction():
					# print("Number of Tabels = ", int(self.nbrTbls))
					if int(self.nbrTbls) == 1:
						# print("Number of Tabels = ", int(self.nbrTbls))
						# Commands
						self.btnTblDel1 = Button(self.Frame_h, text="Next", width=6, font=("ariel", 16, "bold"), command=tblAction, fg="black", bg="lightblue", state='disabled')
						self.btnTblDel1.place(x=20, y=130)

						self.btnTblDel2 = Button(self.Frame_h, text="Submit", width=8, font=("ariel", 16, "bold"), command=tblSubmit, fg="black", bg="lightblue", state='normal')
						self.btnTblDel2.place(x=150, y=130)

					if int(self.nbrTbls) == 2:
						# print("Number of Tabels = ", int(self.nbrTbls))
						# Commands
						self.btnTblDel1 = Button(self.Frame_h, text="Next", width=6, font=("ariel", 16, "bold"), command=tblAction, fg="black", bg="lightblue", state='disabled')
						self.btnTblDel1.place(x=20, y=200)

						self.btnTblDel2 = Button(self.Frame_h, text="Submit", width=8, font=("ariel", 16, "bold"), command=tblSubmit, fg="black", bg="lightblue", state='normal')
						self.btnTblDel2.place(x=150, y=200)

					if int(self.nbrTbls) == 3:
						# print("Number of Tabels = ", int(self.nbrTbls))
						# Commands
						self.btnTblDel1 = Button(self.Frame_h, text="Next", width=6, font=("ariel", 16, "bold"), command=tblAction, fg="black", bg="lightblue", state='disabled')
						self.btnTblDel1.place(x=20, y=270)

						self.btnTblDel2 = Button(self.Frame_h, text="Submit", width=8, font=("ariel", 16, "bold"), command=tblSubmit, fg="black", bg="lightblue", state='normal')
						self.btnTblDel2.place(x=150, y=270)

					if int(self.nbrTbls) == 4:
						# print("Number of Tabels = ", int(self.nbrTbls))
						# Commands
						self.btnTblDel1 = Button(self.Frame_h, text="Next", width=6, font=("ariel", 16, "bold"), command=tblAction, fg="black", bg="lightblue", state='disabled')
						self.btnTblDel1.place(x=20, y=270)

						self.btnTblDel2 = Button(self.Frame_h, text="Submit", width=8, font=("ariel", 16, "bold"), command=tblSubmit, fg="black", bg="lightblue", state='normal')
						self.btnTblDel2.place(x=150, y=270)

					self.delete_list = ""
					
					# Create a Yes / No retention list
					for entries in self.tblDel_entry:
						self.delete_list = self.delete_list + str(entries.get())
	
					# Cycle through the entry list to retain or deleted selected items
					ctr = 0
					Loc_y = 75
					for entry in self.delete_list:
						for char in self.chars_to_check:
							if entry == char:
								if entry == 'n' or entry == 'N':
									delTblLbl = Label(self.Frame_h, text="Retained", font=("ariel", 16, "bold"), fg="dark slate blue", bg="lightblue")
									delTblLbl.place(x=300, y=(Loc_y))

									break	

								elif entry == 'y' or entry == 'Y':
									delColLbl = Label(self.Frame_h, text="Deleted", font=("ariel", 16, "bold"), fg="indian red", bg="lightblue")
									delColLbl.place(x=300, y=(Loc_y))

									break

								else:
									tkinter.messagebox.showinfo(title="Incorrect Entry Choices", message="'Y, y, N, n' \n Only Characters Allowed\n A Correct Choice is\n Required in Every Block", parent=CenterTopFrame2)			

						Loc_y += 50

					self.nbrChg = 0
					for entry in self.delete_list:
						if entry == 'y' or entry == 'Y':
							self.nbrChg += 1
					
					if self.nbrChg <= 0:		
						tkinter.messagebox.showinfo(title="Table Delete", message="There Are No Tables to Delete ", parent=CenterTopFrame2)

					
				def delTableHdrs():
					# Menu Header Labels
					self.lblTblDel1 = Label(self.Frame_h, text="Table Name", font=("ariel", 16, "bold", "underline"), fg="black", bg="lightblue")
					self.lblTblDel1.place(x=10, y=30)

					self.lblTblDel2 = Label(self.Frame_h, text="Delete Table (Y/N)", font=("ariel", 16, "bold", "underline"), fg="black", bg="lightblue")
					self.lblTblDel2.place(x=140, y=30)

					self.lblTblDel3 = Label(self.Frame_h, text="Action", font=("ariel", 16, "bold", "underline"), fg="black", bg="lightblue")
					self.lblTblDel3.place(x=310, y=30)

					self.tblDel_entry = []

				def delTable1():
					# Commands
					self.btnTblDel1 = Button(self.Frame_h, text="Next", width=6, font=("ariel", 16, "bold"), command=tblAction, fg="black", bg="lightblue", state='normal')
					self.btnTblDel1.place(x=20, y=130)

					self.btnTblDel2 = Button(self.Frame_h, text="Submit", width=8, font=("ariel", 16, "bold"), command=tblSubmit, fg="black", bg="lightblue", state='disabled')
					self.btnTblDel2.place(x=150, y=130)

					self.btnTblDel3 = Button(self.Frame_h, text="Exit", width=6, font=("ariel", 16, "bold"), command=exit, fg="black", bg="lightblue", state='normal')
					self.btnTblDel3.place(x=280, y=130)

					# Input Layout
					self.lblNbrTbl1 = Label(self.Frame_h, text=self.tblName1, font=("ariel", 16, "bold"), fg="black", bg="lightblue")
					self.lblNbrTbl1.place(x=20, y=75)

					self.my_entry1 = Entry(self.Frame_h, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="black", bg="lightblue")
					self.my_entry1.place(x=190, y=75)

					self.tblDel_entry.append(self.my_entry1)

				def delTable2():
					# Commands
					self.btnTblDel1 = Button(self.Frame_h, text="Next", width=6, font=("ariel", 16, "bold"), command=tblAction, fg="black", bg="lightblue", state='normal')
					self.btnTblDel1.place(x=20, y=200)

					self.btnTblDel2 = Button(self.Frame_h, text="Submit", width=8, font=("ariel", 16, "bold"), command=tblSubmit, fg="black", bg="lightblue", state='disabled')
					self.btnTblDel2.place(x=150, y=200)

					self.btnTblDel3 = Button(self.Frame_h, text="Exit", width=6, font=("ariel", 16, "bold"), command=exit, fg="black", bg="lightblue", state='normal')
					self.btnTblDel3.place(x=280, y=200)

					# Input Layout
					self.lblNbrTbl1 = Label(self.Frame_h, text=self.tblName1, font=("ariel", 16, "bold"), fg="black", bg="lightblue")
					self.lblNbrTbl1.place(x=20, y=75)

					self.my_entry1 = Entry(self.Frame_h, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="black", bg="lightblue")
					self.my_entry1.place(x=190, y=75)

					self.tblDel_entry.append(self.my_entry1)

					self.lblNbrTbl2 = Label(self.Frame_h, text=self.tblName2, font=("ariel", 16, "bold"), fg="black", bg="lightblue")
					self.lblNbrTbl2.place(x=20, y=125)

					self.my_entry2 = Entry(self.Frame_h, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="black", bg="lightblue")
					self.my_entry2.place(x=190, y=125)

					self.tblDel_entry.append(self.my_entry2)

				def delTable3():
					# Commands
					self.btnTblDel1 = Button(self.Frame_h, text="Next", width=6, font=("ariel", 16, "bold"), command=tblAction, fg="black", bg="lightblue", state='normal')
					self.btnTblDel1.place(x=20, y=270)

					self.btnTblDel2 = Button(self.Frame_h, text="Submit", width=8, font=("ariel", 16, "bold"), command=tblSubmit, fg="black", bg="lightblue", state='disabled')
					self.btnTblDel2.place(x=150, y=270)

					self.btnTblDel3 = Button(self.Frame_h, text="Exit", width=6, font=("ariel", 16, "bold"), command=exit, fg="black", bg="lightblue", state='normal')
					self.btnTblDel3.place(x=280, y=270)

					# Input Layout
					self.lblNbrTbl1 = Label(self.Frame_h, text=self.tblName1, font=("ariel", 16, "bold"), fg="black", bg="lightblue")
					self.lblNbrTbl1.place(x=20, y=75)

					self.my_entry1 = Entry(self.Frame_h, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="black", bg="lightblue")
					self.my_entry1.place(x=190, y=75)

					self.tblDel_entry.append(self.my_entry1)

					self.lblNbrTbl2 = Label(self.Frame_h, text=self.tblName2, font=("ariel", 16, "bold"), fg="black", bg="lightblue")
					self.lblNbrTbl2.place(x=20, y=125)

					self.my_entry2 = Entry(self.Frame_h, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="black", bg="lightblue")
					self.my_entry2.place(x=190, y=125)

					self.tblDel_entry.append(self.my_entry2)

					self.lblNbrTbl3 = Label(self.Frame_h, text=self.tblName3, font=("ariel", 16, "bold"), fg="black", bg="lightblue")
					self.lblNbrTbl3.place(x=20, y=175)

					self.my_entry3 = Entry(self.Frame_h, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="black", bg="lightblue")
					self.my_entry3.place(x=190, y=175)

					self.tblDel_entry.append(self.my_entry3)

				def delTable4():
					# Commands
					self.btnTblDel1 = Button(self.Frame_h, text="Next", width=6, font=("ariel", 16, "bold"), command=tblAction, fg="black", bg="lightblue", state='normal')
					self.btnTblDel1.place(x=20, y=270)

					self.btnTblDel2 = Button(self.Frame_h, text="Submit", width=8, font=("ariel", 16, "bold"), command=tblSubmit, fg="black", bg="lightblue", state='disabled')
					self.btnTblDel2.place(x=150, y=270)

					self.btnTblDel3 = Button(self.Frame_h, text="Exit", width=6, font=("ariel", 16, "bold"), command=exit, fg="black", bg="lightblue", state='normal')
					self.btnTblDel3.place(x=280, y=270)

					# Input Layout
					self.lblNbrTbl1 = Label(self.Frame_h, text=self.tblName1, font=("ariel", 16, "bold"), fg="black", bg="lightblue")
					self.lblNbrTbl1.place(x=20, y=75)

					self.my_entry1 = Entry(self.Frame_h, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="black", bg="lightblue")
					self.my_entry1.place(x=190, y=75)

					self.tblDel_entry.append(self.my_entry1)

					self.lblNbrTbl2 = Label(self.Frame_h, text=self.tblName2, font=("ariel", 16, "bold"), fg="black", bg="lightblue")
					self.lblNbrTbl2.place(x=20, y=125)

					self.my_entry2 = Entry(self.Frame_h, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="black", bg="lightblue")
					self.my_entry2.place(x=190, y=125)

					self.tblDel_entry.append(self.my_entry2)

					self.lblNbrTbl3 = Label(self.Frame_h, text=self.tblName3, font=("ariel", 16, "bold"), fg="black", bg="lightblue")
					self.lblNbrTbl3.place(x=20, y=175)

					self.my_entry3 = Entry(self.Frame_h, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="black", bg="lightblue")
					self.my_entry3.place(x=190, y=175)

					self.tblDel_entry.append(self.my_entry3)

					self.lblNbrTbl4 = Label(self.Frame_h, text=self.tblName4, font=("ariel", 16, "bold"), fg="black", bg="lightblue")
					self.lblNbrTbl4.place(x=20, y=225)

					self.my_entry4 = Entry(self.Frame_h, width=2, bd=1, relief=RIDGE, font=("ariel", 16, "bold"), fg="black", bg="lightblue")
					self.my_entry4.place(x=190, y=225)

					self.tblDel_entry.append(self.my_entry4)

				if int(self.nbrTbls) == 1:
					self.TopFrame5 = Frame(MainFrame1, bd=10, width=420, height=200, relief=RIDGE, bg="darkblue")
					self.TopFrame5.place(x=100,y=100)

					self.Frame_h = Frame(self.TopFrame5, bd=5, width=400, height=180, bg="lightblue", relief=RIDGE)
					self.Frame_h.place(x=1, y=1)	
				
					self.lbl1FrameH = Label(self.Frame_h, text="Select Columns to Retain or Delete", font=("ariel", 16, "bold", "underline"), fg="black", bg="lightblue") 
					self.lbl1FrameH.place(x=60, y=4)

					delTableHdrs()

					delTable1()

				elif int(self.nbrTbls) == 2:				
					self.TopFrame5 = Frame(MainFrame1, bd=10, width=420, height=270, relief=RIDGE, bg="darkblue")
					self.TopFrame5.place(x=100,y=100)

					self.Frame_h = Frame(self.TopFrame5, bd=5, width=400, height=250, bg="lightblue", relief=RIDGE)
					self.Frame_h.place(x=1, y=1)	
				
					self.lbl1FrameH = Label(self.Frame_h, text="Select Columns to Retain or Delete", font=("ariel", 16, "bold", "underline"), fg="black", bg="lightblue") 
					self.lbl1FrameH.place(x=60, y=4)

					delTableHdrs()

					delTable2()

				elif int(self.nbrTbls) == 3:				
					self.TopFrame5 = Frame(MainFrame1, bd=10, width=420, height=340, relief=RIDGE, bg="darkblue")
					self.TopFrame5.place(x=100,y=100)

					self.Frame_h = Frame(self.TopFrame5, bd=5, width=400, height=320, bg="lightblue", relief=RIDGE)
					self.Frame_h.place(x=1, y=1)	
				
					self.lbl1FrameH = Label(self.Frame_h, text="Select Columns to Retain or Delete", font=("ariel", 16, "bold", "underline"), fg="black", bg="lightblue") 
					self.lbl1FrameH.place(x=60, y=4)

					delTableHdrs()

					delTable3()
					
				elif int(self.nbrTbls) == 4:				
					self.TopFrame5 = Frame(MainFrame1, bd=10, width=420, height=340, relief=RIDGE, bg="darkblue")
					self.TopFrame5.place(x=100,y=100)

					self.Frame_h = Frame(self.TopFrame5, bd=5, width=400, height=320, bg="lightblue", relief=RIDGE)
					self.Frame_h.place(x=1, y=1)	
				
					self.lbl1FrameH = Label(self.Frame_h, text="Select Tables to Retain or Delete", font=("ariel", 16, "bold", "underline"), fg="black", bg="lightblue") 
					self.lbl1FrameH.place(x=60, y=4)

					delTableHdrs()

					delTable4()

		#--------------------------------------------------------------#
		############# 8. End - Delete Tables & Columns ###############
		#--------------------------------------------------------------#
			
#------------------------------------------------------------------------------#
#####################  Application and Process Setup  ######################
#------------------------------------------------------------------------------#
			# if v.get() == 1:
				# print("This is the Create Database Name Process")

			# if v.get() == 2:
				# print("This is the Edit Database Name Process")

			# if v.get() == 3:
				# print("This is the Add Table Name(s) Process")

			# if v.get() == 4:
				# print("This is the Change Table Name(s) Process")

			# if v.get() == 5:
				# print("This is Add Column Quantity Process")

			# if v.get() == 6:
				# print("This is the Add Column Name(s) to Table(s) Process")

			# if v.get() == 7:
				# print("This is the Delete Column Process")

			# if v.get() == 8:
				# print("This is the Delete Table + Column Process")

			# if v.get() == 9:
				# print("This is the Complete SQL Setup Process")
	
		def actionMenu():
			# print("v.get = ", v.get())
			if v.get() == 1:
				# print(str(v.get()) + " - Create Database Name")
				# dbNameChg()
				Process()
			elif v.get() == 2:
				# print(str(v.get()) + " - Edit Database Name")
				Process()
			elif v.get() == 3:
				# print(str(v.get()) + " - Add Table(s) (max 4)")
				# self.proc = 'A'
				# delTblName()
				Process()
			elif v.get() == 4:
				# print(str(v.get()) + " - Change Table Name(s)")
				# self.proc = 'B'
				# addTblName()
				Process()
			elif v.get() == 5:
				# print(str(v.get()) + " - Add Column Quantity To Table(s)")
				# addColName()
				Process()
			elif v.get() == 6: 
				# print(str(v.get()) + " - Add Column Name(s)")
				# verifySQLData()
				Process()
			elif v.get() == 7:
				# print(str(v.get()) + " - Delete Column")
				# setupSQL()
				Process()
			elif v.get() == 8:
				# print(str(v.get()) + " - Delete Table(s) and Column(s)")
				# self.proc = 'C'
				# delColName()
				Process()
			elif v.get() == 9:
				# print(str(v.get()) + " - Complete SQL Setup)")
				Process()				
				
			# Establish a list of possible actions for the user to select
			choices = [("1. Create Database Name", 1),
						("2. Edit Database Name", 2),
						("3. Add Table(s) (4 max)", 3),
						("4. Change Table Name(s)", 4),
						("5. Add Column Quantity to Table(s)", 5),
						("6. Add Column Name(s)", 6),
						("7. Delete Column", 7),
						("8. Delete Table(s) & Column(s)", 8),
						("9. Complete SQL Setup", 9)]

			# Create the radio buttons for the various actions
			vert = 35
			for choice, val in choices:
			    Radiobutton(RightTopFrame, text=choice, bg="wheat1", fg="black", font=("ariel", 18, "bold"), padx=15, variable=v, command=actionMenu, value=val).place(x=20, y=vert)
			    vert += 25

			self.choicebtnExit = Button(RightTopFrame, text="Exit", width=5, height=1, font=("ariel", 12, "bold"), fg="black", bg="white", command=exit, state="normal")
			self.choicebtnExit.place(x=300, y=260)


#------------------------------------------------------------------------------#
#=============================== Start Program ================================#
#------------------------------------------------------------------------------#
		
		v = IntVar()
		# v.set(1)  # initializing the choice, ie. Enter Create Database Name
		actionMenu()
		

if __name__=="__main__":
	root = Tk()
	application = BuildDB(root)
	root.mainloop()