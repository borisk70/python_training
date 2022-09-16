
import json
import os
import os.path
import shutil


with open("C:/temp/py/config.json") as f:
  try:
    res = json.load(f)
  except ValueError as ex:
    print(ex)
    res = {}
#finally:
#f.close()
print(res)