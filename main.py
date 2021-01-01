import requests
import random
import time
import plyer

# parameters
from_patch = 199
to_patch = 200
url = "https://download-maple.playpark.net/manual/" \
  + "MaplePatch" + str(from_patch) + "to" + str(to_patch) + ".exe"
min_wait = 300
max_wait = 600
use_notification = True

print("Checking if manual patch on URL " + url + " is available...")
print()

while True:
  req = requests.head(url)

  print("==================================================================")
  print("Time of attempt: " + req.headers["Date"])
  if req.headers["Content-Type"] != "application/x-msdownload":
    print("Patch not uploaded yet, will try again after a random interval.")
    wait_time = random.randint(min_wait, max_wait)
    print("Will retry after " + str(wait_time) + " seconds.")
    print("Sleeping...")
    print()
    time.sleep(wait_time)
  else:
    print("Patch is available now.")
    print("Link: " + url)
    if use_notification: 
      plyer.notification.notify(title="maplesea-patchpoke", 
        message="Patch is on the server!", timeout=0)
    print("Press Enter to exit...")
    input()
    break