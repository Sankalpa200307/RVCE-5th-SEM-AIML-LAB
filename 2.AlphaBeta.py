MAX,MIN=1000,-1000

def minimax(depth,maxi,nodeidx,values,alpha,beta):
    if depth==3:
        return values[nodeidx]
    
    if maxi:
        best=MIN
        for i in range(0,2):
            val=minimax(depth+1,False,nodeidx*2+i,values,alpha,beta)
            best=max(best,val)
            alpha=max(alpha,best)
            if alpha>=beta:
                break
        return best
    else:
        best=MAX
        for i in range(0,2):
            val=minimax(depth+1,True,nodeidx*2+i,values,alpha,beta)
            best=min(best,val)
            beta=min(beta,best)
            if alpha>=beta:
                break
        return best
    
if __name__=='__main__':
    values=[3,5,6,9,2,0,-1]
    print("The optimal value is ",minimax(0,True,0,values,MIN,MAX))
    
                    
