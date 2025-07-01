from dataclasses import dataclass
from typing import List, Dict, Literal

@dataclass
class ChatMessage:
    role: Literal["system", "user", "assistant"]
    content: str

@dataclass
class ChatConfig:
    model: Literal["gemma3:27b",
    "llama3.3:70b"]
    messages: List[ChatMessage]
    stream: bool = True
    think: bool = False
