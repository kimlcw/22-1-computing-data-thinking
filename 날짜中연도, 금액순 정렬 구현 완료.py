import tkinter
import tkinter.ttk
from dataclasses import dataclass


# Data 
info_date_Y = []
info_date_M = []
info_date_D = []
my_money = []
my_item = []
my_type = []

class MYINFO:
    I_date_Y:int = 22
    I_date_M:int = 11
    I_date_D:int = 20
    I_moeny:int = 0
    I_item:str = ''
    I_type:str = ''
    


temp = MYINFO()
#temp = []
print("temp 세팅")


window=tkinter.Tk() # 생성
# 윈도우명이 'window'인 가장 상위 레벨의 윈도우 창 생성
# 생성 ~ 반복 구문 사이에 위젯을 생성하고 적용

window.title("가계부") # 윈도우 창의 제목
window.geometry("700x700+600+100") # 너비*높이 + x좌표 + y좌표
window.resizable(True, True)
window.option_add("*Font", "돋움 15")

#resizeable()을 적용할 때,
# True=1, False=0을 의미하여 상수를 입력해도 적용이 가능합니다.


label1=tkinter.Label(window, text="<< 가계부 프로그램 >>\n", width=30, height=5, bd='0', fg="blue", relief="solid")
label2=tkinter.Label(window, text="본 프로그램은 지출만을 기록합니다. \n수요자가 많을 시 소득 기록 기능이 추가될 수 있습니다.\n")
label3=tkinter.Label(window, text="각 입력창에 연도, 월, 일을 입력한 뒤 [일자 추가] 버튼을 눌러주세요.")


label1.pack() # 위젯을 배치할 수 있습니다.
label2.pack()
label3.pack()

# 리스트박스[date_count] 에 date 추가 함수
def fx_date():

    
    my_date.insert('end', Y_entry.get()+"/"+M_entry.get()+"/"+D_entry.get()) # 추가
    my_date_Y.append(Y_entry.get())
    my_date_M.append(M_entry.get())
    my_date_D.append(D_entry.get())


    print("my_date [index] = ", Y_entry.get()+"/"+M_entry.get()+"/"+D_entry.get())
    my_date.pack()
    
    

# my_date 리스트박스
my_date = tkinter.Listbox(window, selectmode='extended', height=0)
my_date_Y = []
my_date_M = []
my_date_D = []


# 입력창 entry
Y_entry=tkinter.Entry(window) #속성
#Y_entry.bind("<Return>", fx_date) #입력하고 enter 누르면 fx_date 함수 실행
M_entry=tkinter.Entry(window) #속성
D_entry=tkinter.Entry(window) #속성
Y_entry.pack()
M_entry.pack()
D_entry.pack()

