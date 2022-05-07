#sudo systemctl start mongod
#mongodb-compass
#mongosh

def show(Result):
    for x in Result:
        pprint(x)

from unittest import result
import pymongo
from pprint import pprint

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# BDD = myclient["BDD"]
# world = BDD["world"]

def dict_sum(x):
    if("NotOffLang" in x and "OffLang" in x):
        return x["NotOffLang"] + x["OffLang"]
    elif("NotOffLang" in x):
        return x["NotOffLang"]
    elif("OffLang" in x):
        return x["OffLang"]
    return {}


def Question1(world) :
    Result = world.find()
    return (str(len(list(Result))))

def Question2(world):
    Result = world.find()
    Continents = []
    for x in Result:
        if(x["Continent"] not in Continents):
            Continents.append(x["Continent"])
    
    return Continents
    print("La liste des Continents :")
    for x in Continents:
        print(x)

def Question3(world):
    Query = {"Name" : "Algeria"}
    Result = world.find(Query)
    return Result[0]

    for x in Result:
        for k in x.keys():
            if("Cities" in k):
                print("--------------------------------\nCities : ")
                for city in x[k]:
                    print( "Name :", city["Name"], ",Population:", city["Population"])
                continue
            if("_id" not in k):
                print(k,":", x[k])

    # Query = {"Name" : "Algeria"}
    # Result = world.find(Query)
    # for x in Result:
    #     for k in x.keys():
    #         if("Cities" in k):


def Question4(world):
    Query = {"Continent" : "Africa", "Population": {"$lt" : 100000} }
    Result = world.find(Query)
    return Result
    print("Pays Africain ayant un pop inférieure à 100000 habitants :")
    [print(x["Name"]) for x in Result]

def Question5(world):
    Condition = {"IndepYear" : { "$ne" : "NA"}, "Continent" : "Oceania"}
    Projection = {"Name" : 1, "_id" : 0}

    Result = world.find(Condition, Projection).distinct("Name")
    return Result
    show(Result)

def question6(world):
    Query = [
        {
            "$group" : {
            "_id" : "$Continent",
            "SurfaceArea" : {"$sum" : "$SurfaceArea"}
            }
        },
        {
            "$sort": {"SurfaceArea" : -1}
        },
        {"$limit" : 1}
    ]
    Result = world.aggregate(Query)
    return Result

    print("Le contient maximum est : ")
    for x in Result:
        for key in x.keys():
            if(key in '_id'):
                print("Country : ", x[key])
                continue
            print(key, ":", x[key])


def question7(world):
    Query = [
        {
            "$group" : {
            "_id" : "$Continent",
            "Population_Total" : {"$sum" : "$Population"},
            "Pays" : {"$sum" : 1},
            "Pays_indep": { "$sum": {"$cond": [{"$eq": ["$IndepYear", "NA"]}, 0, 1] } }
            }
        }
    ]
    Result = world.aggregate(
        Query
    )

    return Result
    for x in Result:
        print("Continent : ",x["_id"])
        print("Population : ", x["Population_Total"])
        print("Nombre de pays :",x["Pays"])
        print("Nombre de pays Indep :",x["Pays_indep"])
        print('---------------------------')

def question8(world):
    Query = {"Name" : "Algeria"}
    Result = world.find(
        Query
    )

    # print("La population des villes en Algerie :")
    sum = 0
    for x in Result:
        for y in x["Cities"]:
            sum += y["Population"]
        sum1 = sum + x["Capital"]["Population"]
    return [sum, sum1]
    

def question9(world):
    Query = {"Name" : "Algeria"}
    Result = world.find(
        Query
    )

    for x in Result : 
        name = x["Capital"]["District"]
        pop = x["Capital"]["Population"]
    return [name, pop]

def question10(world):
    languages = {}
    for x in world.find():
        for y in (dict_sum(x)):
            if(y['Language'] not in languages.keys()):
                languages[y['Language']] = 1
            else:
                languages[y['Language']] += 1
    langs = []
    for lang in languages.keys():
        if(languages[lang] > 15):
            langs.append(lang)
    return langs

def question11(world):
    cities = {}
    for x in world.find():
        if("Cities" in x):
            if(len((x['Cities'])) > 99):
                cities[x["Name"]] =  len(x['Cities'])

    # for key in sorted(cities, key=cities.get, reverse=True):
        # print("Le pays :",key)
        # print("Nombre de villes : ",cities[key])
        # print("------------------------------------")
    
    return sorted(cities, key=cities.get, reverse=True)

