import unittest

#aes sbox

sbox = [
        0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
        0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
        0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
        0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
        0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
        0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
        0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
        0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
        0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
        0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
        0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
        0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
        0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
        0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
        ]

#constant initial matrix

initialMatrix=[[1, 4, 7, 1], [1, 1, 4, 7], [7, 1, 1, 4], [4, 7, 1, 1]]

#addition in GF(256)

def add(x, y):
    return x^y

#multipilcation in GF(256) mod x^8+x^4+x^3+x+1

def mpy(x, y):
    p = 0b100011011
    m = 0
    for i in range(8):
        m = m << 1
        if m & 0b100000000:
            m = m ^ p
        if y & 0b010000000:
            m = m ^ x
        y = y << 1
    return m

#addition of matrices in GF(256)

def matrixAdd(a,b):
    if len(a)!=len(b) or len(a[0])!=len(b[0]):
        print( "those matrices dont have same size")
        return ""
    sumAandB=[]

    for i in range (0,len(a)):
        temp = []

        for j in range (0,len(a[i])):
            temp.append(add(a[i][j],b[i][j]))
        sumAandB.append(temp)

    return sumAandB

#multiplication of matrices in GF(256)

def matrixMultiplication(a,b):
    multAandB=[]
    if len(a[0])==len(b):
        for i in range(len(a)):
            tab=[]
            for j in range(len(b[0])):
                sum=0
                for k in range(len(b)):
                    sum =add(sum, mpy(a[i][k], b[k][j]))
                tab.append(sum)
            multAandB.append(tab)
        return multAandB
    else:
        print("cannot multiply")

#transforms hex String (which length is multiple of 8) to an array of integers

def hexToDec(input):
    dividedVector=[]
    temp=[]
    for i in range (0,len(input),2):
        tempstr=str(input[i])+str(input[i+1])
        temp.append(tempstr)
        if i % 8==6:
            dividedVector.append(temp)
            temp=[]

    for i in range (0, len(dividedVector)):
        for j in range (0,len(dividedVector[0])):
            dividedVector[i][j]=int(dividedVector[i][j],base=16)

    return dividedVector



#returns transposed matrix

def transposeMatrix(m):
    m2=[]

    for i in range (0,len(m[0])):
        tab=[]
        for j in range (0,len(m)):
            tab.append(m[j][i])
        m2.append(tab)

    return m2

#operation which is part of supermix

def sumsAtTheDiagonal(u):
    matr=[]
    for i in range(0,len(u)):
        matr.append([0]*len(u))
    for i in range (0,len(u)):
        sum=0
        for j in range (0,len(u[0])):
            if i!=j:
                sum=add(sum,u[i][j])
        matr[i][i]=sum

    return matr

#moves ith row of a matrix i times to the left i e <0,3>

def rol(m):
    for i in range (0,len(m)):
        m[i]=rotate(m[i],i)

    return m

#rotates row l n times to the left

def rotate(l, n):
    return l[n:] + l[:n]



def superMix(u):
    return rol(matrixAdd(matrixMultiplication(initialMatrix, u), matrixMultiplication(sumsAtTheDiagonal(u), transposeMatrix(initialMatrix))))


'''
implementation for 224 and 256 bits
'''



#generates initial state

def initialState(iv):
    m=[]
    for i in range (0,30):
        m.append([0]*4)

    deciv=hexToDec(iv)
    for i in range (0,len(deciv)):
        m[len(m)-1-i]=deciv[len(deciv)-1-i]


    return transposeMatrix(m)


def tix(initialState,word):
    for i in range(0,4):
        initialState[i][10]=add(initialState[i][10],initialState[i][0])
        initialState[i][0]=word[i]
        initialState[i][8]=add(initialState[i][8],initialState[i][0])
        initialState[i][1]=add(initialState[i][1],initialState[i][24])

    return initialState



def ror3(initialState):

    for i in range (0,len(initialState)):
        initialState[i]=rotate(initialState[i],27)


    return initialState

def cmix(initialState):

    for i in range(0,4):
        initialState[i][0]=add(initialState[i][0],initialState[i][4])
        initialState[i][1] = add(initialState[i][1], initialState[i][5])
        initialState[i][2] = add(initialState[i][2] , initialState[i][6])
        initialState[i][15] = add(initialState[i][15], initialState[i][4])
        initialState[i][16] = add(initialState[i][16], initialState[i][5])
        initialState[i][17] = add(initialState[i][17], initialState[i][6])



    return initialState


def smix(initialState):
    wAfterSbox=[]
    for i in range(0,4):
        temp=[]
        for j in range(0,4):
            temp.append(sbox[initialState[i][j]])
        wAfterSbox.append(temp)
    w=superMix(wAfterSbox)

    for i in range (0,4):
        for j in range (0,4):
            initialState[i][j]=w[i][j]

    return initialState

