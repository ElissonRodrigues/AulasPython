import requests

def obter_codigo_pais(pais):
    url = "https://restcountries.com/v2/name/{}?fullText=true".format(pais)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        return data[0]["alpha2Code"]
    else:
        return None

def obter_universidades(codigo_pais):
    url = "https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universidades_and_domains.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        universidades = [
            {"name": university["name"], "web_page": university["web_pages"]}
            for university in data
            if university["alpha_two_code"] == codigo_pais
        ]
        return universidades
    else:
        return None

while True:
    pais = input("Digite o nome do país: ")
    codigo_pais = obter_codigo_pais(pais)
    if codigo_pais is not None:
        universidades = obter_universidades(codigo_pais)
        if universidades is not None:
            print("Universidades em {}:".format(pais))
            for university in universidades:
                print("- {} ({})".format(university["name"], ', '.join(university["web_page"])))
        else:
            print("\n\nNão foi possível obter informações sobre universidades no país.")
    else:
        print("\n\nNão foi possível obter informações sobre o país.")
