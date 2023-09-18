Code Improvement is fondamental, like the Ratio tables there's some weaknesses in the code

## Sides

Sides_names_shortcut = response.css("div.uppercase > p > a::text").getall() 
Sides_links = response.css("div.uppercase > p > a::attr(href)").getall() before the links extenstions add https://www.casablanca-bourse.com/

## Sides Details
side_full_name = response.css("div.md\\:-ml-5.md\\:-mr-7 > div > h1::text").get()
management = response.css("div#emetteur_dirigeant > div > div > div > div > div > div.keen-slider__slide > div > p::text").getall()

## Main shareholders

date= response.css("div#emetteur_actionnaires > div > div > div > div > p::text").get()

shareholders= response.css("div#emetteur_actionnaires > div > div > div > div > div > table > tbody > tr > th::text").getall()
Pourcentage= response.css("div#emetteur_actionnaires > div > div > div > div > div > table > tbody > tr > td > span::text").getall()

## Key Indicators

### Company Infos

Info_key = response.css("div#emetteur_société > div > div > div > div > div > table > tbody > tr > th::text").getall()
Info_value = response.css("div#emetteur_société > div > div > div > div > div > table > tbody > tr > td::text").getall()
social_object_value = response.css("div#emetteur_société > div > div > div > div > div > table > tbody > tr > td > div > p::text").getall()
value.extend(social_object_value)

### Key figures

keys = response.css("div#emetteur_CC > div > div > div > div > table > tbody > tr > td:nth-of-type(1)::text").getall()
2022 = response.css("div#emetteur_CC > div > div > div > div > table > tbody > tr > td:nth-of-type(2)::text,div#emetteur_CC > div > div > div > div > table > tbody > tr > td:nth-of-type(2) > span::text").getall()
2021 = response.css("div#emetteur_CC > div > div > div > div > table > tbody > tr > td:nth-of-type(3)::text,div#emetteur_CC > div > div > div > div > table > tbody > tr > td:nth-of-type(3) > span::text").getall()
2020 = response.css("div#emetteur_CC > div > div > div > div > table > tbody > tr > td:nth-of-type(4)::text,div#emetteur_CC > div > div > div > div > table > tbody > tr > td:nth-of-type(4) > span::text").getall()

text = response.css("div.text-white.print\\:text-black.mt-5.lg\\:flex > div > p::text").getall()

### Ratio

ratios = response.css("div#emetteur_ratio > div > div > div > div > div > table > tbody > tr > td:nth-of-type(1)::text").getall()
2022 = response.css("div#emetteur_ratio > div > div > div > div > div > table > tbody > tr > td:nth-of-type(2) span::text, div#emetteur_ratio > div > div > div > div > div > table > tbody > tr > td:nth-of-type(2)::text").getall()
2021 = response.css("div#emetteur_ratio > div > div > div > div > div > table > tbody > tr > td:nth-of-type(3) span::text, div#emetteur_ratio > div > div > div > div > div > table > tbody > tr > td:nth-of-type(3)::text").getall()
2020 = response.css("div#emetteur_ratio > div > div > div > div > div > table > tbody > tr > td:nth-of-type(4) span::text, div#emetteur_ratio > div > div > div > div > div > table > tbody > tr > td:nth-of-type(4)::text").getall()

### Investor Relations - Contacts

keys= response.css("div#emetteur_contact > div > div > div > div > div > div > p:nth-of-type(1)::text").getall()
values = response.css("div#emetteur_contact > div > div > div > div > div > div > p:nth-of-type(2)::text").getall()
mail_website = response.css("div#emetteur_contact > div > div > div > div > div > div > p:nth-of-type(2) > a::text").getall()

## Financial operation

### Capital increase

### Dividend

years = response.css("div#emetteur_dividendes > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(1) > p::text").getall()
Dividend_amount = response.css("div#emetteur_dividendes > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(2) > p > span::text").getall()
Dividend_type = response.css("div#emetteur_dividendes > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(3) > p::text").getall()
Ex-date = response.css("div#emetteur_dividendes > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(4) > p::text").getall()
Payment_date = response.css("div#emetteur_dividendes > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(5) > p::text").getall()

### Bond issue

## Threshold crossing

crossing_Date= response.css("div#test > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(1) > p::text").getall()
Declarant= response.css("div#test > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(2) > p::text").getall()
Quantity= response.css("div#test > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(3) > p > span::text").getall()
Price= response.css("div#test > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(4) > p > span::text").getall()
Treshold_crossed= response.css("div#test > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(5) > p > span::text").getall()
Direction= response.css("div#test > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(6) > p::text").getall()
Intention_of_the_declarant= response.css("div#test > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(7) > p::text,div#test > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(7) > p > span::text").getall()

## Issuer's latest publications

Publications_page= response.css("div#emetteur_publications > div > div > div > div > div > a::attr(href)").get() add the prefix https://www.casablanca-bourse.com

Issuer_name= 
Publication_dates= 
Publication_title= response.css("div._loading_overlay_wrapper.css-w8cb0z > div > div > div:nth-of-type(2) > a > h3::text").getall()
publications= 

the problem of publications page is that when I select a side it doesn'regenerate the html it just filters the publication so when I scrap I got all instruments


## The instruments of the issuer

link = response.css("div#emetteur_instruments > div > div > div > div > div > div > table > tbody > tr > td > p > a::attr(href)").get()
add the prefix https://www.casablanca-bourse.com

### Instrument Information

keys= response.css("div#instrument-info > div > div > div > div > div > table > tbody > tr > th::text").getall()
values = response.css("div#instrument-info > div > div > div > div > div > table > tbody > tr > td::text,div#instrument-info > div > div > div > div > div > table > tbody > tr > td > span::text").getall()

### Session data

keys= response.css("div#instrument-data> div > div > div > div > div > table > tbody > tr > th::text").getall()
values= response.css("div#instrument-data > div > div > div > div > div > table > tbody > tr > td > span::text,div#instrument-data > div > div > div > div > div > table > tbody > tr > td::text").getall()

### Data history
keys= response.css("div#instrument-histo-var > div > div > div > div > div > table > tbody > tr > th::text").getall()
values=  response.css("div#instrument-histo-var > div > div > div > div > div > table > tbody > tr > td > span::text").getall()

### instrument notices

link= response.css("div#instrument-avis > div > div > div > div > div:nth-of-type(3) > a::attr(href)").get() add the prefixe https://www.casablanca-bourse.com/

dates= 
title=
links=

