import requests

while True:
    pais = input("\n\nDigite o nome do país: ")

    url = "https://restcountries.com/v2/name/{}".format(pais)

    req = requests.get(url)

    if req.status_code == 200:
        data = req.json()
        codigo_pais = data[0]["alpha2Code"]

        if codigo_pais:
            url = "https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json"
            req = requests.get(url)

            if req.status_code == 200:
                data = req.json()
                universidades = [
                    {"name": university["name"], "web_page": university["web_pages"]}
                    for university in data
                    if university["alpha_two_code"] == codigo_pais
                ]
               
                if universidades:
                    print("Universidades no(a) {}:\n\n".format(pais))

                    for university in universidades:
                        print(f'- {university["name"]} ({", ".join(university["web_page"])})')
                else:
                    print("\n\nNão foi possível obter informações sobre universidades no país.")
        else:
            print("\n\nNão foi possível obter informações sobre o país.")
    else:
        print ('\n\nNão foi possível encontrar o codigo desse pais.')
