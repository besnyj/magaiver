from dataclasses import dataclass
from typing import List, Dict, Literal

@dataclass
class ChatMessage:
    role: Literal["system", "user", "assistant"]
    content: str

@dataclass
class ChatConfig:
    model: Literal["gemma3:27b",
    "gemma3:12b",
    "gemma2:27b",
    "mistral-small3.1:24b",
    "deepseek-r1:32b",
    "qwen3:32b",
    "phi4-reasoning:14b"]
    messages: List[ChatMessage]
    stream: bool = True
    think: bool = False
