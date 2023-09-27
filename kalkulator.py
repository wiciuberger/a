# import math

# def Pole_Kwadratu(a):
#     return a**2
# def Pole_Prostokata(a, b):
#     return a * b
# def Pole_trapezu(a, b, h):
#     return [(a + b) *h]/2
# def Pole_Trojkata(a, h):
#     return (a * h/2)
# def Pole_trojkata_rownobocznego(a):
#     return [((a**2)*3**(1/2))] /4
# def Pole_kola(r):
#     return(r**2) * 3,14
# def Tw_pitagorasa(a, b):
#     return (a**2 + b**2)**(1/2)
# def Pole_rownolegloboku_i_rombu(a, b):
#     return a * b

# def kalkulator():
#     print("witaj")
#     while True:
#         print("dostepne opcje")
#         print("1, pole kwadratu")
#         print("2, pole prostokata")
#         print("3, pole trapezu")
#         print("4, pole trojkata rownobocznego")
#         print("5, pole kola")
#         print("6, twierdzenie pitagorasa")
#         print("7, pole rownolegloboku i rombu")
#         print("8, wyjscie")

#         wybor = input("wybierz opcje 1/2/3/4/5/6/7/8/9")

#         if wybor == '9':
#             print("koniec")
#             break
#         if wybor not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
#             print("error 404")
#             continue

#         if wybor == '1':
#             a = float(input("podaj dlugosc boku"))
#             wynik = Pole_Kwadratu(a)
#             print("pole kwadratu wynosi: {wynik}")
#         elif wybor == '2':
#             a = float(input("podaj dlugosc boku 1"))
#             b = float(input("podaj dlugosc boku 2"))
#             wynik = Pole_Prostokata(a)
#             print("pole prostokata wynosi: {wynik}")
#         elif wybor == '3':
#             a = float(input("podaj dlugosc boku 1"))
#             b = float(input("podaj dlugosc boku 2"))
#             h = float(input("podaj dlugosc wysokosci"))
#             wynik = Pole_trapezu(a, b, h)
#             print("pole trapezu wynosi: {wynik}")

#         elif wybor == '4':
#             a = float(input("podaj dlugosc boku 1"))
#             h = float(input("podaj dlugosc wysokosci"))
#             wynik = Pole_Trojkata(a, h)
#             print("pole trojkata wynosi: {wynik}")
#         elif wybor == '5':
#             a = float(input("podaj dlugosc boku 1"))
#             wynik = Pole_trojkata_rownobocznego(a)
#             print("pole trojkata rownobocznego wynosi: {wynik}")
#         elif wybor == '6':
#             a = float(input("podaj dlugosc boku 1"))
#             b = float(input("podaj dlugosc boku 2"))
#             wynik = Tw_pitagorasa(a, b)
#             print("twierdzenie pitagorasa wynosi: {wynik}")
#         elif wybor == '7':
#             r = float(input("podaj promien"))
#             wynik = Pole_kola(r)
#             print("pole kola wynosi: {wynik}")
#         elif wybor == '8':
#             a = float(input("podaj dlugosc boku 1"))
#             b = float(input("podaj dlugosc boku 2"))
#             wynik = Pole_rownolegloboku_i_rombu(a, b)
#             print("pole rownolegloboku i rombu wynosi: {wynik}")
#         elif wybor == '9':
#             e = float(input("podaj dlugosc przekatnej 1"))
#             f = float(input("podaj dlugosc przekatnej 2"))
#             wynik = Pole_trapezu(e, f)
#             print("pole trapezu wynosi: {wynik}")
# if __name__ == "_main_":
#     kalkulator()

# x = int(input('x = ')) 
# while 0 <= x:
#   if x % 9 == 0:
#     print(x, ' --- Jest podzielna przez 9')
#   x -= 1

# x = int(input('x = ')) 
# while 0 <= x:
#   if x % 3 != 0:
#     print(x, ' --- NIE jest podzielna przez 3')
#   x -= 1

# n = int(input("Podaj wartość n: "))

# for i in range(n):
#     result = 2 ** i
#     print(f"2^{i} = {result}")

# n = int(input("Ile razy chcesz wyświetlić zdanie? "))

# for i in range(n):
#     print("KOCHAM PROGRAMOWAĆ!!!")

import random

def explore_cave():
    print("Jesteś w ciemnej jaskini. Co chcesz zrobić?")
    print("1. Idź na północ")
    print("2. Idź na wschód")
    print("3. Wyjdź z jaskini")
    
    choice = input("Wybierz opcję (1/2/3): ")
    
    if choice == '1':
        encounter_monster()
    elif choice == '2':
        find_treasure()
    elif choice == '3':
        print("Opuszczasz jaskinię.")
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        explore_cave()

def encounter_monster():
    print("Spotkałeś potwora!")
    print("1. Walcz")
    print("2. Uciekaj")
    
    choice = input("Wybierz opcję (1/2): ")
    
    if choice == '1':
        if random.random() < 0.5:
            print("Pokonałeś potwora i zdobywasz nagrodę!")
        else:
            print("Potwór okazał się zbyt silny. Przegrywasz.")
    elif choice == '2':
        print("Udało Ci się uciec od potwora.")
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        encounter_monster()

def find_treasure():
    print("Znalazłeś skarb!")
    print("Gratulacje, jesteś bogaty!")

def main():
    print("Witaj w grze RPG!")
    explore_cave()

if __name__ == "__main__":
    main()





