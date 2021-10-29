from bs4 import BeautifulSoup #python library for parsing structured html data
import requests #to send http requests and access the html content from the target webpage
import re
from pydub import AudioSegment #for format conversion

base_url = "https://freemusicarchive.org/music/charts/this-month?pageSize=10"
r = requests.get(base_url)

soup = BeautifulSoup(r.content, 'html.parser')

for aTag in soup.findAll("a", attrs = {"class", "icn-arrow js-download"}):
    if 'Overlay' in aTag['data-url'] and aTag['data-url'][-7:] == 'Overlay':
        aTag['data-url'] = aTag['data-url'][:-7]
#find data-url=".../downloadOverlay" and delete "Overlay"
#    seg = filtered.split('/')
#    filtered = [x for x in split if re.match('data-url', x)]
        addr = aTag['data-url']
    i = 0
#    for i in filtered[i]:
#        seg = filtered[i].split('/')
    spliter = addr.split('/')
    title = spliter[4]
#        url = "https://"+seg[2]+'/'+seg[3]+'/'+seg[4]+'/download'
    res = requests.get(addr)
    songs = open(title+".mp3", 'wb')
    songs.write(res.content)
    songs.close() #downloaded mp3 files

    src = title+".mp3"
    dst = title+".wav"
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format = "wav") #convert and save wav files


print ("Download Completed!")
#    subprocess.call(['ffmpeg', '-i', title, title+'.wav'])

