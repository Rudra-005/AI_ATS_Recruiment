import openai
import json
import time
from typing import Dict, Any, List
from app.config import Config

class OpenAIService:
    def __init__(self):
        self.client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
    
    def chat_completion(self, prompt: str, max_retries: int = 3) -> Dict[str, Any]:
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=Config.OPENAI_MODEL,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=Config.MAX_TOKENS,
                    temperature=Config.TEMPERATURE,
                    timeout=30
                )
                
                content = response.choices[0].message.content.strip()
                return json.loads(content)
                
            except (openai.RateLimitError, openai.APITimeoutError) as e:
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                raise Exception(f"OpenAI API error: {str(e)}")
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON response from OpenAI")
            except Exception as e:
                raise Exception(f"OpenAI API error: {str(e)}")
    
    def generate_embedding(self, text: str, max_retries: int = 3) -> List[float]:
        for attempt in range(max_retries):
            try:
                response = self.client.embeddings.create(
                    model=Config.EMBEDDING_MODEL,
                    input=text,
                    timeout=30
                )
                return response.data[0].embedding
                
            except (openai.RateLimitError, openai.APITimeoutError) as e:
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                raise Exception(f"Embedding API error: {str(e)}")
            except Exception as e:
                raise Exception(f"Embedding API error: {str(e)}")
    
    def load_prompt(self, prompt_file: str, **kwargs) -> str:
        with open(f"app/prompts/{prompt_file}", 'r') as f:
            return f.read().format(**kwargs)