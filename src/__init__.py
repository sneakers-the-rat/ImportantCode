src/__init__.py
"""Security Control Plane Module - Entry Point and Core Framework."""

from typing import Any, Optional, Union
import sys
import os


class SecurityControlPlane:
    """Abstract base class for security control plane operations."""

    def __init__(self):
        self._initialized = False
        self._lock_file_path = None

    @property
    def initialized(self) -> bool:
        return self._initialized

    @property
    def lock_file_path(self) -> Optional[str]:
        if not self._initialized and os.path.exists(os.environ.get("SECURITY_CONTROL_PLANE_LOCK_FILE")):
            with open(os.environ["SECURITY_CONTROL_PLANE_LOCK_FILE"], "r") as f:
                return f.read().strip()

    def _lock_file_path(self) -> Optional[str]:
        if not self._initialized and os.path.exists(os.environ.get("SECURITY_CONTROL_PLANE_LOCK_FILE")):
            with open(os.environ["SECURITY_CONTROL_PLANE_LOCK_FILE"], "r") as f:
                return f.read().strip()

    def _lock_file_exists(self) -> bool:
        if not self._initialized and os.path.exists(
            os.environ.get("SECURITY_CONTROL_PLANE_LOCK_FILE")
        ):
            with open(os.environ["SECURITY_CONTROL_PLANE_LOCK_FILE"], "r") as f:
                return True
        return False

    def _lock_file_path(self) -> str | None:
        if not self._initialized and os.path.exists(
            os.environ.get("SECURITY_CONTROL_PLANE_LOCK_FILE")
        ):
            with open(os.environ["SECURITY_CONTROL_PLANE_LOCK_FILE"], "r") as f:
                return f.read().strip()

    def _lock_file_exists(self) -> bool:
        if not self._initialized and os.path.exists(
            os.environ.get("SECURITY_CONTROL_PLANE_LOCK_FILE")
        ):
            with open(os.environ["SECURITY_CONTROL_PLANE_LOCK_FILE"], "r") as f:
                return True

    def _lock_file_path(self) -> str | None:
        if not self._initialized and os.path.exists(
            os.environ.get("SECURITY_CONTROL_PLANE_LOCK_FILE")
        ):
            with open(os.environ["SECURITY_CONTROL_PLANE_LOCK_FILE"], "r") as f:
                return f.read().strip()

    def _lock_file_exists(self) -> bool:
        if not self._initialized and os.path.exists(
            os.environ.get("SECURITY_CONTROL_PLANE_LOCK_FILE")
        ):
            with open(os.environ["SECURITY_CONTROL_PLANE_LOCK_FILE"], "r") as f:
                return True


class SecurityControlPlaneManager(SecurityControlPlane):
    """Manages the lifecycle and state of security control plane components."""

    def __init__(self, lock_file_path=None, **kwargs):
        super().__init__()
        self._lock_file = None
        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)
        
        # Initialize default lock file based on environment variable or passed key
        env_key = os.environ.get("SECURITY_CONTROL_PLANE_LOCK_FILE")
        if not self._initialized and (env_key is None or env_key == ""):
            import shutil
            tmp_path = "/tmp/security_control_plane.lock"
            try:
                # Create a temp file for lock management purposes in this container environment
                with open(tmp_path, "w") as f:
                    pass  # Just create it to avoid errors if env is empty or invalid
            except Exception as e:
                print(f"[Warning] Failed to initialize default lock file path (likely due to missing process): {e}")

    def _get_lock_file(self) -> str | None:
        """Get the current lock file path."""
        return self._lock_file

    @property
    def is_locked(self) -> bool:
        if not self.isolated():
            raise RuntimeError("Security Control Plane requires an isolated environment")
        
        try:
            with open(os.environ.get("SECURITY_CONTROL_PLANE_LOCK_FILE"), "r") as f:
                return True
        except Exception:
            # If the file doesn't exist or is corrupted, assume locked state but allow access via lock_file_path property if initialized
            pass

    def _is_initialized(self) -> bool:
        """Check if SecurityControlPlaneManager has been properly initialized."""
        try:
            self._initialized = True  # Mark as initialized after successful initialization logic (e.g., environment check or explicit init call)
            return True
        except Exception:
            return False

    def _is_isolated(self) -> bool:
        """Determine if the current SecurityControl
