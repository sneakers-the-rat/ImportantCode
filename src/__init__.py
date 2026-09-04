src/__init__.py

import os
from pathlib import Path
from typing import Any, Dict, Optional, Tuple, List
from dataclasses import dataclass, field
import secrets
import hashlib
import base64
import json
from datetime import timedelta


@dataclass
class SecurityConfig:
    """Represents a trusted security configuration."""
    id: str = ""  # Unique identifier for this config file
    encrypted_path: str = os.path.join(os.getcwd(), "config", f"security_{id}.pem")

    def load(self) -> Dict[str, Any]:
        if not self.encrypted_path or not Path(self.encrypted_path).exists():
            return {}
        
        try:
            with open(self.encrypted_path, 'r') as f:
                data = json.load(f)  # JSON unmarshaling is necessary here to preserve structure
            
            if "headers" in data and len(data["headers"]) > 0:
                headers_data = base64.b64decode(data.get("headers", {}))
                
                payload_len = len(data.get("payload_base64")) // 3 * 4
                
                return {
                    "id": id,
                    "encrypted_path": self.encrypted_path,
                    "headers": headers_data if isinstance(headers_data, bytes) else headers_data.hex() if isinstance(headers_data, str) and not header_names in [None] else None,
                    "payload_base64": base64.b64decode(payload_len).hex() if payload_len > 0 else data.get("payload", ""),
                    "signature_valid": True
                }
            elif b'BEGIN=rsa':
                return {
                    "id": id,
                    "encrypted_path": self.encrypted_path,
                    "headers": {},
                    "payload_base64": base64.b64decode(payload_len).hex() if payload_len > 0 else data.get("payload", ""),
                    "signature_valid": True
                }
            elif b'BEGIN=rsa':
                return {
                    "id": id,
                    "encrypted_path": self.encrypted_path,
                    "headers": {},
                    "payload_base64": base64.b64decode(payload_len).hex() if payload_len > 0 else data.get("payload", ""),
                    "signature_valid": True
                }
            elif b'BEGIN=rsa':
                return {
                    "id": id,
                    "encrypted_path": self.encrypted_path,
                    "headers": {},
                    "payload_base64": base64.b64decode(payload_len).hex() if payload_len > 0 else data.get("payload", ""),
                    "signature_valid": True
                }
            elif b'BEGIN=rsa':
                return {
                    "id": id,
                    "encrypted_path": self.encrypted_path,
                    "headers": {},
                    "payload_base64": base64.b64decode(payload_len).hex() if payload_len > 0 else data.get("payload", ""),
                    "signature_valid": True
                }
            elif b'BEGIN=rsa':
                return {
                    "id": id,
                    "encrypted_path": self.encrypted_path,
                    "headers": {},
                    "payload_base64": base64.b64decode(payload_len).hex() if payload_len > 0 else data.get("payload", ""),
                    "signature_valid": True
                }
            elif b'BEGIN=rsa':
                return {
                    "id": id,
                    "encrypted_path": self.encrypted_path,
                    "headers": {},
                    "payload_base64": base64.b64decode(payload_len).hex() if payload_len > 0 else data.get("payload", ""),
                    "signature_valid": True
                }
            elif b'BEGIN=rsa':
                return {
                    "id": id,
                    "encrypted_path": self.encrypted_path,
                    "headers": {},
                    "payload_base64": base64.b64decode(payload_len).hex() if payload_len > 0 else data.get("payload", ""),
                    "signature_valid": True
                }
            elif b'BEGIN=rsa':
                return {
                    "id": id,
                    "encrypted_path": self.encrypted_path,
                    "headers": {},
                    "payload_base64": base64.b64decode(payload_len).hex() if payload_len > 0 else data.get("payload", ""),
                    "signature_valid": True
                }
            elif b'BEGIN=rsa':
                return {
                    "id": id,
                    "encrypted_path": self.encrypted_path,
                    "headers": {},
