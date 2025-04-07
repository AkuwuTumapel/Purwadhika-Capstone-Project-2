from datetime import datetime

# car id - string
# model - string
# brand - string
# year - number/int
# rental price - number/float
# status - 1 (ready) / 0 (in rent) / 2 (in maintenance)
data = [
    ["CR001", "B1234SAT", "Avanza", "Toyota", 2005, 1000000, 1],
    ["CR002", "DA345BX", "Innova", "Toyota", 2015, 1500000, 2],
    ["CR003", "B9834BCN", "Terios", "Daihatsu", 2010, 2000000, 1],
    ["CR004", "R374JKN", "Sigra", "Daihatsu", 2013, 1200000, 3],
    ["CR005", "B34DK", "Xpander", "Mitsubishi", 2018, 3000000, 1]
]

cars = []
carTemplate = {
    "id": "",
    "plateNum": "",
    "model": "",
    "brand": "",
    "year": 0,
    "rentPrice": 0,
    "status": 0 
}

def importData():
    for i in range(5):
        car = carTemplate.copy()
        car["id"] = data[i][0]
        car["plateNum"] = data[i][1]
        car["model"] = data[i][2]
        car["brand"] = data[i][3]
        car["year"] = data[i][4]
        car["rentPrice"] = data[i][5]
        car["status"] = data[i][6]
        cars.append(car)

def printData(list):
    headers = ['No', 'ID', 'Plate Number', 'Model', 'Brand', 'Year', 'Rental Price', 'Status']
    width = 15

    for header in headers:
        print(f"{header:<{width}}", end="| ")
    print("\n" + "-" * (width * len(headers) + 2 * len(headers) - 1))

    i = 1
    for obj in list:
        stat = "Available" if obj['status'] == 1 else "Rented" if obj['status'] == 2 else "In Maintenance" if obj['status'] == 3 else "Unknown"
        print(
            f"{i:<{width}}| "
            f"{obj['id'][:width]:<{width}}| "
            f"{obj['plateNum'][:width]:<{width}}| "
            f"{obj['model'][:width]:<{width}}| "
            f"{obj['brand'][:width]:<{width}}| "
            f"{str(obj['year'])[:width]:<{width}}| "
            f"{str(obj['rentPrice'])[:width]:<{width}}| "
            f"{stat[:width]:<{width}}| "
        )
        i += 1

def insertYear():
    curr_y = datetime.now().year
    while True:
        userInput = input("Masukkan tahun pembuatan:").strip()
        try:
            y = int(userInput)
            if y < 1990 or y > curr_y:
                print("Masukkan tahun antara 1990 dan sekarang.")
            else:
                return y
        except:
            print("Mohon masukkan tahun yang valid.")

def insertPrice():
    while True:
        userInput = input("Masukkan harga:").strip()
        try:
            p = int(userInput)
            if p < 0:
                print("Harga tidak boleh kurang dari 0.")
            else:
                return p
        except:
            print("Mohon masukkan angka harga yang valid.")

def insertStatus():
    while True:
        print("Masukkan status: \n1. Available \n2. Rented\n3. In Maintenance")
        try:
            s = int(input("Status:"))
            if s != 1 and s != 2 and s != 3:
                print("Mohon masukkan pilihan yang valid.")
            else:
                return s
        except:
            print("Mohon masukkan angka status.")

def findRegNumber(plateNum, numIdx):
    regNum = ''
    while numIdx < len(plateNum):
        if plateNum[numIdx].isalpha() == False:
            regNum += plateNum[numIdx]
        else:
            break
        numIdx += 1 
    return regNum, numIdx

def insertPlateNumber():
    while True:
        region = ''
        regNum = ''
        comb = ''
        combStart = -1

        userInput = input("Masukkan pelat nomor:").strip()
        if len(userInput) > 9:
            print("Nomor pelat maksimal 9 digit.")
        else:
            if " " in userInput:
                print("Tidak boleh menggunakan spasi.")
                continue

            if userInput[0].isalpha() and userInput[1].isalpha():
                region = userInput[0] + userInput[1]
                regNum, combStart = findRegNumber(userInput, 2)
            elif userInput[0].isalpha() and userInput[1].isalpha() == False:
                region = userInput[0]
                regNum, combStart = findRegNumber(userInput, 1)
            else:
                print("Kode daerah tidak boleh berisi angka.")
                continue

            # print(f'regnum: {regNum}')
            if regNum == '' or len(regNum) > 4:
                print("Nomor pelat harus memiliki kombinasi angka dari nol sampai empat digit.")
                continue

            idx = combStart
            chCount = 0
            ch = ''
            while idx <= len(userInput) - 1:
                if userInput[idx].isalpha():
                    chCount += 1
                    ch += userInput[idx]
                idx += 1
            if chCount > 3:
                print("Kombinasi akhir pelat melebihi batasan 3 huruf.")
                continue
            elif chCount < 1:
                print("Pelat nomor harus memiliki huruf kombinasi di akhir.")
                continue
            else:
                comb = ch
            # print(f'comb = {comb}')

            return(region + regNum + comb)

