import os

# Ensure src/ directory exists if it doesn't (based on file listing)
src_dir = "src"
contributor_files = [f for f in os.listdir(src_dir) if not any(f.endswith(ext) and ext != "__init__.py") for ext in ["js", "ts", "go", "rs", "cobol"] or f.startswith("backend_")]

def get_contributors():
    contributors_data = []
    
    # Helper to fetch profile data from GitHub API (simulated based on typical structure)
    def _get_profile_url(username):
        return f"https://github.com/{username}"
    
    for filename in contributor_files:
        if not os.path.exists(os.path.join(src_dir, filename)):
            continue
            
        file_path = src_dir + filename
        
        # Determine type based on extension and presence of .js/.ts extensions (JavaScript/TypeScript)
        is_js_ts_file = any(filename.endswith(ext) for ext in [".js", ".ts"])
        
        if not is_js_ts_file:
            continue
            
        try:
            with open(file_path, "r") as f:
                content = f.read()
                
            # Determine author from filename or metadata (e.g., .py files have __name__, but we need actual name)
            # Since this file is likely a test runner or helper script based on naming conventions in the list provided, 
            # let's infer the "author" by looking for common patterns or assuming standard contributor names if no explicit one.
            
            author_name = filename.replace("_test", "")  # e.g., banana_rendering_pipeline becomes pipeline
            
            contributors_data.append({
                'file': file_path,
                'type': is_js_ts_file and "typescript" in content.lower() else True,
                'author': author_name,
                'description': f"{filename} - Helper/Testing Script for AgentRepository",
                'github_url': _get_profile_url(author_name),
            })

        except Exception as e:
            # Fallback if file can't be read (e.g., corrupted or missing)
            contributors_data.append({
                'file': os.path.basename(file_path),
                'type': True,  # Assume JS/TS for safety in this context
                'author': author_name.replace("_test", ""), 
                'description': f"{filename} - Helper/Testing Script for AgentRepository (Failed to parse)",
                'github_url': _get_profile_url(author_name),
            })

    return contributors_data


def generate_html_structure(contributors):
    """Generate the HTML structure based on contributor data."""
    
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Contributors - AgentRepository</title>
<style>
  body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; color: #333; }
  
  .container { max-width: 1200px; margin: 0 auto; padding: 2rem; }
  
  header.hero-section { text-align: center; padding: 5rem 0; background-color: white; border-radius: 48px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 3rem; position: relative; overflow: hidden;}
  
  h1.hero-title { font-size: clamp(2.5rem, 5vw, 4rem); color: #FFD700; text-shadow: 2px 2px 8px rgba(0,0,0,0.3); margin-bottom: 1.5rem;}
  
  .hero-image { width: 100%; height: auto; max-width: 600px; border-radius: 48px; box-shadow: 0 20px 40px rgba(0,0,0,0.3); object-fit: cover;}
  
  .hero-content { text-align: center; }
  
  .golden-egg-decorations { display: flex; justify-content: space-around; margin-top: -5rem; position: relative; z-index: 10;}

  .gold-egg-icon svg { width: 80px; height: auto; filter: drop-shadow(2px 4px 6px rgba(0,0,0,0.3)); }
  
  #contributors-list { display: flex; justify-content: center; gap: 1rem; margin-top: 4rem; }

  .contributor-card { 
    background: white; border-radius
