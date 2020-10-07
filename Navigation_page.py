from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import Global_var
import sys, os
import ctypes
import string
import re
from Insert_On_Datbase import insert_in_Local,create_filename
import wx
import html
app = wx.App()

def ChromeDriver():
    # File_Location = open("D:\\0 PYTHON EXE SQL CONNECTION & DRIVER PATH\\ok.gov\\Location For Database & Driver.txt", "r")
    # TXT_File_AllText = File_Location.read()
    # Chromedriver = str(TXT_File_AllText).partition("Driver=")[2].partition("\")")[0].strip()
    # chrome_options = Options()
    # chrome_options.add_extension('D:\\0 PYTHON EXE SQL CONNECTION & DRIVER PATH\\ok.gov\\Browsec-VPN.crx')  # ADD EXTENSION Browsec-VPN
    # browser = webdriver.Chrome(executable_path=str(Chromedriver),
    #                            chrome_options=chrome_options)
    # time.sleep(20)  # WAIT UNTIL CHANGE THE MANUAL VPN SETTING
    # browser.get('https://www.ok.gov/dcs/solicit/app/solicitationSearch.php?status=open-pending')
    # browser.set_window_size(1024 , 600)
    # browser.maximize_window()
    # browser.switch_to.window(browser.window_handles[1])
    # browser.close()
    # browser.switch_to.window(browser.window_handles[0])
    # browser = webdriver.Chrome(executable_path=str(Chromedriver))
    browser = webdriver.Chrome(executable_path=str(f"C:\\chromedriver.exe"))
    browser.get(
        """https://chrome.google.com/webstore/detail/browsec-vpn-free-and-unli/omghfjlpggmjjaagoclmmobgdodcjboh?hl=en" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://chrome.google.com/webstore/detail/browsec-vpn-free-and-unli/omghfjlpggmjjaagoclmmobgdodcjboh%3Fhl%3Den&amp;ved=2ahUKEwivq8rjlcHmAhVtxzgGHZ-JBMgQFjAAegQIAhAB""")
    
    wx.MessageBox(' -_-  Add Extension and Select Proxy Between 25 SEC -_- ', 'Info', wx.OK | wx.ICON_WARNING)
    time.sleep(25)  # WAIT UNTIL CHANGE THE MANUAL VPN SETTING
    browser.get("https://www.ok.gov/dcs/solicit/app/solicitationSearch.php?status=open-pending")
    browser.maximize_window()
    time.sleep(3)
    href = []
    for pages in range(2, 5, 1):
        for tender_href in browser.find_elements_by_xpath('/html/body/div/div/div[3]/div[2]/div[3]/div/div/form[2]/div[4]/table/tbody//td[2]/a'):
            if tender_href not in href:
                href.append(tender_href.get_attribute('href'))
        browser.get('https://www.ok.gov/dcs/solicit/app/solicitationSearch.php?page='+str(pages)+'&sortBy=swnumber&flip=')
    Scrap_data(browser, href)


