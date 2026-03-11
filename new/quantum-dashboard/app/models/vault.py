from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime

class VaultItem(BaseModel):
    id: Optional[str] = None
    user_id: str
    item_type: str
    item_data: Dict[str, Any]
    access_permissions: List[str] = []
    created_at: datetime = datetime.utcnow()
