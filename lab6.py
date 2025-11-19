import numpy as np
def arrays ():
    array1= np.array([-2.33 ,100, 20, 33.2])
    array2= np.array([[30, 12, 2, 70.2], [98.01, 4, 0, 7]])
    array3= np.arange(2,12,2)
    array4= np.arange(20, -21, -10)
    array5= np.linspace(0,1,4)
    array6= np.ones((3,4))
    array7= np.zeros((2,3))
    array8= np.eye(3,3)
    array9= np.diag(np.ones(2,), -1)
    array10= np.array([np.zeros((4,)),np.ones((4,)), 2*np.ones((4,))])
    
    return  array1, array2, array3, array4, array5, array6, array7, array8, array9, array10
    
    
    # out 4 1D array vektör matrix, out 6 bunu gösterdi, out 7 başka boyut olmadığı için sadece 3 gösterdi
    # iki tane braket koyarak row sayısını arttırdık
    # pattern varsa np.arange kullanılıyor, ilk olarak konsolda dene
    # hem pattern var hem de yoksa np.linspace kullanılıyor, bir sayıdan bir sayıya kadar eşit bölen bir fonksiyon
    # 11111 li olan matrix 2D olarak kabul edildi, np.ones
    #00000 matrix, np.zeros
    # I = AI ---> A,I np.eye veya np.diag(np.ones((3,))) 2D, np.eye(3,3)
    # array9 da pattern var, np.diag(array, k: diagonal index) matrix ortası 0, üstü 1 , altı -1 olarak saylıyor
    # -1. satırda 2 tane 1 olduğundan bu şekilde yazdık
    
def total_displacement(v1x, v1y, v2x, v2y, v3x, v3y):
    v1= np.array([v1x, v1y]) #in km
    v2= np.array([v2x, v2y]) #in km
    v3= np.array([v3x, v3y]) #in km
    vR= v1+ v2+ v3
    u= np.array([1/np.sqrt(2), -1/ np.sqrt(2)])
    vRu= np.dot(vR,u)* u
    len_vRu= np.sqrt ((vRu[0]**2) +(vRu[1]**2))
    
    return vR, len_vRu
    #dot product np.dot
    # lenght vRu iki bileşeni vRux vRuy için tuple kullandık
total_displacement(1,2,3,4,5,6)