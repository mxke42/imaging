import time

def review_leftover_files(fileDictList, allSectionsList):
    for item in fileDictList:
        if item in allSectionsList:
            print("processRemainingFiles error, not yet configured")
            exit()
        else:
            continue
    print("remaining files are not adjacent to any indexed files.")
    ##attempt to index them by creating a new location dictionary
    print("WARNING!!! !! NEW LOCATION DICTIONARY STARTED")
    #time.sleep(1.5)
    allSectionsList = []
    return allSectionsList


