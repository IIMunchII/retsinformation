# Scraping og NLP af Retsinformation 
Et lille projekt der går ud på Scraping &amp; NLP af retsinformation.dk
Det lader til, at retsinformation.dk har et lille API hvor alle dokumenter kan hentes fra.

## Kør skidtet
Kig i retsinfo.py

Kør med kommandoen når du står i folderen med settings.py


/retsinformation/
```bash
scrapy cralw retsinfo
```

Denne lille kommando afprøver et scrape af et API response der indeholder et json array med nogle key/values hvor et af dem er et htmldocument. I parseren bruges der BeautifulSoup til at parse strengen til html og en funktino der hedder get_text() til at trække alt teksten ud. BeautifulSoup er ikke det hurtigeste i verdenen, men super easy og præcist at bruge.