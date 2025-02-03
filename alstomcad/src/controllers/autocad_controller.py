from src.models.autocad_file import AutocadFile

class AutocadController:
  def __init__(self):
        self.autocad_file = AutocadFile();

  def run(self):
    """Método que chama a automação"""
    self.autocad_file.start()