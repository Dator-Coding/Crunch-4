import os
global textList
textList = []
def findTxt():
    cr = open("FileIndexNEW.txt", 'w')
    for root, dirs, files in os.walk("E:\\Files"):
        for file in files:
            if file.endswith(".txt"):
                words = str(os.path.join(root, file))
                print(os.path.join(root, file))
                cr.write(words + "\n")
    cr.close()
findTxt()
print('done')