def create():
    createLoop = True
    while createLoop:
        try:
            amount = int(input("Masukkan jumlah data yang ingin dimasukkan. Tekan 0 untuk kembali:"))
            if amount < 0:
                print("Input harus bilangan positif.")
            elif amount == 0:
                break
            else:
                newData = []
                for i in range(amount):
                    data = carTemplate.copy()
                    data['model'] = input("Masukkan model:").strip()
                    data['brand'] = input("Masukkan brand:").strip()
                    y = insertYear()
                    p = insertPrice()
                    s = insertStatus()
                    
                    while True:
                        pnValid = True
                        pn = insertPlateNumber()
                        for obj in cars:
                            if obj["plateNum"] == pn:
                                print("Pelat nomor baru sudah terdaftar. Mohon masukkan pelat nomor lain.")
                                pnValid = False
                        if pnValid == True:
                            break


                    data['year'] = y
                    data['rentPrice'] = p
                    data['status'] = s
                    data['plateNum'] = pn
                    
                    newData.append(data)
                
                printData(newData)
                while True:
                    userConf = input("Apakah data baru ini sudah benar? (Y/N):")
                    if userConf.upper() == 'Y':
                        if cars:
                            latest_id = max(int(car['id'][2:]) for car in cars)
                        else:
                            latest_id = 0
                        for obj in newData:
                            new_id = f"CR{latest_id + 1:03}"
                            latest_id += 1
                            obj['id'] = new_id    
                            cars.append(obj)
                        createLoop = False
                        print("Data kendaraan baru berhasil dimasukkan.")
                        break
                    elif userConf.upper() == 'N':
                        break
                    else:
                        print("Masukkan konfirmasi yang valid.")
        except:
            print("Hanya boleh masukkan angka.")
    
def read():
    readText = """
==================
1. Baca semua data
2. Filter data
3. Kembali ke menu
==================
"""

    optText = """
=============================
0. Kembali ke menu sebelumnya
1. Cari berdasarkan harga
2. Cari berdasarkan status
3. Cari berdasarkan nomor pelat
=============================
"""
    while True:
        print(readText)
        readOption = input("Pilih opsi baca:")
        if readOption == '1':
            printData(cars)
        elif readOption == '2':
            while True:
                print(optText)
                userOpt = input("Pilih metode pencarian:")
                if userOpt == '1':
                    while True:
                        try:
                            lower = int(input("Masukkan batas terendah harga:"))
                            higher = int(input("Masukkan batas tertinggi harga:"))

                            if lower <= higher and lower > 0 and higher > 0: 
                                break
                            else:
                                print("Batas rendah harus kurang dari atau sama dengan batas tertinggi dan harga tidak boleh kurang dari 0.")
                        except:
                            print("Mohon masukkan angka harga yang valid.")        
                    filteredData = []
                    for obj in cars:
                        if obj['rentPrice'] >= lower and obj['rentPrice'] <= higher:
                            filteredData.append(obj)
                    printData(filteredData)
                elif userOpt == '2':
                    status = insertStatus()
                    filteredData = []
                    for obj in cars:
                        if obj['status'] == status:
                            filteredData.append(obj)
                    printData(filteredData)
                elif userOpt == '3':
                    plateNum = insertPlateNumber()
                    filteredData = []
                    for obj in cars:
                        if obj['plateNum'] == plateNum:
                            filteredData.append(obj)
                    printData(filteredData)
                elif userOpt == '0':
                    break
                else:
                    print("Mohon masukkan pilihan yang valid.")
        elif readOption == '3':
            break
        else:
            print("Mohon masukkan pilihan yang valid.")

