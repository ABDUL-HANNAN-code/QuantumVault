from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum

class MessageType(str, Enum):
    TEXT = "text"
    IMAGE = "image"
    CAPSULE_SHARE = "capsule_share"
    QUANTUM_STATE = "quantum_state"

class MessageStatus(str, Enum):
    SENT = "sent"
    DELIVERED = "delivered"
    READ = "read"

class ChatMessage(BaseModel):
    id: Optional[str] = None
    conversation_id: str
    sender_id: str
    receiver_id: Optional[str] = None  # None for group chats
    message_type: MessageType
    content: Dict[str, Any]
    timestamp: datetime = datetime.utcnow()
    status: MessageStatus = MessageStatus.SENT
    edited_at: Optional[datetime] = None
    reply_to: Optional[str] = None

class Conversation(BaseModel):
    id: Optional[str] = None
    participants: List[str]
    conversation_type: str = "private"  # private, group
    title: Optional[str] = None
    created_at: datetime = datetime.utcnow()
    last_message_at: datetime = datetime.utcnow()
    quantum_encrypted: bool = False

class ChatMessageCreate(BaseModel):
    receiver_id: Optional[str] = None
    conversation_id: Optional[str] = None
    message_type: MessageType = MessageType.TEXT
    content: Dict[str, Any]
    reply_to: Optional[str] = None
