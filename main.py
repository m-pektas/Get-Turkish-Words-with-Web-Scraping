from scraping import loadWordFromVikiToFile

uploadedWordCount,totalTime = loadWordFromVikiToFile()
print("Upladed {} turkish words in {} second.".format(uploadedWordCount,totalTime))