#!/usr/bin/python
# -*- coding utf-8 -*-

a = input("Cien. liet., lūdzu ievadi skaitli:")
# 3.python'ā visi input rezultāti ir ar str datu tipu
# tapēc ievadītā lieluma datu tips vēlāk ir jāpārveido
a = int(a)

# python valoda balstās uz c valodas => print strādā līdzīgi printf
# http://www.cplusplus.com/reference/cstdio/printf/
print("liet., Tu esi ievadījis skaitli: %d"%(a))
aa = a * a
print("Tavs skaitlis kvadrātā ir: %d"%(aa))

