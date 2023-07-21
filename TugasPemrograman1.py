from queue import Empty

# Deklarasikan variabel yang berisikan set dari operator
# Dan urutan presedensi
setofoperators = {'+', '-', '*', '/', '(', ')', '$'}
precedence = {'(':0, ')':0, '+':1, '-':1, '*':2, '/':2, '$':3}

# Buat sebuah class bernama Evaluator untuk perhitungan
class Evaluator:
    # Deklarasikan setiap variabel yang berisi list kosong
    # dan panjang dari input
    def __init__(self, exp):
        self.stackone = []
        self.stacktwo = []
        self.len = self.is_len(exp)
        self.str = ''

    # function untuk melakukan push stack pada
    # variabel stackone
    def push_stackone(self, op):
        return self.stackone.append(op)

    # function untuk melakukan push stack pada
    # variabel stacktwo
    def push_stacktwo(self, op):
        return self.stacktwo.append(op)
    
    # function untuk mengecek isi stack terakhir
    def top(self):
        # jika stack kosong, maka raise Stack Empty
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.stackone[-1]
    
    # function untuk melakukan pop stack pada variabel
    # stackone
    def pop(self):
        # jika stack kosong, maka raise Stack Empty
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.stackone.pop()
    
    # function untuk cek bahwa stack kosong
    def is_empty(self):
        return len(self.stackone) == 0

    # function untuk mengecek panjang dari input/stack
    def is_len(self, op):
        return len(op)
    
    # function untuk melakukan komparasi antar presedensi operator
    def op_compare(self, op):
        op_precedence = precedence[op]              # presedensi operator yang di loop
        top_precedence = precedence[self.top()]     # presedensi operator yang di posisi stack terakhir
        # kondisi jika presedensi stack terakhir lebih tinggi
        if top_precedence >= op_precedence :
            # kondisi untuk presendensi pangkat
            if (op_precedence == top_precedence == 3): 
                return False
            else :
                return True
        # kondisi kebalikannya
        else: return False
    
    # function untuk melakukan convert dari infix ke postfix
    def converter(self, exp):
        count = 0       # sebagai counter
        elemen = ''     # string untuk menggabungkan angka

        # looping setiap karakter pada exp
        for char in exp:
            count += 1
            # kondisi jika karakter adalah spasi
            if char == ' ':
                # cek apakah dia memiliki operatior atau tidak di antara angka
                if exp[count] not in setofoperators and exp[count-2] not in setofoperators:
                    self.str = "[No operation in postfix]"
                else:
                    pass
            # kondisi jika karakter bukan bagian dari operator
            elif char not in setofoperators:
                elemen += char
                try: 
                    if (exp[count] in setofoperators or self.len == 1 
                        or exp[count] == ' '):
                        self.push_stacktwo(elemen)
                        elemen = ''
                except IndexError: 
                    self.push_stacktwo(elemen)
                    elemen = ''

            # kondisi jika karakter merupakan kurung awal
            # lakukan push ke stack untuk operator
            elif char == '(':
                self.push_stackone(char)
            
            # kondisi jika karakter merupakan kurung akhir
            elif char == ')':
                # looping untuk melakukan pop dan push
                while (not self.is_empty() and self.top() != '(') :
                    # kondisi jika tidak ada kurung awal
                    if ('(' not in self.stackone): 
                        self.str = "[Missing open parenthesis]"
                    op = self.pop()
                    self.push_stacktwo(op)
                # kondisi jika terdapat kurung awal
                if (not self.is_empty() and '(' in self.stackone):
                    self.pop()
            
            # kondisi jika karakter selain kurung
            else :
                # cek jika input terakhir bukan angka, melainkan operator 
                if(self.len == 1 and char in setofoperators): 
                    self.str = "[Missing operand]"
                # looping selama stack tidak kosong serta 
                # melakukan perbandingan presedensi
                while(not self.is_empty() and self.op_compare(char)):
                    op = self.pop()
                    self.push_stacktwo(op)
                self.push_stackone(char)
            self.len -= 1

        # looping pada stack untuk operator
        while (not self.is_empty()):
            if (self.top() == '('): 
                op = self.pop()
                self.str = "[Missing close parenthesis]"
            else: 
                op = self.pop()
                self.push_stacktwo(op)
        
        # print hasil
        print("Postfix expression : ", end='')
        result = self.calculate(self.stacktwo)
        for i in self.stacktwo:
            print( i, end=" ")
        print(" ")

        # kondisi jika terdapat error
        if (self.str == "[Missing open parenthesis]"):
            print("Nilai :", result)
            print("Error Messages :", self.str)
        elif (self.str == "[Missing operand]"):
            print("Nilai :",result )
            print("Error Messages :", self.str)
        elif (self.str == "[Division by zero]"):
            print("Nilai :", result)
            print("Error Messages :", self.str)
        elif (self.str == "[No operation in postfix]"):
            print("Error Messages :", self.str)
        elif (self.str == "[Missing close parenthesis]"):
            print("Error Messages :", self.str)
        else:
            print("Nilai:", result)

    # function untuk menghitung hasil dari postfix
    def calculate(self, postfix):
        char = 0
        newstack = []

        # looping karakter pada postfix
        for char in postfix:
            # cek jika angka dan push ke stack baru
            if char.isnumeric(): newstack.append(char)

            # cek jika operator
            else:
                # lakukan pop untuk posisi paling atas pada stack
                first = int(newstack.pop())
                try: 
                    # lakukan pop untuk posisi paling atas pada stack
                    second = int(newstack.pop())
                    
                    # jika operator tambah
                    if char == '+':
                        x = first + second
                        newstack.append(x)
                    # jika operator kurang
                    elif char == '-':
                        x = second-first
                        newstack.append(x)
                    # jika operator kali
                    elif char == '*':
                        x = first*second
                        newstack.append(x)
                    # jika operator bagi
                    elif char == '/':
                        try:
                            x = second//first
                            newstack.append(x)
                        # kondisi jika pembagi adalah 0
                        except ZeroDivisionError:                    
                            newstack.append(second)
                            self.str = "[Division by zero]"
                    # jika operator pangkat
                    elif char == '$':
                        x = second**first
                        newstack.append(x)
                # kondisi jika terdapat index error
                except IndexError:
                    newstack.append(first) 
        # kembalikan hasil dari stack
        return newstack.pop()

# pemanggilan fungsi dan tempat input user
if __name__ == '__main__':
    infix = input("Masukkan infix expression : ")
    result = Evaluator(infix)
    result.converter(infix)