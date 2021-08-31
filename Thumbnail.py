import tkinter
import dload
import tkinter.font
import os
import getpass

from tkinter import *
from selenium import webdriver
from bs4 import BeautifulSoup

window = Tk ()
window.title("썸네일 추출기")
window.geometry('600x300')


Windows_User = getpass.getuser()

string = StringVar()

def export():

    driver = webdriver.Chrome('C:\chromedriver.exe')
    str(driver.get("https://img.youtube.com/vi/"+string.get()[17:]+"/maxresdefault.jpg"))
    
    req = driver.page_source
    Object = BeautifulSoup(req,'html.parser')

    thumnails = Object.select("body > img")

    i=1
    for thumnail in thumnails:
        img = thumnail['src']
        dload.save(img,f'C:/Users/{Windows_User}/Desktop/download.png') #경로 앞에 f를 쓰는 이유: F-string
        i+=1

    driver.quit()

    
   

# window 표기 텍스트 font 설정
Title_Font = tkinter.font.Font(size=20, weight="bold")
Body_Font = tkinter.font.Font(size=15, weight="bold")


# 프로그램 title print부분
Program_Title = tkinter.Label(window, text = "썸네일 추출 프로그램", font = Title_Font)
Program_Title.place(x=120, y=20)


# 링크 입력 문구
Youtube_Link = tkinter.Label(window, text = "유튜브 링크 입력", font = Body_Font)
Youtube_Link.place(x=20, y=115)


#  링크 입력 textbox 부분
textbox = tkinter.Entry(window, width=50, textvariable=string)
textbox.place(x=20, y=150)


# 추출 버튼 부분
Export_Button=tkinter.Button(window, text="Export",width=10, command=export)
Export_Button.place(x=390, y=150)


window.mainloop()
