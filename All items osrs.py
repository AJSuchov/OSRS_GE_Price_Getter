from osrsbox import items_api
from openpyxl import load_workbook #Import workbook
from openpyxl import Workbook #Create and import workbook
import time
from copy import copy, deepcopy
from operator import itemgetter


############################################################################################
########### Appending another excel sheet with sorted values ###############################
######## This is to open that new workbook which will be used latter #######################
#filepath2="C:\\Users\\AJ Suchovsky\\Desktop\\Multiprocessing_Project\\Sorted_Roster_Blank_Sequential.xlsx"
filepath2="C:\\Users\\suchovaj\\Documents\\Python Scripts\\OSRSList.xlsx"
wb2=load_workbook(filepath2)
sheet2=wb2.active


all_db_items = items_api.load()
for item in all_db_items:
    info = []
    if item.tradeable_on_ge == True:
        itid = str(item.id)
        name = item.name
        name_plus = name.replace(' ','+')
        url = "http://services.runescape.com/m=itemdb_oldschool/"+name_plus+"/viewitem?obj="+itid
        info.append(itid)
        info.append(name)
        info.append(url)
        sheet2.append(info)


wb2.save(filepath2)
