from openai import OpenAI
from database import save_script
import logging

def generate_voiceover_script(niche):
    client = OpenAI()
    try:
        response = client.Completion.create(engine="davinci", prompt=f"Generate a unique voiceover script for {niche}", max_tokens=500)
        script = response.choices[0].text.strip()
        save_script(niche, script)
        logging.info(f"Script saved for {niche}")
        return script
    except Exception as e:
        logging.error(f"Error generating script for {niche}: {e}")
        raise