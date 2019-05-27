#https://codelabs.developers.google.com/codelabs/build-your-first-android-app-kotlin/#7

import requests
from bs4 import BeautifulSoup
from webcrawl.models import LatestInfoTbl, RssDataTbl
import sys

class CrawlClass:
        # Sql query
        sqlQuery = { 
                'existMaster' : "SELECT COUNT(*) FROM information_schema.tables WHERE table_name=?;",
                'createLatestInfoTbl' : "CREATE TABLE LatestInfoTbl(FileName nvarchar(100) PRIMARY KEY, Date nvarchar(100));",
                'updateLatestInfo' : "UPDATE LatestInfoTbl SET Date = ? WHERE FileName = ?;",
                'insertLatestInfo' :  "INSERT INTO LatestInfoTbl (FileName, Date) VALUES (?,?);",
                'selectDateLatestInfo' :  "SELECT Date FROM LatestInfoTbl WHERE FileName=?;",
                'createRssTbl'  : "CREATE TABLE RssTable(No INT PRIMARY KEY, Title nvarchar(MAX), Link nvarchar(MAX), Category nvarchar(MAX), Author nvarchar(MAX), PubDate nvarchar(100), Article nvarchar(MAX));",
                'selectTop1RssTbl'  : "SELECT Top 1 No FROM RssTable ORDER BY No DESC;"
                }        
       
        # Create LatestInfoTbl if not exist      

        def __InsertRss(self, bsObject, RssDataTbl):
                
                dictRss = {}
                for item in bsObject.findAll('item'):        
                        dictRss[item.no.string] = {
                                item.title.name : item.title.string, 
                                item.link.name : item.link.string,
                                item.category.name : item.category.string,
                                item.author.name : item.author.string,
                                item.pubDate.name : item.pubDate.string,
                                item.description.name : item.description.string }               
              
                top1Value = 0

                try:
                        top1Entry = RssDataTbl.objects.order_by('-pk')
                        top1Value = top1Entry.no
                except:                                        
                        top1Value = 0

                for dictRssKey in dictRss:
                        if int(dictRssKey) > top1Value :
                                insert = RssDataTbl( 
                                        no=dictRssKey, 
                                        title=dictRss[dictRssKey]['title'], link=dictRss[dictRssKey]['link'], 
                                        category=dictRss[dictRssKey]['category'],
                                        author=dictRss[dictRssKey]['author'], pubDate=dictRss[dictRssKey]['pubDate'],
                                        article=dictRss[dictRssKey]['description'] )         
                                insert.save()                              
               
               
        def ParseRss(self, LatestInfoTbl, RssDataTbl):  

                # Request RSS
                
                html = requests.get("http://file.mk.co.kr/news/rss/rss_30000001.xml")
                bsObject = BeautifulSoup(html.content, 'xml') 
                lastBuildData = bsObject.find('lastBuildDate')

                try:
                        selectRes = LatestInfoTbl.objects.get(fileName = 'rss_30000001.xml')
                except LatestInfoTbl.DoesNotExist:
                        insert = LatestInfoTbl(fileName='rss_30000001.xml', pubDate=lastBuildData.string)
                        insert.save()                    
                finally:
                        if selectRes.pubDate > lastBuildData.string :
                                return
                
                        LatestInfoTbl.objects.filter(fileName = 'rss_30000001.xml').update(pubDate=lastBuildData.string)                        

                        self.__InsertRss(bsObject, RssDataTbl)
               
        def ShowRssTable(self):
                '''
                self.cur.execute("SELECT * FROM RssTable;")
                rows = self.cur.fetchall()
                for row in rows:
                        print(row)
                        print("\n")
                '''
