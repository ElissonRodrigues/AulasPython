from requests import get
from traceback import format_exc

def get_word_info(word, endpoint):
    url = f"https://dicio-api-ten.vercel.app/v2/{endpoint}/{word}"
    response = get(url)

    if response.status_code in [200, 201]:
        return response.json()
    else:
        return None
        
while True:
    try:
        palavra = input("\n\nDigite uma palavra para encontrar seu significado: ")

        if len(palavra.split()) > 1:
            print("\n\nVocê digitou mais de uma palavra, tente novamente digitando apenas uma palavra: ")
        else:
            meanings = get_word_info(palavra, 'significados')
            
            if not meanings:
                print(f'\n\nSem significado para: "{palavra}"')
            else:
                significados= "\n".join(f"{i + 1} - {meaning}" for i, meaning in enumerate(meanings[0]["meanings"]))
                print(f"\n\nSignificado:\n{significados}") if significados else ""
                print(f'\n\nEtimologia:\n{meanings[0]["etymology"]}') if meanings[0]["etymology"] else ""

                sinonimos = get_word_info(palavra, "sinonimos")
                print(f"\nSinônimos:\n{', '.join(sinonimos)}") if sinonimos else ""
                
                silabas = get_word_info(palavra, "silabas")
                print(f"\nSílabas:\n{', '.join(silabas)}") if silabas else ""
                
    except KeyboardInterrupt:
        print("\n\nScript encerrado. Até breve!")
        break
    except:
        print(format_exc())
        
