# -*- coding: utf-8 -*-
import scrapy
import logging
class CrickspriderSpider(scrapy.Spider):

    name = 'CrickSprider'
    
    allowed_domains = ['espncricinfo.com']
    
    start_urls = ['http://www.espncricinfo.com/india/content/player/country.html?country=6']

    logging.log(logging.INFO, "Loading requests")
    # location of csv file
    custom_settings = {
        'FEED_URI': 'tmp/cricinfo.csv'
    }

    def parse(self, response):
        
        players_link = response.xpath("//div[@class='pnl650M']//td[@class='divider']//a/@href").extract()
        
        players_name = response.xpath("//div[@class='pnl650M']//td[@class='divider']//a/text()").extract()

        Commmon_url = "http://www.espncricinfo.com"

        for i in range(0,len(players_link)):
            player_url = Commmon_url + str(players_link[i])
               
            yield scrapy.Request(player_url, callback=self.parse_plyr_dtls)
            
    def parse_plyr_dtls(self,response):
        
        #Extracting the content using xpath selectors.
        
            Full_name_player = response.xpath(
            "//* [@id='ciHomeContentlhs']/div[3]/div[2]/div[1]/p[1]/span/text()").extract()
            Born = response.xpath("//*[@id='ciHomeContentlhs']/div[3]/div[2]/div[1]/p[2]/span/text()").extract()
            Major_teams = response.xpath("//*[@id='ciHomeContentlhs']/div[3]/div[2]/div[1]/p[3]/span/text()").extract()
            Playing_Role = response.xpath("//*[@id='ciHomeContentlhs']/div[3]/div[2]/div[1]/p[4]/span/text()").extract()
            Batting_style = response.xpath("//*[@id='ciHomeContentlhs']/div[3]/div[2]/div[1]/p[5]/span/text()").extract()
            Bowling_style = response.xpath("//*[@id='ciHomeContentlhs']/div[3]/div[2]/div[1]/p[6]/span/text()").extract()

            for item in zip(Full_name_player,Born,Major_teams,Playing_Role,Batting_style,Bowling_style):
                 scraped_info = {
                     'Full_name_player' : item[0],
                     'Born' : item[1],
                     'Major_teams' : item[2],
                     'Playing_Role' : item[3],
                     'Batting_style': item[4],
                     'Bowling_style': item[5]
            }

            yield scraped_info

     
