from fastapi import APIRouter, HTTPException, status, Query
from typing import List
from app.models.chat import ChatMessage, Conversation, ChatMessageCreate
from app.services.chat_service import chat_service

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/messages", response_model=ChatMessage)
async def send_message(
    message_data: ChatMessageCreate,
):
    """Send a chat message (no authentication required)"""
    try:
        # You may want to add a 'sender' field in message_data for identification
        return await chat_service.send_message(message_data.sender_id, message_data)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/conversations", response_model=List[Conversation])
async def get_conversations(
    user_id: str = Query(..., description="User ID for fetching conversations")
):
    """Get user's conversations (no authentication required)"""
    return await chat_service.get_conversations(user_id)

@router.get("/conversations/{conversation_id}/messages")
async def get_conversation_messages(
    conversation_id: str,
    user_id: str = Query(..., description="User ID for fetching messages"),
    limit: int = Query(50, le=100),
    offset: int = Query(0, ge=0)
):
    """Get messages from a conversation (no authentication required)"""
    try:
        messages = await chat_service.get_conversation_messages(
            conversation_id, 
            user_id,
            limit,
            offset
        )
        return {"messages": [msg.dict() for msg in messages]}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.post("/conversations/{conversation_id}/read")
async def mark_conversation_read(
    conversation_id: str,
    user_id: str = Query(..., description="User ID marking conversation as read")
):
    """Mark all messages in conversation as read (no authentication required)"""
    await chat_service.mark_messages_as_read(conversation_id, user_id)
    return {"status": "success"}

@router.get("/online-users")
async def get_online_users():
    """Get list of online users (no authentication required)"""
    from app.services.connection_manager import connection_manager
    online_users = await connection_manager.get_online_users()
    return {"online_users": online_users}