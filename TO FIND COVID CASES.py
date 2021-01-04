from covid import Covid

corona = Covid()

country = input("enter your country:")
case = corona.get_status_by_country_name(country)
for country in case:
    print(country,":",case[country])
