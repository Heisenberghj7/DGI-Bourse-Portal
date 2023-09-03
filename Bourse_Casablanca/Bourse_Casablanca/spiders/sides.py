import scrapy
import json

class Sides(scrapy.Spider):
    name = "Sides"
    start_urls=["https://www.casablanca-bourse.com/en/live-market/emetteurs/AFM151215"]

    def parse(self, response):
        side_names = response.css("div.uppercase > p > a::text").getall() 
        sides_links = response.css("div.uppercase > p > a::attr(href)").getall()
        for name,link in zip(side_names,sides_links):
            yield {
                'name': name,
                'link': "https://www.casablanca-bourse.com"+link
            }
class Sides_details(scrapy.Spider):
    name="Sides_details"
    with open('sides.json', 'r') as f:
        data= json.load(f)
    start_urls=[item['link'] for item in data]

    def parse(self, response):
        side_full_name = response.css("div.md\\:-ml-5.md\\:-mr-7 > div > h1::text").get()
        management = response.css("div#emetteur_dirigeant > div > div > div > div > div > div.keen-slider__slide > div > p::text").getall()
        date= response.css("div#emetteur_actionnaires > div > div > div > div > p::text").get()
        shareholders= response.css("div#emetteur_actionnaires > div > div > div > div > div > table > tbody > tr > th::text").getall()
        Pourcentage= response.css("div#emetteur_actionnaires > div > div > div > div > div > table > tbody > tr > td > span::text").getall()
        Info_key = response.css("div#emetteur_société > div > div > div > div > div > table > tbody > tr > th::text").getall()
        Info_value = response.css("div#emetteur_société > div > div > div > div > div > table > tbody > tr > td::text").getall()
        paragraph= response.css("div#emetteur_société > div > div > div > div > div > table > tbody > tr > td > div > p::text,div#emetteur_société > div > div > div > div > div > table > tbody > tr > td > div::text,div#emetteur_société > div > div > div > div > div > table > tbody > tr > td > p > ul li::text,div#emetteur_société > div > div > div > div > div > table > tbody > tr > td > div > ul li::text").getall()
        key_figures= response.css("div#emetteur_CC > div > div > div > div > table > tbody > tr > td:nth-of-type(1)::text").getall()
        y2022 = response.css("div#emetteur_CC > div > div > div > div > table > tbody > tr > td:nth-of-type(2)::text,div#emetteur_CC > div > div > div > div > table > tbody > tr > td:nth-of-type(2) > span::text").getall()
        y2021 = response.css("div#emetteur_CC > div > div > div > div > table > tbody > tr > td:nth-of-type(3)::text,div#emetteur_CC > div > div > div > div > table > tbody > tr > td:nth-of-type(3) > span::text").getall()
        y2020 = response.css("div#emetteur_CC > div > div > div > div > table > tbody > tr > td:nth-of-type(4)::text,div#emetteur_CC > div > div > div > div > table > tbody > tr > td:nth-of-type(4) > span::text").getall()
        text = response.css("div.text-white.print\\:text-black.mt-5.lg\\:flex > div > p::text").getall()
        ratios = response.css("div#emetteur_ratio > div > div > div > div > div > table > tbody > tr > td:nth-of-type(1)::text").getall()
        yy2022 = response.css("div#emetteur_ratio > div > div > div > div > div > table > tbody > tr > td:nth-of-type(2) span::text, div#emetteur_ratio > div > div > div > div > div > table > tbody > tr > td:nth-of-type(2)::text").getall()
        yy2021 = response.css("div#emetteur_ratio > div > div > div > div > div > table > tbody > tr > td:nth-of-type(3) span::text, div#emetteur_ratio > div > div > div > div > div > table > tbody > tr > td:nth-of-type(3)::text").getall()
        yy2020 = response.css("div#emetteur_ratio > div > div > div > div > div > table > tbody > tr > td:nth-of-type(4) span::text, div#emetteur_ratio > div > div > div > div > div > table > tbody > tr > td:nth-of-type(4)::text").getall()
        investors_keys= response.css("div#emetteur_contact > div > div > div > div > div > div > p:nth-of-type(1)::text").getall()
        investors_values= response.css("div#emetteur_contact > div > div > div > div > div > div > p:nth-of-type(2)::text,div#emetteur_contact > div > div > div > div > div > div > p:nth-of-type(2) > a::text").getall()
        dividend_years=response.css("div#emetteur_dividendes > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(1) > p::text").getall()
        Dividend_amount = response.css("div#emetteur_dividendes > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(2) > p > span::text").getall()
        Dividend_type = response.css("div#emetteur_dividendes > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(3) > p::text").getall()
        ex_date = response.css("div#emetteur_dividendes > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(4) > p::text").getall()
        Payment_date = response.css("div#emetteur_dividendes > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(5) > p::text").getall()
        crossing_Date= response.css("div#test > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(1) > p::text").getall()
        declarant= response.css("div#test > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(2) > p::text").getall()
        Quantity= response.css("div#test > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(3) > p > span::text").getall()
        Price= response.css("div#test > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(4) > p > span::text").getall()
        Treshold_crossed= response.css("div#test > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(5) > p > span::text").getall()
        Direction= response.css("div#test > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(6) > p::text").getall()
        Intention_of_the_declarant= response.css("div#test > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(7) > p::text,div#test > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(7) > p > span::text").getall()
        Publications_page= response.css("div#emetteur_publications > div > div > div > div > div > a::attr(href)").get()
        instrument_link= response.css("div#emetteur_instruments > div > div > div > div > div > div > table > tbody > tr > td > p > a::attr(href)").get()
        yield {
           "side_full_name": side_full_name,
           "management":management,
           "date":date,
           "shareholders":shareholders,
           "Pourcentage":Pourcentage,
            "Info_key":Info_key,
            "Info_value":Info_value,
            "paragraph":paragraph,
            "key_figures":key_figures,
            "2022":y2022,
            "2021":y2021,
            "2020":y2020,
            "text":text,
            "ratios":ratios,
            "y2022":yy2022,
            "y2021":yy2021,
            "y2020":yy2020,
            "investors_keys":investors_keys,
            "investors_values":investors_values,
            "Dividend_years":dividend_years,
            "Dividend_amount":Dividend_amount,
            "Dividend_type":Dividend_type,
            "ex_date":ex_date,
            "Payment_date":Payment_date,
            "crossing_Date":crossing_Date,
            "declarant":declarant,
            "Quantity":Quantity,
            "Price":Price,
            "Treshold_crossed":Treshold_crossed,
            "Direction":Direction,
            "Intention_of_the_declarant":Intention_of_the_declarant,
            "Publications_page":"https://www.casablanca-bourse.com"+Publications_page,
            "instrument_link":"https://www.casablanca-bourse.com"+instrument_link
}

