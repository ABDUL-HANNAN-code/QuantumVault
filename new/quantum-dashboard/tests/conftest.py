import pytest
import asyncio
from httpx import AsyncClient
from app.main import app
from app.database import get_database, connect_to_mongo, close_mongo_connection
import os

# Set test environment
os.environ["DATABASE_NAME"] = "quantum_dashboard_test"
os.environ["JWT_SECRET_KEY"] = "test-secret-key"

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def setup_database():
    """Setup test database."""
    await connect_to_mongo()
    yield
    await close_mongo_connection()

@pytest.fixture
async def client(setup_database):
    """Create test client."""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.fixture
async def test_user(client):
    """Create a test user."""
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword123",
        "full_name": "Test User"
    }
    
    response = await client.post("/auth/register", json=user_data)
    assert response.status_code == 200
    
    # Login to get token
    login_data = {
        "username": "testuser",
        "password": "testpassword123"
    }
    
    response = await client.post("/auth/token", data=login_data)
    token_data = response.json()
    
    return {
        "user": response.json(),
        "token": token_data["access_token"]
    }