def Scrap_data(browser, Tender_href):
    global a
    a = True
    while a == True:
        try:
            for href in Tender_href:
                browser.get(href)
                Global_var.Total += 1
                for Submission_date in browser.find_elements_by_xpath('//*[@id="CLOSING_DATE"]'):
                    Submission_date = Submission_date.get_attribute('innerText').strip()
                    if Submission_date != '':
                        nowdate = datetime.now()
                        date2 = nowdate.strftime("%Y-%m-%d")
                        deadline = time.strptime(Submission_date, "%m/%d/%Y")
                        currentdate = time.strptime(date2, "%Y-%m-%d")
                        if deadline > currentdate:
                            SegFeild = []
                            for data in range(45):
                                SegFeild.append('')
                            SegFeild[24] = date2
                            get_htmlSource = ""
                            for outerHTML in browser.find_elements_by_xpath('/html/body/div/div/div[3]/div[2]/div[3]/div/form/div[3]'):
                                get_htmlSource = outerHTML.get_attribute('outerHTML')
                                get_htmlSource = get_htmlSource.replace('href="viewAttachment', 'href="https://www.ok.gov/dcs/solicit/app/viewAttachment')\
                                    .replace('<input type="submit" name="button" id="MAIN_MENU" value="Return To Main Menu" tabindex="16" class="sm_button">','')\
                                    .replace('<input type="submit" name="button" id="MAIN_MENU" value="Return To Main Menu" tabindex="14" class="sm_button">','')\
                                    .replace('<input type="submit" name="button" id="MAIN_MENU" value="Return To Main Menu" tabindex="13" class="sm_button">','')\
                                    .replace('<input type="submit" name="button" id="MAIN_MENU" value="Return To Main Menu" tabindex="12" class="sm_button">','')\
                                    .replace('<input type="submit" name="button" id="MAIN_MENU" value="Return To Main Menu" tabindex="15" class="sm_button">','')\
                                    .replace('<input type="submit" name="button" id="MAIN_MENU" value="Return To Main Menu" tabindex="11" class="sm_button">','')\
                                    .replace('<input type="submit" name="button" id="MAIN_MENU" value="Return To Main Menu" tabindex="17" class="sm_button">','')\
                                    .replace('<input type="submit" name="button" id="MAIN_MENU" value="Return To Main Menu" tabindex="18" class="sm_button">','')\
                                    .replace('<input type="submit" name="button" id="MAIN_MENU" value="Return To Main Menu" tabindex="19" class="sm_button">','')\
                                    .replace('<input type="submit" name="button" id="MAIN_MENU" value="Return To Main Menu" tabindex="20" class="sm_button">','')\
                                    .replace('<input type="submit" name="button" id="MAIN_MENU" value="Return To Main Menu" tabindex="10" class="sm_button">','')\
                                    .replace('<input type="submit" name="button" id="BACK" value="Back" tabindex="15" class="sm_button">','') \
                                    .replace('<input type="submit" name="button" id="BACK" value="Back" tabindex="13" class="sm_button">', '')\
                                    .replace('<input type="submit" name="button" id="BACK" value="Back" tabindex="14" class="sm_button">', '')\
                                    .replace('<input type="submit" name="button" id="BACK" value="Back" tabindex="16" class="sm_button">', '')\
                                    .replace('<input type="submit" name="button" id="BACK" value="Back" tabindex="17" class="sm_button">', '')\
                                    .replace('<input type="submit" name="button" id="BACK" value="Back" tabindex="18" class="sm_button">', '')\
                                    .replace('<input type="submit" name="button" id="BACK" value="Back" tabindex="19" class="sm_button">', '')\
                                    .replace('<input type="submit" name="button" id="BACK" value="Back" tabindex="20" class="sm_button">', '')\
                                    .replace('<input type="submit" name="button" id="BACK" value="Back" tabindex="12" class="sm_button">', '')
                                break
                            # Attachment
                            for attachment in browser.find_elements_by_xpath('//*[@class="table_wrapper"]'):
                                attachment = attachment.get_attribute('outerHTML')
                                SegFeild[4] = attachment.replace('href="viewAttachment', 'href="https://www.ok.gov/dcs/solicit/app/viewAttachment')
                                break
                            # Purchaser
                            for Agency in browser.find_elements_by_xpath('//*[@id="AGENCY_ID"]'):
                                Agency = Agency.get_attribute('innerText').upper()
                                SegFeild[12] = Agency.strip()
                                break

                            # Title
                            for Description in browser.find_elements_by_xpath('//*[@id="DESCRIPTION"]'):
                                Description = Description.get_attribute('innerText').strip()
                                Description = string.capwords(str(Description))
                                SegFeild[19] = Description
                                break

                            # tender NO
                            for SOL_NUMBER in browser.find_elements_by_xpath('//*[@id="SOL_NUMBER"]'):
                                SOL_NUMBER = SOL_NUMBER.get_attribute('innerText').strip()
                                SegFeild[13] = SOL_NUMBER.strip()
                                break

                            # Tender Details
                            CONTRACT_TYPE = ""
                            BUYER_ID = ''
                            DATE_STATUS = ''
                            STATUS = ''
                            for CONTRACT_TYPE in browser.find_elements_by_xpath('//*[@id="CONTRACT_TYPE"]'):
                                CONTRACT_TYPE = CONTRACT_TYPE.get_attribute('innerText').replace('&nbsp;', '').strip()
                                break
                            for BUYER_ID in browser.find_elements_by_xpath('//*[@id="BUYER_ID"]'):
                                BUYER_ID = BUYER_ID.get_attribute('innerText').strip()
                                break
                            for DATE_STATUS in browser.find_elements_by_xpath('//*[@id="DATE_STATUS"]'):
                                DATE_STATUS = DATE_STATUS.get_attribute('innerText').strip()
                                break
                            for STATUS in browser.find_elements_by_xpath('//*[@id="STATUS"]'):
                                STATUS = STATUS.get_attribute('innerText').strip()
                                break
                            # CPV
                            global result2
                            for CPV in browser.find_elements_by_xpath('//*[@class="commodity"]'):
                                CPV = CPV.get_attribute('innerText').strip().replace('\n', '')
                                if CPV != "":
                                    copy_cpv = ""
                                    Cpv_status = True
                                    all_string = ""
                                    try:
                                        while Cpv_status == True:
                                            phoneNumRegex = re.compile(r'\d\d\d\d\d\d\d\d')
                                            CPv_main = phoneNumRegex.search(CPV)
                                            mainNumber = CPv_main.groups()
                                            if CPv_main:
                                                copy_cpv = CPv_main.group(), ", "
                                                CPV = CPV.replace(CPv_main.group(), "")
                                            else:
                                                Cpv_status = False
                                            result = "".join(str(x) for x in copy_cpv)
                                            result = result.replace("", "").strip()
                                            result2 = result.replace("\n", "")
                                            # print(result2)
                                            all_string += result2+','
                                    except:
                                        pass
                                    all_string = all_string.replace(',,', ',')
                                    if all_string.endswith(','):
                                        all_string = all_string[:-1]
                                    print(all_string)
                                    SegFeild[36] = all_string
                                else:
                                    SegFeild[36] = ""
                                break
                            CPV = ''
                            for CPV in browser.find_elements_by_xpath('//*[@class="commodity"]'):
                                CPV = CPV.get_attribute('innerText').strip().replace('\n', ', ')
                                break
                            SegFeild[18] = "Agency: " + str(SegFeild[12]) + "<br>\n""Contract Type: " + CONTRACT_TYPE + "<br>\n""Solicitation Number: " + str(SegFeild[13]) + "<br>\n"\
                                            "Status: " + STATUS + "<br>\n""Closing Date Status: " + DATE_STATUS + "<br>\n""DESCRIPTION: " + str(SegFeild[19]) + "<br>\n""BUYER: " + BUYER_ID+"<br>\n""CPV: " + CPV

                            SegFeild[7] = "US"

                            # notice type
                            SegFeild[14] = "2"

                            SegFeild[22] = "0"

                            SegFeild[26] = "0.0"

                            SegFeild[27] = "0"  # Financier

                            SegFeild[28] = browser.current_url

                            # Source Name
                            SegFeild[31] = 'ok.gov'

                            SegFeild[42] = SegFeild[7]  # project_location

                            SegFeild[43] = ''  # set_aside

                            for SegIndex in range(len(SegFeild)):
                                print(SegIndex, end=' ')
                                print(SegFeild[SegIndex])
                                SegFeild[SegIndex] = html.unescape(str(SegFeild[SegIndex]))
                                SegFeild[SegIndex] = str(SegFeild[SegIndex]).replace("'", "''")

                            if len(SegFeild[19]) >= 200:
                                SegFeild[19] = str(SegFeild[19])[:200]+'...'

                            if len(SegFeild[18]) >= 1500:
                                SegFeild[18] = str(SegFeild[18])[:1500]+'...'
                            
                            a = False
                            insert_in_Local(get_htmlSource , SegFeild)
                            print(" Total: " + str(Global_var.Total) + " Duplicate: " + str(
                                Global_var.duplicate) + " Expired: " + str(Global_var.expired) + " Inserted: " + str(
                                Global_var.inserted) + " Skipped: " + str(
                                Global_var.skipped) + " Deadline Not given: " + str(
                                Global_var.deadline_Not_given) + " QC Tenders: " + str(Global_var.QC_Tender), "\n")
                            a = False
                        else:
                            print("Tender Expired")
                            Global_var.expired += 1
                            a = False
                            print(" Total: " + str(Global_var.Total) + " Duplicate: " + str(
                                Global_var.duplicate) + " Expired: " + str(Global_var.expired) + " Inserted: " + str(
                                Global_var.inserted) + " Skipped: " + str(
                                Global_var.skipped) + " Deadline Not given: " + str(
                                Global_var.deadline_Not_given) + " QC Tenders: " + str(Global_var.QC_Tender), "\n")
                    else:
                        print("Deadline was not given")
                        Global_var.deadline_Not_given += 1
                        print(" Total: " + str(Global_var.Total) + " Duplicate: " + str(
                            Global_var.duplicate) + " Expired: " + str(Global_var.expired) + " Inserted: " + str(
                            Global_var.inserted) + " Skipped: " + str(
                            Global_var.skipped) + " Deadline Not given: " + str(
                            Global_var.deadline_Not_given) + " QC Tenders: " + str(Global_var.QC_Tender), "\n")
                        a = False

            ctypes.windll.user32.MessageBoxW(0, "Total: " + str(Global_var.Total) + "\n""Duplicate: " + str(
                Global_var.duplicate) + "\n""Expired: " + str(Global_var.expired) + "\n""Inserted: " + str(
                Global_var.inserted) + "\n""Skipped: " + str(
                Global_var.skipped) + "\n""Deadline Not given: " + str(
                Global_var.deadline_Not_given) + "\n""QC Tenders: " + str(Global_var.QC_Tender) + "",
                                             "ok.gov", 1)
            a = False
            Global_var.Process_End()
            browser.close()
            sys.exit()
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("Error ON : ", sys._getframe().f_code.co_name + "--> " + str(e), "\n", exc_type, "\n", fname, "\n", exc_tb.tb_lineno)
            a = True

    sys.exit()
ChromeDriver()