import pytest
from httpx import AsyncClient
from datetime import datetime, timedelta

class TestAuthentication:
    async def test_user_registration(self, client: AsyncClient):
        """Test user registration"""
        user_data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "password123",
            "full_name": "New User"
        }
        
        response = await client.post("/auth/register", json=user_data)
        assert response.status_code == 200
        
        data = response.json()
        assert data["username"] == "newuser"
        assert data["email"] == "newuser@example.com"
        assert "id" in data

    async def test_user_login(self, client: AsyncClient):
        """Test user login"""
        # First register a user
        user_data = {
            "username": "loginuser",
            "email": "loginuser@example.com",
            "password": "password123"
        }
        await client.post("/auth/register", json=user_data)
        
        # Then login
        login_data = {
            "username": "loginuser",
            "password": "password123"
        }
        
        response = await client.post("/auth/token", data=login_data)
        assert response.status_code == 200
        
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"

class TestTemporalCapsules:
    async def test_create_capsule(self, client: AsyncClient, test_user):
        """Test creating a temporal capsule"""
        headers = {"Authorization": f"Bearer {test_user['token']}"}
        
        capsule_data = {
            "title": "Test Capsule",
            "description": "A test temporal capsule",
            "capsule_type": "memory",
            "content": {"message": "Hello from the past!"},
            "unlock_date": (datetime.utcnow() + timedelta(days=1)).isoformat(),
            "tags": ["test", "memory"]
        }
        
        response = await client.post("/capsules/", json=capsule_data, headers=headers)
        assert response.status_code == 200
        
        data = response.json()
        assert data["title"] == "Test Capsule"
        assert data["status"] == "locked"

    async def test_get_user_capsules(self, client: AsyncClient, test_user):
        """Test retrieving user capsules"""
        headers = {"Authorization": f"Bearer {test_user['token']}"}
        
        response = await client.get("/capsules/", headers=headers)
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)

class TestQuantumOperations:
    async def test_create_quantum_circuit(self, client: AsyncClient, test_user):
        """Test creating a quantum circuit"""
        headers = {"Authorization": f"Bearer {test_user['token']}"}
        
        circuit_data = {
            "circuit_name": "Bell State",
            "qasm_code": """OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
creg c[2];
h q[0];
cx q[0],q[1];
measure q -> c;""",
            "description": "Simple Bell state circuit"
        }
        
        response = await client.post("/quantum/circuits", json=circuit_data, headers=headers)
        assert response.status_code == 200
        
        data = response.json()
        assert data["circuit_name"] == "Bell State"
        assert data["qubit_count"] == 2

    async def test_image_analysis(self, client: AsyncClient, test_user):
        """Test quantum image analysis"""
        headers = {"Authorization": f"Bearer {test_user['token']}"}
        
        # Create a simple base64 encoded test image (1x1 pixel)
        test_image_data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/PchI7wAAAABJRU5ErkJggg=="
        
        analysis_data = {
            "image_data": test_image_data,
            "analysis_type": "basic"
        }
        
        response = await client.post("/quantum/image-analysis", json=analysis_data, headers=headers)
        assert response.status_code == 200
        
        data = response.json()
        assert data["success"] == True
        assert "pixel_entropy" in data
