import pytest
from httpx import AsyncClient
from datetime import datetime, timedelta

class TestChatIntegration:
    async def test_send_and_receive_message(self, client: AsyncClient, test_user):
        """Test complete message flow"""
        headers = {"Authorization": f"Bearer {test_user['token']}"}
        
        # Create second user
        user2_data = {
            "username": "testuser2",
            "email": "test2@example.com",
            "password": "testpassword123"
        }
        response = await client.post("/auth/register", json=user2_data)
        user2 = response.json()
        
        # Login second user
        login_data = {"username": "testuser2", "password": "testpassword123"}
        response = await client.post("/auth/token", data=login_data)
        user2_token = response.json()["access_token"]
        
        # Send message
        message_data = {
            "receiver_id": user2["id"],
            "content": {"text": "Hello from user 1!"},
            "message_type": "text"
        }
        
        response = await client.post("/chat/messages", json=message_data, headers=headers)
        assert response.status_code == 200
        
        message = response.json()
        conversation_id = message["conversation_id"]
        
        # Check conversations for both users
        response = await client.get("/chat/conversations", headers=headers)
        assert response.status_code == 200
        conversations = response.json()
        assert len(conversations) == 1
        
        user2_headers = {"Authorization": f"Bearer {user2_token}"}
        response = await client.get("/chat/conversations", headers=user2_headers)
        assert response.status_code == 200
        conversations = response.json()
        assert len(conversations) == 1

class TestCapsuleSharing:
    async def test_share_capsule_workflow(self, client: AsyncClient, test_user):
        """Test complete capsule sharing workflow"""
        headers = {"Authorization": f"Bearer {test_user['token']}"}
        
        # Create capsule
        capsule_data = {
            "title": "Shared Test Capsule",
            "capsule_type": "memory",
            "content": {"message": "This will be shared!"},
            "unlock_date": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
            "tags": ["test", "shared"]
        }
        
        response = await client.post("/capsules/", json=capsule_data, headers=headers)
        assert response.status_code == 200
        capsule = response.json()
        
        # Create second user
        user2_data = {
            "username": "shareuser",
            "email": "share@example.com",
            "password": "sharepass123"
        }
        await client.post("/auth/register", json=user2_data)
        
        # Share capsule
        share_data = {
            "username": "shareuser",
            "permission_level": "view",
            "message": "Check out this capsule!"
        }
        
        response = await client.post(
            f"/capsules/{capsule['id']}/share",
            json=share_data,
            headers=headers
        )
        assert response.status_code == 200
        
        # Login as second user and check shared capsules
        login_data = {"username": "shareuser", "password": "sharepass123"}
        response = await client.post("/auth/token", data=login_data)
        user2_token = response.json()["access_token"]
        user2_headers = {"Authorization": f"Bearer {user2_token}"}
        
        response = await client.get("/capsules/shared", headers=user2_headers)
        assert response.status_code == 200
        shared_capsules = response.json()
        assert len(shared_capsules["shared_capsules"]) == 1
        assert shared_capsules["shared_capsules"][0]["title"] == "Shared Test Capsule"

class TestFriendSystem:
    async def test_friend_request_workflow(self, client: AsyncClient, test_user):
        """Test complete friend request workflow"""
        headers = {"Authorization": f"Bearer {test_user['token']}"}
        
        # Create second user
        user2_data = {
            "username": "frienduser",
            "email": "friend@example.com",
            "password": "friendpass123"
        }
        response = await client.post("/auth/register", json=user2_data)
        user2 = response.json()
        
        # Send friend request
        request_data = {
            "addressee_username": "frienduser",
            "message": "Let's be quantum friends!"
        }
        
        response = await client.post("/friends/request", json=request_data, headers=headers)
        assert response.status_code == 200
        friendship = response.json()
        
        # Login as second user
        login_data = {"username": "frienduser", "password": "friendpass123"}
        response = await client.post("/auth/token", data=login_data)
        user2_token = response.json()["access_token"]
        user2_headers = {"Authorization": f"Bearer {user2_token}"}
        
        # Check friend requests
        response = await client.get("/friends/requests", headers=user2_headers)
        assert response.status_code == 200
        requests = response.json()
        assert len(requests["friend_requests"]) == 1
        
        # Accept friend request
        response = await client.post(
            f"/friends/respond/{friendship['id']}?accept=true",
            headers=user2_headers
        )
        assert response.status_code == 200
        
        # Check friends list
        response = await client.get("/friends/", headers=headers)
        assert response.status_code == 200
        friends = response.json()
        assert len(friends) == 1
        assert friends[0]["username"] == "frienduser"
