# Issue #2053: [Bounty: 23 USDC] Create contributors webpage

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contributors · AgentPipe</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            background: #fef9f0;
            font-family: 'Segoe UI', Roboto, system-ui, sans-serif;
            color: #2d2a24;
            padding: 2rem 1rem;
        }
        .container {
            max-width: 1300px;
            margin: 0 auto;
        }

        /* ----- HERO ----- */
        #hero {
            background: #f5eee1;
            border-radius: 3rem 3rem 0 0;
            padding: 2rem 1.5rem 1.5rem;
            margin-bottom: 3rem;
            box-shadow: 0 12px 30px rgba(0,0,0,0.05);
            position: relative;
            overflow: hidden;
        }
        #hero h1 {
            font-size: 3rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            color: #2b4f3b;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        #hero p {
            text-align: center;
            font-size: 1.2rem;
            color: #5a4e3e;
            margin-bottom: 1.5rem;
        }
        .hero-svg {
            display: block;
            width: 100%;
            max-width: 900px;
            height: auto;
            margin: 0 auto;
            border-radius: 2rem;
            background: #d9d0bd;
        }

        /* ----- CONTRIBUTORS ----- */
        #contributors {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 2rem;
            margin: 3rem 0 4rem;
        }
        .contrib-card {
            background: #ffffffdd;
            backdrop-filter: blur(2px);
            border-radius: 2rem;
            padding: 1.5rem 1.2rem 1.2rem;
            box-shadow: 0 6px 20px rgba(0,0,0,0.04);
            border: 1px solid #e6dccc;
            transition: 0.15s;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }
        .contrib-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(0,0,0,0.08);
        }
        .portrait {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            background: #f0ebe1;
            margin-bottom: 0.8rem;
            border: 3px solid #dbbd8f;
            padding: 0.2rem;
        }
        .portrait svg {
            width: 100%;
            height: 100%;
            display: block;
            border-radius: 50%;
        }
        .contrib-card h3 {
            font-size: 1.5rem;
            font-weight: 600;
            color: #1f3a2b;
        }
        .contrib-card .username {
            font-weight: 500;
            color: #7a6b54;
            margin-bottom: 0.6rem;
        }
        .contrib-card .username a {
            color: #3b6b4f;
            text-decoration: none;
            border-bottom: 1px dotted #b8a68b;
        }
        .contrib-card .username a:hover {
            color: #1f3a2b;
            border-bottom-color: #1f3a2b;
        }
        .facts {
            background: #f8f3ea;
            border-radius: 1.2rem;
            padding: 0.8rem 1rem;
            width: 100%;
            font-size: 0.95rem;
            color: #3f3529;
            margin-top: 0.4rem;
        }
        .facts span {
            display: block;
            padding: 0.2rem 0;
        }
        .facts .label {
            font-weight: 600;
            color: #8a7a62;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }

        /* ----- GOLDEN EGGS DECORATION ----- */
        .egg-deco {
            position: fixed;
            pointer-events: none;
            font-size: 2.2rem;
            opacity: 0.25;
            z-index: 0;
            user-select: none;
        }

        /* ----- EASTER EGG GAME ----- */
        #easter-egg-game {
            background: #f2eadb;
            border-radius: 3rem;
            padding: 2rem 1.5rem;
            margin: 3rem 0 2rem;
            text-align: center;
            border: 2px dashed #c9b696;
            position: relative;
            z-index: 2;
        }
        #easter-egg-game h2 {
            font-size: 1.8rem;
            color: #2b4f3b;
            margin-bottom: 0.5rem;
        }
        .egg-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1rem;
            max-width: 400px;
            margin: 1.5rem auto;
        }
        .egg-cell {
            background: #fef9f0;
            border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
            aspect-ratio: 3/4;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.5rem;
            cursor: pointer;
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
            border: 2px solid #dbbd8f;
            transition: 0.1s;
            background: #f9f0e3;
            color: #c9b696;
        }
        .egg-cell.revealed {
            background: #fef4d9;
            border-color: #c9a87c;
            color: #b58a4b;
        }
        .egg-cell.winner {
            background: #f7e3b0;
            border-color: #e0b45a;
            color: #9e7a3a;
            animation: pulse-gold 0.8s ease-in-out 3;
        }
        @keyframes pulse-gold {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); background: #f7d97a; }
            100% { transform: scale(1); }
        }
        #game-message {
            font-size: 1.3rem;
            font-weight: 500;
            color: #2b4f3b;
            min-height: 3rem;
            margin-top: 0.5rem;
        }
        #game-reset {
            background: #dbbd8f;
            border: none;
           

## Verification
- Generated by DevilX auto-claim (OpenRouter/NVIDIA)
- Wed Sep  2 00:01:26 UTC 2026

Closes #2053
