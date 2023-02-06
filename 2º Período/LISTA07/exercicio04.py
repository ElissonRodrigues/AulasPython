import requests

def get_country_code(country_name):
    url = "https://restcountries.com/v2/name/{}?fullText=true".format(country_name)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        return data[0]["alpha2Code"]
    else:
        return None

def get_universities(country_code):
    url = "https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        universities = [
            {"name": university["name"], "web_page": university["web_pages"]}
            for university in data
            if university["alpha_two_code"] == country_code
        ]
        return universities
    else:
        return None

while True:
    country_name = input("Digite o nome do país: ")
    country_code = get_country_code(country_name)
    if country_code is not None:
        universities = get_universities(country_code)
        if universities is not None:
            print("Universidades em {}:".format(country_name))
            for university in universities:
                print("- {} ({})".format(university["name"], ', '.join(university["web_page"])))
        else:
            print("Não foi possível obter informações sobre universidades no país.")
    else:
        print("Não foi possível obter informações sobre o país.")
