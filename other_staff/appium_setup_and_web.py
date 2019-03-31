from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
 
# MAIN DOC of desired_caps https://nishantverma.gitbooks.io/appium-for-android/understanding_desired_capabilities.html

""" Mini Guide Appium Python Selenium 
1 Install JDK
2 Setup JAVA_HOME
3 Install Android studio
4 Setup ANDROID_HOME
5 Install Appium and Python module >> pip install Appium-Python-Client
6 Install drivers for android xx versions and adb device driver
7 Check adb devices (if need write device id in %HOMEPATH%\.android   adb_usb.ini > 0x<device id>)
8 Setup desired_caps in script
9 Install Chrome on phone
10 Launch Appium server and insert adress in webdriver >> driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
11 Try to launch script

IMPORTANT! Make sure that your Chromedriver compatible with Chrome browser installed on phone . URL for solution: http://appium.io/docs/en/writing-running-appium/web/chromedriver/

Data:
ANDROID_HOME = C:\Users\User\AppData\Local\Android\Sdk\
JAVA_HOME = C:\Program Files\Java\jdk-10.0.1\bin
Full_path = %JAVA_HOME%;C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\Program Files (x86)\Python36-32\Scripts\;
C:\Program Files (x86)\Python36-32\;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;
C:\Program Files (x86)\Skype\Phone\;C:\Program Files (x86)\Intel\OpenCL SDK\2.0\bin\x86;C:\Program Files (x86)\Intel\OpenCL SDK\2.0\bin\x64;
C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;C:\Program Files\Git\cmd;C:\Program Files\Git\mingw64\bin;C:\Program Files\Git\usr\bin;
C:\Program Files (x86)\Python36-32\lib\site-packages\pytesseract;C:\Program Files\Java\jdk-10.0.1\bin;C:\Program Files\Java\jdk-10.0.1;
C:\Users\User\AppData\Local\Android\Sdk\platform-tools;%ANDROID_HOME%/platform-tools;%ANDROID_HOME%/tools

HZ >> on phone > appium settings and Unloock > Thought that install in first appium launch !?

selen-appium doc http://appium.io/docs/en/about-appium/api/


SETTINGS FOR APPIUM INSPECTOR

{
  "deviceName": "MEIZU 16",
  "platformName": "Android",
  "platformVersion": "8.1.0",
  "app": "http://localhost:8000/APK_Info_v1.2.11_apkpure.com.apk"
}

for app, you can up http server:
python -m http.server 8000

"""


 
desired_caps = {
    "deviceName": "Meizu",
	"browserName": "Chrome",
	"platformName": "Android",
    "platformVersion": "5.1"
}

#AndroidDriver
 
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

driver.get("https://price.ua")
time.sleep(2)

select_block = driver.find_element_by_xpath('//*[@id="main-categories-menu"]/li[1]/a')
select_block.click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-categories-menu"]/li[1]/div/div/ul/li[1]/a')))
mobile_phones = driver.find_element_by_xpath('//*[@id="main-categories-menu"]/li[1]/div/div/ul/li[1]/a')
mobile_phones.click()

time.sleep(8)


 
driver.quit()
