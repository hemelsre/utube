from openai import OpenAI
from database import save_script

def generate_voiceover_script(niche):
    client = OpenAI()
    response = client.Completion.create(engine="davinci", prompt=f"Generate a unique voiceover script for {niche}", max_tokens=500)
    script = response.choices[0].text.strip()
    save_script(niche, script)
    return script

