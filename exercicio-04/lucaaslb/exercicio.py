import csv

with open('../pessoas.csv', 'r') as f:   
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    next(reader, None) # skip header

    lines = 0
    masc = 0
    fem = 0
    dMaior = 0
    dMenor = 0

    for row in reader:        
        lines += 1
        if row[2] == 'M':
            masc += 1
        elif row[2] == 'F':
            fem += 1

        if int(row[1]) >= 18:
            dMaior +=1
        elif int(row[1]) < 18:
            dMenor +=1

        print(row)


    print(masc*100 / lines, "% são homens" ) #porcentagem de homens
    print(fem*100 / lines, "% são mulheres")  #porcentagem de mulheres 
    print(dMaior, 'pessoas maiores de idade.')
    print(dMenor, 'pessoas menores de idade') 