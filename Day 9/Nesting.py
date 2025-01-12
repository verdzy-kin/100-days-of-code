Capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}
travel_log = {
    "France": {"Citiesvisited": ["paris", "Lille", "Dijan"], "totalvisited": 12},
    "Germany": {"Citiesvisited": ["Berlin", "Hanburg", "stuttgart"], "Totalvisited": 10},
}
travel_log = [
    {
        "Country": "France", 
        "Cities": ["paris", "Lille", "Dijan"], 
        "Visits": 12
    },
    {
        "Country": "Germany", 
        "Cities": ["Berlin", "Hanburg", "stuttgart"], 
        "Visits": 10
    },
]
def Addnewcountry(countryvisited, timevisited, Citiesvisited):
    Newcountry = {}
    Newcountry["Country"] = countryvisited
    Newcountry["Visits"] = timevisited
    Newcountry["Cities"] = Citiesvisited
    travel_log.append(Newcountry)
Addnewcountry("Russia", 2, ["Moscow", "Saint petra"])
print(travel_log)