#Module 3.2.10 & 3.2.11
counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}

#for county in counties_dict:
#    print(county)
#    print(counties_dict[county])

total_vote = 0
for voters in counties_dict.values():
    total_vote = total_vote + voters

for county, voters in counties_dict.items():
#    print(county + " county has " + str(voters) + " registered voters.")
    print(f"{county} county has {voters} registered voters.")
    print(f"{county} county has {voters / total_vote * 100:.2f}% of the total votes.")




#Module 3.2.10 (Second Half) & 3.2.11
voting_data = [{"county":"Arapahoe","registered_voters": 422829},
                {"county":"Denvers","registered_voters": 463353},
                {"county":"Jefferson","registered_voters": 432438}]

for county_dict in voting_data:
#    print(county_dict)
#    print(county_dict['county'])
    print(f"{county_dict['county']} county has {county_dict['registered_voters']} registered voters")

for county_dict in voting_data:
        for value in county_dict.values():
            print(value)


    