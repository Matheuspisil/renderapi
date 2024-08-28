import requests
import json
from typing import Optional
import warnings

try:
    from langflow.load import upload_file
except ImportError:
    warnings.warn("Langflow provides a function to help you upload files to the flow. Please install langflow to use it.")
    upload_file = None

BASE_API_URL = "http://127.0.0.1:7860"
FLOW_ID = "cb38a8f6-24e0-4e89-b93e-df8b357baae9"
ENDPOINT = ""  # Pode ser configurado nas configurações do fluxo

# Personalize o fluxo com tweaks, se necessário
TWEAKS = {
    "Prompt-gPuw2": {},
    "ChatInput-yraYc": {},
    "OpenAIModel-kAh9o": {},
    "ChatOutput-nxwxd": {},
    "Memory-TmAlx": {},
    "UpdateData-ah4sm": {}
}

def run_flow(message: str,
             endpoint: str = FLOW_ID,
             output_type: str = "chat",
             input_type: str = "chat",
             tweaks: Optional[dict] = None,
             api_key: Optional[str] = None) -> dict:
    """
    Executa o fluxo do Langflow com uma mensagem dada e ajustes opcionais.
    
    :param message: Mensagem a ser enviada para o fluxo
    :param endpoint: O ID ou o nome do endpoint do fluxo
    :param tweaks: Ajustes opcionais para customizar o fluxo
    :param api_key: Chave da API para autenticação
    :return: Resposta em JSON do fluxo
    """
    api_url = f"{BASE_API_URL}/api/v1/run/{endpoint}"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if api_key:
        headers = {"x-api-key": api_key}

    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

# Esta função foi adaptada para ser chamada na sua view Django