# class Publications(scrapy.Spider):
#     name="Publications"
#     with open('sides_details.json', 'r',encoding="utf8") as f:
#         data= json.load(f)
#     start_urls=[item['Publications_page'] for item in data]
#     def parse(self, response):
#         Issuer_name = 
#         Publication_date= 
#         Publication_title= 
#         publications= 
#         yield{
#             "Issuer_name":Issuer_name,
#             "Publication_date":Publication_date,
#             "Publication_title":Publication_title,
#             "publications":publications

#         }


# class Instrument(scrapy.Spider):
#     name="Instrument"
#     with open('sides_details.json', 'r',encoding="utf8") as f:
#         data= json.load(f)
#     start_urls=[item['instrument_link'] for item in data]
#     def parse(self, response):
#         Instrument_Information_keys= response.css("div#instrument-info > div > div > div > div > div > table > tbody > tr > th::text").getall()
#         Instrument_Information_values= response.css("div#instrument-info > div > div > div > div > div > table > tbody > tr > td::text,div#instrument-info > div > div > div > div > div > table > tbody > tr > td > span::text").getall()
#         Session_data_keys=response.css("div#instrument-data> div > div > div > div > div > table > tbody > tr > th::text").getall()
#         Session_data_values=response.css("div#instrument-data > div > div > div > div > div > table > tbody > tr > td > span::text,div#instrument-data > div > div > div > div > div > table > tbody > tr > td::text").getall()
#         data_history_keys=response.css("div#instrument-histo-var > div > div > div > div > div > table > tbody > tr > th::text").getall()
#         data_history_values=response.css("div#instrument-histo-var > div > div > div > div > div > table > tbody > tr > td > span::text").getall()
#         instrument_notices_link= response.css("div#instrument-avis > div > div > div > div > div:nth-of-type(3) > a::attr(href)").get()

#         yield {
#             "Instrument_Information_keys":Instrument_Information_keys,
#             "Instrument_Information_values":Instrument_Information_values,
#             "Session_data_keys" :Session_data_keys,
#             "Session_data_values":Session_data_values,
#             "data_history_keys":data_history_keys,
#             "data_history_values":data_history_values,
#             "instrument_notices_link":"https://www.casablanca-bourse.com"+instrument_notices_link

        # }
# class Instrument_notices(scrapy.Spider):
#     name="Instrument_notices"
#     with open('instrument.json', 'r',encoding="utf8") as f:
#         data= json.load(f)
#     start_urls=[item['instrument_notices_link'] for item in data]
#     def parse(self, response):
#         date=
#         title=
#         documents_link=
#         yield {
#             "date":date,
#             "title":title,
#             "documents" : documents_link
#         }