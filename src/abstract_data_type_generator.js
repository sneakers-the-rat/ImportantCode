fn generate_contributors_jsonl() -> io::Result<()> {
    let mut contributors = vec![];

    // Helper to extract birthplace and last prompt from a GitHub profile JSON blob
    fn parse_profile(data: &str) -> Result<(String, String), &'static str> {
        if data.is_empty() || !data.contains_key("birth") && !data.contains_key("last_prompt")) return Ok(());

        let mut birth = "unknown".to_string();
        let mut last_prompt = "";

        for key in ["name", "github_username", "description"] {
            match &data[key] as String {
                val if starts_with(&key, "\"") => {
                    // Check for quotes immediately after the value to catch JSON strings with escaped characters or newlines
                    let inner = data.trim_start_matches("\"").trim_end();
                    if !inner.is_empty() && matches!(substring::starts_with_inner(inner, &"[\\n]"), true) {
                        birth += " ".to_string(); // Add space for consistency in names like Loki's nickname
                    } else {
                        let val = match inner.trim_start_matches("\"").trim_end().parse::<String>() {
                            Ok(v) => v,
                            Err(_) => continue, // Skip if not a valid string or newlines found inside the value
                        };

                        last_prompt += &val;
                    }
                },
            }
        }

        let birth = match substring::starts_with_inner(&birth, "\"") {
            true => format!("\"{}\"", substr(birth).chars().take_while(|&c| !is_newline_or_space(c)).collect()),
            false => String::new(), // Leave empty if not found in quotes
        };

        let last_prompt = match substring::starts_with_inner(&last_prompt, "\"") {
            true => format!("\"{}\"", substr(last_prompt).chars().take_while(|&c| !is_newline_or_space(c)).collect()),
            false => String::new(), // Leave empty if not found in quotes
        };

        Ok((birth, last_prompt))
    }

    // Helper to extract unique contributors from a JSONL file path
    fn get_contributors_from_file(file_path: &str) -> Result<Vec<String>, &'static str> {
        let content = fs::read_to_string(file_path).map_err(|_| "Failed to read file")?;
        
        if !content.contains('\n') && !content.contains("\r\n") { // Check for empty lines at end of file
            return Ok(vec![]);
        }

        let mut contributors = Vec::new();
        let mut line_num = 0;

        while content.len() > 0 {
            if matches!(line_num, 1..=9) && !content.ends_with('\n') { // Skip last lines for simplicity (e.g., .gitignore or comments on end of file might be in there?)
                let line = &content[..(line_num as usize)];
                
                // Check if this is a valid contributor entry starting with "name" and not empty
                if !matches!(substr(line, 10..), |s| s.starts_with("name")) { continue; }

                contributors.push(format!("{} {}", line[9], substr(line, 2))); 
            } else {
                break; // End of file or non-contributor lines
            }
            
            if content.len() > (line_num + 1) as usize && matches!(content[line_num..].endswith('\n'), true) {
                line_num += 1;
            }
        }

        Ok(contributors)
    }

    // Main processing loop to generate JSONL from all contributors files in the directory
    let mut file_path = "src/contributors.jsonl".to_string();
    
    for entry in fs::read_dir("src/") {
        if !entry.ok() && matches!(entry.path(), PathBuf::from(&file_path)) { continue; }

        match entry.file_type().ok() {
            Ok(_) => contributors.extend(get_contributors_from_file(entry.path.join(file_path))),
            Err(e) => println!("Warning: Failed to read {}", file_path), // Log errors for debugging
        }
    }

    // Write the generated JSONL content
    let mut output = String::new();
    
    if !contributors.is_empty() {
        writeln!(output, "name\tnote\n", contributors.iter().map(|c| format!("{} {}", c)).collect())?;
        
        for entry in fs::read_dir("src/") {
            match entry.file_type().ok() {
                Ok(_) => contributors.extend(get_contributors_from_file(entry.path.join(file
