from full_version import *
print('''
1.circle
2.ethad_2jomlei_negetiv
3.ethad_mozdvj
4.ethad_2jomlei_plus
5.mokab_2jomlei_negetiv
6.mokab_2jomlei_plus
7.fisaqores
8.fat_larg_negetiv
9.fat_larg_plus
10.tak_jomlei_mshtrk
11.sqrt
12.moraba
13.mosalas
14.zozanaqe
15.info
''')
option =int( input(">> "))
if option == 1:
    circle()
elif option == 2:
    ethad_2jomlei_negetiv()
elif option == 3:
    ethad_mozdvj()
elif option == 4:
    ethad_2jomlei_plus()
elif option == 5:
    mokab_2jomlei_negetiv()
elif option == 6:
    mokab_2jomlei_plus()
elif option == 7:
    fisaqores()
elif option == 8:
    fat_larg_negetiv()
elif option == 9:
    fat_larg_plus()
elif option == 10:
    tak_jomlei_mshtrk()
elif option == 11:
    sqrt()
elif option == 12:
    moraba()
elif option == 13:
    musalas()
elif option == 14:
    zozanqe()
elif option == 15:
    info()
else: print("wrong option")
