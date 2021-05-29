def grayCode(n):
        ret = [0]
        for k in range(0, n):
                for i in range(len(ret)-1, -1, -1):
                        ret.append(ret[i]+(2**k))
                        # print("k = ",k,"i = ",i,"ret[i] = ", ret[i], "k = ",k,"ret = ",ret,ret[i]+(2**k))
                print(ret)
        return ret

print(grayCode(4))