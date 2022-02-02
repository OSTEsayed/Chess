import tkinter as tk
from tkinter.ttk import *
from turtle import width

def startup():
    s.destroy()
    fr.destroy()
    global ucan,umust,blocker,bmust,gofrom,goto,bord,white,black,Game,tour,non,cc,rr
    ucan=[]
    umust=[]
    blocker=[]
    bmust=[]
    cc=0
    rr=0
    gofrom="NULL"
    goto="NULL"
    Game="none"
    tour="white"
    def checkmate(x):
        global tour,bord,black,white,umust
        y=0
        z=1
        if tour=="black":
            king=kingb
        else :
            king=kingw
        for i in range(8):
            for j in range(8):
                if bord[i][j][1]==king:
                    c=i
                    r=j 
        if x==2:
            if test(c+1,r)==0 and test(c+1,r+1)==0 and  test(c+1,r-1)==0 and test(c,r+1)==0 and  test(c,r-1)==0 and test(c-1,r)==0 and test(c-1,r+1)==0 and test(c-1,r-1)==0 :
                return y
        if x==1:
            for i in umust:
                if matet(i)==1:
                    return z
            if test(c+1,r)==1 or test(c+1,r+1)==1 or  test(c+1,r-1)==1 or test(c,r+1)==1 or  test(c,r-1)==1 or test(c-1,r)==1 or test(c-1,r+1)==1 or test(c-1,r-1)==1 :
                return z
            return y
    def matet(k):
        global tour,bord,black,white,bmust
        y=1
        z=0
        if tour=="black":
            tst=black
        else :
            tst=white
        for i in range(8):
            for j in range(8):
                if bord[i][j]==k:
                    c=i
                    r=j 
        if tour=="black":
            if c<6:
                if bord[c+1][r][1]==tst[0] and bord[c][r][1]=="e":
                    return y
                if bord[c+1][r-1][1]==tst[0] and bord[c][r][1]!="e":
                    return y
                if bord[c+1][r+1][1]==tst[0] and bord[c][r][1]!="e":
                    return y
        elif tour=="white":
            if c>1:
                if bord[c-1][r][1]==tst[0] and bord[c][r][1]=="e":
                    return y
                if bord[c-1][r-1][1]==tst[0] and bord[c][r][1]!="e":
                    return y
                if bord[c-1][r+1][1]==tst[0] and bord[c][r][1]!="e":
                    return y

        for i in range(r+1,8):
            if  bord[c][i][1]==tst[4] or bord[c][i][1]==tst[1]:
                return y
            elif bord[c][i][1]!="e":
                break
        for i in range(r-1,-1,-1):
            if  bord[c][i][1]==tst[4] or  bord[c][i][1]==tst[1]:
                return y
            elif bord[c][i][1]!="e":
                break
        for i in range(c+1,8):
            if  bord[i][r][1]==tst[4] or bord[i][r][1]==tst[1]:
                return y
            elif bord[i][r][1]!="e":
                break
        for i in range(c-1,-1,-1):
            if  bord[i][r][1]==tst[4] or bord[i][r][1]==tst[1]:
                return y
            elif bord[i][r][1]!="e":
                break
        t=1
        for i in range(r+1,8):
            if c+t==8:
                break
            elif bord[c+t][i][1]==tst[4] or bord[c+t][i][1]==tst[3]:
                return y
            elif bord[c+t][i][1]!="e":
                break
            t=t+1
        t=1
        for i in range(r-1,-1,-1):
            if c+t==8:
                break
            elif bord[c+t][i][1]==tst[4] or bord[c+t][i][1]==tst[3]:
                return y
            elif bord[c+t][i][1]!="e":
                break
            t=t+1
        t=1
        for i in range(r+1,8):
            if c-t==-1:
                break
            
            elif bord[c-t][i][1]==tst[4] or bord[c-t][i][1]==tst[3]:
                return y
            elif bord[c-t][i][1]!="e":
                break
            t=t+1
        t=1
        for i in range(r-1,-1,-1):
            if c-t==-1:
                break
            elif bord[c-t][i][1]==tst[4] or bord[c-t][i][1]==tst[3]:
                return y
            elif bord[c-t][i][1]!="e":
                break
            t=t+1
        if r>0 and c<6 : 
            if bord[c+2][r-1][1]==tst[2]:return y
        if r>1 and c<7:
            if bord[c+1][r-2][1]==tst[2]:return y  
        if r>1 and c>0: 
            if bord[c-1][r-2][1]==tst[2]:return y  
        if r>0 and c>1:
            if bord[c-2][r-1][1]==tst[2]:return y  
        if r<7 and c>1:
            if bord[c-2][r+1][1]==tst[2]:return y  
        if r<6 and c>0:
            if bord[c-1][r+2][1]==tst[2]:return y  
        if r<6 and c<7:
            if bord[c+1][r+2][1]==tst[2]:return y  
        if r<7 and c<6: 
            if bord[c+2][r+1][1]==tst[2]:return y
        return z
    def test(c,r):
        global tour,kingb,kingw,bord,black,white
        x=0
        y=1
        if tour=="black":
            tst=white
            ref=black
            if c>0:
                if bord[c-1][r+1][1]==tst[0]:
                    return x
                if bord[c-1][r-1][1]==tst[0]:
                    return x
        else :
            tst=black
            ref=white
            if c<7:
                if bord[c+1][r+1][1]==tst[0]:
                    return x
                if bord[c+1][r-1][1]==tst[0]:
                    return x
        if c<0 or c>7 or r<0 or r>8:
            return x
        elif bord[c][r][1] in ref:
            return x
        else :
            for i in range(r+1,8):
                if  bord[c][i][1]==tst[4] or bord[c][i][1]==tst[1]:
                    return x
                elif bord[c][i][1]!="e":
                    break
            for i in range(r-1,-1,-1):
                if  bord[c][i][1]==tst[4] or  bord[c][i][1]==tst[1]:
                    return x
                elif bord[c][i][1]!="e":
                    break
            for i in range(c+1,8):
                if  bord[i][r][1]==tst[4] or bord[i][r][1]==tst[1]:
                    return x
                elif bord[i][r][1]!="e":
                    break
            for i in range(c-1,-1,-1):
                if  bord[i][r][1]==tst[4] or bord[i][r][1]==tst[1]:
                    return x
                elif bord[i][r][1]!="e":
                    break
            t=1
            for i in range(r+1,8):
                if c+t==8:
                    break
                elif bord[c+t][i][1]==tst[4] or bord[c+t][i][1]==tst[3]:
                    return x
                elif bord[c+t][i][1]!="e":
                    break
                t=t+1
            t=1
            for i in range(r-1,-1,-1):
                if c+t==8:
                    break
                elif bord[c+t][i][1]==tst[4] or bord[c+t][i][1]==tst[3]:
                    return x
                elif bord[c+t][i][1]!="e":
                    break
                t=t+1
            t=1
            for i in range(r+1,8):
                if c-t==-1:
                    break
                
                elif bord[c-t][i][1]==tst[4] or bord[c-t][i][1]==tst[3]:
                    return x
                elif bord[c-t][i][1]!="e":
                    break
                t=t+1
            t=1
            for i in range(r-1,-1,-1):
                if c-t==-1:
                    break
                elif bord[c-t][i][1]==tst[4] or bord[c-t][i][1]==tst[3]:
                    return x
                elif bord[c-t][i][1]!="e":
                    break
                t=t+1
            return y
    def block():
        global tour,bord,white,black,bmust,blocker
        blocker=[]
        bmust=[]
        tt=[]
        tster=[]
        if tour=="black":
            king=kingb
            tst=white
            ref=black
        else :
            king=kingw
            tst=black
            ref=white
        for i in range(8):
            for j in range(8):
                if bord[i][j][1]==king:
                    c=i
                    r=j 
        b=0
        for i in range(r+1,8):
            if bord[c][i][1]=="e":
                tt.append(bord[c][i])
            elif  bord[c][i][1] in ref and b==0:
                tster.append(bord[c][i])
                b=1
            elif  bord[c][i][1] in ref and b==1:
                break
            elif b==1:
                if  bord[c][i][1]==tst[4] or bord[c][i][1]==tst[1]:
                    tt.append(bord[c][i])
                    tt.extend(tster)
                    x=tt
                    bmust.append(x)
                    blocker.extend(tster)
                    break
            else:break
        b=0

        tster =[]
        tt=[]
        for i in range(r-1,-1,-1):
            if bord[c][i][1]=="e":
                tt.append(bord[c][i])
            elif  bord[c][i][1] in ref and b==0:
                tster.append(bord[c][i])
                b=1
            elif  bord[c][i][1] in ref and b==1:
                break
            elif b==1:
                if  bord[c][i][1]==tst[4] or bord[c][i][1]==tst[1]:
                    tt.append(bord[c][i])
                    tt.extend(tster)
                    x=tt
                    bmust.append(x)
                    blocker.extend(tster) 
                    break
            else:break
        tster =[]
        tt=[]
        b=0
        for i in range(c+1,8):
            if bord[i][r][1]=="e":
                tt.append(bord[i][r])
            elif  bord[i][r][1] in ref and b==0:
                tster.append(bord[i][r])
                b=1
            elif  bord[i][r][1] in ref and b==1:
                break
            elif b==1:
                if  bord[i][r][1]==tst[4] or bord[i][r][1]==tst[1]:
                    tt.append(bord[i][r])   
                    tt.extend(tster)
                    x=tt
                    bmust.append(x)
                    blocker.extend(tster) 
                    break
            else:break
        b=0
        tster =[]
        tt=[]
        for i in range(c-1,-1,-1):
            if bord[i][r][1]=="e":
                tt.append(bord[i][r])
            elif  bord[i][r][1] in ref and b==0:
                tster.append(bord[i][r])
                b=1
            elif  bord[i][r][1] in ref and b==1:
                break
            elif b==1:
                if  bord[i][r][1]==tst[4] or bord[i][r][1]==tst[1]:
                
                    tt.append(bord[i][r])
                    tt.extend(tster)
                    x=tt
                    bmust.append(x)
                    blocker.extend(tster) 
                    break
            else:break
        b=0
        t=1
        tster =[]
        tt=[]
        for i in range(r+1,8):
            if c+t==8:
                break
            elif bord[c+t][i][1]=="e":
                tt.append(bord[c+t][i])
                t=t+1
            elif  bord[c+t][i][1] in ref and b==0:
                tster.append(bord[c+t][i])
                b=1
                t=t+1
            elif  bord[c+t][i][1] in ref and b==1:
                break
            elif b==1:
                if  bord[c+t][i][1]==tst[4] or bord[c+t][i][1]==tst[3]:
                    tt.append(bord[c+t][i])
                    tt.extend(tster)
                    x=tt
                    bmust.append(x)
                    blocker.extend(tster) 
                    break
            else:break
        b=0
        t=1 
        tster =[]
        tt=[]
        for i in range(r-1,-1,-1):
            if c+t==8:
                break
            elif bord[c+t][i][1]=="e" :
                tt.append(bord[c+t][i])
                t=t+1
            elif  bord[c+t][i][1] in ref and b==0:
                tster.append(bord[c+t][i])
                b=1
                t=t+1
            elif  bord[c+t][i][1] in ref and b==1:
                break
            elif b==1:
                if  bord[c+t][i][1]==tst[4] or bord[c+t][i][1]==tst[3]:
                    
                    
                    tt.append(bord[c+t][i])
                    tt.extend(tster)
                    x=tt
                    bmust.append(x)
                    blocker.extend(tster) 
                    break
            else:break
        b=0
        t=1 
        tster =[]
        tt=[]
        for i in range(r+1,8):
            if c-t==-1:
                break
            elif bord[c-t][i][1]=="e":
                tt.append(bord[c-t][i])
                t=t+1
            elif  bord[c-t][i][1] in ref and b==0:
                tster.append(bord[c-t][i])
                b=1
                t=t+1
            elif  bord[c-t][i][1] in ref and b==1:
                break
            elif b==1:
                if  bord[c-t][i][1]==tst[4] or bord[c-t][i][1]==tst[3]:
                    tt.append(bord[c-t][i])
                    tt.extend(tster)
                    x=tt
                    bmust.append(x)
                    blocker.extend(tster) 
                    break
            else:break
        b=0
        t=1
        tster =[]
        tt=[]
        for i in range(r-1,-1,-1):
            if c-t==-1:
                break
            elif bord[c-t][i][1]=="e" :
                tt.append(bord[c-t][i])
                t=t+1
            elif  bord[c-t][i][1] in ref and b==0:
                tster.append(bord[c-t][i])
                b=1
                t=t+1
            elif  bord[c-t][i][1] in ref and b==1:
                break
            elif b==1:
                if  bord[c-t][i][1]==tst[4] or bord[c-t][i][1]==tst[3]:
                    
                    tt.append(bord[c-t][i])
                    tt.extend(tster)
                    x=tt
                    bmust.append(x)
                    blocker.extend(tster) 
                    
                    break
            else:break      
    def check():
        global umust,tour,bord,white,black
        umust=[]    
        check=0
        tster=[]
        if tour=="black":
            king=kingb
            tst=white
            
        else :
            king=kingw
            tst=black
        for i in range(8):
            for j in range(8):
                if bord[i][j][1]==king:
                    c=i
                    r=j 
        if tour=="black":
            if c>0:
                if bord[c-1][r+1][1]==tst[0]:
                    check=check+1
                    umust.append(bord[c-1][r+1])
                if bord[c-1][r-1][1]==tst[0]:
                    check=check+1
                    umust.append(bord[c-1][r-1])
        else:
            if c<7:
                if bord[c+1][r+1][1]==tst[0]:
                    check=check+1
                    umust.append(bord[c+1][r+1])
                if bord[c+1][r-1][1]==tst[0]:
                    check=check+1
                    umust.append(bord[c+1][r-1])
                    
        for i in range(r+1,8):
            if bord[c][i][1]=="e" :
                tster.append(bord[c][i])
            elif  bord[c][i][1]==tst[4] or bord[c][i][1]==tst[1]:
                tster.append(bord[c][i])
                check=check+1
                umust.extend(tster)
                tster.clear()
                break
            else:
                tster.clear()
                break
        for i in range(r-1,-1,-1):
            if bord[c][i][1]=="e":
                tster.append(bord[c][i])
            elif  bord[c][i][1]==tst[4] or  bord[c][i][1]==tst[1] :
                tster.append(bord[c][i])
                check=check+1
                umust.extend(tster)
                tster.clear()
                break
            else:
                tster.clear()
                break
        for i in range(c+1,8):
            if bord[i][r][1]=="e":
                tster.append(bord[i][r])
            elif bord[i][r][1]==tst[1] or bord[i][r][1]==tst[4]:
                tster.append(bord[i][r])
                check=check+1
                umust.extend(tster)
                tster.clear()
                break
            else:
                tster.clear()
                break

        for i in range(c-1,-1,-1):
            if bord[i][r][1]=="e":
                tster.append(bord[i][r])
            elif bord[i][r][1]==tst[1] or bord[i][r][1]==tst[4]:
                tster.append(bord[i][r])
                check=check+1
                umust.extend(tster)
                tster.clear()
                break
            else:
                tster.clear()
                break
        t=1
        for i in range(r+1,8):
            if c+t==8:
                break
            elif bord[c+t][i][1]=="e" :
                tster.append(bord[c+t][i])
                t=t+1
            elif bord[c+t][i][1]==tst[3] or bord[c+t][i][1]==tst[4]:
                check=check+1
                tster.append(bord[c+t][i])
                umust.extend(tster)
                tster.clear()
                break
            else:
                tster.clear()
                break
        t=1
        for i in range(r-1,-1,-1):
            if c+t==8:
                break
            elif bord[c+t][i][1]=="e" :
                tster.append(bord[c+t][i])
                t=t+1
            elif bord[c+t][i][1]==tst[3] or bord[c+t][i][1]==tst[4] :
                tster.append(bord[c+t][i])
                check=check+1
                umust.extend(tster)
                tster.clear()
                break
            else:
                tster.clear()
                break
        t=1
        for i in range(r+1,8):
            if c-t==-1:
                break
            elif bord[c-t][i][1]=="e":
                tster.append(bord[c-t][i])
                t=t+1
            elif bord[c-t][i][1]==tst[3] or bord[c-t][i][1]==tst[4]:
                tster.append(bord[c-t][i])
                check=check+1
                umust.extend(tster)
                tster.clear()
                break
            else:
                tster.clear() 
                break
        t=1
        for i in range(r-1,-1,-1):
            if c-t==-1:
                break
            elif bord[c-t][i][1]=="e" :
                tster.append(bord[c-t][i])
                t=t+1
            elif bord[c-t][i][1]==tst[3] or bord[c-t][i][1]==tst[4]:
                tster.append(bord[c-t][i])
                check=check+1
                umust.extend(tster)
                tster.clear()
                break
            else:
                tster.clear()
                break
        if r>0 and c<6 : 
            if bord[c+2][r-1][1] ==tst[2]:
                check=check+1
                umust.append(bord[c+2][r-1])  
        if r>1 and c<7:
            if bord[c+1][r-2][1]==tst[2]:
                check=check+1
                umust.append(bord[c+1][r-2])  
        if r>1 and c>0: 
            if bord[c-1][r-2][1]==tst[2]:
                check=check+1
                umust.append(bord[c-1][r-2])  
        if r>0 and c>1:
            if bord[c-2][r-1][1]==tst[2]:
                check=check+1
                umust.append(bord[c-2][r-1])  
        if r<7 and c>1:
            if bord[c-2][r+1][1]==tst[2]:
                check=check+1
                umust.append(bord[c-2][r+1])  
        if r<6 and c>0:
            if bord[c-1][r+2][1]==tst[2]:
                check=check+1
                umust.append(bord[c-1][r+2])  
        if r<6 and c<7:
            if bord[c+1][r+2][1]==tst[2]:
                check=check+1
                umust.append(bord[c+1][r+2])  
        if r<7 and c<6: 
            if bord[c+2][r+1][1]==tst[2]:
                check=check+1
                umust.append(bord[c+2][r+1])
        return check
    def move(r,c):
        global gofrom,goto,Game,tour,black,white,cc,rr,non,blocker,bmust
        global bord,ucan
        x=check() 
        block()
        Y=checkmate(x)
        if Y==0:
            print("checkmate")
        elif gofrom=="NULL" and bord[c][r][1]!="e":
                    if tour=="black" and bord[c][r][1] in black :
                        gofrom=bord[c][r] 
                        cc=c
                        rr=r
                        if bord[c][r][1]==pb:
                            if bord[c-1][r][1]=="e":
                                ucan.append(bord[c-1][r])
                                if c==6:
                                    if bord[c-2][r][1]=="e":  ucan.append(bord[c-2][r])
                            if r!=0 and bord[c-1][r-1][1] in white :
                                ucan.append(bord[c-1][r-1])
                            if r!=7 and bord[c-1][r+1][1] in white:
                                ucan.append(bord[c-1][r+1])
                        elif bord[c][r][1]==rb:
                            for i in range(r+1,8):
                                if bord[c][i][1]=="e":
                                    ucan.append(bord[c][i])
                                elif bord[c][i][1] in white:
                                    ucan.append(bord[c][i])
                                    break
                                else:
                                    break                            
                            for i in range(r-1,-1,-1):
                                if bord[c][i][1]=="e":
                                    ucan.append(bord[c][i])
                                elif bord[c][i][1] in white:
                                    ucan.append(bord[c][i])
                                    break
                                else:
                                    break 

                            for i in range(c+1,8):
                                if bord[i][r][1]=="e":
                                    ucan.append(bord[i][r])
                                elif bord[i][r][1] in white:
                                    ucan.append(bord[i][r])
                                    break
                                else:
                                    break
                            for i in range(c-1,-1,-1):
                                if bord[i][r][1]=="e":
                                    ucan.append(bord[i][r])
                                elif bord[i][r][1] in white:
                                    ucan.append(bord[i][r])
                                    break
                                else:
                                    break 
                                
                        elif bord[c][r][1]==fb:
                            t=1
                            for i in range(r+1,8):
                                if c+t==8:
                                    break
                                elif bord[c+t][i][1]=="e":
                                    ucan.append(bord[c+t][i])
                                    t=t+1
                                elif bord[c+t][i][1] in white:
                                    ucan.append(bord[c+t][i])
                                    break
                                else:
                                    break 
                            t=1
                            for i in range(r-1,-1,-1):
                                if c+t==8:
                                    break
                                elif bord[c+t][i][1]=="e":
                                    ucan.append(bord[c+t][i])
                                    t=t+1
                                elif bord[c+t][i][1] in white:
                                    ucan.append(bord[c+t][i])
                                    break
                                else:
                                    break 
                            t=1
                            for i in range(r+1,8):
                                if c-t==-1:
                                    break
                                elif bord[c-t][i][1]=="e":
                                    ucan.append(bord[c-t][i])
                                    t=t+1
                                elif bord[c-t][i][1] in white:
                                    ucan.append(bord[c-t][i])
                                    break
                                else:
                                    break 
                            t=1
                            for i in range(r-1,-1,-1):
                                if c-t==-1:
                                    break
                                elif bord[c-t][i][1]=="e":
                                    ucan.append(bord[c-t][i])
                                    t=t+1
                                elif bord[c-t][i][1] in white:
                                    ucan.append(bord[c-t][i])
                                    break
                                else:
                                    break 
                        elif bord[c][r][1]==qb:
                            for i in range(r+1,8):
                                if bord[c][i][1]=="e":
                                    ucan.append(bord[c][i])
                                elif bord[c][i][1] in white:
                                    ucan.append(bord[c][i])
                                    break
                                else:
                                    break                            
                            for i in range(r-1,-1,-1):
                                if bord[c][i][1]=="e":
                                    ucan.append(bord[c][i])
                                elif bord[c][i][1] in white:
                                    ucan.append(bord[c][i])
                                    break
                                else:
                                    break 
                            for i in range(c+1,8):
                                if bord[i][r][1]=="e":
                                    ucan.append(bord[i][r])
                                elif bord[i][r][1] in white:
                                    ucan.append(bord[i][r])
                                    break
                                else:
                                    break
                            for i in range(c-1,-1,-1):
                                if bord[i][r][1]=="e":
                                    ucan.append(bord[i][r])
                                elif bord[i][r][1] in white:
                                    ucan.append(bord[i][r])
                                    break
                                else:
                                    break 
                            t=1
                            for i in range(r+1,8):
                                if c+t==8:
                                    break
                                elif bord[c+t][i][1]=="e":
                                    ucan.append(bord[c+t][i])
                                    t=t+1
                                elif bord[c+t][i][1] in white:
                                    ucan.append(bord[c+t][i])
                                    break
                                else:
                                    break 
                            t=1
                            for i in range(r-1,-1,-1):
                                if c+t==8:
                                    break
                                elif bord[c+t][i][1]=="e":
                                    ucan.append(bord[c+t][i])
                                    t=t+1
                                elif bord[c+t][i][1] in white:
                                    ucan.append(bord[c+t][i])
                                    break
                                else:
                                    break 
                            t=1
                            for i in range(r+1,8):
                                if c-t==-1:
                                    break
                                elif bord[c-t][i][1]=="e":
                                    ucan.append(bord[c-t][i])
                                    t=t+1
                                elif bord[c-t][i][1] in white:
                                    ucan.append(bord[c-t][i])
                                    break
                                else:
                                    break 
                            t=1
                            for i in range(r-1,-1,-1):
                                if c-t==-1:
                                    break
                                elif bord[c-t][i][1]=="e":
                                    ucan.append(bord[c-t][i])
                                    t=t+1
                                elif bord[c-t][i][1] in white:
                                    ucan.append(bord[c-t][i])
                                    break
                                else:
                                    break 
                        elif bord[c][r][1]==kb:
                            
                            if r>0 and c<6 : 
                                if bord[c+2][r-1][1]=="e" or bord[c+2][r-1][1] in white:ucan.append(bord[c+2][r-1])  
                            if r>1 and c<7:
                                if bord[c+1][r-2][1]=="e" or bord[c+1][r-2][1] in white:ucan.append(bord[c+1][r-2])  
                            if r>1 and c>0: 
                                if bord[c-1][r-2][1]=="e" or bord[c-1][r-2][1] in white:ucan.append(bord[c-1][r-2])  
                            if r>0 and c>1:
                                if bord[c-2][r-1][1]=="e" or bord[c-2][r-1][1] in white:ucan.append(bord[c-2][r-1])  
                            if r<7 and c>1:
                                if bord[c-2][r+1][1]=="e" or bord[c-2][r+1][1] in white:ucan.append(bord[c-2][r+1])  
                            if r<6 and c>0:
                                if bord[c-1][r+2][1]=="e" or bord[c-1][r+2][1] in white:ucan.append(bord[c-1][r+2])  
                            if r<6 and c<7:
                                if bord[c+1][r+2][1]=="e" or bord[c+1][r+2][1] in white:ucan.append(bord[c+1][r+2])  
                            if r<7 and c<6: 
                                if bord[c+2][r+1][1]=="e" or bord[c+2][r+1][1] in white:ucan.append(bord[c+2][r+1])
                        elif bord[c][r][1]==kingb:
                            if test(c+1,r)==1:
                                ucan.append(bord[c+1][r])
                            if test(c+1,r+1)==1:
                                ucan.append(bord[c+1][r+1])
                            if test(c+1,r-1)==1:
                                ucan.append(bord[c+1][r-1])
                            if test(c,r+1)==1:
                                ucan.append(bord[c][r+1])
                            if test(c,r-1)==1:
                                ucan.append(bord[c][r-1])
                            if test(c-1,r)==1:
                                ucan.append(bord[c-1][r])
                            if test(c-1,r+1)==1:
                                ucan.append(bord[c-1][r+1])
                            if test(c-1,r-1)==1:
                                ucan.append(bord[c-1][r-1])

                        if x==1 and bord[c][r][1]!=kingb:
                            copie=ucan.copy()
                            ucan.clear()
                            for i in copie:
                                if i in umust:
                                    ucan.append(i) 
                            copie.clear()
                        elif x>1 and bord[c][r][1]!=kingb:
                            ucan.clear()
                            return
                        if bord[c][r] in blocker:
                            copie=ucan.copy()
                            ucan.clear()
                            for i in bmust:
                                if bord[c][r] in i:
                                        for g in copie:
                                            if g in i:
                                                ucan.append(g)
                            copie.clear()
                        for i in range(len(ucan)):
                            ucan[i][0].config(bg="green")     


                    if tour=="white" and bord[c][r][1] in white:
                        gofrom=bord[c][r]
                        cc=c
                        rr=r
                        
                        if bord[c][r][1]==pw:
                            if bord[c+1][r][1]=="e":
                                ucan.append(bord[c+1][r])
                                if c==1:
                                    if bord[c+2][r][1]=="e": ucan.append(bord[c+2][r])
                            if r!=0 and  bord[c+1][r-1][1] in black:
                                ucan.append(bord[c+1][r-1])
                            if r!=7 and bord[c+1][r+1][1] in black:
                                ucan.append(bord[c+1][r+1])

                        elif bord[c][r][1]==rw:
                            for i in range(r+1,8):
                                if bord[c][i][1]=="e":
                                    ucan.append(bord[c][i])
                                elif bord[c][i][1] in black:
                                    ucan.append(bord[c][i])
                                    break
                                else:
                                    break                            
                            for i in range(r-1,-1,-1):
                                if bord[c][i][1]=="e":
                                    ucan.append(bord[c][i])
                                elif bord[c][i][1] in black:
                                    ucan.append(bord[c][i])
                                    break
                                else:
                                    break 

                            for i in range(c+1,8):
                                if bord[i][r][1]=="e":
                                    ucan.append(bord[i][r])
                                elif bord[i][r][1] in black:
                                    ucan.append(bord[i][r])
                                    break
                                else:
                                    break
                            for i in range(c-1,-1,-1):
                                if bord[i][r][1]=="e":
                                    ucan.append(bord[i][r])
                                elif bord[i][r][1] in black:
                                    ucan.append(bord[i][r])
                                    break
                                else:
                                    break 

                        elif bord[c][r][1]==fw:
                            t=1
                            for i in range(r+1,8):
                                if c+t==8:
                                    break
                                elif bord[c+t][i][1]=="e":
                                    ucan.append(bord[c+t][i])
                                    t=t+1
                                elif bord[c+t][i][1] in black:
                                    ucan.append(bord[c+t][i])
                                    break
                                else:
                                    break 
                            t=1
                            for i in range(r-1,-1,-1):
                                if c+t==8:
                                    break
                                elif bord[c+t][i][1]=="e":
                                    ucan.append(bord[c+t][i])
                                    t=t+1
                                elif bord[c+t][i][1] in black:
                                    ucan.append(bord[c+t][i])
                                    break
                                else:
                                    break 
                            t=1
                            for i in range(r+1,8):
                                if c-t==-1:
                                    break
                                elif bord[c-t][i][1]=="e":
                                    ucan.append(bord[c-t][i])
                                    t=t+1
                                elif bord[c-t][i][1] in black:
                                    ucan.append(bord[c-t][i])
                                    break
                                else:
                                    break 
                            t=1
                            for i in range(r-1,-1,-1):
                                if c-t==-1:
                                    break
                                elif bord[c-t][i][1]=="e":
                                    ucan.append(bord[c-t][i])
                                    t=t+1
                                elif bord[c-t][i][1] in black:
                                    ucan.append(bord[c-t][i])
                                    break
                                else:
                                    break 
                        elif bord[c][r][1]==qw:
                            for i in range(r+1,8):
                                if bord[c][i][1]=="e":
                                    ucan.append(bord[c][i])
                                elif bord[c][i][1] in black:
                                    ucan.append(bord[c][i])
                                    break
                                else:
                                    break                            
                            for i in range(r-1,-1,-1):
                                if bord[c][i][1]=="e":
                                    ucan.append(bord[c][i])
                                elif bord[c][i][1] in black:
                                    ucan.append(bord[c][i])
                                    break
                                else:
                                    break 
                            for i in range(c+1,8):
                                if bord[i][r][1]=="e":
                                    ucan.append(bord[i][r])
                                elif bord[i][r][1] in black:
                                    ucan.append(bord[i][r])
                                    break
                                else:
                                    break
                            for i in range(c-1,-1,-1):
                                if bord[i][r][1]=="e":
                                    ucan.append(bord[i][r])
                                elif bord[i][r][1] in black:
                                    ucan.append(bord[i][r])
                                    break
                                else:
                                    break 
                            t=1
                            for i in range(r+1,8):
                                if c+t==8:
                                    break
                                elif bord[c+t][i][1]=="e":
                                    ucan.append(bord[c+t][i])
                                    t=t+1
                                elif bord[c+t][i][1] in black:
                                    ucan.append(bord[c+t][i])
                                    break
                                else:
                                    break 
                            t=1
                            for i in range(r-1,-1,-1):
                                if c+t==8:
                                    break
                                elif bord[c+t][i][1]=="e":
                                    ucan.append(bord[c+t][i])
                                    t=t+1
                                elif bord[c+t][i][1] in black:
                                    ucan.append(bord[c+t][i])
                                    break
                                else:
                                    break 
                            t=1
                            for i in range(r+1,8):
                                if c-t==-1:
                                    break
                                elif bord[c-t][i][1]=="e":
                                    ucan.append(bord[c-t][i])
                                    t=t+1
                                elif bord[c-t][i][1] in black:
                                    ucan.append(bord[c-t][i])
                                    break
                                else:
                                    break 
                            t=1
                            for i in range(r-1,-1,-1):
                                if c-t==-1:
                                    break
                                elif bord[c-t][i][1]=="e":
                                    ucan.append(bord[c-t][i])
                                    t=t+1
                                elif bord[c-t][i][1] in black:
                                    ucan.append(bord[c-t][i])
                                    break
                                else:
                                    break 
                        elif bord[c][r][1]==kw:
                            
                            if r>0 and c<6 : 
                                if bord[c+2][r-1][1]=="e" or bord[c+2][r-1][1] in black:ucan.append(bord[c+2][r-1])  
                            if r>1 and c<7:
                                if bord[c+1][r-2][1]=="e" or bord[c+1][r-2][1] in black:ucan.append(bord[c+1][r-2])  
                            if r>1 and c>0: 
                                if bord[c-1][r-2][1]=="e" or bord[c-1][r-2][1] in black:ucan.append(bord[c-1][r-2])  
                            if r>0 and c>1:
                                if bord[c-2][r-1][1]=="e" or bord[c-2][r-1][1] in black:ucan.append(bord[c-2][r-1])  
                            if r<7 and c>1:
                                if bord[c-2][r+1][1]=="e" or bord[c-2][r+1][1] in black:ucan.append(bord[c-2][r+1])  
                            if r<6 and c>0:
                                if bord[c-1][r+2][1]=="e" or bord[c-1][r+2][1] in black:ucan.append(bord[c-1][r+2])  
                            if r<6 and c<7:
                                if bord[c+1][r+2][1]=="e" or bord[c+1][r+2][1] in black:ucan.append(bord[c+1][r+2])  
                            if r<7 and c<6: 
                                if bord[c+2][r+1][1]=="e" or bord[c+2][r+1][1] in black:ucan.append(bord[c+2][r+1]) 
                        elif bord[c][r][1]==kingw:
                            if test(c+1,r)==1:
                                ucan.append(bord[c+1][r])
                            if test(c+1,r+1)==1:
                                ucan.append(bord[c+1][r+1])
                            if test(c+1,r-1)==1:
                                ucan.append(bord[c+1][r-1])
                            if test(c,r+1)==1:
                                ucan.append(bord[c][r+1])
                            if test(c,r-1)==1:
                                ucan.append(bord[c][r-1])
                            if test(c-1,r)==1:
                                ucan.append(bord[c-1][r])
                            if test(c-1,r+1)==1:
                                ucan.append(bord[c-1][r+1])
                            if test(c-1,r-1)==1:
                                ucan.append(bord[c-1][r-1])
                        if x==1 and bord[c][r][1]!=kingw:
                            copie=ucan.copy()
                            ucan.clear()
                            for i in copie:
                                if i in umust:
                                    ucan.append(i) 
                            copie.clear()
                        elif x>1 and bord[c][r][1]!=kingw:
                            ucan.clear()
                            return
                        if bord[c][r] in blocker:
                            copie=ucan.copy()
                            ucan.clear()
                            for i in bmust:
                                if bord[c][r] in i:
                                        for g in copie:
                                            if g in i:
                                                ucan.append(g)
                            copie.clear()
                        for i in range(len(ucan)):
                            ucan[i][0].config(bg="red")    
                            
    
        elif gofrom!="NULL":
                
                if bord[c][r] in ucan:
                    if bord[cc][rr][1]==pw and c==7:
                        goto=bord[c][r]
                        goto[0].config(image=qw,width=88,height=65)
                        gofrom[0].config(image=non)
                        bord[c][r][1]=qw
                        bord[cc][rr][1]="e"
                        if tour=="black":
                            tour="white"
                        else:tour="black"
                        goto="NULL"
                        gofrom="NULL"
                        ucan.clear()
                    elif bord[cc][rr][1]==pb and c==0:
                        goto=bord[c][r]
                        goto[0].config(image=qb,width=88,height=65)
                        gofrom[0].config(image=non)
                        bord[c][r][1]=qb
                        bord[cc][rr][1]="e"
                        if tour=="black":
                            tour="white"
                        else:tour="black"
                        goto="NULL"
                        gofrom="NULL"
                        ucan.clear()
                    else:
                        goto=bord[c][r]
                        goto[0].config(image=gofrom[1],width=88,height=65)
                        gofrom[0].config(image=non)
                        bord[c][r][1]=gofrom[1]
                        bord[cc][rr][1]="e"
                        
                        if tour=="black":
                            tour="white"
                        else:tour="black"
                        goto="NULL"
                        gofrom="NULL"
                        ucan.clear()
                else :
                    gofrom="NULL"
                    ucan.clear()

        if Game!="none":
            return
   

    Frame1= tk.Frame(chess,bg="black",width=900,height=500)
    Frame1.place(x=0,y=0)
    non = tk.PhotoImage(file=r'im/none.png')

    pb = tk.PhotoImage(file=r'im/pb.png')
    pw = tk.PhotoImage(file=r'im/pw.png')

    rb = tk.PhotoImage(file=r'im/rb.png')
    rw = tk.PhotoImage(file=r'im/rw.png')

    kb = tk.PhotoImage(file=r'im/kb.png')
    kw = tk.PhotoImage(file=r'im/kw.png')

    fb = tk.PhotoImage(file=r'im/fb.png')
    fw = tk.PhotoImage(file=r'im/fw.png')

    qb = tk.PhotoImage(file=r'im/qb.png')
    qw = tk.PhotoImage(file=r'im/qw.png')

    kingb = tk.PhotoImage(file = r"im/kingb.png")
    kingw = tk.PhotoImage(file = r"im/kingw.png")


    white=[pw,rw,kw,fw,qw,kingw]
    black=[pb,rb,kb,fb,qb,kingb]



    a1=tk.Button(Frame1,bg="#A75907",width=88,height=65,image=rw,command=lambda:move(0,0))

    a1.grid(row=8,column=1)
    a2=tk.Button(Frame1,width=88,height=65,bg="#E4BB62",image=pw,command=lambda:move(0,1))
    a2.grid(row=7,column=1)
    a3=tk.Button(Frame1,bg="#A75907",width=12,height=4,command=lambda:move(0,2))
    a3.grid(row=6,column=1)
    a4=tk.Button(Frame1,bg="#E4BB62",width=12,height=4,command=lambda:move(0,3))
    a4.grid(row=5,column=1)
    a5=tk.Button(Frame1,bg="#A75907",width=12,height=4,command=lambda:move(0,4))
    a5.grid(row=4,column=1)
    a6=tk.Button(Frame1,bg="#E4BB62",width=12,height=4,command=lambda:move(0,5))
    a6.grid(row=3,column=1)
    a7=tk.Button(Frame1,bg="#A75907",width=88,height=65,image=pb,command=lambda:move(0,6))
    a7.grid(row=2,column=1)
    a8=tk.Button(Frame1,bg="#E4BB62",width=88,height=65,image=rb,command=lambda:move(0,7))
    a8.grid(row=1,column=1)


    b1=tk.Button(Frame1,bg="#E4BB62",width=88,height=65,image=kw,command=lambda:move(1,0))
    b1.grid(row=8,column=2)
    b2=tk.Button(Frame1,bg="#A75907",width=88,height=65,image=pw,command=lambda:move(1,1))
    b2.grid(row=7,column=2)
    b3=tk.Button(Frame1,bg="#E4BB62",width=12,height=4,command=lambda:move(1,2))
    b3.grid(row=6,column=2)
    b4=tk.Button(Frame1,bg="#A75907",width=12,height=4,command=lambda:move(1,3))
    b4.grid(row=5,column=2)
    b5=tk.Button(Frame1,bg="#E4BB62",width=12,height=4,command=lambda:move(1,4))
    b5.grid(row=4,column=2)
    b6=tk.Button(Frame1,bg="#A75907",width=12,height=4,command=lambda:move(1,5))
    b6.grid(row=3,column=2)
    b7=tk.Button(Frame1,bg="#E4BB62",width=88,height=65,image=pb,command=lambda:move(1,6))
    b7.grid(row=2,column=2)
    b8=tk.Button(Frame1,bg="#A75907",width=88,height=65,image=kb,command=lambda:move(1,7))
    b8.grid(row=1,column=2)

    c1=tk.Button(Frame1,bg="#A75907",width=88,height=65,image=fw,command=lambda:move(2,0))
    c1.grid(row=8,column=3)
    c2=tk.Button(Frame1,bg="#E4BB62",width=88,height=65,image=pw,command=lambda:move(2,1))
    c2.grid(row=7,column=3)
    c3=tk.Button(Frame1,bg="#A75907",width=12,height=4,command=lambda:move(2,2))
    c3.grid(row=6,column=3)
    c4=tk.Button(Frame1,bg="#E4BB62",width=12,height=4,command=lambda:move(2,3))
    c4.grid(row=5,column=3)
    c5=tk.Button(Frame1,bg="#A75907",width=12,height=4,command=lambda:move(2,4))
    c5.grid(row=4,column=3)
    c6=tk.Button(Frame1,bg="#E4BB62",width=12,height=4,command=lambda:move(2,5))
    c6.grid(row=3,column=3)
    c7=tk.Button(Frame1,bg="#A75907",width=88,height=65,image=pb,command=lambda:move(2,6))
    c7.grid(row=2,column=3)
    c8=tk.Button(Frame1,bg="#E4BB62",width=88,height=65,image=fb,command=lambda:move(2,7))
    c8.grid(row=1,column=3)

    d1=tk.Button(Frame1,bg="#E4BB62",width=88,height=65,image=qw,command=lambda:move(3,0))
    d1.grid(row=8,column=4)
    d2=tk.Button(Frame1,bg="#A75907",width=88,height=65,image=pw,command=lambda:move(3,1))
    d2.grid(row=7,column=4)
    d3=tk.Button(Frame1,bg="#E4BB62",width=12,height=4,command=lambda:move(3,2))
    d3.grid(row=6,column=4)
    d4=tk.Button(Frame1,bg="#A75907",width=12,height=4,command=lambda:move(3,3))
    d4.grid(row=5,column=4)
    d5=tk.Button(Frame1,bg="#E4BB62",width=12,height=4,command=lambda:move(3,4))
    d5.grid(row=4,column=4)
    d6=tk.Button(Frame1,bg="#A75907",width=12,height=4,command=lambda:move(3,5))
    d6.grid(row=3,column=4)
    d7=tk.Button(Frame1,bg="#E4BB62",width=88,height=65,image=pb,command=lambda:move(3,6))
    d7.grid(row=2,column=4)
    d8=tk.Button(Frame1,bg="#A75907",width=88,height=65,image=qb,command=lambda:move(3,7))
    d8.grid(row=1,column=4)

    e1=tk.Button(Frame1,bg="#A75907",width=88,height=65,image=kingw,command=lambda:move(4,0))
    e1.grid(row=8,column=5)
    e2=tk.Button(Frame1,bg="#E4BB62",width=88,height=65,image=pw,command=lambda:move(4,1))
    e2.grid(row=7,column=5)
    e3=tk.Button(Frame1,bg="#A75907",width=12,height=4,command=lambda:move(4,2))
    e3.grid(row=6,column=5)
    e4=tk.Button(Frame1,bg="#E4BB62",width=12,height=4,command=lambda:move(4,3))
    e4.grid(row=5,column=5)
    e5=tk.Button(Frame1,bg="#A75907",width=12,height=4,command=lambda:move(4,4))
    e5.grid(row=4,column=5)
    e6=tk.Button(Frame1,bg="#E4BB62",width=12,height=4,command=lambda:move(4,5))
    e6.grid(row=3,column=5)
    e7=tk.Button(Frame1,bg="#A75907",width=88,height=65,image=pb,command=lambda:move(4,6))
    e7.grid(row=2,column=5)
    e8=tk.Button(Frame1,bg="#E4BB62",width=88,height=65,image=kingb,command=lambda:move(4,7))
    e8.grid(row=1,column=5)

    f1=tk.Button(Frame1,bg="#E4BB62",width=88,height=65,image=fw,command=lambda:move(5,0))
    f1.grid(row=8,column=6)
    f2=tk.Button(Frame1,bg="#A75907",width=88,height=65,image=pw,command=lambda:move(5,1))
    f2.grid(row=7,column=6)
    f3=tk.Button(Frame1,bg="#E4BB62",width=12,height=4,command=lambda:move(5,2))
    f3.grid(row=6,column=6)
    f4=tk.Button(Frame1,bg="#A75907",width=12,height=4,command=lambda:move(5,3))
    f4.grid(row=5,column=6)
    f5=tk.Button(Frame1,bg="#E4BB62",width=12,height=4,command=lambda:move(5,4))
    f5.grid(row=4,column=6)
    f6=tk.Button(Frame1,bg="#A75907",width=12,height=4,command=lambda:move(5,5))
    f6.grid(row=3,column=6)
    f7=tk.Button(Frame1,bg="#E4BB62",width=88,height=65,image=pb,command=lambda:move(5,6))
    f7.grid(row=2,column=6)
    f8=tk.Button(Frame1,bg="#A75907",width=88,height=65,image=fb,command=lambda:move(5,7))
    f8.grid(row=1,column=6)

    g1=tk.Button(Frame1,bg="#A75907",width=88,height=65,image=kw,command=lambda:move(6,0))
    g1.grid(row=8,column=7)
    g2=tk.Button(Frame1,bg="#E4BB62",width=88,height=65,image=pw,command=lambda:move(6,1))
    g2.grid(row=7,column=7)
    g3=tk.Button(Frame1,bg="#A75907",width=12,height=4,command=lambda:move(6,2))
    g3.grid(row=6,column=7)
    g4=tk.Button(Frame1,bg="#E4BB62",width=12,height=4,command=lambda:move(6,3))
    g4.grid(row=5,column=7)
    g5=tk.Button(Frame1,bg="#A75907",width=12,height=4,command=lambda:move(6,4))
    g5.grid(row=4,column=7)
    g6=tk.Button(Frame1,bg="#E4BB62",width=12,height=4,command=lambda:move(6,5))
    g6.grid(row=3,column=7)
    g7=tk.Button(Frame1,bg="#A75907",width=88,height=65,image=pb,command=lambda:move(6,6))
    g7.grid(row=2,column=7)
    g8=tk.Button(Frame1,bg="#E4BB62",width=88,height=65,image=kb,command=lambda:move(6,7))
    g8.grid(row=1,column=7)

    h1=tk.Button(Frame1,bg="#E4BB62",width=88,height=65,image=rw,command=lambda:move(7,0))
    h1.grid(row=8,column=8)
    h2=tk.Button(Frame1,bg="#A75907",width=88,height=65,image=pw,command=lambda:move(7,1))
    h2.grid(row=7,column=8)
    h3=tk.Button(Frame1,bg="#E4BB62",width=12,height=4,command=lambda:move(7,2))
    h3.grid(row=6,column=8)
    h4=tk.Button(Frame1,bg="#A75907",width=12,height=4,command=lambda:move(7,3))
    h4.grid(row=5,column=8)
    h5=tk.Button(Frame1,bg="#E4BB62",width=12,height=4,command=lambda:move(7,4))
    h5.grid(row=4,column=8)
    h6=tk.Button(Frame1,bg="#A75907",width=12,height=4,command=lambda:move(7,5))
    h6.grid(row=3,column=8)
    h7=tk.Button(Frame1,bg="#E4BB62",width=88,height=65,image=pb,command=lambda:move(7,6))
    h7.grid(row=2,column=8)
    h8=tk.Button(Frame1,bg="#A75907",width=88,height=65,image=rb,command=lambda:move(7,7))
    h8.grid(row=1,column=8)

    bord=[
        [[a1,rw],[b1,kw],[c1,fw],[d1,qw],[e1,kingw],[f1,fw],[g1,kw],[h1,rw]],
        [[a2,pw],[b2,pw],[c2,pw],[d2,pw],[e2,pw],[f2,pw],[g2,pw],[h2,pw]],
        [[a3,"e"],[b3,"e"],[c3,"e"],[d3,"e"],[e3,"e"],[f3,"e"],[g3,"e"],[h3,"e"]],
        [[a4,"e"],[b4,"e"],[c4,"e"],[d4,"e"],[e4,"e"],[f4,"e"],[g4,"e"],[h4,"e"]],
        [[a5,"e"],[b5,"e"],[c5,"e"],[d5,"e"],[e5,"e"],[f5,"e"],[g5,"e"],[h5,"e"]],
        [[a6,"e"],[b6,"e"],[c6,"e"],[d6,"e"],[e6,"e"],[f6,"e"],[g6,"e"],[h6,"e"]],
        [[a7,pb],[b7,pb],[c7,pb],[d7,pb],[e7,pb],[f7,pb],[g7,pb],[h7,pb]],
        [[a8,rb],[b8,kb],[c8,fb],[d8,qb],[e8,kingb],[f8,fb],[g8,kb],[h8,rb]]
        ]
    chess.mainloop()