def fx_contents():
    text = my_date.curselection()[0]
    # 0, 1, 2 ...
    
    window2=tkinter.Tk() # 생성
    window2.title(text) # 윈도우 창의 제목
    temp.I_date_Y = my_date_Y[text]
    temp.I_date_M = my_date_M[text]
    temp.I_date_D = my_date_D[text]
    print("text =", text)
    print("temp.I_date_Y =", temp.I_date_Y)
    print("temp.I_date_M =", temp.I_date_M)
    print("temp.I_date_D =", temp.I_date_D)
    
    window2.geometry("700x700+900+100") # 너비*높이 + x좌표 + y좌표
    window2.resizable(True, True)
    window2.option_add("*Font", "돋움 15")

    label4=tkinter.Label(window2, text="지출 항목을 선택하세요.")
    label4.pack() # 위젯을 배치할 수 있습니다.


    # Combobox 생성 및 출력
    type_list = ["식품비", "저축", "통신비", "교통비", "문화생활비", "의류미용비", "교육비", "의료건강비", "기타"]
    cb = tkinter.ttk.Combobox(window2)
    cb.config(values = type_list)
    cb.pack()

    
    # [항목 선택] 버튼 정의
    btn = tkinter.Button(window2)
    btn.config(text = "항목 선택")
    

    # [항목]값 불러와서 출력
    def click():
        temp.I_type = cb.get() # 선택한 콤보박스 항목값 temp.I_type에 넣기
        print("temp.I_type =", temp.I_type)

        lab = tkinter.Label(window2)
        lab.config(text = temp.I_type)
        lab.pack()

        cl_label=tkinter.Label(window2, text="지출 내용을 입력해주세요.\n", width=30, height=5, bd='0', fg="blue", relief="solid")
        cl_label.pack()


        # [지출 내용 입력] 버튼 정의
        btn2 = tkinter.Button(window2)
        btn2.config(text = "지출 내용 입력")
        
        
        # 지출 내용 입력받는 entry 생성 (1)
        cl_entry=tkinter.Entry(window2)
        cl_entry.pack()

        def fx_what():
            temp.I_item = cl_entry.get() # 입력한 지출 내용 temp.I.item에 넣기
            print("temp.I_item =", temp.I_item)
            
            la = tkinter.Label(window2, text=temp.I_item) # 지출 내용 출력
            la.pack()

            # 지출 금액 입력받기
            cl2_entry=tkinter.Entry(window2)
            cl2_entry.pack()
            
            # [지출 금액 입력] 버튼 정의
            btn3 = tkinter.Button(window2)
            btn3.config(text = "지출 금액 입력")
            
        
            def fx_money():
                temp.I_money = cl2_entry.get() # 입력한 지출 금액 temp.I_money에 넣기
                print("temp.I_money =", temp.I_money)

                # [확인] 버튼 정의
                Y_btn = tkinter.Button(window2)
                Y_btn.config(text = "확인")

                def fx_Y():
                    info_date_Y.append(temp.I_date_Y)  # 맨 앞에서 선언한 리스트에 temp.I_date_Y의 값 추가
                    info_date_M.append(temp.I_date_M)
                    info_date_D.append(temp.I_date_D)
                    my_type.append(temp.I_type)
                    my_item.append(temp.I_item)
                    my_money.append(temp.I_money)

                    
                    print("--------------------------------append(temp)--------------------------------")
                    print(temp.I_date_Y)
                    print(temp.I_date_M)
                    print(temp.I_date_D)
                    print("\n")
                    print(info_date_Y)
                    print(info_date_M)
                    print(info_date_D)
                    print(my_type)
                    print(my_item)
                    
                    
                    label_list = []

                    print("날짜   항목   내용   금액")
                  
        
                    for i in range (len(info_date_Y)):
                        print("\n"+str(i)+"번째 for문")
                        print("len(my_date_Y)=", len(my_date_Y))
                        print("info_date_Y["+str(i)+"] = "+str(info_date_Y[i]))
                        print("info_date_M["+str(i)+"] = "+str(info_date_M[i]))
                        print("info_date_D["+str(i)+"] = "+str(info_date_D[i]))
                        print("my_type["+str(i)+"] = "+ my_type[i])
                        print("my_item["+str(i)+"] = "+ my_item[i])
                        print("my_money["+str(i)+"] = "+ str(my_money[i]))
                        print("\n")
                        my_label = tkinter.Label(window2, text = str(info_date_Y[i]) + "/"+ str(info_date_M[i]) + "/"+ str(info_date_D[i]) + "   " + my_type[i] + "   " + str(my_money[i]) + "   " + my_item[i])
                        label_list.append(my_label)
                        
        
                    for i in range(0, len(info_date_Y), 1):
                        label_list[i].pack()
                        print("label_list[i].pack()", label_list[i])

                    
                
                # [확인] 버튼 출력 , 버튼 클릭 시 fx_Y 함수 실행 
                Y_btn.config(command = fx_Y)
                Y_btn.pack()


            # [지출 금액 입력] 버튼 출력, 버튼 클릭 시 fx_money 함수 실행
            btn3.config(command = fx_money)
            btn3.pack()


            # [지출 내용 입력] 버튼 출력, 버튼 클릭 시 fx_what 함수 실행
        btn2.config(command = fx_what)
        btn2.pack()


