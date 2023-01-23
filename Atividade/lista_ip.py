from socket import gethostbyname

sites = [

    "google.com",
    "youtube.com",
    "github.com",
    "netflix.com",
    "facebook.com",
    "twitter.com",
    "whatsapp.com",
    "globo.com",
    "play.google.com",
    "web.telegram.org"
]

print ("LISTANDO IPS")
print ("\n".join([gethostbyname(x) for x in sites]))
    
    