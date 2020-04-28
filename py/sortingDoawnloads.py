import os
downloads = 'C:/Users/MHAPC/Downloads'
archieve = ["zip", "rar", "iso", "7z", "gz"]
torrent = ["torrent"]
exe = ["exe", "msi", "bat"]
films = ["mp4", "mkv"]
music = ["mp3", "flac", "wav"]
pics = ["jpg", "png"]
text = ["txt", "doc", "docx", "pdf"]
entries = os.scandir(downloads)
def makeDir(dirName):
    os.mkdir(downloads + '/' + dirName)
def do(fType, entry):
    if (fType in exe):
        os.rename(downloads + '/' + entry.name, downloads + '/exe/' + entry.name)
    if (fType in torrent):
        os.rename(downloads + '/' + entry.name, downloads + '/torrent/' + entry.name)
    if (fType in archieve):
        os.rename(downloads + '/' + entry.name, downloads + '/archieve/' + entry.name)
    if (fType in films):
        os.rename(downloads + '/' + entry.name, downloads + '/films/' + entry.name)
    if (fType in music):
        os.rename(downloads + '/' + entry.name, downloads + '/music/' + entry.name)
    if (fType in pics):
        os.rename(downloads + '/' + entry.name, downloads + '/pics/' + entry.name)
    if (fType in text):
        os.rename(downloads + '/' + entry.name, downloads + '/text/' + entry.name)
for entry in entries:
     if os.path.isfile(os.path.join(downloads, entry)):
        nameSplitted = entry.name.split(".")
        fType = nameSplitted[-1]
        do(fType, entry)
        print(fType)