def subround(initialState):
    return smix(cmix(ror3(initialState)))

def round(initialState,word):
    return subround(subround(tix(initialState,word)))



def R(initialState,message):
    dividesMes=hexToDec(message)

    for i in range (0,len(dividesMes)):
        initialState=round(initialState,dividesMes[i])


    return initialState

def finalRoundG(initialState):
    for i in range (0,10):
        initialState=subround(initialState)
    for j in range (0,13):
        for i in range (0,4):
            initialState[i][4]=add(initialState[i][4],initialState[i][0])
            initialState[i][15]=add(initialState[i][15],initialState[i][0])
            initialState[i] = rotate(initialState[i], 15)


        initialState=smix(initialState)

        for i in range (0,4):
            initialState[i][4]=add(initialState[i][4],initialState[i][0])
            initialState[i][16]=add(initialState[i][16],initialState[i][0])
            initialState[i] = rotate(initialState[i], 16)


        initialState=smix(initialState)

    for i in range(0, 4):
        initialState[i][4] = add(initialState[i][4],  initialState[i][0])
        initialState[i][15] = add(initialState[i][15], initialState[i][0])

    return initialState

'''
implementation for 384 and 512 bits
'''

def ror3384and512(initialState):

    for i in range (0,len(initialState)):
        initialState[i]=rotate(initialState[i],33)


    return initialState

def initialState384and512(iv):
    m=[]
    for i in range (0,36):
        m.append([0]*4)

    deciv=hexToDec(iv)
    for i in range (0,len(deciv)):
        m[len(m)-1-i]=deciv[len(deciv)-1-i]

    return transposeMatrix(m)

def tix384(initialState,word):
    for i in range(0,4):
        initialState[i][16]=add(initialState[i][16],initialState[i][0])
        initialState[i][0]=word[i]
        initialState[i][8]=add(initialState[i][8],initialState[i][0])
        initialState[i][1]=add(initialState[i][1],initialState[i][27])
        initialState[i][4]=add(initialState[i][4],initialState[i][30])

    return initialState


def cmix384and512(initialState):

    for i in range(0,4):
        initialState[i][0]=add(initialState[i][0],initialState[i][4])
        initialState[i][1] = add(initialState[i][1], initialState[i][5])
        initialState[i][2] = add(initialState[i][2] , initialState[i][6])
        initialState[i][18] = add(initialState[i][18], initialState[i][4])
        initialState[i][19] = add(initialState[i][19], initialState[i][5])
        initialState[i][20] = add(initialState[i][20], initialState[i][6])

    return initialState


def finalRoundG384(initialState,message):
    words = hexToDec(message)

    for word in words:
        initialState=tix384(initialState,word)
        for i in range (0,3):
            initialState=ror3384and512(initialState)
            initialState=cmix384and512(initialState)
            initialState=smix(initialState)

    for j in range (0,18):
        initialState = ror3384and512(initialState)
        initialState = cmix384and512(initialState)
        initialState = smix(initialState)

    for i in range (0,13):
        for i in range (0,4):
            initialState[i][4]=add(initialState[i][4],initialState[i][0])
            initialState[i][12]=add(initialState[i][12],initialState[i][0])
            initialState[i][24]=add(initialState[i][24],initialState[i][0])
            initialState[i] = rotate(initialState[i], 24)

        initialState=smix(initialState)

        for i in range(0, 4):
            initialState[i][4] = add(initialState[i][4], initialState[i][0])
            initialState[i][13] = add(initialState[i][13], initialState[i][0])
            initialState[i][24] = add(initialState[i][24], initialState[i][0])
            initialState[i] = rotate(initialState[i], 24)

        initialState=smix(initialState)

        for i in range(0, 4):
            initialState[i][4] = add(initialState[i][4], initialState[i][0])
            initialState[i][13] = add(initialState[i][13], initialState[i][0])
            initialState[i][25] = add(initialState[i][25], initialState[i][0])
            initialState[i] = rotate(initialState[i], 25)

        initialState=smix(initialState)
    for i in range(0, 4):
        initialState[i][4] = add(initialState[i][4], initialState[i][0])
        initialState[i][12] = add(initialState[i][12], initialState[i][0])
        initialState[i][24] = add(initialState[i][24], initialState[i][0])
    return initialState




def tix512(initialState,word):
    for i in range(0,4):
        initialState[i][22]=add(initialState[i][22],initialState[i][0])
        initialState[i][0]=word[i]
        initialState[i][8]=add(initialState[i][8],initialState[i][0])
        initialState[i][1]=add(initialState[i][1],initialState[i][24])
        initialState[i][4]=add(initialState[i][4],initialState[i][27])
        initialState[i][7]=add(initialState[i][7],initialState[i][30])

    return initialState





