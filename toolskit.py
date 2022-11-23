from selenium import webdriver
import pyautogui
import time
import tkinter as tk
import os
import cv2

pencere = tk.Tk()
pencere.title("Otomatik Tıklayıcı")
pencere.geometry("800x600")
pencere.resizable(width="FALSE", height="FALSE")
pencere.attributes('-topmost', 'true') 
pencere.iconphoto(False, tk.PhotoImage(file='soname.ico'))

def knmbul():
    time.sleep(3)
    global screen
    global pos 
    screen  = pyautogui.size()
    pos = pyautogui.position()
    konumlar.config(text = pos)
    screenw.config(text = screen)

def click():
    time.sleep(1)
    pyautogui.click(pos, clicks=int(tekrar.get()), interval=int(waitime.get()))
def yazdir():
    time.sleep(5)
    pyautogui.typewrite(yazi.get())
def screenshotake():
    time.sleep(0.5)
    pencere.lower()
    isim = sensec.get()
    ekran_goruntusu = pyautogui.screenshot()
    dosya_yolu = os.path.join('C:\\Users\makif\Desktop', isim)
    ekran_goruntusu.save(dosya_yolu)
    os.startfile(dosya_yolu)
def shutdownc():
    time.sleep(int(shuttime.get()))
    kapatmaKodu = "shutdown /s /t " + shuttime.get()
    os.system(kapatmaKodu)
def resystem():
    time.sleep(int(yenidenBaslats.get()))
    yenidenBaslatmaKodu = "shutdown /r" + yenidenBaslats.get()
    os.system(yenidenBaslatmaKodu)
def camera():
    global kamera 
    kamera= cv2.VideoCapture(0)
    while(True):
        ret, videoGoruntu = kamera.read()
        cv2.imshow("Bilgisayar Kamerası", videoGoruntu)
        if cv2.waitKey(50) & 0xFF == ord("x"):
            break
    kamera.release()
def filmbul():
    film_adi = film_adi2.get()
    browser = webdriver.Firefox()
    browser.get('https://www.fullhdfilmizlesene.pw/')

    time.sleep(3)
    search = browser.find_element("xpath","/html/body/div[2]/div/div[2]/input")
    search.send_keys(film_adi)
    ara = browser.find_element("xpath", "/html/body/div[2]/div/div[2]/button")
    ara.click()
    time.sleep(3)
    filmsec = browser.find_element("xpath", '/html/body/div[5]/div[1]/main/section/ul/li[1]')
    filmsec.click()
    time.sleep(2)
    pyautogui.scroll(-10)
    acfilm = browser.find_element("id", "plx")
    acfilm.click()
    time.sleep(1)

    
    



hosgeldin = tk.Label(text="Otomatik Tıklayıcı", font="Helvatica 20")
hosgeldin.place(x=260 , y=20)

konumlarText = tk.Label(text = "Tıklanacak yeri seçmek için aşağıdaki butona basıp 3 saniye içinde o konuma götürünüz.")
konumlarText.place(x=20, y=80)

knmbulbtn = tk.Button(text="Konumu Seç", font="Helvatica 10", command=knmbul)
knmbulbtn.place(x=20, y=110)

konumlar = tk.Label(text="", font="Helvatica 10")
konumlar.place(x=160, y=140)

posi = tk.Label(text="Fare Konumu", font="Helvatica 10")
posi.place(x=150, y=120)

counter = tk.Label(text="", font="Impact 20")
counter.place(x= 720, y=10)

screenw = tk.Label(text="", font="Helvatica 10")
screenw.place(x=310, y=140)

ms = tk.Label(text="Ekran Boyutu", font="Helvatica 10")
ms.place(x=300, y=120)

knmbulbtn = tk.Button(text="Tıklama Yap", font="Helvatica 10", command=click)
knmbulbtn.place(x=20, y=180)

ms = tk.Label(text="Tıklama Sayısı: ", font="Helvatica 10")
ms.place(x=140, y=185)

tekrar = tk.Entry()
tekrar.insert(0, "1")
tekrar.place(x=270, y=185, width=40)

wait = tk.Label(text="| Bekleme Süresi: ", font="Helvatica 10")
wait.place(x=320, y=185)

waitime = tk.Entry()
waitime.insert(0, "0")
waitime.place(x=455, y=185, width=40)


otoyaz = tk.Label(text="Otomatik Yazıcı", font="Helvatica 20")
otoyaz.place(x=260 , y=220)

rehber = tk.Label(text = "Yazılacak yazıyı giriniz ve 5 saniye içinde otomatik yazılacak yeri seçip bekleyiniz.")
rehber.place(x=20, y=270)

yazi = tk.Entry()
yazi.insert(0, "İstediğini yaz...")
yazi.place(x=70, y=300, width=600)

yaz = tk.Label(text="Yazı: ", font="Helvatica 10")
yaz.place(x=20 , y=300)

yazdirbtn = tk.Button(text="Yazdir", font="Helvatica 10", command=yazdir)
yazdirbtn.place(x=20, y=340)

diger = tk.Label(text="Diğer Özellikler", font="Helvatica 20")
diger.place(x=260 , y=390)

screenshot = tk.Button(text="Ekran Görüntüsü Al", font="Helvatica 10", command=screenshotake)
screenshot.place(x=20, y=440)

sensec = tk.Entry()
sensec.insert(0, "Dosyaadı.png")
sensec.place(x=210, y=443, width=150)

shutdown = tk.Button(text="Bilgisayarı Kapat", font="Helvatica 10", command=shutdownc)
shutdown.place(x=20, y=480)

shuttime = tk.Entry()
shuttime.insert(0, "Süre Girin")
shuttime.place(x=210, y=483, width=150)

yenidenBaslat = tk.Button(text="Yeniden Başlat", font="Helvatica 10", command=resystem)
yenidenBaslat.place(x=20, y=520)

yenidenBaslats = tk.Entry()
yenidenBaslats.insert(0, "Süre Girin")
yenidenBaslats.place(x=210, y=523, width=150)

kameraAc = tk.Button(text="Kamera Aç", font="Helvatica 10", command=camera)
kameraAc.place(x=420, y=440)

kameraKapa = tk.Label(text="*Kamerayı kapatmak için 'x' tuşuna basınız \n ardından pencereyi kapatınız.", font="Helvatica 10")
kameraKapa.place(x=420 , y=480)

films = tk.Button(text="Film Bul", font="Helvatica 10", command=filmbul)
films.place(x=420, y=540)

film_adi2 = tk.Entry()
film_adi2.insert(0, "Harry Potter")
film_adi2.place(x=510, y=543, width=160)

kameraKapa = tk.Label(text="*Geckodriver gerektirir!", font="Helvatica 10")
kameraKapa.place(x=420 , y=575)

pencere.mainloop()
