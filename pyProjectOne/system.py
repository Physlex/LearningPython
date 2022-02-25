import sys

lineLen = 10

def DrawLine() :
    for x in range(spaceOffset) :
        print(' ', end = '')

    for i in range(lineLen) :
        print('*', end = '')
    return

spaceOffset = 0
indent = 1

def Indent() :
    global spaceOffset
    global indent
    global indentMode
    spaceOffset += (indentMode * indent)
    return

indentMode = 1

def OffsetIncrementing() :
    global spaceOffset
    global indentMode
    #controls change in range boundaries at 0, 10
    if (spaceOffset == 0) :
        indentMode = 1
    elif (spaceOffset == 10) :
        indentMode = -1

def TEST() :
    global indentMode
    global spaceOffset
    global indent
    print('Mode: %d' % indentMode)
    print('Indent: %d' % indent)
    print('Space Offset: %d' % spaceOffset)
    return True

while True :
    try :
        OffsetIncrementing()
        Indent()
        DrawLine()
        input()
    except KeyboardInterrupt :
        sys.exit()