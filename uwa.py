# Read csv
# import csv
# with open('hospital_data.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ' and ',', quotechar='|')
#     # for row in spamreader:
#     #     print(', '.join(row))
#     country = []
#     for row in spamreader:
#         country.append(row['country'])

# file = open("hospital_data.txt", "r")
# content = file.read()
# print(content)
# file.close()

# file = open("hospital_data.csv", "r")
# content = file.read()
# # print(content)
# country = []
# for row in content:
#     country.append(row[0])
# print(country)
# file.close()

with open('hospital_data.csv', 'r') as f:
    country0 = []
    hospital0 = []
    for row in f:
        # print(row)
        row1 = row.split(',')
        # print(row1)
        country0.append(row1[0])
        hospital0.append(row1[1])
        country = country0[1:]
        hospital = hospital0[1:]
    
    f.seek(0)

    country_to_hospital = {i:[] for i in country}

    # for i in country:
    #     country_to_hospital[i] = None 

    for row in f:
        row1 = row.split(',')
        if row1[0] == 'afghanistan':
            country_to_hospital['afghanistan'].append(row1[1])
        elif row1[0] == 'albania':
            country_to_hospital['albania'].append(row1[1]) 
        elif row1[0] == 'algeria':
            country_to_hospital['algeria'].append(row1[1])
        elif row1[0] == 'angola':
            country_to_hospital['angola'].append(row1[1])
        elif row1[0] == 'anguilla':
            country_to_hospital['anguilla'].append(row1[1])
        elif row1[0] == 'argentina':
            country_to_hospital['argentina'].append(row1[1])
        elif row1[0] == 'australia':
            country_to_hospital['australia'].append(row1[1])
        elif row1[0] == 'austria':
            country_to_hospital['austria'].append(row1[1])
        elif row1[0] == 'bahamas':
            country_to_hospital['bahamas'].append(row1[1])
        elif row1[0] == 'bahrain':
            country_to_hospital['bahrain'].append(row1[1])
        elif row1[0] == 'bangladesh':
            country_to_hospital['bangladesh'].append(row1[1])
        elif row1[0] == 'belgium':
            country_to_hospital['belgium'].append(row1[1])
        elif row1[0] == 'botswana':
            country_to_hospital['botswana'].append(row1[1])
        elif row1[0] == 'brazil':
            country_to_hospital['brazil'].append(row1[1])
        elif row1[0] == 'brunei darussalam':
            country_to_hospital['brunei darussalam'].append(row1[1])
        elif row1[0] == 'bulgaria':
            country_to_hospital['bulgaria'].append(row1[1])
        elif row1[0] == 'cambodia':
            country_to_hospital['cambodia'].append(row1[1])
        elif row1[0] == 'cameroon':
            country_to_hospital['cameroon'].append(row1[1])
        elif row1[0] == 'canada':
            country_to_hospital['canada'].append(row1[1])
        elif row1[0] == 'chad':
            country_to_hospital['chad'].append(row1[1])
        elif row1[0] == 'chile':
            country_to_hospital['chile'].append(row1[1])
        elif row1[0] == 'china':
            country_to_hospital['china'].append(row1[1])
        elif row1[0] == 'colombia':
            country_to_hospital['colombia'].append(row1[1])
        elif row1[0] == 'comoros':
            country_to_hospital['comoros'].append(row1[1])
        elif row1[0] == 'congo':
            country_to_hospital['congo'].append(row1[1])
        elif row1[0] == 'cook islands':
            country_to_hospital['cook islands'].append(row1[1])
        elif row1[0] == 'costa rica':
            country_to_hospital['costa rica'].append(row1[1])
        elif row1[0] == "cote d'ivoire":
            country_to_hospital["cote d'ivoire"].append(row1[1])
        elif row1[0] == "croatia":
            country_to_hospital['croatia'].append(row1[1])
        elif row1[0] == "cuba":
            country_to_hospital['cuba'].append(row1[1])
        elif row1[0] == "cyprus":
            country_to_hospital['cyprus'].append(row1[1])
        elif row1[0] == "czech republic":
            country_to_hospital['czech republic'].append(row1[1])

    # print(country_to_hospital)

    f.seek(0)

    country_to_death = {i:[] for i in country}

    for row in f:
        row1 = row.split(',')
        if row1[0] == 'afghanistan':
                country_to_death['afghanistan'].append(row1[8])
        elif row1[0] == 'albania':
            country_to_death['albania'].append(row1[8]) 
        elif row1[0] == 'algeria':
            country_to_death['algeria'].append(row1[8])
        elif row1[0] == 'angola':
            country_to_death['angola'].append(row1[8])
        elif row1[0] == 'anguilla':
            country_to_death['anguilla'].append(row1[8])
        elif row1[0] == 'argentina':
            country_to_death['argentina'].append(row1[8])
        elif row1[0] == 'australia':
            country_to_death['australia'].append(row1[8])
        elif row1[0] == 'austria':
            country_to_death['austria'].append(row1[8])
        elif row1[0] == 'bahamas':
            country_to_death['bahamas'].append(row1[8])
        elif row1[0] == 'bahrain':
            country_to_death['bahrain'].append(row1[8])
        elif row1[0] == 'bangladesh':
            country_to_death['bangladesh'].append(row1[8])
        elif row1[0] == 'belgium':
            country_to_death['belgium'].append(row1[8])
        elif row1[0] == 'botswana':
            country_to_death['botswana'].append(row1[8])
        elif row1[0] == 'brazil':
            country_to_death['brazil'].append(row1[8])
        elif row1[0] == 'brunei darussalam':
            country_to_death['brunei darussalam'].append(row1[8])
        elif row1[0] == 'bulgaria':
            country_to_death['bulgaria'].append(row1[8])
        elif row1[0] == 'cambodia':
            country_to_death['cambodia'].append(row1[8])
        elif row1[0] == 'cameroon':
            country_to_death['cameroon'].append(row1[8])
        elif row1[0] == 'canada':
            country_to_death['canada'].append(row1[8])
        elif row1[0] == 'chad':
            country_to_death['chad'].append(row1[8])
        elif row1[0] == 'chile':
            country_to_death['chile'].append(row1[8])
        elif row1[0] == 'china':
            country_to_death['china'].append(row1[8])
        elif row1[0] == 'colombia':
            country_to_death['colombia'].append(row1[8])
        elif row1[0] == 'comoros':
            country_to_death['comoros'].append(row1[8])
        elif row1[0] == 'congo':
            country_to_death['congo'].append(row1[8])
        elif row1[0] == 'cook islands':
            country_to_death['cook islands'].append(row1[8])
        elif row1[0] == 'costa rica':
            country_to_death['costa rica'].append(row1[8])
        elif row1[0] == "cote d'ivoire":
            country_to_death["cote d'ivoire"].append(row1[8])
        elif row1[0] == "croatia":
            country_to_death['croatia'].append(row1[8])
        elif row1[0] == "cuba":
            country_to_death['cuba'].append(row1[8])
        elif row1[0] == "cyprus":
            country_to_death['cyprus'].append(row1[8])
        elif row1[0] == "czech republic":
            country_to_death['czech republic'].append(row1[8])

    # print(country_to_death)

with open('hospital_data.txt', 'r') as f:
    f1 = f.readlines()
    for row in f1[:-1]:
        text_one_delimiter = row.replace(':', ', ')
        row1 = text_one_delimiter.split(', ')
        print(row1)
    
    f.seek(0)
    country_to_covid_stroke = {i:[] for i in country}

    for row in f1[:-1]:
        text_one_delimiter = row.replace(':', ', ')
        row1 = text_one_delimiter.split(', ')
        if row1[1] == 'afghanistan':
                country_to_covid_stroke['afghanistan'].append(sum(int(row1[5]), int(row1[7])))
    print(country_to_covid_stroke)


        



