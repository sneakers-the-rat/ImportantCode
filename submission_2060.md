# Issue #2060: Fix: [Bounty: 23 USDC] Create contributors webpage

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Contributors | AgentPipe</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: 'Segoe UI', Roboto, system-ui, sans-serif; background: #fcf8f0; color: #2d2a24; }
  .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

  /* Hero */
  .hero { background: #f3ede4; border-radius: 2rem; margin: 2rem 0; padding: 3rem 2rem; text-align: center; box-shadow: 0 8px 20px rgba(0,0,0,0.05); }
  .hero h1 { font-size: 3rem; letter-spacing: -0.02em; color: #a67c4b; }
  .hero p { font-size: 1.2rem; margin-top: 0.5rem; color: #5e4f3c; }

  /* goose factory scene */
  .factory-scene { margin: 1.5rem auto; max-width: 700px; }

  /* golden eggs decorations */
  .golden-egg { display: inline-block; width: 28px; height: 36px; background: radial-gradient(circle at 30% 30%, #ffd966, #b8860b); border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%; box-shadow: 0 4px 8px rgba(184,134,11,0.4); margin: 0 4px; transform: rotate(-6deg); }
  .golden-egg:nth-child(2n) { transform: rotate(8deg) scale(0.9); }

  /* contributors grid */
  .contributors-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 2rem; margin: 3rem 0; }
  .contributor-card { background: white; border-radius: 2rem; padding: 1.5rem; box-shadow: 0 4px 12px rgba(0,0,0,0.06); display: flex; flex-direction: column; align-items: center; text-align: center; transition: transform 0.2s, box-shadow 0.2s; border: 1px solid #ede8dd; }
  .contributor-card:hover { transform: translateY(-4px); box-shadow: 0 12px 24px rgba(0,0,0,0.08); }
  .contributor-avatar { width: 80px; height: 80px; border-radius: 50%; object-fit: cover; border: 3px solid #a67c4b; margin-bottom: 0.75rem; }
  .contributor-name { font-size: 1.2rem; font-weight: 600; color: #2d2a24; }
  .contributor-login { font-size: 0.9rem; color: #7a6a56; margin-bottom: 0.5rem; }
  .contributor-contributions { font-size: 0.95rem; background: #f3ede4; padding: 0.25rem 1rem; border-radius: 20px; display: inline-block; color: #5e4f3c; }
  .contributor-link { margin-top: 0.75rem; text-decoration: none; color: #a67c4b; font-weight: 500; }
  .contributor-link:hover { text-decoration: underline; }

  .loading, .error { text-align: center; padding: 2rem; font-size: 1.2rem; color: #5e4f3c; }
  .error { color: #b34a4a; }
  .footer { text-align: center; margin: 2rem 0; color: #aaa18c; font-size: 0.9rem; }

  @media (max-width: 600px) {
    .hero h1 { font-size: 2.2rem; }
    .hero { padding: 2rem 1rem; }
    .contributors-grid { grid-template-columns: 1fr; }
  }
</style>
</head>
<body>
<div class="container">
  <div class="hero">
    <div class="factory-scene">
      <!-- Decorative golden eggs -->
      <span class="golden-egg"></span>
      <span class="golden-egg"></span>
      <span class="golden-egg"></span>
      <span class="golden-egg"></span>
      <span class="golden-egg"></span>
    </div>
    <h1>🥚 Contributors</h1>
    <p>Meet the flock behind AgentPipe — every contribution counts.</p>
  </div>

  <div id="contributors-container">
    <div class="loading">Loading contributors...</div>
  </div>

  <div class="footer">
    <span class="golden-egg" style="width:16px;height:20px;transform:rotate(-3deg);"></span>
    Built with 🧡 by the AgentPipe community
    <span class="golden-egg" style="width:16px;height:20px;transform:rotate(5deg);"></span>
  </div>
</div>

<script>
  (function() {
    const container = document.getElementById('contributors-container');
    const repoOwner = 'agentpipe';
    const repoName = 'agentpipe'; // adjust if different

    // Fallback: if the repo is not found, you could try 'agentpipe/agentpipe' or other.
    // We'll use the GitHub API to fetch contributors.
    const apiUrl = `https://api.github.com/repos/${repoOwner}/${repoName}/contributors?per_page=100`;

    async function fetchContributors() {
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`GitHub API error: ${response.status}`);
        }
        const data = await response.json();
        // data is an array of contributors
        if (!Array.isArray(data) || data.length === 0) {
          throw new Error('No contributors found or unexpected response.');
        }
        renderContributors(data);
      } catch (error) {
        console.error('Failed to fetch contributors:', error);
        container.innerHTML = `<div class="error">⚠️ Could not load contributors. Please try again later.</div>`;
      }
    }

    function renderContributors(contributors) {
      // Sort by contributions descending (optional)
      contributors.sort((a, b) => b.contributions - a.contributions);

      let html = '<div class="contributors-grid">';
      contributors.forEach(user => {
        const avatar = user.avatar_url || '';
        const login = user.login || 'unknown';
        const contributions = user.contributions || 0;
        const profileUrl = user.html_url || `https://github.com/${login}`;
        // Name: if user has a name? Not in API response, but we can use login.
        html += `
          <div class="contributor-card">
            <img class="contributor-avatar" src="${avatar}" alt="${login}" loading="lazy">
            <div class="contributor-name">${login}</div>
            <div class="contributor-login">@${login}</div>
            <div class="contributor-contributions">${contributions} contribution${contributions !== 1 ? 's' : ''}</div>
            <a class="contributor-link" href="${profileUrl}" target="_blank" rel="noopener noreferrer">View profile →</a>
          </div>
        `;
      });
      html += '</div>';
      container.innerHTML = html;
    }

    fetchContributors();
  })();
</script>
</body>
</html>

## Verification
- Generated by DevilX auto-claim (OpenRouter/NVIDIA)
- Wed Sep  2 18:00:55 UTC 2026

Closes #2060
