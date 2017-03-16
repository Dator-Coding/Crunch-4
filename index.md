import os, codecs
class Core():
    print('CRUNCH frameworks version 4.0 loaded')
    global FirstPass #Used in verification process
    global SecondPass
    FirstPass = False
    SecondPass = False #Used in verification process
    def __init__(self): #Gets required information to run Crunch
        filePathToUse = input('State the file index to use: ')
        if ((os.path.isfile(filePathToUse)) == True):
            print('index found')
            #Module to be passed to
            Core.fileWorker(filePathToUse)
            #Module to be passed to
        else:
            print('index not found')
            Core()

    def fileWorker(filepath):
        locatedName = False
        #breaks down file's into word based outputs
        with open(filepath) as inputfile:
            for fileName in inputfile:
                fileName = fileName.replace('\n','')
                try:
                    print('passed file name')
                    with codecs.open(fileName,'r','utf-8') as ins:
                        for line in ins:
                            line = line.replace(')',' ')
                            line = line.replace('(', ' ')
                            line = line.replace('_', ' ')
                            line = line.replace('!', ' ')
                            line = line.replace('-', ' ')
                            line = line.replace('.', ' ')
                            line = line.replace('"', ' ')
                            line = line.replace(';', ' ')
                            line = line.replace(':', ' ')
                            line = line.replace(',', ' ')
                            line = line.replace('/', ' ')
                            line = line.replace('\\', ' ')
                            line = line.replace('|', ' ')
                            line = line.replace("'", ' ')
                            line = line.replace('+', ' ')
                            line = line.replace('-', ' ')
                            line = line.replace('=', ' ')
                            line = line.replace('*', ' ')
                            words = (line.split(" "))
                            for word in words:
                                print(word) #This could be outputted to a new module
                                result = (Core.CrunchWordBreaker(word))
                                if (result == True): #To exit for loop when critera is met
                                    print (fileName)
                                    break
                            if (result == True): #To exit for loop when critera is met
                                break
                        if (result == True): #To exit for loop when critera is met
                            break

                except:
                    print('error with file',fileName)

    def CrunchWordBreaker(wordToProcess):
        if (wordToProcess == 'communism'):
            print('Criteria to exit loop has been met')
            return True
        else:
            return False

Core()
#result = Core.CrunchMain('E:\\Files\\gutenberg\\1\\0\\0\\0\\10003\\10003.txt')
#if (result == False):
#    print('failed to locate file')
#else:
#    print('succeeded in locating file')
os.system('pause')