def finalRoundG512(initialState,message):
    words = hexToDec(message)

    for word in words:
        initialState=tix512(initialState,word)
        for i in range (0,4):
            initialState=ror3384and512(initialState)
            initialState=cmix384and512(initialState)
            initialState=smix(initialState)

    for j in range (0,32):
        initialState = ror3384and512(initialState)
        initialState = cmix384and512(initialState)
        initialState = smix(initialState)

    for i in range (0,13):
        for i in range (0,4):
            initialState[i][4]=add(initialState[i][4],initialState[i][0])
            initialState[i][9]=add(initialState[i][9],initialState[i][0])
            initialState[i][18]=add(initialState[i][18],initialState[i][0])
            initialState[i][27]=add(initialState[i][27],initialState[i][0])
            initialState[i] = rotate(initialState[i], 27)

        initialState=smix(initialState)

        for i in range(0, 4):
            initialState[i][4] = add(initialState[i][4], initialState[i][0])
            initialState[i][10] = add(initialState[i][10], initialState[i][0])
            initialState[i][18] = add(initialState[i][18], initialState[i][0])
            initialState[i][27] = add(initialState[i][27], initialState[i][0])
            initialState[i] = rotate(initialState[i], 27)

        initialState=smix(initialState)

        for i in range(0, 4):
            initialState[i][4] = add(initialState[i][4], initialState[i][0])
            initialState[i][10] = add(initialState[i][10], initialState[i][0])
            initialState[i][19] = add(initialState[i][19], initialState[i][0])
            initialState[i][27] = add(initialState[i][27], initialState[i][0])
            initialState[i] = rotate(initialState[i], 27)

        initialState=smix(initialState)


        for i in range(0, 4):
            initialState[i][4] = add(initialState[i][4], initialState[i][0])
            initialState[i][10] = add(initialState[i][10], initialState[i][0])
            initialState[i][19] = add(initialState[i][19], initialState[i][0])
            initialState[i][28] = add(initialState[i][28], initialState[i][0])
            initialState[i] = rotate(initialState[i], 28)

        initialState=smix(initialState)
    for i in range(0, 4):
        initialState[i][4] = add(initialState[i][4], initialState[i][0])
        initialState[i][9] = add(initialState[i][9], initialState[i][0])
        initialState[i][18] = add(initialState[i][18], initialState[i][0])
        initialState[i][27] = add(initialState[i][27], initialState[i][0])
    return initialState




def fugue(initialVector,message):
    config=(len(initialVector)-64)/8
    tab = []
    if config <=0:
        istate=initialState(initialVector)
        istate=finalRoundG(R(istate,message))


        for i in range (1,5):
            for j in range (0,4):
                tab.append(istate[j][i])

        for i in range (15,19+int(config)):
            for j in range (0,4):
                tab.append(istate[j][i])

    elif config==4:
        istate = initialState384and512(initialVector)
        istate = finalRoundG384(istate,message)

        for i in range(1, 5):
            for j in range(0, 4):
                tab.append(istate[j][i])

        for i in range(12, 16):
            for j in range(0, 4):
                tab.append(istate[j][i])

        for i in range(24, 28):
            for j in range(0, 4):
                tab.append(istate[j][i])

    else:
        istate = initialState384and512(initialVector)
        istate = finalRoundG512(istate,message)

        for i in range(1, 5):
            for j in range(0, 4):
                tab.append(istate[j][i])
        for i in range(9, 13):
            for j in range(0, 4):
                tab.append(istate[j][i])
        for i in range(18, 22):
            for j in range(0, 4):
                tab.append(istate[j][i])

        for i in range(27, 31):
            for j in range(0, 4):
                tab.append(istate[j][i])
    output = ""
    for x in tab:
        if len(str(hex(x))[2:]) == 1:
            output = output + str(0) + str(hex(x))[2:].upper()
        else:
            output = output + str(hex(x))[2:].upper()
    return output


class FugueTest(unittest.TestCase):
    def test_area(self):
        hashSizes = [224, 256, 384, 512]
        for i in range(0, 5):
            for j in range(0, 4):
                file = open('TestVectors/Test_' + str(2 ** i) + 'TableKAT_' + str(hashSizes[j]) + '.txt', 'r')
                lines = file.readlines()
                for x in range(0, len(lines)):
                    if lines[x].startswith("IV"):
                        iv = lines[x].split()[2]
                        mess = lines[x + 1].split()[2]
                        expval = lines[x + 2].split()[2]
                        self.assertEqual(fugue(iv, mess), expval)
                file.close()
