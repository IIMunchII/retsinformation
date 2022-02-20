# Scraping og NLP af Retsinformation 
Et lille projekt der går ud på Scraping &amp; NLP af retsinformation.dk
Det lader til, at retsinformation.dk har et lille API hvor alle dokumenter kan hentes fra.

## Introduktion
Der er nu opsat et lille Django projekt med en database og tabel til at lagre retursvaret fra API-et.
- Scrapy sørger for at kalde API-et asynkront og parser retursvaret på en effektiv måde
- Django Models integeres med Scrapy Items.
- Scrapy sørger for at mappe keys fra JSON responset til felter i django models.
- Django gemmer i sqlite3 databasen.

### 1 - Opsæt database og Django
Når du står i `/retsinformation/retsinfo_app/` (samme folder som manage.py ligger i)
Så kør nedenstående.
```bash
python manage.py migrate
```

### 2 - Kør Crawler
Kig i retsinfo.py

Kør med kommandoen når du står i folderen `/retsinfo_scraper/` (der hvor settings.py også er).

/retsinformation/
```bash
scrapy crawl retsinfo
```

### 3 - Resultatet
Hvis man er interesseret i at se resultatet kan man enten dykke ned i databasen med et selvvalgt interface eller bruge Django's shell.

```bash
python manage.py shell
```
Og dernæst køres
```python
from scrapers.models import RetsinfoDocument
docs = RetsinfoDocument.objects.all()
```

objektet `docs`indeholder nu alle de dokumenter der kom ned via API-et da crawleren blev kørt.
