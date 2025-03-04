from pathlib import Path;
import win32com.client
from src.utils.helper import getRelayInfos
from colorama import Fore, Back, Style
class AutocadFile:
  def __init__(self):
    self.autocad = win32com.client.Dispatch("AutoCad.Application").ActiveDocument
    self.base_dir = Path(__file__).parent.parent.parent.resolve();
    self.file_name =  self.autocad.name
    self.file_path = self.base_dir / "autocad_draws" / self.file_name
  
  def start(self, prev_cabs):
     
     if not self.file_path.exists():
       raise FileNotFoundError(f"O arquivo {self.file_path} não foi encontrado.")
     print(Fore.GREEN,f"Iniciando automação para {self.file_name}")
     
     cabinets = { "08": [], "09": []}
     cab_limits = {
       "08": {'x_min': 32.5249, 'x_max': 417.0879, 'y_min': 583.1531, 'y_max': 81.6581},
       "09": {'x_min': 439.3269, 'x_max': 823.8899, 'y_min': 583.1531, 'y_max': 81.6581}
     }

     for object in self.autocad.modelSpace:
       if(object.EntityName == 'AcDbBlockReference'):
         if(object.name == 'RELE' and object.HasAttributes):
            # Object Position
            x, y, z = object.insertionPoint

            for cab in cab_limits.keys():
              if(x >= cab_limits[cab]["x_min"] and x <= cab_limits[cab]["x_max"]):
                relay = getRelayInfos(object, cab)
                cabinets[cab].append(relay)
                break
      
      
     print(Fore.YELLOW, "Gabinets successful analised! Returning infos... ")
     
     return cabinets
      

      
                



    
