#task1 basic dictionary operation

cities ={
    "mysore" : "mysore pak",
    "banglore" : "bisi bele bath",
    "manglore" : "neer dosa",
    "dharwad" : "dharwad peda",
    "udupi" : "masala dosa"
}

cities["shivmogga"] = "akki rotti"

cities["banglore"] = "ragi mudde"

cities.pop("dharwad")
print (cities)

print(cities.keys())
print(cities.values())

#task2 nested dictionary

freinds={
    "freind1" :{
    "name" : "rahul",
    "fav_subject" : "python",
    "fav_food" : "dosa"
    },

    "freind2" :{
        "name" : "kiran",
        "fav_subject" : "maths",
        "fav_food" : "Biriyani"
    }
}
print (freinds)
print (freinds["freind1"]["fav_food"])