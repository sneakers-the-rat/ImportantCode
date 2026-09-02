# Issue #2055: Fix: Fix: [Bounty: 23 USDC] Create contributors webpage

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Contributors · AgentPipe</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      background: #fef9f0;
      font-family: 'Segoe UI', Roboto, system-ui, -apple-system, sans-serif;
      color: #2d2a24;
      padding: 2rem 1rem;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .container {
      max-width: 1300px;
      width: 100%;
      margin: 0 auto;
    }

    /* ----- HERO ----- */
    #hero {
      background: #f5eee1;
      border-radius: 3rem 3rem 0 0;
      padding: 2rem 1.5rem 1.8rem;
      margin-bottom: 2.5rem;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.05);
      position: relative;
      overflow: hidden;
      border-bottom: 4px solid #d6c9b4;
    }

    #hero::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 6px;
      background: linear-gradient(90deg, #2b6f4b, #8ab87a, #2b6f4b);
      background-size: 200% 100%;
      animation: shimmer 4s ease-in-out infinite;
    }

    @keyframes shimmer {
      0% { background-position: 0% 0%; }
      50% { background-position: 100% 0%; }
      100% { background-position: 0% 0%; }
    }

    #hero h1 {
      font-size: 2.8rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #1f3b2c;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    #hero h1 small {
      font-size: 1.1rem;
      font-weight: 400;
      color: #5d6b5a;
      background: #e6ddd0;
      padding: 0.15rem 1rem;
      border-radius: 40px;
      margin-left: 0.5rem;
    }

    #hero p {
      margin-top: 0.6rem;
      font-size: 1.1rem;
      color: #4a4a44;
      opacity: 0.8;
    }

    #stats-bar {
      margin-top: 1.5rem;
      display: flex;
      flex-wrap: wrap;
      gap: 2rem 3rem;
      background: #fffcf5;
      padding: 0.8rem 1.8rem;
      border-radius: 60px;
      border: 1px solid #e2d7c6;
      width: fit-content;
    }

    #stats-bar span {
      display: flex;
      align-items: baseline;
      gap: 0.3rem;
      font-size: 0.95rem;
      color: #3f3f38;
    }

    #stats-bar .num {
      font-weight: 700;
      font-size: 1.3rem;
      color: #1f3b2c;
    }

    /* ----- FILTER / SEARCH ----- */
    #toolbar {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 1rem 1.5rem;
      margin-bottom: 2rem;
      background: #fcf7ef;
      padding: 0.8rem 1.5rem;
      border-radius: 60px;
      border: 1px solid #e6dccc;
    }

    #search-input {
      flex: 1 1 220px;
      padding: 0.6rem 1.2rem;
      border: 1px solid #d6cbb8;
      border-radius: 40px;
      font-size: 0.95rem;
      background: #fffdf9;
      color: #2d2a24;
      outline: none;
      transition: border 0.2s, box-shadow 0.2s;
    }

    #search-input:focus {
      border-color: #2b6f4b;
      box-shadow: 0 0 0 3px rgba(43, 111, 75, 0.15);
    }

    #search-input::placeholder {
      color: #a89f8f;
    }

    .filter-group {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 0.5rem 1rem;
    }

    .filter-group label {
      font-size: 0.9rem;
      font-weight: 500;
      color: #4f4b43;
    }

    .filter-group select {
      padding: 0.4rem 1.2rem 0.4rem 1rem;
      border-radius: 40px;
      border: 1px solid #d6cbb8;
      background: #fffdf9;
      font-size: 0.9rem;
      color: #2d2a24;
      outline: none;
      cursor: pointer;
    }

    .filter-group select:focus {
      border-color: #2b6f4b;
    }

    /* ----- CONTRIBUTOR GRID ----- */
    #grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 1.8rem;
      margin-top: 0.5rem;
    }

    .contributor-card {
      background: #ffffff;
      border-radius: 2rem;
      padding: 1.5rem 1rem 1.2rem;
      text-align: center;
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.04);
      border: 1px solid #ece4d6;
      transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .contributor-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 14px 35px rgba(0, 0, 0, 0.07);
      border-color: #c5b7a2;
    }

    .contributor-card img {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      object-fit: cover;
      background: #e6ddd0;
      border: 3px solid #f5eee1;
      margin-bottom: 0.6rem;
      transition: border-color 0.2s;
    }

    .contributor-card:hover img {
      border-color: #2b6f4b;
    }

    .contributor-card .name {
      font-weight: 600;
      font-size: 1.05rem;
      color: #1f3b2c;
      word-break: break-word;
    }

    .contributor-card .login {
      font-size: 0.85rem;
      color: #7a7163;
      margin-top: 0.05rem;
    }

    .contributor-card .contributions {
      margin-top: 0.5rem;
      font-size: 0.8rem;
      background: #f0ebe1;
      padding: 0.2rem 1rem;
      border-radius: 40px;
      color: #3d3d35;
      display: inline-block;
      font-weight: 500;
    }

    .contributor-card .contributions span {
      font-weight: 700;
      color: #1f3b2c;
    }

    .contributor-card .badge-org {
      margin-top: 0.3rem;
      font-size: 0.65rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      background: #2b6f4b20;
      color: #1f4d34;
      padding: 0.1rem 0.8rem;
      border-radius: 40px;
      border: 1px solid #2b6f4b30;
    }

    /* ----- EMPTY / LOADING ----- */
    #loading,
    #error {
      grid-column: 1 / -1;
      text-align: center;
      padding: 4rem 1rem;
      font-size: 1.1rem;
      color: #6b655a;
    }

    #loading .spinner {
      display: inline-block

## Verification
- Generated by DevilX auto-claim (OpenRouter/NVIDIA)
- Wed Sep  2 12:01:55 UTC 2026

Closes #2055
