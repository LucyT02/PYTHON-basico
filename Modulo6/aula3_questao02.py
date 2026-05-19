urls = ["www.google.com", "www.gmail.com", "www.github.com", 
        "www.reddit.com", "www.yahoo.com"]

dominios = []

for site in urls:
    dominios.append(site[4:-4])

print("URLs:", urls)
print("Domínios:", dominios)