def update():
    updateText = """
======================
1. Ubah status
2. Ubah data kendaraan
3. Kembali ke menu
======================
"""
    optText = """
===================================
Angka: Nomor data yang ingin diubah
0. Kembali ke menu sebelumnya
===================================
"""

    while True:
        print(updateText)
        upOption = input("Pilih opsi perubahan data:")
        if upOption == '1':
            upLoop = True
            while upLoop:
                printData(cars)
                lastIndex = len(cars)
                print(optText)
                try:
                    idx = int(input("Masukkan nomor data yang ingin diubah:"))
                    if idx > 0 and idx <= lastIndex:
                        obj = cars[idx-1]
                        printData([obj])
                        newStatus = insertStatus()
                        while True:
                            userConf = input("Apakah data baru ini sudah benar? (Y/N):")
                            if userConf.upper() == 'Y':
                                obj['status'] = newStatus
                                print("Data berhasil diubah")
                                upLoop = False
                                break
                            elif userConf.upper() == 'N':
                                print("Perubahan data tidak tersimpan.\n")
                                break
                            else:
                                print("Masukkan konfirmasi yang valid.\n")
                    elif idx == 0:
                        upLoop = False
                    else:
                        print(f"Masukkan angka yang valid (0 atau 1 -  {lastIndex})")
                except:
                    print("Mohon masukkan nomor data yang valid.")
        elif upOption == '2':
            upLoop2 = True
            while upLoop2:
                printData(cars)
                lastIndex = len(cars)
                print(optText)
                try:
                    idx = int(input("Masukkan nomor data yang ingin diubah:"))
                    if idx > 0 and idx <= lastIndex:
                        newObj = cars[idx-1].copy()
                        printData([newObj])

                        while True:
                            m = input("Apakah ingin mengubah model? (Y/N)")
                            if m.upper() == 'Y':
                                newObj['model'] = input("Masukkan model:").strip()
                                break
                            elif m.upper() == 'N':
                                 break
                            else:
                                print("Mohon masukkan pilihan yang valid.")
                        
                        while True:
                            b = input("Apakah ingin mengubah brand? (Y/N)")
                            if b.upper() == 'Y':
                                newObj['brand'] = input("Masukkan brand:").strip()
                                break
                            elif b.upper() == 'N':
                                break
                            else:
                                print("Mohon masukkan pilihan yang valid.")

                        while True:
                            y = input("Apakah ingin mengubah tahun? (Y/N):")
                            if y.upper() == 'Y':
                                newObj['year'] = insertYear()
                                break
                            elif y.upper() == 'N':
                                break
                            else:
                                print("Mohon masukkan pilihan yang valid.")
                        
                        while True:
                            p = input("Apakah ingin mengubah harga rental? (Y/N):")
                            if p.upper() == 'Y':
                                newObj['rentPrice'] = insertPrice()
                                break
                            elif p.upper() == 'N':
                                break
                            else:
                                print("Mohon masukkan pilihan yang valid.")
                        
                        while True:
                            s = input("Apakah ingin mengubah status? (Y/N):")
                            if s.upper() == 'Y':
                                newObj['status'] = insertStatus()
                                break
                            elif s.upper() == 'N':
                                break
                            else:
                                print("Mohon masukkan pilihan yang valid.")

                        while True:
                            s = input("Apakah ingin mengubah pelat nomor? (Y/N):")
                            if s.upper() == 'Y':
                                pn = newObj['plateNum']
                                while True:
                                    pnValid = True
                                    newPn = insertPlateNumber()
                                    for obj in cars:
                                        if obj["plateNum"] == newPn and obj["plateNum"] != pn:
                                            print("Pelat nomor baru sudah terdaftar. Mohon masukkan pelat nomor lain.")
                                            pnValid = False
                                    if pnValid == True:
                                        break
                                newObj['plateNum'] = newPn
                                break
                            elif s.upper() == 'N':
                                break
                            else:
                                print("Mohon masukkan pilihan yang valid.")

                        printData([newObj])

                        while True:
                            userConf = input("Apakah data baru ini sudah benar? (Y/N):")
                            if userConf.upper() == 'Y':
                                obj = cars[idx-1]
                                obj['model'] = newObj['model']
                                obj['brand'] = newObj['brand']
                                obj['year'] = newObj['year']
                                obj['rentPrice'] = newObj['rentPrice']
                                obj['status'] = newObj['status']
                                obj['plateNum'] = newObj['plateNum']
                                print("Data berhasil diubah")
                                upLoop2 = False
                                break
                            elif userConf.upper() == 'N':
                                print("Perubahan data tidak tersimpan.\n")
                                break
                            else:
                                print("Masukkan konfirmasi yang valid.\n")                        
                    elif idx == 0:
                        upLoop2 = False
                    else:
                        print(f"Masukkan angka yang valid (0 atau 1 -  {lastIndex})")
                except:
                    print("Mohon masukkan nomor data yang valid.")
        elif upOption == '3':
            break
        else:
            print("Mohon masukkan pilihan yang valid.")

def delete():
    delText = """
====================================
Angka: Nomor data yang ingin dihapus
0. Kembali ke menu
====================================
"""
    delLoop = True
    while delLoop:
        printData(cars)
        lastIndex = len(cars)
        print(delText)
        try:
            idx = int(input("Masukkan nomor data yang ingin dihapus:"))
            if idx > 0 and idx <= lastIndex:
                obj = cars[idx-1]
                printData([obj])
                while True:
                    userConf = input("Apakah data ini ingin dihapus? (Y/N):")
                    if userConf.upper() == 'Y':
                        cars.remove(obj)
                        delLoop = False
                        print("Data berhasil dihapus.")
                        break
                    elif userConf.upper() == 'N':
                        break
                    else:
                        print("Masukkan konfirmasi yang valid.")
            elif idx == 0:
                delLoop = False
            else:
                print(f"Masukkan angka yang valid (0 atau 1 -  {lastIndex})")
        except:
            print("Mohon masukkan nomor data yang valid.")

def endProgram():
    print("end program")

def menu():
    menuText = """
=====================
1. Create
2. Read
3. Update
4. Delete
5. Exit Program
=====================
    """
    importData()
    while True:
        print(menuText)
        
        menuOption = input("Pilih menu:")
        # if menuOption == '0':
        #     importData()
        if menuOption == '1':
            create()
        elif menuOption == '2':
            read()
        elif menuOption == '3':
            update()
        elif menuOption == '4':
            delete()
        elif menuOption == '5':
            endProgram()
            break
        else:
            print("Mohon masukkan pilihan yang valid.")
        

menu()
# insertPlateNumber()