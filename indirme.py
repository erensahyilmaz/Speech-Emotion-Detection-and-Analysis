from bs4 import BeautifulSoup
from selenium import webdriver
from yt_dlp import YoutubeDL
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=demba+ba")
soup=BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
video_karti = soup.find_all("ytd-video-renderer",attrs={'class':'style-scope ytd-item-section-renderer'})
for video in video_karti:
    # Başlık
    baslik = video.find('a', {'id': 'video-title'}).text.strip()
    # Video linki
    link_basi = "https://www.youtube.com"
    link_sonu=video.find('a', {'id': 'video-title'})['href']
    if(link_sonu.split('/')[1]!='shorts'):
        link=link_basi+link_sonu
        print("Başlık:", baslik)
        print("Link:", link)
        print()
        opts={
            'format':'bestaudio/best'
            }
        with YoutubeDL(opts) as yt:
            yt.download([link])
        print(f'Yüklenen Video: {link}')