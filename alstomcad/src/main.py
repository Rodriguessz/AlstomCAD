from src.controllers.autocad_controller import AutocadController
from src.utils.helper import getModDate
from src.utils.helper import getDiffs

from colorama import Fore, Back, Style
import time

try:
   
  # Current Autocad file
  autocad = AutocadController()

  # Modification Date
  last_mod_date = getModDate(autocad.autocad_file.file_path)

  #Previous Cabinets
  previous_cabinets = autocad.run([]);
  
  while True:
      time.sleep(5)
      new_mod_date = getModDate(autocad.autocad_file.file_path)

      if new_mod_date != last_mod_date:
        print(Fore.GREEN, "-------------> File has been modified  <-------------")
        new_cabinets = autocad.run(previous_cabinets)
        diffs = getDiffs(previous_cabinets, new_cabinets)
        print(diffs)

        previous_cabinets = new_cabinets;
        last_mod_date = new_mod_date;
      else:
        print(Fore.RED, "-------------> File has not been modified  <-------------")

except FileNotFoundError as error:
      print(Fore.RED, "-------------> Erro: Arquivo não encontrado  <-------------")
      print(Fore.RED, "Por favor, abra um arquivo  CAD!")

except AttributeError as e:
      print(Fore.RED, "-------------> Erro: Atributo não encontrado  <-------------")
      print(Fore.RED, "Por favor, feche a edição de atributos!")





      

  
  

  
