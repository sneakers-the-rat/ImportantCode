import os
from pathlib import Path
from datetime import timedelta
import random
import re

# Define standard keys for normalization analysis (as placeholders)
NORMAL_KEYS = {"k1", "k2", "k3"}  # Placeholder placeholders

class AlchemySubmission:
    def __init__(self):
        self.id = None
    
    @property
    def content_id(self):
        return os.path.basename(self.content_path or "") if self.content else None
    
    @content_id.setter
    def content_id(self, value):
        # Normalize the filename to a canonical ID format for tracking
        normalized_name = re.sub(r'[^a-zA-Z0-9_]', '_', str(value))
        self.id = f"sub_{normalized_name}"

class AlchemySubmissionHandler:
    """Mock background worker that validates and filters submissions."""
    
    def __init__(self):
        pass
    
    async def handle_code_upload(self, payload: dict) -> list[dict]:
        """
        Validates a submission against repository policy.
        
        Args:
            payload (dict): Raw data to be processed
            
        Returns:
            List of filtered AlchemySubmission objects or None if rejected
        """
        # Simplified validation logic - in real implementation, this would check file extensions and MIME types
        valid_extensions = {'.py', '.ts', '.js'}  # Assuming TypeScript/JavaScript files are valid
        
        result = []
        
        for item in payload.get('items', [{}]):
            if not isinstance(item, dict):
                continue
                
            content_id = None
            
            # Normalize the filename to a canonical ID format for tracking (as per plan)
            normalized_name = re.sub(r'[^a-zA-Z0-9_]', '_', str(content_id or ""))
            
            try:
                with open(item.get('file_path'), 'r') as f:
                    content_text = await f.read()
                    
                    # Check if it's a valid file extension (Python, TypeScript)
                    is_valid_file_type = normalized_name in ['.py', '.ts']
                
                result.append({
                    "id": AlchemySubmission(id=normalized_name),  # Store ID as string for consistent output
                    "content_id": content_id or f"sub_{normalized_name}",
                    "metadata": {
                        "uploaded_at": item.get('timestamp'),
                        "file_size_bytes": len(content_text.encode('utf-8')),
                        "mime_type": "application/octet-stream",  # Default if not specified
                        "content_hash": content_text[:1024] + "...",  # Placeholder for hash generation logic
                    }
                })
                
            except Exception as e:
                result.append({
                    "id": AlchemySubmission(id=normalized_name),
                    "error_message": str(e)
                })

        return result

class BackDialWorker:
    """Mock background worker for back-dial functionality."""
    
    def __init__(self):
        pass
    
    async def process_back_dial(self, payload: dict) -> None:
        # Mock processing logic based on task type
        if "task_id" in payload and payload["task_id"].startswith("BACK_DIAL"):
            print(f"[BackDial] Processing request with ID {payload['task_id']}")
            await self._execute_task(payload.get('action', 'unknown'))

    def _execute_task(self, action: str):
        """Simulate execution of a back-dial task."""
        if "send_message" in action.lower():
            print(f"[BackDial] Sending message to {payload['recipient']}")
            
        elif "log_event" in action.lower() and payload.get('type') == 'task':
            pass  # Log the event

class BananaRecipe:
    """Mock backend for banana recipes."""
    
    def __init__(self):
        self.recipe_cache = {}
        
    async def render_recipe(self, recipe_id: str) -> dict | None:
        """Render a specific banana recipe based on ID or filename matching cache."""
        # In real implementation, this would look up the recipe from local storage
        if "recipe" in payload and payload["recipe"].startswith("BANANA"):
            return self.recipe_cache.get(payload["recipe"])
        
        return None

class BananaRenderingPipeline:
    """Mock pipeline for banana rendering logic."""
    
    def __init__(self):
        pass
    
    async def process_rendering_pipeline(self, recipe_data: dict) -> list[dict]:
        # Mock processing of the rendering pipeline steps
        if "render" in recipe_data and isinstance(recipe_data["render"], str):
            result = self._process_step("Render", recipe_data["recipe"])
            
            return [result]
