import pytest
from datetime import datetime, timedelta
from app.models.chat import ChatMessage, Conversation, MessageType
from app.models.friendship import Friendship, FriendshipStatus
from app.models.permissions import CapsulePermission, PermissionLevel

class TestChatModels:
    def test_chat_message_creation(self):
        """Test ChatMessage model creation"""
        message = ChatMessage(
            conversation_id="conv123",
            sender_id="user123",
            receiver_id="user456",
            message_type=MessageType.TEXT,
            content={"text": "Hello world"}
        )
        
        assert message.conversation_id == "conv123"
        assert message.sender_id == "user123"
        assert message.message_type == MessageType.TEXT
        assert message.content["text"] == "Hello world"
    
    def test_conversation_creation(self):
        """Test Conversation model creation"""
        participants = ["user123", "user456"]
        
        conversation = Conversation(
            participants=participants,
            conversation_type="private"
        )
        
        assert conversation.participants == participants
        assert conversation.conversation_type == "private"
        assert isinstance(conversation.created_at, datetime)

class TestFriendshipModels:
    def test_friendship_creation(self):
        """Test Friendship model creation"""
        friendship = Friendship(
            requester_id="user123",
            addressee_id="user456",
            status=FriendshipStatus.PENDING
        )
        
        assert friendship.requester_id == "user123"
        assert friendship.addressee_id == "user456"
        assert friendship.status == FriendshipStatus.PENDING

class TestPermissionModels:
    def test_capsule_permission_creation(self):
        """Test CapsulePermission model creation"""
        permission = CapsulePermission(
            capsule_id="capsule123",
            owner_id="owner123",
            shared_with_user_id="user456",
            permission_level=PermissionLevel.VIEW
        )
        
        assert permission.capsule_id == "capsule123"
        assert permission.owner_id == "owner123"
        assert permission.permission_level == PermissionLevel.VIEW
