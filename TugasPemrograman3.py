import hashlib
import math

login_user = []     # variabel penanda kalau ada user yang sudah login
hash_table = []     # array hash table
table_size = 11     # default size dari hash table
element = 0         # counter banyak username
load_factor = 0.7   # default load factor

# masukkan isi list jadi None
for i in range(table_size):
    hash_table.append([None, None])

# cek panjang hashtable
def len_hash(hash_table):
    if len(hash_table) == None:
        return 0
    else:
        return len(hash_table)

# encrypt value atau password 
def encrypt(password):
    result = hashlib.md5(password.encode())
    return result.hexdigest()

# function hash pertama untuk mendapatkan index (selama masih kosong)
def hash_one(hash_code, size_of_table):
    return hash_code % size_of_table

# function hash kedua untuk mendapatkan index 
def hash_two(hash_code):
    return 7 - (hash_code % 7)

# gabungan hash pertama dan kedua untuk mendapatkan index 
# saat index yang dituju pertama kali tidak kosong 
def doubleHashing(key, hashtable):
    var1 = hash_one(key, table_size)
    buffer = var1
    counter = 0
    while counter < table_size:
        current = hashtable[var1]
        if current != [None, None]:
            var1 = (buffer + (counter*hash_two(key))) % table_size
        else:
            return var1
            
        counter += 1

# cek username
def get_key(input):
    bool = True
    global current  # deklarasi posisi input key
    global index    # index dari hash table

    hash_code = convert_to_hashcode(input)    # ubah ke hashcode
    start = hash_one(hash_code, table_size)  # cek lokasi pertama yang lebih dekat
    for i in range(table_size):
        index = (start + i) % table_size
        current = hash_table[index]   # ambil index current dari lokasi pertama
        if current[0] == input: 
            return True
        else: bool = False
    return bool

# convert key ke hashcode
def convert_to_hashcode(key):
    code = 0
    for i in key:
        code += ord(i)
    return code

# untuk cek size dari hashtable
def check_table_size(table_size):
    return element/table_size >= load_factor

# cek prima atau tidak
# use refereces from geeksforgeeks
def checkPrima(size):
    if(size <= 1):
        return False
    if(size <= 3):
        return True
     
    if(size % 2 == 0 or size % 3 == 0):
        return False
     
    for i in range(5,int(math.sqrt(size) + 1), 6):
        if(size % i == 0 or size % (i + 2) == 0):
            return False
     
    return True

# mencari bilangan prima selanjutnya
def nextPrima(size):
    if (size <= 1):
        return 2
 
    prime = size
    found = False
 
    while(not found):
        prime = prime + 1
 
        if(checkPrima(prime) == True):
            found = True
 
    return prime

# extend hashtable
def extend_table():
    global hash_table
    global table_size
    temp = table_size   # nampung table size sebelumnya
    table_size *= 2 
    new_table = []
    # cek sizenya apakah bilangan prima atau bukan
    if (checkPrima(table_size) == False):
        table_size = nextPrima(table_size)
    
    # buat table baru yang di perbesar
    for i in range(table_size):
        new_table.append([None, None])

    # pindahin isi hash table lama ke yang baru
    for i in range(temp):
        if hash_table[i] != [None, None]:
            hash_code = convert_to_hashcode(hash_table[i][0])
            new_table[doubleHashing(hash_code, new_table)] = hash_table[i]
    
    hash_table = new_table  # balikin ke hashtable yang lama
    return hash_table

