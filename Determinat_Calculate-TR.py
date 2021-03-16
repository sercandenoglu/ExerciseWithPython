import copy#deepcopy fonksiyonunu kullanabilmek için import ettim

def GetMatrix():
    # Kullanıcıdan matrixi alma işlemleri
    # Kullanım hakkında bilgilendirme
    print("If you want to exit, please write \"exit\"")
    print("You can split with ',' each value")
    print("Please enter each row")
    matrix = []#Matrixi tutacağımız listemiz
    counter = 1#Kullanıcıya kaçıncı satırda olduğunu belirtmek için sayaç
    while True:#Kullanıcı exit yazmadığı sürece döngüye kullanıcıdan matrixin her bir satırını almaya devam edecek olan döngü
        row = input(f"Enter {counter}. row: ")

        if row == "exit":
            break
        else:
            matrix.append(row.split(","))#Matrixe kullanıcının girdiği satırı ekleme işlemi
        counter += 1
    return matrix

def SquareMatrixCheck(matrix):
    # Kare matrix mi diye kontrol etme işlemi
    # Matrix'in toplam eleman sayısı bize sütun sayısını veriyor
    # Eğer matrix'in herhangi bir satırının uzunluğu sütunlarının uzunluğundan farklı ise
    # False değerini döndürüp matrix'in kare olmadığını belirtiyoruz
    for i in matrix:
        if len(i) != len(matrix):
            return False
    else:
        return True

def TwotoTwo(matrix):
    # Kare matrixlerde determinat hesaplaması
    # Örneğin [2 3
    #          4 5] matriximiz olsun
    # 2 ile 5'i çarpıp(10), 3 ile 4'u çarpıp çıkan bulduğumuz değeri 10'dan çıkartıyoruz
    # 10-12=-2 şeklinde
    x1 = int(matrix[0][0]) * int(matrix[1][1])
    x2 = int(matrix[0][1]) * int(matrix[1][0])
    return x1 - x2

def Sarrus(matrix):
    # Matrix'imiz 3 e 3 ise sarrus yöntemi ile çözüyoruz
    temporaryMatrix = matrix.copy()#Matriximizin yedeğini alıyoruz
    # Aldığımız yedekteki matrixe, matriximizin 1. ve 2. satırlarını sonuna ekliyoruz
    # Örneğin matriximizin yeni satırları şu şekilde olacak
    # [2 3 4
    #  3 4 5
    #  5 6 7
    #  2 3 4
    #  3 4 5]
    temporaryMatrix.append(matrix[0])
    temporaryMatrix.append(matrix[1])
    # Sağdan ve soldan yapacağımız çarpma işlemlerini tutacağımız listelerimiz
    temporarySumForPositive = []
    temproraySumForNegative = []

    # Soldan sağa yapacağımız çarpma işlemleri
    for n in range(3):
        counter = 0#çaprazındaki değerleri tutmak için sayaç
        product = 1#her bir çaprazlama değerinde çarpımları tutacağımız değişken
        x = []#Herbir çarpma işlemi için tutacağımız değerler
        for j in range(n, n + 3, 1):#n. satırdan başlayıp, 3 satır geziyor
            x.append(temporaryMatrix[j][counter])#Örneğin yukarıdaki satırdaki 2, 4, 7 değerlerini alıyoruz
            counter += 1
        for i in x:
            product *= int(i)#Aldığımız 2,4,7 değerlerini burada çarpıyoruz
        temporarySumForPositive.append(product)#Bulduğumuz çarpım sonucunu listemize ekliyoruz ve döngüye devam ediyoruz(toplamda bu adımlar 3 kere uygulanıyor)

    # Yukarıdaki işlmelerin sağdan sola versiyonu
    for n in range(3):
        counter = 2#counter'ın 2den başlaması işlemi sağdan sola doğru yapabilmek için
        product = 1
        x = []
        for j in range(n, n + 3, 1):
            x.append(temporaryMatrix[j][counter])
            counter -= 1
        for i in x:
            product *= int(i)
        temproraySumForNegative.append(product)

    return sum(temporarySumForPositive) - sum(temproraySumForNegative)#bulduğumuz değerlerin toplamlarını çıkartıp determinatı return ediyoruz

def MultilineMatrix(matrix):
    determinant = 0
    for i in range(len(matrix)):
        if matrix[i][0] != 0:#her zaman 1. sütun 1. satıra göre bu işlemi yapıyoruz, en fazla sıfırın olduğu sütunu veya satırı bulup hızlandırmak için optimize edilebilir buna dönüştürmek için esneklik bıraktım
            temporaryMatrix = copy.deepcopy(matrix)#burada deepcopy fonksiyonunu kullanmamın çok ilginç bir nedeni var
            # Normal koşullarda copy methodu ile listelerimizi kopyaladığımızda herhangi bir sıkıntı olmuyor ancak
            # listenin geçerlilik alanı değişince(burada ilgili satır aşağıdaki for j in range(len(temporaryMatrix)):) copy methodu kopyalamak yerine
            # Referans alma işlemi yapıyor bunu alınan yedeği tekrar yedeklesek dahi çözülmüyor
            # Bende deepcopy fonksiyonu ile bu sorunu çözdüm. Muhtemelen önceki listedeki her bir elemanı tek tek yeni listemize ekleseydikde sorun çözülebilirdi
            # Ama o yöntemi denemekle uğraşmadım
            temporaryDeterminant = temporaryMatrix[i][0] * ((-1) ** ((i+1) + 1))#Geçici matrixteki i. satırın ilk değerini formülümüz gereği işleme tabi tutuyoruz
            # Geçici olarak silinmesi gereken satır ve sütunları silme işlemimizi burada yapıyoruz
            del temporaryMatrix[i]
            for j in range(len(temporaryMatrix)):
                del temporaryMatrix[j][0]
            # Silindikten sonra determinatımız hala 3 e 3'ten büyük ise matrixin son hali ile özyenileme yapıyoruz
            if len(temporaryMatrix) == 3:
                temporaryDeterminant *= Sarrus(temporaryMatrix)
            else:#3 e 3 ise arkadaşı ilgili fonksiyona yönlendiriyoruz
                temporaryDeterminant *= MultilineMatrix(temporaryMatrix)
            determinant += temporaryDeterminant#bulduğumuz determinantı daha önce bulduklarımız ile topluyoruz
    return determinant


matrix = GetMatrix()#Matrixi kullanıcdan alma işlemleri
if SquareMatrixCheck(matrix) is True and len(matrix) > 0:#Matrixin büyüklüğüne göre hesaplama işlemleri
    if len(matrix) == 1:
        print(f"Determinant is {matrix[0][0]}")
    elif len(matrix) == 2:
        print(f"Determinant is {TwotoTwo(matrix)}")
    elif len(matrix) == 3:
        print(f"Determinant is {Sarrus(matrix)}")
    else:
        print(f"Determinant is {MultilineMatrix(matrix)}")
else:
    print("Matrix is not square")

