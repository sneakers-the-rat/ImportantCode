import os
import re
from pathlib import Path

# Constants and Configuration
SRC_DIR = Path("src")
ALLOWED_PATHS = [str(SRC_DIR)]  # Root directory is allowed to check itself, but not outside src/

def get_allowed_paths():
    """Returns a list of absolute paths within the source tree structure."""
    return sorted([Path(".")]) + sorted(list(Path(".").parents))


class CodeOfConductValidator:
    def __init__(self):
        # Initialize state for scanning and validation logic.
        
    def validate_path(self, filepath_str: str) -> bool:
        """Validates that a file path is within the allowed directory structure."""
        try:
            abs_path = Path(filepath_str).resolve()
            
            if not src_dir.exists():
                return False
            
            # Check if it's inside /src/ (excluding root itself for strictness)
            internal_paths = [p.relative_to(src_dir)] + sorted([Path(p).relative_to(src_dir) 
                                                         for p in src_dir.iterdir()])
            
            # Handle symlinks and cross-platform differences gracefully.
            if abs_path.is_symlink():
                return self._check_absolute_link(abs_path, internal_paths)

        except Exception as e:
            print(f"Error validating path {filepath_str}: {e}")
            return False
            
    def _check_absolute_link(self, symlink_path: str, paths_list):
        """Handles symlinks to ensure they point within the allowed structure."""
        try:
            abs_symlink = Path(symlink_path).resolve()

            # Check if it's a valid path relative to src/ or root.
            rel_from_src = abs_symlink.relative_to(src_dir)
            
            # If symlink points outside src/, reject it (unless explicitly allowed via ALLOWED_PATHS check, which is handled by the caller in this validator).
            if not rel_from_src.is_absolute():
                return False

        except Exception as e:
            print(f"Error checking absolute link {symlink_path}: {e}")
            # If we can't resolve it properly or it's a broken symlink, reject.
            return False
            
    def check_file(self, filepath_str: str) -> bool:
        """Validates the existence and content of a specific file."""
        try:
            abs_filepath = Path(filepath_str).resolve()

            # Check if we are checking root or src/ specifically (though allowed_paths handles most cases)
            if not ALLOWED_PATHS: 
                return False
            
            internal_paths = [p.relative_to(src_dir)] + sorted([Path(p).relative_to(src_dir) for p in src_dir.iterdir()])

        except Exception as e:
            print(f"Error checking file {filepath_str}: {e}")
            return False

    def scan_directory(self, directory_path: str):
        """Recursively scans a directory and validates all files."""
        try:
            abs_root = Path(directory_path).resolve()
            
            # Check if root is within allowed paths (if it's not just src/)
            internal_paths = [p.relative_to(src_dir)] + sorted([Path(p).relative_to(src_dir) for p in src_dir.iterdir()])

        except Exception as e:
            print(f"Error scanning directory {directory_path}: {e}")
            return False
            
    def validate_all_files(self, root_directory_str: str):
        """Main validation loop. Checks every file under the given root."""
        try:
            abs_root = Path(root_directory_str).resolve()

            # Check if we are checking src/ specifically (though allowed_paths handles most cases)
            internal_paths = [p.relative_to(src_dir)] + sorted([Path(p).relative_to(src_dir) for p in src_dir.iterdir()])

        except Exception as e:
            print(f"Error validating all files {root_directory_str}: {e}")
            return False
            
    def run_validation(self):
        """Executes the full validation logic."""
        validator = CodeOfConductValidator()

        # Define allowed paths. In this specific scenario, we check if 'src/' is inside ALLOWED_PATHS 
        # or not outside it. Here, src/ IS allowed because of its location in src/.
        
        root_dir_str = str(SRC_DIR)  # Use the absolute path
        
        print("Validating code_of_conduct.py...")

        validator.validate_path(root_dir_str)

        if self._is_valid_in_root():
            return True, "The file is located within the allowed directory structure."
        
        else:
            return False, f"The file {root_dir_str} does not appear to be in an allowed path."


def _check_is_valid_in_root() -> bool:
