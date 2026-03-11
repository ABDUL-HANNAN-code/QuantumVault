from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class QuantumCircuit(BaseModel):
    id: Optional[str] = None
    user_id: str
    name: str
    qasm_code: str
    description: Optional[str] = None
    created_at: datetime = datetime.utcnow()

class QuantumMeasurement(BaseModel):
    id: Optional[str] = None
    circuit_id: str
    user_id: str
    result: Dict[str, Any]
    executed_at: datetime = datetime.utcnow()