def question12(world):
    Query = [
        {"$unwind" : "$Cities"},
        {"$project" : 
            {"Name": 1, "Cities.Population" : 1, "_id":0, "Cities.Name":1}
        },
        {"$sort" : 
            {"Cities.Population" : -1}
        },
        {"$limit" : 10}
    ]
    Result = world.aggregate(Query)
    return Result

    print("Les 10 villes les plus habitées:")
    for x in Result:
        print("Le pays :",x["Name"])
        print("Nom de la ville: ",x["Cities"]["Name"])
        print("Population de la ville:",x["Cities"]["Population"])
        print("-----------------------------------------------------")

def question13(world):
    Query = [
        {"$unwind" : "$OffLang"},
        {"$project" : 
            {"Name" : 1, "OffLang.Language" : 1, "_id":0}
        }
    ]
    Result = world.aggregate(Query)
    
    resu = []
    for x in Result:
        if("Arabic" in x['OffLang']['Language']):
            resu.append(x["Name"])

    return resu

def question14(world):
    Languages_spoken = {}
    for x in world.find():
        Languages_spoken[x["Name"]] = len(dict_sum(x))

    i=1
    resu = []
    for key in sorted(Languages_spoken, key=Languages_spoken.get, reverse=True):
        # print("Le pays: ",key)
        # print("Le nombre de langues parlées :", Languages_spoken[key])
        # print('-----------------------------------------------------------------')
        if(i != 5):
            resu.append(key)
            i += 1
        else:
            break
    return resu

def question15(world):
    resu = []
    for x in world.find():
        sum = 0
        if("Cities" in x):
            for y in x['Cities']:
                sum += y["Population"]
        if("Capital" in x):
            sum += x["Capital"]["Population"]
        if(sum > x["Population"]):
            pay = {"name" : x["Name"], "population": x["Population"], "villes" : sum}
            resu.append(pay)
            # print("Le pays :",x["Name"])
            # print("La population du pays", x["Population"])
            # print("La population des villes :", sum)
            # print("----------------------------------------")
    return resu


# y = 1
# while(y!=0):

#     print("--------------------------------------------Bienvenu-------------------------------------------")
#     print("-----------------------------------Que voulez vous afficher ?--------------------------------------")
#     print("1. Déterminer le nombre exact de pays")
#     print("2. Lister les différents continents")
#     print("3. Lister les informations de l’Algérie")
#     print("4. Lister les pays du continent Africain, ayant une population inférieure à 100000 habitants")
#     print("5. Lister les pays indépendant du continent océanique")
#     print("6. Quel est le plus gros continent en termes de surface")
#     print("7. Le continent avec le nombre de pays, la population totale et le nombre de pays indépendant")
#     print("8. Donner la population totale des villes d’Algérie")
#     print("9. Donner la capitale et sa population d’Algérie")
#     print("10. Quelles sont les langues parlées dans plus de 15 pays ?")
#     print("11. les pays ayant au moins 100 villes")
#     print("12. Les 10 villes les plus habitées, ainsi que leur pays avec leurs population")
#     print("13. Les pays pour lesquels l'Arabe est une langue officielle")
#     print("14. Les 5 pays avec le plus de langues parlées")
#     print("15. Les pays pour lesquels la somme des populations des villes est supérieure à la population du pays")
#     print("------------------------------------------------------------------------------------------------------------------")

#     x = int(input("\n--Enter your value--\n"))
#     print("\n----------------------------------------------------------------")
#     while(x > 15 or x < 1):
#         x = int(input("--Wrong value, please re-select the correct range of values--\n"))

#     if(x == 1):
#         Question1()
#     elif(x == 2):
#         Question2()
#     elif(x == 3):
#         Question3()
#     elif(x == 4):
#         Question4()
#     elif(x == 5):
#         Question5()
#     elif(x == 6):
#         question6()
#     elif(x == 7):
#         question7()
#     elif(x == 8):
#         question8()
#     elif(x == 9):
#         question9()
#     elif(x == 10):
#         question10()
#     elif(x == 11):
#         question11()
#     elif(x == 12):
#         question12()
#     elif(x == 13):
#         question13()
#     elif(x == 14):
#         question14()
#     elif(x == 15):
#         question15()

#     print("----------------------------------------------------------------\n")
#     y = int(input("\n--Please Choose : \n 0-Quit\n 1-Relaunch\n"))
#     print("\n")
#     if(y==0):
#         print("------------------------------------Thank you for using our program !!----------------------------")
