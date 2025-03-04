from src.controllers.autocad_controller import AutocadController
from src.utils.helper import getModDate
from src.utils.helper import getDiffs


from colorama import Fore, Back, Style
import time


# Current Autocad file
autocad = AutocadController()

# Modification Date
last_mod_date = getModDate(autocad.autocad_file.file_path)

#Previous Cabinets
previous_cabinets = []
previous_cabinets = autocad.run(previous_cabinets);

while True:
    

    time.sleep(5)
    new_mod_date = getModDate(autocad.autocad_file.file_path)

    if new_mod_date != last_mod_date:
      print(Fore.GREEN, "-------------> File has been modified  <-------------")
      new_cabinets = autocad.run(previous_cabinets)
      teste = getDiffs(previous_cabinets, new_cabinets)

      print(teste)

      previous_cabinets = new_cabinets;
      last_mod_date = new_mod_date;
    else:
      print(Fore.RED, "-------------> File has not been modified  <-------------")

      

  
  

  
