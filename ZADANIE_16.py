groshi = int(input("Введите сумму в рублях: "))

if groshi < 2 or groshi % 2 != 0:

   print("Молодой человек,извините, но копеек нет")

else:

   sotochki = groshi // 100

   groshi = groshi % 100

   desynchiki = groshi // 10

   groshi = groshi % 10

   duble = groshi // 2

   print(f"Галя,неси деньги из своей кассы,мы тут молодому человеку разменяем")