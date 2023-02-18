#import openai
from enum import StrEnum
import keys

# Prompt Example: "<lamp1, lamp3, ceiling>, Change color to green\n\n"
# Response Example: " <all> #00FF00\n"

class Selection(StrEnum):
    ALL = 'all'
    NONE = 'none'

class Command(StrEnum):
    ON = 'on'
    OFF = 'off'

class Lights:
    def __init__(self, lights_list):
        self.lights = {light: (0, 0, 0) for light in lights_list}

    def make_prompt(self, command):
        prompt_lights = f"<{', '.join(self.lights.keys())}>"
        prompt = f"{prompt_lights}, {command}\n\n"
        return prompt

print(Lights(['lamp1', 'lamp3', 'ceiling']).make_prompt('Change color to green'))
    