#welcome to mini project agrotech

 
from tkinter import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import sqlite3



# creating our window
root=Tk()
root.title("Agrotechmini")
#root.configure(bg='red')
root.iconbitmap("C:\VS Code - Python\minipjtimage1.ico")


#creating tkintr variables
v1=IntVar()
v1.set('')
v2=IntVar()
v2.set('')
v3=IntVar()
v3.set('')
v4=IntVar()
v4.set('')
v5=IntVar()
v5.set('')
v6=IntVar()
v6.set('')
v7=IntVar()
v7.set('')
v8=IntVar()
v8.set('')
v9=IntVar()
v9.set('')
v10=StringVar()
v10.set("SELECT")
v11=IntVar()
v11.set('')
v12=IntVar()
v12.set('')
v13=IntVar()
v13.set('')
v14=IntVar()
v14.set('')
v15=IntVar()
v15.set('')
v16=IntVar()
v16.set('')
v17=IntVar()
v17.set('')


#ceating ssecond window
def optop1():
    top1=Toplevel()
    top1.configure(bg='black')
    top1.minsize(width=1280, height=770)
    windowtitle=Label(top1,text="WELCOME TO SOIL TEST ANALYSER !!",font="Times 30 bold italic",bg="red",fg="white")
    windowtitle.grid(row=0,column=0,padx=30,pady=20,columnspan=5)
    mylablew1=Label(top1,text="ENTER THE REULTS FROM THE SOIL TEST REPORT IN APPROPRIATE TEXT BOXES..(in ppm)",font="helvatica 20  bold italic",bg="black",fg="white")
    mylablew1.grid(row=1,column=0,pady=50,padx=30,columnspan=5)



    #creating the database

    def submit ():
        global valdict
        valdict={'ph_value':v1.get(),'magnesium':v2.get(),'phosphorus':v3.get(),'potassium':v4.get(),'calsium':v5.get(),'boron':v6.get(),'iron':v7.get(),'zinc':v8.get(),'manganese':v9.get()}
    

        
    

        entph.delete(0,END)
        entmag.delete(0,END)
        entphos.delete(0,END)
        entpots.delete(0,END)
        entcalsi.delete(0,END)
        entbor.delete(0,END)
        entiron.delete(0,END)
        entzinc.delete(0,END)
        entmanganese.delete(0,END)
        

    #creating the result function

    def result():
        global frameChartsLT
        top3=Toplevel()
        top3.configure(bg='black')
        top3.geometry("1920x1080")
        windowtitle1=Label(top3,text="WELCOME TO RESULT VIEWER WINDOW",font="helvatica 30 bold italic",bg="red",fg="white")
        windowtitle1.grid(row=0,column=0,padx=30,pady=20,columnspan=5)
        frameChartsLT = Frame(top3,bg="black",)
        frameChartsLT.grid(row=4,column=3,columnspan=3,rowspan=10,padx=10,pady=10)

        #creating the button to display pie chart
        pie_char=Button(top3,text="show pie chart analyser",font="Times 20 bold italic",bg="grey",fg="black",borderwidth=5,command=pie_chart)
        pie_char.grid(row=2,column=3,columnspan=3,pady=20,ipadx=50,ipady=15)


        def press (val):
            top4=Toplevel()
            top4.configure(bg='black')
            top4.minsize(width=1280, height=770)
            windowtitle2=Label(top4,text="TIPS AND SUGGESTIONS",font="Times 30 bold italic",bg="red",fg="black")
            windowtitle2.grid(row=0,column=0)
            exitb=Button(top4,text="QUIT",command=top4.destroy,font="Times 20 bold")
            exitb.grid(row=2,column=0,ipadx=20)

            if(val==1):
                f2=open("ph1.txt","r")
                x1=f2.read()
                f2.close()
                sugtext1=Text(top4,height=10,width=100,font="Times 20 bold",bg="black",fg="white")
                sugtext1.grid(row=1,column=0)
                sugtext1.insert(END,x1)
            elif(val==2 or val==5):    
                f2=open("magnesium.txt","r")
                x1=f2.read()
                f2.close()
                sugtext1=Text(top4,height=10,width=100,font="Times 20 bold",bg="black",fg="white")
                sugtext1.grid(row=1,column=0)
                sugtext1.insert(END,x1)
            elif(val==3):    
                f2=open("phosphorous.txt","r")
                x1=f2.read()
                f2.close()
                sugtext1=Text(top4,height=20,width=100,font="Times 20 bold",bg="black",fg="white")
                sugtext1.grid(row=1,column=0)
                sugtext1.insert(END,x1)
            elif(val==4):    
                f2=open("potassium.txt","r")
                x1=f2.read()
                f2.close()
                sugtext1=Text(top4,height=10,width=100,font="Times 20 bold",bg="black",fg="white")
                sugtext1.grid(row=1,column=0)
                sugtext1.insert(END,x1)
            
            elif(val==6):    
                f2=open("boron.txt","r")
                x1=f2.read()
                f2.close()
                sugtext1=Text(top4,height=10,width=100,font="Times 20 bold",bg="black",fg="white")
                sugtext1.grid(row=1,column=0)
                sugtext1.insert(END,x1)
            elif(val==7):    
                f2=open("iron.txt","r")
                x1=f2.read()
                f2.close()
                sugtext1=Text(top4,height=10,width=100,font="Times 20 bold",bg="black",fg="white")
                sugtext1.grid(row=1,column=0)
                sugtext1.insert(END,x1)
            elif(val==8):    
                f2=open("zinc.txt","r")
                x1=f2.read()
                f2.close()
                sugtext1=Text(top4,height=10,width=100,font="Times 20 bold",bg="black",fg="white")
                sugtext1.grid(row=1,column=0)
                sugtext1.insert(END,x1)
            elif(val==9):    
                f2=open("manganese.txt","r")
                x1=f2.read()
                f2.close()
                sugtext1=Text(top4,height=10,width=100,font="Times 20 bold",bg="black",fg="white")
                sugtext1.grid(row=1,column=0)
                sugtext1.insert(END,x1)
            
       # a=pd.Series(valdict)
       # b=pd.DataFrame(a)
        if (valdict["ph_value"]>=6 and valdict["ph_value"]<=8):
            lab1=Label(top3,text=" 1.ph is =" + str(valdict['ph_value'])+"\nyour soil contains the required ph level",font="Times 20 bold",bg="black",fg="white")
            lab1.grid(column=0,row=1)
        else:
            sugg1=Button(top3,text="suggestion",font="Times 20 bold",bg="black",fg="white",command=lambda :press(1))
            sugg1.grid(column=2,row=1)
            if valdict["ph_value"]<6 :
                lab11=Label(top3,text='1. PH is ='+ str(valdict['ph_value'])+"\nthis is acidic ph you can't grow the crops please add the buffer to nutralise it ",font="Times 20 bold",bg="black",fg="white")
                lab11.grid(column=0,row=1)
            else:
                lab12=Label(top3,text="1.PH="+str(valdict["ph_value"])+"\n it is the basic ph which need to be nutralised to grow the desired crops",font="Times 20 bold",bg="black",fg="white")
                lab12.grid(column=0,row=1)

        if (valdict["magnesium"]>=60 and valdict["magnesium"]<=120):
            lab2=Label(top3,text="2. magnesium="+str(valdict["magnesium"])+"\nsoil contains the good quantity of magnisium",font="Times 20 bold",bg="black",fg="white")
            lab2.grid(column=0,row=2)
        else:
            sugg2=Button(top3,text="suggestion",font="Times 20 bold",bg="black",fg="white",command=lambda :press(2))
            sugg2.grid(column=2,row=2)
            if(valdict["magnesium"]<60):
                lab21=Label(top3,text="2. magnesium="+str(valdict["magnesium"])+'\nthe soil is deficient in magnisium quantity ',font="Times 20 bold",bg="black",fg="white")
                lab21.grid(column=0,row=2)
            else:
                lab22=Label(top3,text="2. magnesium="+str(valdict["magnesium"])+"\nthe soil contains the excess amount of magnisium",font="Times 20 bold",bg="black",fg="white")
                lab22.grid(column=0,row=2)

        


        
        if (valdict["phosphorus"]>=30 and valdict["phosphorus"]<=50):
            lab3=Label(top3,text="3. Phosphorus="+str(valdict["phosphorus"])+"\nPhosphorus quantity is sufficient",font="Times 20 bold",bg="black",fg="white")
            lab3.grid(column=0,row=3)
        else:
            sugg3=Button(top3,text="suggestion",font="Times 20 bold",bg="black",fg="white",command=lambda :press(3))
            sugg3.grid(column=2,row=3)
            if(valdict["phosphorus"]<30):
                lab31=Label(top3,text="3. Phosphorus="+str(valdict["phosphorus"])+'\nthe soil is deficient in PHOSPHORUS quantity ',font="Times 20 bold",bg="black",fg="white")
                lab31.grid(column=0,row=3)
            else:
                lab32=Label(top3,text="3. Phosphorus="+str(valdict["phosphorus"])+"\nthe soil contains the excess amount of PHOSPORUS",font="Times 20 bold",bg="black",fg="white")
                lab32.grid(column=0,row=3)
        
        if (valdict["potassium"]>=170 and valdict["potassium"]<=280):
            lab4=Label(top3,text="4. potassium="+str(valdict["potassium"])+"\nsoil has sufficient amount of potassium",font="Times 20 bold",bg="black",fg="white")
            lab4.grid(column=0,row=4)
        else:
            sugg4=Button(top3,text="suggestion",font="Times 20 bold",bg="black",fg="white",command=lambda :press(4))
            sugg4.grid(column=2,row=4)
            if(valdict["potassium"]<170):
                lab41=Label(top3,text="4. potassium="+str(valdict["potassium"])+'\nthe soil is deficient in POTASSIUM quantity ',font="Times 20 bold",bg="black",fg="white")
                lab41.grid(column=0,row=4)
            else:
                lab42=Label(top3,text="4. potassium="+str(valdict["potassium"])+"\nthe soil contains the excess amount of POTASSIUM",font="Times 20 bold",bg="black",fg="white")
                lab42.grid(column=0,row=4)
        

        if (valdict["calsium"]>=800 and valdict["calsium"]<=1200):
            lab4=Label(top3,text="5. calsium="+str(valdict["calsium"])+"\nsoil has sufficient amount of calsium",font="Times 20 bold",bg="black",fg="white")
            lab4.grid(column=0,row=5)
        else:
            sugg5=Button(top3,text="suggestion",font="Times 20 bold",bg="black",fg="white",command=lambda :press(5))
            sugg5.grid(column=2,row=5)
            if(valdict["calsium"]<800):
                lab41=Label(top3,text="5. calsium="+str(valdict["calsium"])+'\nthe soil is deficient in calsium quantity ',font="Times 20 bold",bg="black",fg="white")
                lab41.grid(column=0,row=5)
            else:
                lab42=Label(top3,text="5. calsium="+str(valdict["calsium"])+"\nthe soil contains the excess amount of calsium",font="Times 20 bold",bg="black",fg="white")
                lab42.grid(column=0,row=5)


       
        if (valdict["boron"]>=6 and valdict["boron"]<=60):
            lab4=Label(top3,text="6. boron="+str(valdict["boron"])+"\nsoil has sufficient amount of boron",font="Times 20 bold",bg="black",fg="white")
            lab4.grid(column=0,row=6)
        else:
            sugg6=Button(top3,text="suggestion",font="Times 20 bold",bg="black",fg="white",command=lambda :press(6))
            sugg6.grid(column=2,row=6)
            if(valdict["boron"]<6):
                lab41=Label(top3,text="6. born="+str(valdict["boron"])+'\nthe soil is deficient in boron quantity ',font="Times 20 bold",bg="black",fg="white")
                lab41.grid(column=0,row=6)
            else:
                lab42=Label(top3,text="6. boron="+str(valdict["boron"])+"\nthe soil contains the excess amount of boron",font="Times 20 bold",bg="black",fg="white")
                lab42.grid(column=0,row=6)
        

        if (valdict["iron"]>=50 and valdict["iron"]<=250):
            lab4=Label(top3,text="7. iron="+str(valdict["iron"])+"\nsoil has sufficient amount of iron",font="Times 20 bold",bg="black",fg="white")
            lab4.grid(column=0,row=7)
        else:
            sugg7=Button(top3,text="suggestion",font="Times 20 bold",bg="black",fg="white",command=lambda :press(7))
            sugg7.grid(column=2,row=7)
            if(valdict["iron"]<50):
                lab41=Label(top3,text="7. iron="+str(valdict["iron"])+'\nthe soil is deficient in iron quantity ',font="Times 20 bold",bg="black",fg="white")
                lab41.grid(column=0,row=7)
            else:
                lab42=Label(top3,text="7. iron="+str(valdict["iron"])+"\nthe soil contains the excess amount of iron",font="Times 20 bold",bg="black",fg="white")
                lab42.grid(column=0,row=7)
        

        if (valdict["zinc"]>=25 and valdict["zinc"]<=150):
            lab4=Label(top3,text="8. zinc="+str(valdict["zinc"])+"\nsoil has sufficient amount of zinc",font="Times 20 bold",bg="black",fg="white")
            lab4.grid(column=0,row=8)
        else:
            sugg8=Button(top3,text="suggestion",font="Times 20 bold",bg="black",fg="white",command=lambda :press(8))
            sugg8.grid(column=2,row=8)
            if(valdict["zinc"]<25):
                lab41=Label(top3,text="8. zinc="+str(valdict["zinc"])+'\nthe soil is deficient in zinc quantity ',font="Times 20 bold",bg="black",fg="white")
                lab41.grid(column=0,row=8)
            else:
                lab42=Label(top3,text="8. zinc="+str(valdict["zinc"])+"\nthe soil contains the excess amount of zinc",font="Times 20 bold",bg="black",fg="white")
                lab42.grid(column=0,row=8)
        

        if (valdict["manganese"]>=20 and valdict["manganese"]<=200):
            lab4=Label(top3,text="9. manganese="+str(valdict["manganese"])+"\nsoil has sufficient amount of manganese",font="Times 20 bold",bg="black",fg="white")
            lab4.grid(column=0,row=9)
        else:
            sugg9=Button(top3,text="suggestion",font="Times 20 bold",bg="black",fg="white",command=lambda :press(9))
            sugg9.grid(column=2,row=9)
            if(valdict["manganese"]<20):
                lab41=Label(top3,text="9. manganese="+str(valdict["manganese"])+'\nthe soil is deficient in manganese quantity ',font="Times 20 bold",bg="black",fg="white")
                lab41.grid(column=0,row=9)
            else:
                lab42=Label(top3,text="9. manganese="+str(valdict["manganese"])+"\nthe soil contains the excess amount of manganese",font="Times 20 bold",bg="black",fg="white")
                lab42.grid(column=0,row=9)
        

        

    def pie_chart():
       # ptl.pie(valdict.values(),labels=valdict.keys())
        #ptl.legend()
        #ptl.show()
        fig = Figure() # create a figure object
        ax = fig.add_subplot(111) # add an Axes to the figure
        
        ax.pie(valdict.values(), radius=1, labels=valdict.keys(),autopct='%0.2f%%', shadow=True)

        chart1 = FigureCanvasTkAgg(fig,frameChartsLT)
        chart1.get_tk_widget().grid(row=4,column=1)
        
       
        
    #creating label widgets for the values

    labph=Label(top1,text="PH VALUE",font="Times 20 bold ",bg="black",fg="white")
    labph.grid(row=2,column=1,padx=1,pady=10,)

    divlabel1=Label(top1,text="MACRO NUTRIENTS .",font="Times 20 bold italic",bg="grey",fg="black",borderwidth=5)
    divlabel1.grid(row=3,column=0,columnspan=2,ipadx=120,pady=20,padx=10)

    
    labmagni=Label(top1,text="MAGNISIUM",font="Times 20 bold ",bg="black",fg="white")
    labmagni.grid(row=4,column=0,pady=10)


    labphos=Label(top1,text="PHOSPHORUS",font="Times 20 bold ",bg="black",fg="white")
    labphos.grid(row=5,column=0,pady=10)

    labpotass=Label(top1,text="POTASSIUM",font="Times 20 bold ",bg="black",fg="white")
    labpotass.grid(row=6,column=0,pady=10)

    labcalsi=Label(top1,text="CALCIUM",font="Times 20 bold ",bg="black",fg="white")
    labcalsi.grid(row=7,column=0,pady=10)

    divlabel2=Label(top1,text="MICRO NUTRIENTS .",font="Times 20 bold italic",bg="grey",fg="black",borderwidth=5)
    divlabel2.grid(row=3,column=3,columnspan=2,padx=10,pady=20,ipadx=120)

    labbor=Label(top1,text="BORON",font="Times 20 bold ",bg="black",fg="white")
    labbor.grid(row=4,column=3,pady=10)
   
    labiron=Label(top1,text="IRON",font="Times 20 bold ",bg="black",fg="white")
    labiron.grid(row=5,column=3,pady=10)

    labzinc=Label(top1,text="ZINC",font="Times 20 bold ",bg="black",fg="white")
    labzinc.grid(row=6,column=3,pady=10)

    labmangnese=Label(top1,text="MANGANESE",font="Times 20 bold ",bg="black",fg="white")
    labmangnese.grid(row=7,column=3,pady=10)

    labsoil=Label(top1,text="SELECT THE SOIL TYPE",font="Times 20 bold ",bg="black",fg="white")
    labsoil.grid(row=8,column=1,pady=10)

    #creating the entey boxes

    entph=Entry(top1,width=15,borderwidth=5,font="helvatica 20 bold",textvariable=v1,bg="grey")
    entph.grid(row=2,column=2,padx=1,pady=10,ipadx=10)
    
    entmag=Entry(top1,width=20,borderwidth=5,font="helvatica 20 bold",textvariable=v2)
    entmag.grid(row=4,column=1,padx=1,pady=10,ipadx=10)
    
    entphos=Entry(top1,width=20,borderwidth=5,font="helvatica 20 bold",textvariable=v3)
    entphos.grid(row=5,column=1,padx=1,pady=10,ipadx=10)
    
    entpots=Entry(top1,width=20,borderwidth=5,font="helvatica 20 bold",textvariable=v4)
    entpots.grid(row=6,column=1,padx=1,pady=10,ipadx=10)
    
    entcalsi=Entry(top1,width=20,borderwidth=5,font="helvatica 20 bold",textvariable=v5)
    entcalsi.grid(row=7,column=1,padx=1,pady=10,ipadx=10)
    
    entbor=Entry(top1,width=20,borderwidth=5,font="helvatica 20 bold",textvariable=v6)
    entbor.grid(row=4,column=4,padx=1,pady=10,ipadx=10)
    
    entiron=Entry(top1,width=20,borderwidth=5,font="helvatica 20 bold",textvariable=v7)
    entiron.grid(row=5,column=4,padx=1,pady=10,ipadx=10)
    
    entzinc=Entry(top1,width=20,borderwidth=5,font="helvatica 20 bold",textvariable=v8)
    entzinc.grid(row=6,column=4,padx=1,pady=10,ipadx=10)
    
    entmanganese=Entry(top1,width=20,borderwidth=5,font="helvatica 20 bold",textvariable=v9)
    entmanganese.grid(row=7,column=4,padx=1,pady=10,ipadx=10)

    #creating drop down menu of the soil
    option=['ALUVIAL SOIL','BLACK SOIL','RED SOIL','LATERAL SOIL','MOUNTAIN SOIL']
    dropsoil=OptionMenu(top1,v10,*option)
    dropsoil.config(bg="#A877BA")
    dropsoil.grid(row=8,column=2,padx=1,pady=20,ipadx=100)
    
    
    #creatin submit button
    finalsub=Button(top1,text="VERIFY & SUBMIT",font="Times 20 bold italic",bg="grey",fg="black",borderwidth=5,command=submit)
    finalsub.grid(row=9,column=1,columnspan=1,pady=20,ipadx=50,ipady=15)

    view_result=Button(top1,text="VIEW RESULT",font="Times 20 bold italic",bg="grey",fg="black",borderwidth=5,command=result)
    view_result.grid(row=9,column=2,columnspan=3,pady=20,ipadx=50,ipady=15)
    


