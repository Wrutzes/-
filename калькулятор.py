
import time
import random
import os

time.sleep(2)
l = int(random.randint(10,40))
print("Идёт загрузка...",l,"%", sep="")
time.sleep(3)
ll = int(random.randint(41,67))
print("Идёт загрузка...",ll,"%", sep="")
time.sleep(2)
lll = int(random.randint(68,99))
print("Идёт загрузка...",lll,"%", sep="")
time.sleep(2)
print("Идёт загрузка...Выполнено")

const = s = (6)     #Общеее число действий
const = i = int(0)  #просто константа(для менюхи)

print("\nПривет, это калькулятор. Введите действие \n")

if (i < s):
    print("Сложение                     (", (i+1), ")")
    print("Вычитание                    (", (i+2), ")")
    print("Умножение                    (", (i+3), ")")
    print("Деление                      (", (i+4), ")")
    print("Возведение числа в степень   (", (i+5), ")")
    print("Деление нацело               (", (i+6), ")\n")

n = input("")
print("__________________________")
if(n == "1"): 

    print(">>>Вы выбрали : Сложение (+)")
    print("\tВводите ваши числа:\n")
    a1 = float(input("Первое число: "))
    a2 = float(input("Второе число: "))
    a = a1 + a2
    print("\n\tВаш результат: ", a , "\n")
    
    
if(n == "2"):
    
    print(">>>Вы выбрали : Вычитание (-)")
    print("\tВводите ваши числа:\n")
    b1 = float(input("Первое число: "))
    b2 = float(input("Второе число: "))
    b = b1 - b2
    print("\n\tВаш результат: ", b , "\n")
    
if(n == "3"):
    
    print(">>>Вы выбрали : Умножение (*)")
    print("\tВводите ваши числа:\n")
    c1 = float(input("Первое число: "))
    c2 = float(input("Второе число: "))
    c = c1 * c2
    print("\n\tВаш результат: ", c , "\n")
    
if(n == "4"):
    
    print(">>>Вы выбрали : Деление (/)")
    print("\tВводите ваши числа:\n")
    d1 = float(input("Первое число: "))
    d2 = float(input("Второе число: "))
    d = d1 / d2
    print("\n\tВаш результат: ", d , "\n")
    
if(n == "5"):
    
    print("Вы выбрали : Возведение числа в степень (^)")
    print("\tВведите ваше действие:\n")
    
    print("Возведение в квадрат              (", (i+1), ")")
    print("Возведение в куб                  (", (i+2), ")")
    print("Возведение в степень своего числа (", (i+3), ")")

    j = input("")
    if(j == "1"):
        
        print("\t>>>Возведение в квадрат (^2)\n")
        print("Введите число: ")
        f1 = float(input())
        f = f1**2
        print("\n\tВаше результат: ", f , "\n")
        
    if(j == "2"):
        
        print("\t>>>Возведение в куб (^3)\n")
        print("Введите число: ")
        f2 = float(input())
        ff = f2**3
        print("\n\tВаше результат: ", ff , "\n")
        
    if(j == "3"):
        print("\t>>>Возведение в степень своего числа (ваше число^ваша степень)\n")
        f3 = float(input("Введите ваше число: "))    #ЧИСЛО
        f_n = float(input("Введите вашу степень: ")) #СТЕПЕНЬ
        fff = f3**f_n
        print("\n\tВаше результат: ", fff , "\n")
        
if(n == "6"):
    
    print("\t>>>Вы выбрали : Деление числа нацело\n")
    g1 = float(input("Первое число: "))
    g2 = float(input("Второе число: "))
    g = g1//g2
    print("\n\tВаш результат: ", g  , "\n")
    
os.system("PAUSE")