chess= tk.Tk()
chess.title("Chess 2 Player")
chess.geometry("1200x600")

b = tk.PhotoImage(file = r"im/kingb.png")
w = tk.PhotoImage(file = r"im/kingw.png")
q = tk.PhotoImage(file = r"im/qw.png")
qw = tk.PhotoImage(file = r"im/qb.png")
fr=tk.Frame(chess)
frW=tk.Frame(fr,bg="white")
frB=tk.Frame(fr,bg="black")
fr.place(x=40,y=40,width=1100,height=450)
frW.place(x=40,y=20,width=470,height=420)
frB.place(x=550,y=20,width=470,height=420)
labw= tk.Label(frW,text="white Setting:",font=("arial",25),fg="#A75907")
labw.grid(row=0,column=0,columnspan=5,sticky="N")
namw= tk.Label(frW,text="Name:",font=("arial",25),fg="#A75907",bg="white")
namw.grid(row=1,column=0,sticky="W")
wa= tk.Entry(frW,border=5,font=("Courrier",20),justify="center")
wa.grid(row=1,column=1,columnspan=2,sticky="SE")
z="Player One"
wa.insert(0,z)
wa.update()
timw= tk.Label(frW,text=" Time:",font=("arial",25),fg="#A75907",bg="white")
timw.grid(row=2,column=0,sticky="W")
waT= tk.Entry(frW,border=5,font=("Courrier",20),justify="center")
waT.grid(row=2,column=1,columnspan=2,sticky="SE")
z="00:00"
waT.insert(0,z)
waT.update()
ranw= tk.Label(frW,text="RANK :",font=("arial",25),fg="#A75907",bg="white")
ranw.grid(row=3,column=0,sticky="W")
war= tk.Entry(frW,border=5,font=("Courrier",20),justify="center")
war.grid(row=3,column=1,columnspan=2,sticky="SE")
z="1200"
war.insert(0,z)
war.update()
butw=tk.Button(frW,image=b,width=200,height=100,bg="white")
butw.place(x=20,y=250)
butw2=tk.Button(frW,image=qw,width=200,height=100,bg="white")
butw2.place(x=250,y=250)


