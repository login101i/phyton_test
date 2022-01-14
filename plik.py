from unittest import result

#Sprawdzenie czy argument funkcji jest liczba Fibbinary
#Liczba Fibbinary to taka liczba naturalna, ktora w zapisie binarnym nie posiada dwoch cyfr 1 polozonych obok siebie.
def is_binnary_number_Fibbinary(number):

    #sprawdzenie czy parametr jest liczba calkowita
    check_int = isinstance(number, int)
    if(check_int is False):
        print("Prosze wprowadzic liczbe calkowita.")
        return False
    
    #konwersja na liczbe binarna    
    converted_to_binnary=bin(number)[2:] 

    #zamiana na string
    converted_to_string=str(converted_to_binnary)
  
    #sprawdz za pomoca metody find() czy w converted_to_string  wystepuje '11'
    if converted_to_string.find("11")!=-1:
        print("Wprowadzona liczba nie jest liczba Fibbinary. W rozwinieciu binarnym to",  converted_to_binnary)
        return False
    else:
         print('Ta liczba w rozwinieciu binarnym to: ', converted_to_binnary, ' i  jest liczba Fibbonary. ')
         return True
    #Jesli nie jest liczba fibbinary zwroc False
  
  
#Wprowadz liczbe naturalna aby sprawdzic czy jest liczba Fibbonary.")
your_number=33
is_binnary_number_Fibbinary(your_number)



#zapisanie danych wejsciowych do sprawdzenia
list_to_check = [your_number]

#TEST---TEST---TEST---TEST---TEST---TEST---TEST---TEST---TEST
def test_if_binnary_numbers_are_Fibbinary():

    #sprawdzenie kazdego elementu tablicy czy jest liczba Fibbonary
    for i in list_to_check:

    #przypisanie testu
        result=is_binnary_number_Fibbinary(i)
    #assert
        assert result

#uruchamiam test jednostkowy w konsoli przy pomocy komendy:
# python -m pytest -plik.py -vvv
# aby test przeszedl pomyslnie, wszystkie elementy tablicy musza byc liczbami Fibbornary.



   







