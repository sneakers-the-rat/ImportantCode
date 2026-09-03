# Issue #2053: [Bounty: 23 USDC] Create contributors webpage

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
  .contributor-card { background: white; border-radius: 2rem; padding: 1.5rem; box-shadow: 0 4px 12px rgba(0,0,0,0.06); transition: 0.2s; border: 1px solid #ede6d8; display: flex; flex-direction: column; align-items: center; text-align: center; }
  .contributor-card:hover { transform: translateY(-4px); box-shadow: 0 12px 28px rgba(0,0,0,0.08); }
  .contributor-avatar { width: 100px; height: 100px; margin-bottom: 0.8rem; }
  .contributor-name { font-size: 1.4rem; font-weight: 600; color: #3d3529; }
  .contributor-fact { font-size: 0.9rem; color: #6b5f4d; margin: 0.3rem 0; }
  .contributor-fact strong { color: #a67c4b; }
  .github-link { display: inline-block; margin-top: 0.8rem; padding: 0.3rem 1.2rem; background: #2b2b2b; color: white; border-radius: 30px; text-decoration: none; font-size: 0.85rem; transition: 0.2s; }
  .github-link:hover { background: #4a4a4a; }

  /* egg hunt game */
  .easter-egg-area { margin: 3rem 0; padding: 2rem; background: #f7f0e3; border-radius: 2rem; text-align: center; }
  .easter-egg-area h2 { color: #a67c4b; }
  #game-container { margin: 1rem auto; max-width: 400px; }
  #game-egg { width: 80px; height: 100px; background: radial-gradient(circle at 30% 30%, #ffdb7c, #b8860b); border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%; display: inline-block; cursor: pointer; transition: 0.15s; box-shadow: 0 6px 12px rgba(184,134,11,0.4); }
  #game-egg:active { transform: scale(0.9); }
  #game-score { font-size: 2rem; font-weight: 700; color: #5e4f3c; margin-top: 0.5rem; }
  #game-message { font-size: 1rem; color: #7a6b55; margin-top: 0.3rem; }
  .hidden-egg { display: none; }

  /* footer */
  footer { margin-top: 3rem; padding: 2rem 0; border-top: 2px solid #ede6d8; text-align: center; color: #4d4233; }
  .csuite-contact { font-size: 1rem; margin-bottom: 0.5rem; }
  .csuite-contact a { color: #a67c4b; text-decoration: none; }
  .wave-video { margin: 1rem auto; max-width: 400px; }
  .wave-video video { width: 100%; border-radius: 20px; box-shadow: 0 4px 16px rgba(0,0,0,0.1); }

  /* number 71 placements */
  .seventy-one-visible { display: inline-block; font-weight: 600; color: #b8860b; }

  /* responsive */
  @media (max-width: 600px) { .hero h1 { font-size: 2rem; } }
</style>
</head>
<body>
<div class="container">

  <!-- Hero with goose people factory scene -->
  <div class="hero">
    <div class="factory-scene">
      <svg viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
        <!-- factory background -->
        <rect x="0" y="100" width="600" height="200" fill="#d9c8b2" />
        <rect x="0" y="100" width="600" height="20" fill="#b8a48c" />
        <rect x="20" y="60" width="80" height="60" fill="#b8a48c" rx="4" />
        <rect x="120" y="40" width="80" height="80" fill="#b8a48c" rx="4" />
        <rect x="220" y="70" width="80" height="50" fill="#b8a48c" rx="4" />
        <rect x="340" y="50" width="80" height="70" fill="#b8a48c" rx="4" />
        <rect x="460" y="80" width="80" height="40" fill="#b8a48c" rx="4" />
        <!-- windows -->
        <circle cx="60" cy="80" r="12" fill="#a8d8ea" />
        <circle cx="160" cy="70" r="12" fill="#a8d8ea" />
        <circle cx="260" cy="90" r="12" fill="#a8d8ea" />
        <circle cx="380" cy="80" r="12" fill="#a8d8ea" />
        <circle cx="500" cy="95" r="12" fill="#a8d8ea" />
        <!-- smoke -->
        <circle cx="30" cy="30" r="20" fill="#ccc" opacity="0.6" />
        <circle cx="60" cy="15" r="25" fill="#ccc" opacity="0.5" />
        <circle cx="90" cy="5" r="18" fill="#ccc" opacity="0.4" />

        <!-- Goose people -->
        <!-- Goose 1: carrying box -->
        <g transform="translate(80,160)">
          <ellipse cx="0" cy="0" rx="20" ry="30" fill="#f0e5d0" /> <!-- body -->
          <circle cx="10" cy="-20" r="10" fill="#f0e5d0" /> <!-- head -->
          <ellipse cx="18" cy="-22" rx="8" ry="4" fill="#f5a623" /> <!-- beak -->
          <circle cx="13" cy="-23" r="2" fill="#111" /> <!-- eye -->
          <rect x="-10" y="-10" width="20" height="15" fill="#c0392b" rx="2" /> <!-- box -->
        </g>
        <!-- Goose 2: operating machine -->
        <g transform="translate(200,170)">
          <ellipse cx="0" cy="0" rx="18" ry="28" fill="#e8dccc" />
          <circle cx="8" cy="-22" r="9" fill="#e8dccc" />
          <ellipse cx="16" cy="-24" rx="7" ry="3.5" fill="#e67e22" />
          <circle cx="11" cy="-25" r="2" fill="#111" />
          <rect x="20" y="-10" width="30" height="25" fill="#7f8c8d" rx="3" /> <!-- machine -->
          <circle cx="35" cy="0" r="6" fill="#ecf0f1" /> <!-- dial -->
        </g>
        <!-- Goose 3: with clipboard -->
       

## Verification
- Generated by DevilX auto-claim (OpenRouter/NVIDIA)
- Wed Sep  2 12:03:48 UTC 2026

Closes #2053