labb= tk.Label(frB,text="Black Setting:",font=("arial",25),fg="#A75907")
labb.grid(row=0,column=0,columnspan=5,sticky="N")
namb= tk.Label(frB,text="Name:",font=("arial",25),fg="white",bg="black")
namb.grid(row=1,column=0,sticky="W")
ba= tk.Entry(frB,border=5,font=("Courrier",20),justify="center")
ba.grid(row=1,column=1,columnspan=2,sticky="SE")
z="Player Two"
ba.insert(0,z)
ba.update()
timb= tk.Label(frB,text=" Time:",font=("arial",25),fg="white",bg="black")
timb.grid(row=2,column=0,sticky="W")
baT= tk.Entry(frB,border=5,font=("Courrier",20),justify="center")
baT.grid(row=2,column=1,columnspan=2,sticky="SE")
z="00:00"
baT.insert(0,z)
baT.update()
ranb= tk.Label(frB,text="RANK :",font=("arial",25),fg="white",bg="black")
ranb.grid(row=3,column=0,sticky="W")
bar= tk.Entry(frB,border=5,font=("Courrier",20),justify="center")
bar.grid(row=3,column=1,columnspan=2,sticky="SE")
z="1200"
bar.insert(0,z)
bar.update()
butb=tk.Button(frB,image=w,width=200,height=100,bg="black")
butb.place(x=20,y=250)
butb2=tk.Button(frB,image=q,width=200,height=100,bg="black")
butb2.place(x=250,y=250)

s=tk.Button(chess,bg="#A75907",text="Start Playing",command=startup,fg="white")
s.place(x=500,y=500,width=200,height=70)

chess.mainloop()