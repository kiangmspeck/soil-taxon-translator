print("Welcome to the Soil Taxonomy Translator")

taxon = input("Please enter your soil taxon at the subgroup level:\n")

if len(taxon) > 0:
    ord = len(taxon) - 4
    ord = taxon[ord:len(taxon)]
    if ord == 'alfs':
        print('Order: Alfisols')
    elif ord == 'ands':
        print('Order: Andisols')
    elif ord == 'ents':
        print('Order: Entisols')
    elif ord == 'ists':
        print('Order: Histosols')
    elif ord == 'epts':
        print('Order: Inceptisols')
    elif ord == 'olls':
        print('Order: Mollisols')
    elif ord == 'ults':
        print('Order: Ultisols')
    elif ord == 'erts':
        print('Order: Vertisols')
    else:
        ord = len(taxon) - 3
        ord = taxon[ord:len(taxon)]
        if ord == 'ids':
            print('Order: Aridisols')
        elif ord == 'els':
            print('Order: Gelisols')
        elif ord == 'ods':
            print('Order: Spodosols')
        else:
            ord = len(taxon) - 2
            ord = taxon[ord:len(taxon)]
            if ord == 'ox':
                print('Order: Oxisols')
            else:
                print('Not a valid order')
else:
    print('Invalid entry')

subord = ['aqualfs', 'cryalfs', 'ustalfs', 'xeralfs', 'udalfs',
    'aquands', 'gelands','cryands', 'torrands', 'xerands', 'vitrands',
    'ustands', 'udands', 'cryids', 'salids', 'durids', 'gypsids', 'argids', 'calcids',
    'cambids', 'wassents', 'aquents', 'psamments', 'fluvents', 'orthents',
    'histels', 'turbels', 'orthels', 'folists', 'wassists', 'fibrists', 'saprists',
    'hemists', 'aquepts', 'gelepts', 'cryepts', 'ustepts', 'xerepts', 'udepts',
    'albolls', 'aquolls', 'rendolls', 'gelolls', 'cryolls', 'xerolls', 'ustolls',
    'udolls', 'aquox', 'torrox', 'ustox', 'perox', 'udox', 'aquods', 'gelods', 'cryods',
    'humods', 'orthods', 'aquults', 'humults', 'udults', 'ustults', 'xerults', 'aquerts',
    'cryerts', 'xererts', 'torrerts', 'usterts', 'uderts']

search = [taxon.find(n) for n in subord]

for n in search:
    if n > -1:
        so_ind = search.index(n)
    else:
        pass


gg_ind = taxon.find(" ")

gg_ind +=1

print("Suborder:", subord[so_ind].capitalize())

grtgrp = taxon[gg_ind:len(taxon)].capitalize()
print("Great Group:", grtgrp)

subgrp = taxon.split()
subgrp = subgrp[0].capitalize()
print("Subgroup:",subgrp + ' ' + taxon[gg_ind:len(taxon)].capitalize())
