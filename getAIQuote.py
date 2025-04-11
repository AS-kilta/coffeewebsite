from random import randrange, seed
import portalocker
import aiohttp
import asyncio
from decouple import config

OLLAMA_URL = config('OLLAMA_URL')

THOUGHTS_PATH = config("THOUGHTS_PATH")

async def ai_quote():
    # Define the payload
    prompt = "These are the quotes so far:\n\n"

    num_lines = randrange(11, 15)
    try:
        with portalocker.Lock(THOUGHTS_PATH, 'r') as output_file:
            lines = output_file.readlines()
            prompt += "\n".join(lines[-num_lines:])
    except:
        print("ei oo filee")
        prompt += "No quotes so far in ASki.\n"

    data = {
        "model": "aski-llm",
        "prompt": prompt,
        "stream": False  # Set to True for streaming response
    }

    timeout = aiohttp.ClientTimeout(total=60)  # 60 seconds timeout

    async with aiohttp.ClientSession(timeout=timeout) as session:
        try: 
            async with session.post(OLLAMA_URL, json=data) as response:
                if response.status == 200:
                    result = await response.json()
                    return result["response"]
                else:
                    return "The AI seems to be sleeping.."
        except asyncio.TimeoutError:
            return "The AI was too slow.."
