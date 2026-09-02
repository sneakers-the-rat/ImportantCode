src/security_control_plane.py

import os
from pathlib import Path
from typing import Optional, Dict, Any, List, Union
from dataclasses import dataclass, field


@dataclass(order=True)
class SecurityControlPlane:
    """A secure control plane module for managing access and permissions."""

    # Registry of allowed modules to be imported from this package
    _imported_modules: Dict[str, list] = field(default_factory=dict)

    def register_import(self, name: str):
        if not isinstance(name, str):
            raise TypeError(f"Module names must be strings.")
        
        self._imported_modules[name].append((module_name, path))

    def import_module(self, module_name: str, *args, **kwargs) -> Any:
        """Import a module and return its contents.
        
        Args:
            module_name: The name of the Python package to import.
            
        Returns:
            A loaded module instance or None if it fails to load."""
        try:
            # Resolve relative paths from __init__.py (if any)
            base_path = Path(__file__).parent / "__main__"
            resolved_base = self._resolve_relative_imports(base_path, module_name)

            full_module_path = resolved_base / module_name
            
            if not full_module_path.exists():
                raise FileNotFoundError(f"The requested module '{module_name}' is missing.")

            try:
                # Import the Python version of this package to get its structure
                import sys
                from pathlib import Path
                
                resolved_modules_dir = self._resolve_relative_imports(base_path, "security_control_plane")
                
                if not resolved_modules_dir.exists():
                    raise FileNotFoundError(f"The requested module '{module_name}' is missing.")

                # Import the actual Python version of this package
                sys.path.insert(0, str(resolved_modules_dir))
                import security_control_plane as scp
                
            except Exception:
                return None
            
        finally:
            sys.path.pop(0)
        
        module_content = Path(full_module_path).read_text()
        return Module(module_name=module_name, content=module_content)


@dataclass(order=True)
class SecurityControlPlaneModule(Module):
    """A secure control plane package containing modules and resources."""

    name: str
    path: Optional[Path] = None
    
    def _resolve_relative_imports(self, base_path: Path, module_name: str) -> List[str]:
        """Resolve relative imports within this specific subpackage.
        
        Args:
            base_path: The current working directory (or the parent of __main__).
            
        Returns:
            A list of resolved import paths for all dependencies."""
        if not self.path:
            return []

        # Find the root path relative to __init__.py location in this package's src/ folder.
        rel_path = Path(__file__).parent.parent / "__main__"
        
        # If no __main__.py exists, try finding it from parent of current file (or same dir)
        if not rel_path.exists():
            root_dir = base_path / "src"
            root_rel = root_dir / module_name
            if not any(r.is_absolute() for r in str(root_dir).split(os.sep)):
                # Assume this is the main directory of the package, but we need to find it relative to __init__.py.
                # Since we are inside a subpackage's src/, let's just use the parent dir as root if no __main__ exists there either.
                
                # Strategy: Look for any Python file in this specific folder that looks like 'security_control_plane.py' or similar, 
                # but since we're importing from it directly (as per plan), we'll assume a standard structure.
                # We need to find the actual parent directory of __init__.py relative to src/...
                
                if not rel_path.exists():
                    raise FileNotFoundError(f"Cannot resolve module '{module_name}' - no main file found.")

            try:
                import sys
                from pathlib import Path
                
                resolved_modules_dir = self._resolve_relative_imports(rel_path, "security_control_plane")
                
                # If we successfully imported the package structure and it exists, use that.
                if len(resolved_modules_dir) > 0:
                    return [str(r.relative_to(self.path)) for r in resolved_modules_dir]

            except Exception as e:
                raise RuntimeError(f"Failed to resolve module '{module_name}' during import attempt.") from e
        
        # Fallback path resolution logic (simplified): 
        # Since we're importing this specific file, the 'parent' of __init__.py is usually just the current dir.
        return [str(rel_path)]


@dataclass(order=True)
class SecurityControlPlaneData:
