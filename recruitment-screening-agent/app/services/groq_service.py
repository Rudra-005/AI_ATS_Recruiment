from groq import Groq
import json
import time
from typing import Dict, Any
from app.config import Config

class GroqService:
    def __init__(self):
        self.client = Groq(api_key=Config.GROQ_API_KEY)
    
    def chat_completion(self, prompt: str, max_retries: int = 3) -> Dict[str, Any]:
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=Config.GROQ_MODEL,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=Config.MAX_TOKENS,
                    temperature=Config.TEMPERATURE
                )
                
                content = response.choices[0].message.content.strip()
                
                # Try to parse JSON
                try:
                    return json.loads(content)
                except json.JSONDecodeError:
                    # Extract JSON from markdown code blocks
                    if "```json" in content:
                        json_start = content.find("```json") + 7
                        json_end = content.find("```", json_start)
                        content = content[json_start:json_end].strip()
                    elif "```" in content:
                        json_start = content.find("```") + 3
                        json_end = content.find("```", json_start)
                        content = content[json_start:json_end].strip()
                    else:
                        # Try to find JSON object
                        json_start = content.find('{')
                        json_end = content.rfind('}') + 1
                        if json_start != -1 and json_end > json_start:
                            content = content[json_start:json_end]
                    
                    return json.loads(content)
                
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON from Groq: {str(e)}")
            except Exception as e:
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                raise Exception(f"Groq API error: {str(e)}")
    
    def load_prompt(self, prompt_file: str, **kwargs) -> str:
        with open(f"app/prompts/{prompt_file}", 'r') as f:
            return f.read().format(**kwargs)