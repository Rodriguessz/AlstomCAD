from src.models.autocad_file import AutocadFile

class AutocadController:
  def __init__(self):
        self.autocad_file = AutocadFile();

  def run(self, cabinets):
    """Método que chama a automação"""
    previous_cabs = self.autocad_file.start(cabinets)

    return previous_cabs