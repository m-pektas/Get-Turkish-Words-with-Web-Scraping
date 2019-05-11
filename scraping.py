from bs4 import BeautifulSoup
import urllib.request
import LineCleaner as lc
import time
from config import root_URL,filepath,letters

def loadWordFromVikiToFile():
        print("Words Loading..")
        start = time.time()
        file = open(filepath,"a")
        uploadedWordCount=0
        for i in letters:
            url = root_URL+"("+i+")"
            read_url = urllib.request.urlopen(url)
            soup = BeautifulSoup(read_url, 'html.parser')
            if i=="A":
                wordList = soup.select("html body table tbody tr td ul li a")
            else:
                wordList = soup.select("html body div div div div  ul li a")

            for j in wordList:
                word = lc.cleanLine(str(j)).lower()                
                if word[0] == i.lower() and len(word.split(" ")) <= 2: #accept the word / phrase if it starts with the desired letter and 
                    try:                                               #consists of two pieces at most
                        uploadedWordCount = uploadedWordCount + 1
                        file.write(word)
                        file.write("\n")
                    except:
                        continue;
        file.close()
        end = time.time()
        print("Words Loading Done.")
        totalTime = str(end-start)
        return uploadedWordCount,totalTime