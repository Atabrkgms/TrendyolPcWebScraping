import requests
from bs4 import BeautifulSoup
import pandas as pd
basic_url = "https://www.trendyol.com/"
url = ["https://www.trendyol.com/laptop-x-c103108","https://www.trendyol.com/laptop-x-c103108?pi="]
liste = []
a = 1
index = 0
while a<=50:
    if a ==1:
        r = requests.get(url[0])
        soup = BeautifulSoup(r.content, "lxml")
        urunler = soup.find_all("div", attrs={"class":"with-campaign-view"})
        for urun in urunler:
            urun_img = urun.find("div",{"class":"p-card-img-wr"}).img.get("src")
            urun_link = basic_url + urun.a.get("href")
            urun_price = urun.find("div",{"class":"prc-box-dscntd"}).text
            urun_name4 = urun.find("div", attrs={"class":"two-line-text"}).span.text
            urun_name5 = urun.find("span", attrs={"class":"prdct-desc-cntnr-name"}).text
            urun_name6 = urun_name4 + urun_name5
            r_ozellik = requests.get(urun_link)
            soup_ozellik = BeautifulSoup(r_ozellik.content,"lxml")
            urun_ozellikler = soup_ozellik.find_all("li",{"class":"detail-attr-item"})
            for urun_ozellik in urun_ozellikler:
                
                if urun_ozellik.find_all("span")[0].text=="İşlemci Tipi":
                    urun_islemci_tipi = urun_ozellik.find_all("span")[1].text
                if urun_ozellik.find_all("span")[0].text=="SSD Kapasitesi":
                    urun_ssd = urun_ozellik.find_all("span")[1].text
                if urun_ozellik.find_all("span")[0].text=="İşletim Sistemi":
                    urun_isletim_sistemi = urun_ozellik.find_all("span")[1].text
                if urun_ozellik.find_all("span")[0].text=="Çözünürlük":
                    urun_cozunurluk = urun_ozellik.find_all("span")[1].text
                if urun_ozellik.find_all("span")[0].text=="Ram (Sistem Belleği)":
                    urun_ram = urun_ozellik.find_all("span")[1].text
                if urun_ozellik.find_all("span")[0].text=="Ekran Boyutu":
                    urun_ekran_boyutu = urun_ozellik.find_all("span")[1].text
                                   
            liste.append([urun_name6,urun_link,urun_price,urun_img,urun_islemci_tipi,urun_isletim_sistemi,urun_ram,urun_ssd,urun_cozunurluk,urun_ekran_boyutu])
            index+=1
    else:
        r = requests.get(url[1]+str(a))
        soup = BeautifulSoup(r.content, "lxml")
        urunler = soup.find_all("div", attrs={"class":"with-campaign-view"})
        for urun in urunler:
            urun_img1 = urun.find("div",{"class":"p-card-img-wr"}).img.get("src")
            urun_link1 = basic_url +  urun.a.get("href")
            urun_price1 = urun.find("div",{"class":"prc-box-dscntd"}).text
            urun_name1 = urun.find("div", attrs={"class":"two-line-text"}).span.text
            urun_name2 = urun.find("span", attrs={"class":"prdct-desc-cntnr-name"}).text
            urun_name3 = urun_name1 + urun_name2
            r_ozellik1 = requests.get(urun_link1)
            soup_ozellik1 = BeautifulSoup(r_ozellik1.content,"lxml")
            urun_ozellikler1 = soup_ozellik1.find_all("li",{"class":"detail-attr-item"},limit = 6)
            for urun_ozellik1 in urun_ozellikler1:

                if urun_ozellik1.find_all("span")[0].text=="İşlemci Tipi":
                    urun_islemci_tipi1 = urun_ozellik1.find_all("span")[1].text
                if urun_ozellik1.find_all("span")[0].text=="SSD Kapasitesi":
                    urun_ssd1 = urun_ozellik1.find_all("span")[1].text
                if urun_ozellik1.find_all("span")[0].text=="İşletim Sistemi":
                    urun_isletim_sistemi1 = urun_ozellik1.find_all("span")[1].text
                if urun_ozellik1.find_all("span")[0].text=="Çözünürlük":
                    urun_cozunurluk1 = urun_ozellik1.find_all("span")[1].text
                if urun_ozellik1.find_all("span")[0].text=="Ram (Sistem Belleği)":
                    urun_ram1 = urun_ozellik1.find_all("span")[1].text
                if urun_ozellik1.find_all("span")[0].text=="Ekran Boyutu":
                    urun_ekran_boyutu = urun_ozellik1.find_all("span")[1].text
                
            liste.append([urun_name3,urun_link1,urun_price1,urun_img1,urun_islemci_tipi1,urun_isletim_sistemi1,urun_ram1,urun_ssd1,urun_cozunurluk1,urun_ekran_boyutu])
            index+=1

    a+=1        

print(index)
df = pd.DataFrame(liste)
df.columns=["ürün adi","ürün link","ürün fiyatı","ürün resmi","ürün işlemci tipi","ürün işletim sistemi","ürün ram","ürün ssd","ürün ekran çözünürlüğü","ürün ekran boyutu"]
df.to_excel("trendyolButunVeri.xlsx")