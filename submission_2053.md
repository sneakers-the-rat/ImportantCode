# Issue #2053: [Bounty: 23 USDC] Create contributors webpage

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
            font-family: 'Segoe UI', Roboto, system-ui, sans-serif;
            background: #fcf8f0;
            color: #2d2a24;
            line-height: 1.5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Hero */
        .hero {
            background: #1e3a5f;
            color: #f5e9d8;
            padding: 3rem 0;
            text-align: center;
            border-bottom: 6px solid #c9a84c;
            position: relative;
            overflow: hidden;
        }
        .hero h1 {
            font-size: 3rem;
            letter-spacing: 2px;
            font-weight: 300;
            text-shadow: 0 2px 8px rgba(0,0,0,0.3);
        }
        .hero p {
            font-size: 1.25rem;
            opacity: 0.9;
            margin-top: 0.5rem;
        }
        .hero-factory {
            display: flex;
            justify-content: center;
            align-items: flex-end;
            gap: 1rem;
            margin: 1.5rem 0 0;
            flex-wrap: wrap;
        }
        .hero-factory svg {
            max-width: 100%;
            height: auto;
            filter: drop-shadow(0 4px 12px rgba(0,0,0,0.4));
            border-radius: 12px;
            background: #2a4b6e;
            padding: 0.5rem;
        }

        /* Golden Eggs decoration */
        .golden-egg {
            position: fixed;
            pointer-events: none;
            font-size: 2rem;
            opacity: 0.2;
            z-index: 0;
            user-select: none;
            animation: floatEgg 6s ease-in-out infinite alternate;
        }
        @keyframes floatEgg {
            0% { transform: translateY(0) rotate(0deg); }
            100% { transform: translateY(-20px) rotate(8deg); }
        }

        /* Contributors grid */
        .contributors {
            padding: 3rem 0;
            position: relative;
            z-index: 1;
        }
        .contributors h2 {
            font-size: 2.5rem;
            border-bottom: 3px solid #c9a84c;
            display: inline-block;
            padding-bottom: 0.25rem;
            margin-bottom: 2rem;
            color: #1e3a5f;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 2rem;
        }
        .card {
            background: #ffffff;
            border-radius: 24px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.08);
            padding: 1.5rem 1.5rem 2rem;
            transition: transform 0.2s ease;
            border: 1px solid #ede6d6;
            position: relative;
        }
        .card:hover {
            transform: translateY(-6px);
            border-color: #c9a84c;
        }
        .card .portrait {
            display: flex;
            justify-content: center;
            margin-bottom: 0.75rem;
        }
        .card .portrait svg {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            background: #eae3d3;
            padding: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .card h3 {
            font-size: 1.5rem;
            color: #1e3a5f;
            margin-bottom: 0.25rem;
        }
        .card .github-link {
            display: inline-block;
            margin: 0.5rem 0 0.75rem;
            color: #1e3a5f;
            font-weight: 600;
            text-decoration: none;
            border-bottom: 2px solid #c9a84c;
        }
        .card .github-link:hover {
            color: #c9a84c;
        }
        .card .facts {
            font-size: 0.95rem;
            color: #3d352b;
            background: #f8f4ea;
            padding: 0.75rem 1rem;
            border-radius: 12px;
            margin-top: 0.5rem;
        }
        .card .facts strong {
            color: #1e3a5f;
        }

        /* Easter egg game */
        .easter-egg-trigger {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 70px;
            height: 70px;
            background: radial-gradient(circle, #ffd966, #b8860b);
            border-radius: 50%;
            border: 4px solid #8b6508;
            box-shadow: 0 0 0 6px rgba(184, 134, 11, 0.3);
            cursor: pointer;
            z-index: 100;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            transition: transform 0.3s;
            color: #fff;
            text-shadow: 0 2px 4px rgba(0,0,0,0.5);
        }
        .easter-egg-trigger:hover {
            transform: scale(1.1) rotate(15deg);
        }
        .easter-game-modal {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.6);
            z-index: 200;
            align-items: center;
            justify-content: center;
        }
        .easter-game-modal.active {
            display: flex;
        }
        .game-box {
            background: #fcf8f0;
            border-radius: 40px;
            padding: 2rem 2.5rem;
            max-width: 500px;
            width: 90%;
            text-align: center;
            box-shadow: 0 20px 60px rgba(0,0,0,0.5);
            border: 4px solid #c9a84c;
            position: relative;
        }
        .game-box h2 {
            font-size: 2rem;
            color: #1e3a5f;
            margin-bottom: 0.5rem;
        }
        .game-box p {
            font-size: 1rem;
            color: #3d352b;
        }
        .game-box .score {
            font-size: 3rem;
            font-weight: bold;
            color

## Verification
- Generated by DevilX auto-claim (OpenRouter/NVIDIA)
- Wed Sep  2 06:02:29 UTC 2026

Closes #2053
