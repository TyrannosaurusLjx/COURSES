def printTrue(x1,x2,x3,w):
    boolLst = [x1,x2,x3,(not x1)or(not x2),(not x2)or(not x3),(not x1)or(not x3),x1 or (not w), x2 or (not w), x3 or (not w),w]
    boolLst = [bool(i) for i in boolLst]
    print(boolLst)  
    return boolLst

def testBool():
    for x1, x2, x3 in [(1, 1, 1), (1, 1, 0), (1, 0, 0), (0, 0, 0)]:  
        for w in [0,1]:
            print("x1,x2,x3,w= {},{},{},{}".format(x1,x2,x3,w))
            print(sum(printTrue(x1,x2,x3,w)))
    return 0

testBool()
