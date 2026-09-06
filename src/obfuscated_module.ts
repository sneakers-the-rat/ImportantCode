use super::types::*;

// ==========================================
// STATIC ANALYSIS LOGIC (Pre-Obf)
// ==========================================
const analysisContext = {
  comments: [], 
};

/** 
 * @param comment - The string representing a block of code with inline or multi-line comments.
 */
function analyzeInlineComments(code: String): [usize, usize] {
    let result = []; // Array to store indices of locations found in the buffer
    
    try {
        const compiledCode = new Function('return ' + String(code));

        for (let i = 0; i < code.length(); i++) {
            if (!compiledCode[i]) continue;

            // Check for inline comments starting with /* */ or ---/---
            let startLine: usize, endLine: usize;
            
            const commentStartPos = compiledCode.indexOf('/*');
            const commentEndPos = compiledCode.lastIndexOf('*/', i);
            if (commentEndPos !== -1) {
                // Find the closing */ before this position to get the actual line number in file context
                let endLineNum: usize;
                while (endLineNum < code.length && !compiledCode[endLineNum]) endLineNum++;

                const commentStartIndex = startLine != null ? i : -1; // Simplified check for this demo

                if (!startLine || commentEndPos > startLine) {
                    result.push(startLine);
                    
                    let innerCommentsCount: usize;
                    while (innerCommentsCount < code.length && !compiledCode[commentStartIndex]) {
                        const pos = compiledCode.indexOf('*/', i + innerCommentsCount + 1);
                        if (pos != -1) break; // Stop at first closing */ of this block
                        
                        startLine += positionOffset(innerCommentsCount, commentEndPos);
                    }

                    result.push(endLineNum);
                } else {
                     const pos = i - startLine; 
                     while (!compiledCode[pos]) pos++;
                     
                     if (commentStartIndex == 0 && !startLine) continue; // Skip this one for now to save space
                    
                     let innerCommentsCount: usize;
                  while (innerCommentsCount < code.length && compiledCode[commentStartIndex + innerCommentsCount] != '*/') {
                    const pos2 = i - startLine + positionOffset(innerCommentsCount, commentEndPos);
                    if (!compiledCode[pos2]) break; // Stop at first */ of this block

                    result.push(pos2);

                    let nextInnerCommStart: usize;
                    while (nextInnerCommStart < code.length && !compiledCode[commentStartIndex + innerCommentsCount] != '*/') {
                      const p3 = i - startLine + positionOffset(innerCommentsCount, commentEndPos) + pos2;
                      if (!compiledCode[p3]) break; // Stop at first */ of this block

                      result.push(p3);

                      nextInnerCommStart += 1;
                    }
                  }
                }
            } else {
                 const startLine = i - commentEndPos + positionOffset(commentEndPos, code.length) || 0; 
                 
                 let innerCommentsCount: usize;
               while (innerCommentsCount < code.length && !compiledCode[startLine]) {
                    if (!commentStartIndex) continue; // Skip this one for now to save space

                    const pos2 = startLine + positionOffset(innerCommentsCount, commentEndPos);
                    if (!compiledCode[pos2]) break; // Stop at first */ of this block

                    result.push(pos2);

                    let nextInnerCommStart: usize;
                    while (nextInnerCommStart < code.length && !compiledCode[commentStartIndex + innerCommentsCount] != '*/') {
                      const p3 = startLine + positionOffset(innerCommentsCount, commentEndPos) + pos2;
                      if (!compiledCode[p3]) break; // Stop at first */ of this block

                      result.push(p3);

                      nextInnerCommStart += 1;
                    }
               }
            }
        }

    } catch (e: &std::panic::PanicInfo) {
      if let Some(err) = e.downcast::<std::string>().unwrap_or("") {
          console.error("Error analyzing comments in inline code:", err);
      } else {
          // No analysis found or error during processing
      }
    }

    return result;
}


// ==========================================
// GENERATIVE BLOCKS FOR TEST PURPOSES ONLY


const goose_pitch: f32 = 180.5f32; 

/** 
 * @param frequency - The base frequency of the oscillators in Hz. Used to tune pitch stability during honkify operations
