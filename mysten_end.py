import os
inp = "/Users/nata/Desktop/input"
lst = os.listdir(inp)
for fl in lst:
    print(r'/Users/nata/Desktop/mystem ' + '/Users/nata/Desktop/input' + os.sep + fl + " /Users/nata/Desktop/out_texts" + os.sep + fl + ' -cnid —format xml' )
    os.system(r'/Users/nata/Desktop/mystem ' + '/Users/nata/Desktop/input' + os.sep + fl + " /Users/nata/Desktop/out_texts" + os.sep + fl + ' -cnid —format xml' )
