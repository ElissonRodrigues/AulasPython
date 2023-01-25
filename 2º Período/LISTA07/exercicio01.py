from requests import get

base_url = "https://dicio-api-ten.vercel.app/v2/"

while True:
    try:
        palavra = input("\n\nDigite uma palavra para encontrar seu significado: ")

        if len(palavra.split()) > 1:
            print("\n\nVocê digitou mais de uma palavra, tente novamente digitando apenas uma palavra: ")
        else:
            req_sig = get(f"{base_url}significados/{palavra}")

            if req_sig.status_code in [200, 201]:
                json = req_sig.json()

                if not json[0]["meanings"]:
                    print(f'\n\nSem significado para: "{palavra}"')
                else:
                    signifidos = "\n".join(map(lambda x: f"{x[0]+1} - {x[1]}", enumerate(json[0]["meanings"])))
                    print(f"\n\nSignificado:\n{signifidos}") if signifidos else ""
                    print(f'\n\nEtimologia:\n{json[0]["etymology"]}') if json[0]["etymology"] else ""

                    endpoints = [f"{base_url}sinonimos/{palavra}", f"{base_url}silabas/{palavra}"]

                    for url in endpoints:
                        req = get(url)

                        if req.status_code in [200, 201]:
                            json = req.json()

                            resultado = "\n".join(map(lambda x: f"{x}", json))

                            if "sinonimos" in url:
                                print(f"\n\nSinonimos:\n{resultado}") if resultado else ""
                            else:
                                print(f"\n\nSilabas:\n{resultado}") if resultado else ""

            else:
                print("Palavra não encontrada, use outra palavra")
    except KeyboardInterrupt:
        print("\n\nScript encerrado. Até breve!")
        break
    except Exception as e:
        print(e)
