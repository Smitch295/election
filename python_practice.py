counties = ["Arapahoe", "Denver", "Jefferson"]
if counties [1] == 'Denver' :
    print(counties[1])

if 'El Paso' in counties:
    print ('El Paso is in the list of counties.')
else:
    print ('El Paso is not the list of counties')

if 'Arapahoe' in counties and 'El Paso' in counties:
    print ('Arapahoe and El Paso are in the list of counties.')
else:
    print ('Arapahoe or El Paso is not in the list of counties.')

for county in counties:
    print (county)

for i in range (len(counties)):
    print (counties[i])

counties_dict = {"Arapahoe":422829, "Denver":463353,"Jefferson":432438}
for county in counties_dict:
    print(county)
    