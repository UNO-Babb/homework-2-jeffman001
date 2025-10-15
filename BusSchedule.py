#BusSchedule.py
#Name:
#Date:
#Assignment:

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def loadURL(url):
  """
  This function loads a given URL and returns the text
  that is displayed on the site. It does not return the
  raw HTML code but only the code that is visible on the page.
  """

  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument("--headless");
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(url)
  content=driver.find_element(By.XPATH, "/html/body").text
  driver.quit()

  return content

def loadTestPage():
  """
  This function returns the contents of our test page.
  This is done to avoid unnecessary calls to the site
  for our testing.
  """
  page = open("testPage.txt", 'r')
  contents = page.read()
  page.close()

  return contents

def isTime(time):
  value = 0
  for ch in time:
    if ch == "A" or ch == "P":
          value = value + 1
    if ch == "M":
          value = value + 1
    if ch == ":":
      value = value + 1
  if value == 3:
    return time
  else:
     return False


def getTimes():
  busTimes = open("testPage.txt", "r")
  #making a list for times
  timeList = [ ]

  
  for line in busTimes:
    word = line.split()
    #print(word)
    for wrd in word:
      if isTime(wrd) != False:
         timeList.append(isTime(wrd))
        
  #print(timeList)
  return timeList

def isPastNoon(input):
  for ch in input:
     if ch == "P":
        #print("tru")
        return True
     
def getHoursdatetime(H):
   hours = H.split(":")[0]
   if isPastNoon(H) == True:
      hours = int(hours) + 12
   hours = (int(hours) - 5 + 24) % 24
   #print(hours)
   return hours

def getHours(H):
   hours = H.split(":")[0]
   if isPastNoon(H) == True:
      hours = int(hours) + 12
   hours = int(hours)
   #print(hours)
   return hours

def getMin(M):
   min = M.split(":")[1]
   min = min.replace("A" , "")
   min = min.replace("P" , "")
   min = min.replace("M" , "")
   #print(min)
   return min

def timeInMin(aMpM):  #gets time in minutes
   totalmin = (getHours(aMpM) * 60) + int(getMin(aMpM))
   #print(getHours(aMpM))
   return totalmin
   
   

def isPastNow(testtime):
   wow = datetime.now() 
   now = wow.strftime("%I:%M %p")
   baseTime = (str(getHoursdatetime(now)) + ":" + getMin(now))
   current = timeInMin(baseTime)
   check = timeInMin(testtime)
   #print(current)
   #print(check)
   if current < check: 
      new = check - current
      return new
   else:
      return False
   


  
  

      
def main():
  wow = datetime.now() 
  now = wow.strftime("%I:%M %p")
  #print(now)
  baseTime = (str(getHoursdatetime(now)) + ":" + getMin(now))
  #print("Orbit Dodge route, stop= 6023, route#00, 92 dodge Express, stop code 3273, route #92, 2269 11")
  stopCode= input("StopCode: ")
  rteNum= input("Route #: ")
  direction= input("EAST or WEST: ")
  print("The current time is ", baseTime)
  url = "https://myride.ometro.com/Schedule?stopCode="+ stopCode + "&routeNumber=" + rteNum + "&directionName=" + direction
  #c1 = loadURL(url) #loads the web page
  #c1 = loadTestPage() #loads the test page
  #print(c1)
  #t = getTimes()
  #print(currentTime)
  timecheck = 0
  for tme in getTimes():
    if isPastNow(tme) != False:
      print("A bus is arriving in", isPastNow(tme), "minutes")
      timecheck = timecheck + 1
      if timecheck == 2:
        return

        


main()
