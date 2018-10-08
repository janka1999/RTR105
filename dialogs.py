#!/usr/bin/python
# -"- coding utf-8 -"-

a = input("Cien, liet, lūdzu, ievadi skaitli: ")
# 3. pythona visi input rezultātiir ar str datu tipu
# tāpēc ievadītā lieluma datu tipā vēlāk ir jāpārveido 
a = int(a)

# python valoda balstās uz C valodu == print strādā līdzīgi printf
# https://www.cplusplus.com/reference/cstdio/print/f
print("Liet., Tu esi ievadījis skaitli : %d"%(a))
aa = a * a
print("Tavs skaitlis kvadrātā ir: %d"%(aa))

