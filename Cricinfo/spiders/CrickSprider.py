# -*- coding: utf-8 -*-
import scrapy
#from scrapy.selector import HtmlXPathSelector

class CrickspriderSpider(scrapy.Spider):

    name = 'CrickSprider'
    
    allowed_domains = ['www.espncricinfo.com']
    
    start_url = ['www.espncricinfo.com/india/content/player/country.html?country=6']

    # location of csv file
    custom_settings = {
        'FEED_URI': 'tmp/cricinfo.csv'
    }

    Commmon_url = "www.espncricinfo.com"

    def parse(self, response):
        
        players_link = response.xpath("//div[@class='pnl650M']//td[@class='divider']//a/@href").extract()
        
        players_name = response.xpath("//div[@class='pnl650M']//td[@class='divider']//a/text()").extract()
        
        for i in range(0,len(players_link)):
            
            player_url = super.Commmon_url + str(players_link[i])
               
            yield scrapy.Request(player_url, callback=self.parse_plyr_dtls)
            
    def parse_plyr_dtls(self,response):
        
        #Extracting the content using xpath selectors.
        
            item['Full_name_player'] = response.xpath(
            "//* [@id='ciHomeContentlhs']/div[3]/div[2]/div[1]/p[1]/span/text()").extract()
            item['Born'] = response.xpath("//*[@id='ciHomeContentlhs']/div[3]/div[2]/div[1]/p[2]/span/text()").extract()
            item['Major_teams'] = response.xpath("//*[@id='ciHomeContentlhs']/div[3]/div[2]/div[1]/p[3]/span/text()").extract()
            item['Playing Role'] = response.xpath("//*[@id='ciHomeContentlhs']/div[3]/div[2]/div[1]/p[4]/span/text()").extract()
            item['Batting style'] = response.xpath("//*[@id='ciHomeContentlhs']/div[3]/div[2]/div[1]/p[5]/span/text()").extract()
            item['Bowling style'] = response.xpath("//*[@id='ciHomeContentlhs']/div[3]/div[2]/div[1]/p[6]/span/text()").extract()
            
            
     
