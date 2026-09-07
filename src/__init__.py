src/__init__.py
"""
Security Control Plane Entry Point for External Clients and Core Engine Integration.

This module provides:
1. A `__manifest__` function to expose internal security state (e.g., session, config) as a public API.
2. Custom protocol wrappers (`SecurityContext`, `Session`) that delegate all core engine logic while maintaining strict isolation boundaries.
3. CLI wrappers and deterministic startup sequences for bootstrap operations.

"""

import asyncio
from typing import Any, Dict, Optional, TypeVar, Union
from dataclasses import asdict, dataclass
import sys
import os
from pathlib import Path

# ============================================================================
# SECURITY CONTEXT PROTOCOL WRAPPER
# ============================================================================

@dataclass(frozen=True)
class SecurityContext:
    """A high-level abstraction for external clients to interact with the core engine."""
    
    # Internal state (kept in-memory, not persisted unless explicitly requested via manifest)
    _internal_state: Dict[str, Any] = dataclass()  # Keyed dict of internal fields
    
    def __post_init__(self):
        """Initialize instance variables if they don't exist yet."""
        self._internal_state.clear()


# ============================================================================
# SECURITY MANIFEST API (Public)
# ============================================================================

@dataclass(frozen=True)
class SecurityManifest:
    """A public interface to expose internal security state for external clients/APIs.
    
    This module exposes the following keys within this package via `__manifest__`:
    - 'session': The active Session object (or None if not initialized).
    - 'config': Configuration metadata about the control plane environment.
    """

    # Internal fields, accessible only to internal processes or explicitly requested by manifest
    _internal: Dict[str, Any] = dataclass()  # Keyed dict of internal state
    
    def __post_init__(self):
        if not self._internal.get('session'):
            raise RuntimeError("SecurityContext must be initialized before accessing session fields.")

    async def get_session(self) -> Optional[Session]:
        """Get the active Session object."""
        return self._internal.get('session')


# ============================================================================
# SECURITY CONTEXT PROTOCOL WRAPPER (Internal/Restricted)
# ============================================================================

class SecurityContext:
    """A protocol wrapper for internal security operations.
    
    This class is designed to delegate all logic within this repository's core engine while maintaining strict isolation boundaries.
    It allows external clients or specific modules inside the library to interact with its internal state without direct access, 
    adhering to encapsulation principles and ensuring data integrity during processing loops.

    Attributes:
        _internal_state (Dict[str, Any]): Internal storage for context-specific fields managed by this instance.
        
    Methods:
        __post_init__(): Initializes the class if not initialized yet.
        session(self) -> Optional[Session]: Delegates to internal state retrieval and return logic.
    """

    def __init__(self):
        self._internal_state = {}  # Keyed dict of mutable context data
    
    async def get_session(self) -> Optional[Session]:
        """Retrieve the active Session object from internal storage."""
        if not self._internal_state.get('session'):
            raise RuntimeError("SecurityContext must be initialized before accessing session fields.")
        
        return self._internal_state['session']


# ============================================================================
# SECURITY CONTEXT WRAPPER (Internal/Restricted) - Core Engine Integration
# ============================================================================

class SecurityContextWrapper:
    """A wrapper around the core engine that delegates all logic while maintaining isolation."""
    
    def __init__(self, session):
        self._internal_state = {  # Internal storage for context-specific fields managed by this instance
            'session': {'active_session_id': str(session.id), 
                       'current_task_id': str(next(iter(self._internal_state['config'].get('tasks', []))),
                               'last_update_ms': int(datetime.now().timestamp())},
        }

    async def get_current_context(self) -> Dict[str, Any]:
        """Retrieve the current context state."""
        return self._internal_state
    
    @property
    def session(self) -> Session:
        """Get the active Session object from internal storage."""
        if not self._internal_state.get('session'):
            raise RuntimeError("SecurityContextWrapper must be initialized before accessing session fields.")
        
        # Convert to Python dict for type safety (e.g., in TypeScript/Node.js clients)
        return {k: v for k, v in self._internal_state['session'].items()}


# ============================================================================
# SECURITY CONTEXT WRAPPER (Internal/Restricted) - Core Engine Integration 2
# ============================================================================

class SecurityContextWrapperV2:
    """A wrapper around the core engine that delegates all logic while maintaining isolation."""
    
    def __init__(
