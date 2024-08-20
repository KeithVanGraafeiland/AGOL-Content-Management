
## run user report for arcgis online items
# https://developers.arcgis.com/python/guide/accessing-and-creating-content/

import time
from arcgis.gis import GIS
from AGOL_Credentials import AGOLusername, AGOLpassword
import csv
import pandas as pd
import os

URL = 'https://esri.maps.arcgis.com/home'
gis = GIS(url=URL, username=AGOLusername, password=AGOLpassword)
me = gis.users.me
csv_report = 'esri_oceans_report.csv'

search_result_image = gis.content.search(query='owner:'+ AGOLusername, sort_field="numViews" ,sort_order="desc", max_items = 1000)
#for item in search_result:
    #display(item)
    #last_udpated = time.localtime(item.modified / 1000)
    #print(f"{item.itemid} {item.title:<40} {time.asctime(last_udpated)} {item.numViews:<40} {item.type:25} {item.tags} {item.owner}")
    #print(item)
    #writer.writerow(f"{item.itemid} {item.title:<40} {time.asctime(last_udpated)} {item.numViews:<40} {item.type:25} {item.tags} {item.owner}")
#user_item.close()
df_imageitem = pd.DataFrame(search_result_image)
df_imageitem.to_csv(csv_report)