# looping untuk input
print('Masukkin perintah: ')
while True:
    user_input = input().strip()  # Menghapus spasi di awal dan akhir

    # Handle input kosong
    if not user_input:
        continue

    # Split input menjadi perintah dan argumen
    split_input = user_input.split(' ', 1)
    command = split_input[0]
    rest = split_input[1] if len(split_input) > 1 else ''

    # kasus untuk register
    if command == 'REGISTER':
        # Mendapatkan username dan password
        if '[' in rest and ']' in rest:
            username_start = rest.find('[') + 1
            username_end = rest.find(']')
            username = rest[username_start:username_end]
            
            password_start = rest.find('[', username_end) + 1
            password_end = rest.find(']', password_start)
            password = rest[password_start:password_end]
            
            if login_user == []:
                key = username

                # jika username sudah teregister
                if get_key(key):
                    print('Username Already Exist')
                else:
                    value = encrypt(password)
                    hashcode = convert_to_hashcode(key)

                    hash_table[doubleHashing(hashcode, hash_table)] = [key, value]
                    print('Register Successful')
                    element += 1

                    if check_table_size(table_size):
                        extend_table()
            else: 
                print("You're Still Logged In")

        else:
            print('Invalid format! Please use: REGISTER [Username] [Password]')
            
    # kasus untuk login
    elif command == 'LOGIN' and len(split_input) == 2:
        key = split_input[0]                 # Ambil username
        value = encrypt(split_input[1])

        # jika user belum login
        if not login_user:
            if get_key(key) == False: 
                print('Username Not Found\n')   # cek apakah username sudah teregister
            else:
                if current[1] != value:
                    print('Incorrect Password\n')   # jika pw yang dimasukkin salah
                else:
                    # tambahin user input yang login ke variabel login_user
                    login_user = current
                    print('Login Successful\n')
        # jika user sudah login
        else: 
            print("You've already logged in\n")
                                                    
    # edit usn atau password
    elif len(user_input) == 12 and user_input == 'EDIT_CURRENT':
        pilihan = user_input[1]                # opsi antara username atau password
        value = user_input[2]                  # ambil value yang ingin diubah
        hashcode = convert_to_hashcode(value)  # Ubah username ke hashcode
        
        if login_user != []:
            if pilihan == 'USERNAME':
                # cek keberadaan username pada hash table
                if get_key(value) == True:
                    print('Username Already Exist\n')
                else: 
                    get_key(login_user[0])              # ambil posisi username yg sedang login
                    password = hash_table[index][1]     # copy password dari hash table 
                    hash_table[index] = [None, None]    # ubah posisi lama jadi None
                    hash_table[doubleHashing(hashcode, hash_table)] = [value, password]   # Masukkin ke posisi baru di hashtable
                    login_user[0] = value               # ganti username
                    print('Your Account Has Been Updated\n')
                    
            elif pilihan == 'PASSWORD':
                get_key(login_user[0])
                value = encrypt(value)  
                hash_table[index][1] = value    # ganti password
                print('Your Account Has Been Updated\n')

        else: 
            print("You Have Not Been Logged In\n")

    # untuk ngasih tau siapa yang login
    elif len(user_input) == 16 and user_input == 'IS_AUTHENTICATED':
        # kondisi belum ada yg login
        if login_user == []:
            print('Please Login\n')
        # kondisi udah login
        else:
            print(login_user[0], login_user[1], '\n')

    elif len(user_input) == 10 and user_input == 'UNREGISTER':
        key = user_input[1]             # username
        value = encrypt(user_input[2])  # password yg sudah di enkripsi

        if login_user == []:
            # cek lokasi username pd hash table
            if get_key(key) == True:
                if hash_table[index][1] == value:
                    hash_table[index] = [None, None]
                    element -= 1
                    print('Your Account Has Been Deleted\n')
                    current = []
                else:
                    print('Incorrect Password\n')
            else:
                print('Username Not Found\n')
        else: 
            print('Please Log Out Your Account\n')
    
    # kondisi buat user yang mau logout
    elif len(user_input) == 6 and user_input == 'LOGOUT':
        # kalo user belum login
        if login_user == []:
            print('You Have Not Been Logged In\n')
        # lakukan logout saat user keadaannya sedang login
        else:
            login_user = []
            current = []
            print('You Have Been Logged Out\n')

    elif len(user_input) == 7 and user_input == 'INSPECT':
        row = int(user_input[1])             # Ambil username

        try:
            # kasih tau kalo isinya hanya [None, None]
            if hash_table[row] == [None, None]:
                print('Row Is Empty\n')
            else:
                print(hash_table[row][0], hash_table[row][1], '\n')
        except IndexError:
            print('Inspect out of table size\n')

    # cek username apakah ada di hashtable/teregistrasi
    elif len(user_input) == 14 and user_input == 'CHECK_USERNAME':
        key = user_input[1]                 # Ambil username

        if (get_key(key) == True): 
            print('Username Is Registered\n')
        else: 
            print('Username Not Found\n')

     # kasus untuk count_username
    elif command == 'COUNT_USERNAME' and len(rest) == 0:
        print(element)
    
    # cek kapasitas hashtable
    elif len(user_input) == 8 and user_input == 'CAPACITY':
        print(len_hash(hash_table))
    
    # nyoba print semua hashtable
    elif len(user_input) == 5 and user_input == 'PRINT':
        print(hash_table)

    # kasus untuk exit
    elif command == 'EXIT':
        print('Program End')
        break
    
    # inputan user salah
    else:
        print('Wrong input! Please put correct input\n')

# end program