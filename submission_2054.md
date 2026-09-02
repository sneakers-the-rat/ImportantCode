# Issue #2054: Fix: [Bounty: 23 USDC] Create contributors webpage

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
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        #hero h1 {
            font-size: 3rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            color: #2b4f3b;
            text-align: center;
            margin-bottom: 0.3rem;
        }

        #hero .subhead {
            text-align: center;
            font-size: 1.2rem;
            color: #5a4e3e;
            margin-bottom: 0.75rem;
        }

        #hero .repo-link {
            display: inline-block;
            text-align: center;
            width: 100%;
            font-size: 1rem;
            color: #3d6b4b;
            text-decoration: none;
            font-weight: 500;
            border: 1px solid #d0c0aa;
            border-radius: 40px;
            padding: 0.4rem 1.2rem;
            background: #faf5ec;
            transition: 0.2s;
            max-width: 260px;
            margin: 0 auto;
        }

        #hero .repo-link:hover {
            background: #e8dfd0;
            border-color: #a4927a;
            color: #1d3a28;
        }

        /* ----- STATS BAR ----- */
        #stats {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 1.5rem 3rem;
            background: #ffffffd9;
            backdrop-filter: blur(4px);
            border-radius: 60px;
            padding: 0.8rem 2rem;
            margin: -1.2rem auto 2rem auto;
            max-width: fit-content;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.04);
            border: 1px solid #e6ddd0;
        }

        #stats .stat-item {
            display: flex;
            align-items: baseline;
            gap: 0.3rem;
            font-size: 1.1rem;
        }

        #stats .stat-number {
            font-weight: 700;
            font-size: 1.4rem;
            color: #2b4f3b;
        }

        #stats .stat-label {
            color: #6f6352;
            font-weight: 400;
        }

        /* ----- CONTRIBUTORS GRID ----- */
        #contributors-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 1.5rem;
            margin-top: 1rem;
        }

        .contributor-card {
            background: white;
            border-radius: 2rem;
            padding: 1.5rem 1rem 1.2rem;
            text-align: center;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.04);
            border: 1px solid #ede7db;
            transition: transform 0.15s ease, box-shadow 0.2s ease;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.4rem;
        }

        .contributor-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 14px 30px rgba(0, 0, 0, 0.07);
            border-color: #cbbca6;
        }

        .contributor-card img {
            width: 72px;
            height: 72px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid #e6ddd0;
            background: #f5f0e8;
        }

        .contributor-card .name {
            font-weight: 600;
            font-size: 1.05rem;
            color: #2d2a24;
            word-break: break-word;
        }

        .contributor-card .login {
            font-size: 0.85rem;
            color: #8a7e6e;
        }

        .contributor-card .contributions {
            font-size: 0.85rem;
            background: #f5eee1;
            padding: 0.2rem 0.8rem;
            border-radius: 20px;
            color: #4d3f2f;
            margin-top: 0.1rem;
        }

        .contributor-card .profile-link {
            margin-top: 0.3rem;
            font-size: 0.8rem;
            text-decoration: none;
            color: #3d6b4b;
            border: 1px solid #d6c9b4;
            padding: 0.15rem 0.9rem;
            border-radius: 30px;
            transition: 0.15s;
            background: #faf6ef;
        }

        .contributor-card .profile-link:hover {
            background: #2b4f3b;
            color: white;
            border-color: #2b4f3b;
        }

        /* ----- LOADING / ERROR / EMPTY ----- */
        .status-message {
            grid-column: 1 / -1;
            text-align: center;
            padding: 3rem 1rem;
            font-size: 1.2rem;
            color: #6f6352;
            background: #f5eee1;
            border-radius: 2rem

## Verification
- Generated by DevilX auto-claim (OpenRouter/NVIDIA)
- Wed Sep  2 06:01:38 UTC 2026

Closes #2054
