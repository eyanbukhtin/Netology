countries = {
    "Thailand" : {"sea" : True,
                  "shengene" : False,
                  "average_temperature" : 30,
                  "curancy_rate" : 1.8},
    "Hugary" : {"sea" : False,
                  "shengene" : True,
                  "average_temperature" : 10,
                  "curancy_rate" : 0.3},
    "Germany" : {"sea" : True,
                  "shengene" : True,
                  "average_temperature" : 5,
                  "curancy_rate" : 80},
    "Japan" : {"sea" : True,
                  "shengene" : False,
                  "average_temperature" : 21,
                  "curancy_rate" : 0.61},
}

def get_countries_warmer_than(countrise, temperature=20):
    hot_countries = []
    for country, properties in countries.items():
        if properties["average_temperature"] > temperature:
            hot_countries.append(country)
    return hot_countries

def input_temperature():
    t = input("type the temp:")
    return t

def main():
    while True:
        temp = input_temperature()
        if temp.isdigit():
            temp = int(temp)
        else:
            exit()
        c = get_countries_warmer_than(countries, temperature=temp)
        print("Горячие страны:", c)
        print("Очень горячие путевки") 

main()