# 이거 클릭하면     
        

    # [항목 선택] 버튼 활성화. 버튼 클릭 시 click 함수 실행
    btn.config(command = click)
    btn.pack()

    window2.mainloop()



# 버튼 누르면 listbox 추가
lb_button = tkinter.Button(window)
lb_button.config(overrelief="solid", command=fx_date)
lb_button.config(repeatdelay=1000, repeatinterval=100)
lb_button.config(width=20, height=1, bd='0.5', bg='OliveDrab1')
lb_button.config(text = "일자 추가")
lb_button.pack() # 위젯 배치


# 버튼 누르면 fx_contents 실행
button = tkinter.Button(window)
button.config(overrelief="solid", command=fx_contents)
button.config(repeatdelay=1000, repeatinterval=100)
button.config(width=20, height=1, bd='0.5', bg='cadetblue1')
button.config(text = "해당 일자 기록하기")
button.pack() # 위젯 배치



def fx_show():
    window3=tkinter.Tk() # 생성
    window3.title("가계부 기록 열람") 
    
    window3.geometry("700x1000+900+100") # 너비*높이 + x좌표 + y좌표
    window3.resizable(True, True)
    window3.option_add("*Font", "돋움 15")

    label4=tkinter.Label(window3, text="날짜 | 항목 | 금액 | 내용")
    label4.pack() # 위젯을 배치할 수 있습니다
   
    temp_index = []
    temp_index = [0, 0, 0, 0, 0, 0]
    
    def fx_sorting_mon():
        print("fx_sorting_mon 실핼")
        for k in range(0, len(info_date_Y)-1):
            min = k
            for j in range(k+1, len(info_date_Y)):
                if info_date_Y[j]<info_date_Y[min]:
                    min = j
            temp_index[0] = info_date_Y[k]
            info_date_Y[k] = info_date_Y[min]
            info_date_Y[min] = temp_index[0]

            temp_index[1] = info_date_M[k]
            info_date_M[k] = info_date_M[min]
            info_date_M[min] = temp_index[1]

            temp_index[2] = info_date_D[k]
            info_date_D[k] =info_date_D[min]
            info_date_D[min] = temp_index[2]

            temp_index[3] = my_money[k]
            my_money[k]= my_money[min]
            my_money[min] = temp_index[3]

            temp_index[4] = my_item[k]
            my_item[k] = my_item[min]
            my_item[min] = temp_index[4]

            temp_index[5] = my_type[k]
            my_type[k] = my_type[min]
            my_type[min] = temp_index[5]
            print("for문 %d회차"%(k+1))
        fx_show()
            

    def fx_sorting_money():
        print("fx_sorting_money 실핼")
        for k in range(0, len(my_money)-1):
            min = k
            for j in range(k+1, len(my_money)):
                if my_money[j]<my_money[min]:
                    min = j
            temp_index[0] = info_date_Y[k]
            info_date_Y[k] = info_date_Y[min]
            info_date_Y[min] = temp_index[0]

            temp_index[1] = info_date_M[k]
            info_date_M[k] = info_date_M[min]
            info_date_M[min] = temp_index[1]

            temp_index[2] = info_date_D[k]
            info_date_D[k] =info_date_D[min]
            info_date_D[min] = temp_index[2]

            temp_index[3] = my_money[k]
            my_money[k] = my_money[min]
            my_money[min] = temp_index[3]

            temp_index[4] = my_item[k]
            my_item[k] = my_item[min]
            my_item[min] = temp_index[4]

            temp_index[5] = my_type[k]
            my_type[k] = my_type[min]
            my_type[min] = temp_index[5]
            print("for문 %d회차"%(k+1))
        fx_show()
                           

    sort1_button = tkinter.Button(window3)
    sort1_button.config(overrelief="solid", command=fx_sorting_mon)
    sort1_button.config(repeatdelay=1000, repeatinterval=100)
    sort1_button.config(width=8, height=1, bd='0', bg='PaleTurquoise1')
    sort1_button.config(text = "날짜 순")
    sort1_button.place(x=600, y=0) # 위젯 배치




    sort2_button = tkinter.Button(window3)
    sort2_button.config(overrelief="solid", command=fx_sorting_money)
    sort2_button.config(repeatdelay=1000, repeatinterval=100)
    sort2_button.config(width=8, height=1, bd='0', bg='PaleTurquoise1')
    sort2_button.config(text = "금액 순")
    sort2_button.place(x=500, y=0) # 위젯 배치
    







    label_list = []
        
    for i in range (len(info_date_Y)):
        print("\n"+str(i)+"번째 for문")
        print("len(my_date_Y)=", len(my_date_Y))
        print("info_date_Y["+str(i)+"] = "+str(info_date_Y[i]))
        print("info_date_M["+str(i)+"] = "+str(info_date_M[i]))
        print("info_date_D["+str(i)+"] = "+str(info_date_D[i]))
        print("my_type["+str(i)+"] = "+ my_type[i])
        print("my_item["+str(i)+"] = "+ my_item[i])
        print("my_money["+str(i)+"] = "+ str(my_money[i]))
        print("\n")

        if(int(my_money[i]) >= 10000 and int(my_money[i]) < 30000):
            my_label = tkinter.Label(window3, text = str(info_date_Y[i]) + "/"+ str(info_date_M[i]) + "/"+ str(info_date_D[i]) + "   " + my_type[i] + "   " + str(my_money[i]) + "   " + my_item[i], fg = "orange")
        elif(int(my_money[i]) >= 30000 and int(my_money[i]) < 1000000):
            my_label = tkinter.Label(window3, text = str(info_date_Y[i]) + "/"+ str(info_date_M[i]) + "/"+ str(info_date_D[i]) + "   " + my_type[i] + "   " + str(my_money[i]) + "   " + my_item[i], fg = "tomato")
        elif(int(my_money[i]) >= 100000):
            my_label = tkinter.Label(window3, text = str(info_date_Y[i]) + "/"+ str(info_date_M[i]) + "/"+ str(info_date_D[i]) + "   " + my_type[i] + "   " + str(my_money[i]) + "   " + my_item[i], fg = "red")
        else :
            my_label = tkinter.Label(window3, text = str(info_date_Y[i]) + "/"+ str(info_date_M[i]) + "/"+ str(info_date_D[i]) + "   " + my_type[i] + "   " + str(my_money[i]) + "   " + my_item[i], fg = "blue")
        
        label_list.append(my_label)
                        
        
    for i in range(0, len(info_date_Y), 1):
        label_list[i].pack()
        print("label_list[i].pack()", label_list[i])



# 버튼 누르면 fx_show 실행
show_button = tkinter.Button(window)
show_button.config(overrelief="solid", command=fx_show)
show_button.config(repeatdelay=1000, repeatinterval=100)
show_button.config(text = "기록 열람하기")
show_button.pack() # 위젯 배치




def fx_delete():
    text = my_date.curselection()[0]  # listbox.curselection()은 튜플 형태, 튜플의 첫번째 인자를 저장
    my_date.delete(text)
    # 0, 1, 2 ... 
    del info_date_Y[text]
    del info_date_M[text]
    del info_date_D[text]
    del my_type[text]
    del my_item[text]
    del my_money[text]
    

del_button = tkinter.Button(window)
del_button.config(overrelief="solid", command=fx_delete)
del_button.config(repeatdelay=1000, repeatinterval=100)
del_button.config(width=20, height=1, bd='0.5', bg ='tomato2')
del_button.config(text = "해당 일자 삭제하기")
del_button.pack() # 위젯 배치


window.mainloop() # 반복
# window의 윈도우 창을 윈도우가 종료될 때까지 실행