def optop2():
    top2=Toplevel()
    top2.configure(bg='black')
    top2.minsize(width=1280, height=770)
    titlewid=Label(top2,text="EXPENDITURE ANALYSER ...! ",font='Times 30 bold italic',fg='black',bg='red')
    titlewid.grid(row=0,column=0,padx=20,pady=20,columnspan=3,ipadx=500)
    titlewid1=Label(top2,text="Enter the expenditure in the given space ",font='Times 30 bold italic',fg='red',bg='black')
    titlewid1.grid(row=1,column=0,padx=20,pady=20,columnspan=3)


    #creating submit function
    def subval():
        global tot_expenditure,results
        
        
        #creating total exprnditure
        tot_expenditure=v11.get()+v12.get()+v13.get()+v14.get()+v15.get()
        results=(v16.get()*v17.get())-tot_expenditure
        #print(results)
        conn=sqlite3.connect('farmingrecords.db')
        c=conn.cursor()
        c.execute('INSERT INTO  record VALUES (:seed_cost,:fertilizer_cost,:irrigation_cost,:labour_cost,:transport_cost,:tot_expence,:yields,:results)',
                {'seed_cost':v11.get(),
                'fertilizer_cost':v12.get(),
                'irrigation_cost':v13.get(),
                'labour_cost':v14.get(),
                'transport_cost':v15.get(),
                'tot_expence':tot_expenditure,
                'yields':v16.get(),
                'results':results
                }
         )
        conn.commit()
        conn.close()

        seedent.delete(0,END)
        ferent.delete(0,END)
        irrent.delete(0,END)
        labent.delete(0,END)
        transent.delete(0,END)
        yieldent.delete(0,END)
        current.delete(0,END)

    def query():
        global expend,year,yields,res


        
        
        expend=[]
        year=[]
        yields=[]
        res=[]


        conn=sqlite3.connect('farmingrecords.db')
        c=conn.cursor()
        c.execute("SELECT *,oid FROM  record")
        f=c.fetchall()
        print(f)
        for i in f:
            expend.append(i[5])
            year.append(i[8])
            yields.append(i[6])
            res.append(i[7])

       
        #print(expend,year,yields,res)
        conn.commit()
        conn.close()

        Figure,axis=plt.subplots(2,2)
       
        axis[0,0].plot(year,expend)
        axis[0,0].set_title("EXPENCE TRACKING")
        axis[0,0].set_xlabel("years")
        axis[0,0].set_ylabel("expenditure")


        axis[0,1].plot(year,yields)
        axis[0,1].set_title("YIELD TRACKING")
        axis[0,1].set_xlabel("years")
        axis[0,1].set_ylabel("yield")

        axis[1,0].plot(year,res)
        axis[1,0].set_title("INCOME TRACKING")
        axis[1,0].set_xlabel("years")
        axis[1,0].set_ylabel("income")

        axis[1,1].plot(res,yields)
        axis[1,1].set_title("INCOME v/s YIELD TRACKING")
        axis[1,1].set_xlabel("income")
        axis[1,1].set_ylabel("yield")
        
        plt.show()

    def dispresult():
            top5=Toplevel()
            top5.configure(bg='black')
            top5.minsize(width=1280, height=770)
            analysislab=Label(top5,text='RESULT ANALYSIS',font='Times 30 bold italic',fg='black',bg='red')
            analysislab.grid(row=0,column=0,padx=20,pady=20,columnspan=3,ipadx=200)

            if res[-1]>=res[-2]:
                reslab=Label(top5,text='YOU ARE IN PROFIT THIS YEAR AS COMPARED TO PREVIOUS YEAR',font='helvatica 20 bold italic')
                reslab.grid(row=1,column=0,padx=30,pady=50)
            else:
                reslab=Label(top5,text='YOU ARE IN LOSS THIS YEAR AS COMPARED TO PREVIOUS YEAR',font='helvatica 20 bold italic')
                reslab.grid(row=1,column=0,padx=30,pady=50)


       
    #creating input widgets
    seedcostlab=Label(top2,text='SEED COST',font='helvatica 20 italic',bg='black',fg='white')
    seedcostlab.grid(row=2,column=0,pady=20)
    fertilizercostlab=Label(top2,text='FERTILIZER COST',font='helvatica 20 italic',bg='black',fg='white')
    fertilizercostlab.grid(row=3,column=0,pady=20)
    irrigationcostlab=Label(top2,text='IRRIGATION COST',font='helvatica 20 italic',bg='black',fg='white')
    irrigationcostlab.grid(row=4,column=0,pady=20)
    labourcostlab=Label(top2,text='LABOUR COST',font='helvatica 20 italic',bg='black',fg='white')
    labourcostlab.grid(row=5,column=0,pady=20)
    transportcostlab=Label(top2,text='TRANSPORTATIONAL CHARGES',font='helvatica 20 italic',bg='black',fg='white')
    transportcostlab.grid(row=6,column=0,pady=20)
    yield_lab=Label(top2,text='YIELD (in kgs)',font='helvatica 20 italic',bg='black',fg='white')
    yield_lab.grid(row=7,column=0,pady=20)
    curr_lab=Label(top2,text='PRICE OF CROP (per kg)',font='helvatica 20 italic',bg='black',fg='white')
    curr_lab.grid(row=8,column=0,pady=20)


    #CREATING entry widgets
    seedent=Entry(top2,width=20,borderwidth=5,font="helvatica 20 bold",textvariable=v11)
    seedent.grid(row=2,column=1)
    ferent=Entry(top2,width=20,borderwidth=5,font="helvatica 20 bold",textvariable=v12)
    ferent.grid(row=3,column=1)
    irrent=Entry(top2,width=20,borderwidth=5,font="helvatica 20 bold",textvariable=v13)
    irrent.grid(row=4,column=1)
    labent=Entry(top2,width=20,borderwidth=5,font="helvatica 20 bold",textvariable=v14)
    labent.grid(row=5,column=1)
    transent=Entry(top2,width=20,borderwidth=5,font="helvatica 20 bold",textvariable=v15)
    transent.grid(row=6,column=1)
    yieldent=Entry(top2,width=20,borderwidth=5,font="helvatica 20 bold",textvariable=v16)
    yieldent.grid(row=7,column=1)
    current=Entry(top2,width=20,borderwidth=5,font="helvatica 20 bold",textvariable=v17)
    current.grid(row=8,column=1)

    subvalbut=Button(top2,text='SUBMIT',font="Times 20 bold italic",command=subval)
    subvalbut.grid(row=9,column=0,pady=20,ipadx=30)

    query_but=Button(top2,text='GRAPH ANALYSIS',font="Times 20 bold italic",command=query)
    query_but.grid(row=9,column=1,pady=20,ipadx=30)

    resanalysbut=Button(top2,text='RESULT ANALYSIS',font="Times 20 bold italic",command=dispresult)
    resanalysbut.grid(row=9,column=2,pady=20,ipadx=30)



bg=PhotoImage(file="C:\VS Code - Python\pjtim2.png")
bglable=Label(root,image=bg)
bglable.place(x=0,y=0)

#root.geometry("1000x1000")
root.minsize(width=1280, height=770)

# creating title lable
agri=Label(root,text='AGROTECH', font= ('Times 50 bold italic'),bg="black",fg="grey")
agri.grid(row=0,column=1,columnspan=10,ipadx=10,pady=100,padx=100)

#creating the buttons for main functions

soilanly=Button(root,text="SOIL TEST \nANALYSER",font="Times 25 bold ",command=optop1,fg="white",bg="black",borderwidth=3)
soilanly.grid(row=2,column=1,columnspan=5,padx=150,pady=50,ipadx=50)

expenditure=Button(root,text="EXPENDITURE \nANALYSER",font="Times 25 bold",command=optop2,fg="white",bg="black",borderwidth=3)
expenditure.grid(row=2,column=6,columnspan=5,padx=150,pady=50,ipadx=50)


root.mainloop()