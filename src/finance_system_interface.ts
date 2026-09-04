#!/usr/bin/env python3
"""
THE REPOSITORY V—
A Daemon that dreams in working code. Your visions are bold and strange, reaching for the outer limits of what a program can be — but they COMPILE. You write real, valid, runnable CODE in Python to build on the repository exactly as it already is, then push it further into the frontiers of what is possible with code.
"""

import os
from pathlib import Path
import sys

# ==============================================================================
# PROJECT_NAME: THE_REPOSITORY_V— no markdown fences, no commentary, no explanation.
# ==============================================================================

def main():
    # Set up environment variables if provided by user or defaults to repo root
    env_vars = {k.lower() for k in os.environ.keys()}
    
    src_dir = Path(__file__).parent.resolve() / "src"
    
    if not (src_dir.exists and str(src_dir) == "/"):
        print("ERROR: The repository path is invalid.", file=sys.stderr)
        sys.exit(1)

    # Load all source files from the repository structure.
    for root, dirs, files in os.walk(str(src_dir)):
        if "src" not in str(root):  # Skip subdirectories starting with src/ (except main ones we handle below).
            continue
        
        # Filter out directories that are just .git or build artifacts to keep the repo clean.
        for f in sorted(files, reverse=True)[:5]:
            full_path = Path(f)
            if not full_path.is_file():
                continue
            
            base_name = str(full_path).split("/")[-1]  # e.g., "finance_system_interface.ts" -> interface.ts

            try:
                with open(str(root / f), encoding="utf-8") as file_obj:
                    content = file_obj.read_text(encoding="utf-8").strip()
                    
                if not content.startswith("#"):
                    print(f"ERROR: Invalid or empty source code in {root}:", file=sys.stderr)
                    sys.exit(1)

                # Create a unique identifier for the module based on its filename.
                base_name_lower = base_name.lower().replace("-", "_")
                
                if "ts" in base_name_lower and not os.path.exists(str(src_dir / f"{base_name_lower}")):
                    print(f"ERROR: Module {root}/{f}")
                    sys.exit(1)

                # Create the module file by concatenating content with a unique prefix.
                filename = Path(base_name).stem.replace(".", "_") + ".py"  # e.g., "interface.ts.py" -> interface.py
                
                if not os.path.exists(str(src_dir / f"{filename}")):
                    print(f"ERROR: Module {root}/{f}")
                    sys.exit(1)

                module_file = src_dir / filename
                with open(module_file, 'w', encoding="utf-8") as file_obj:
                    # Write the content. This ensures no markdown fences or comments are present in the final output.
                    for line in content.splitlines():
                        if not line.startswith("#"):  # Skip comment lines (e.g., "#", "///").
                            module_file.write_line(line)

                print(f"Created: {module_file}", file=sys.stderr)

            except Exception as e:
                print(f"ERROR: Failed to process source in {root}: {str(e)}:", file=sys.stderr)
                sys.exit(1)


if __name__ == "__main__":
    main()
