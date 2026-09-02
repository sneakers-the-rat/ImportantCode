# Issue #2056: Fix: [Bounty: 23 USDC] Create contributors webpage

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
            padding: 3rem 0 2.5rem;
            text-align: center;
            border-bottom: 6px solid #c9a84c;
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
            align-items: center;
            gap: 0.75rem;
            margin-top: 1.5rem;
            flex-wrap: wrap;
        }
        .hero-factory span {
            background: rgba(255,255,255,0.08);
            padding: 0.3rem 1rem;
            border-radius: 40px;
            font-size: 0.85rem;
            letter-spacing: 1px;
            border: 1px solid rgba(201,168,76,0.4);
        }

        /* Controls */
        .controls {
            background: #fff;
            padding: 1.5rem 0;
            border-bottom: 1px solid #e8e0d4;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
        }
        .controls .search-box {
            flex: 1;
            min-width: 200px;
            display: flex;
            gap: 0.5rem;
            align-items: center;
        }
        .controls .search-box input {
            width: 100%;
            padding: 0.6rem 1rem;
            border: 1px solid #d6cec0;
            border-radius: 40px;
            font-size: 1rem;
            background: #fcf8f0;
            outline: none;
            transition: 0.2s;
        }
        .controls .search-box input:focus {
            border-color: #1e3a5f;
            box-shadow: 0 0 0 3px rgba(30,58,95,0.15);
        }
        .controls .stats {
            font-size: 0.95rem;
            color: #5e5546;
            white-space: nowrap;
        }
        .controls .stats strong {
            color: #1e3a5f;
        }

        /* Grid */
        .contributors-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 1.5rem;
            padding: 2.5rem 0 4rem;
        }
        .contributor-card {
            background: #fff;
            border-radius: 16px;
            padding: 1.5rem 1rem 1.2rem;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            border: 1px solid #ede7db;
            transition: transform 0.15s, box-shadow 0.15s;
        }
        .contributor-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 24px rgba(0,0,0,0.07);
            border-color: #c9a84c;
        }
        .contributor-card img {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            object-fit: cover;
            background: #ede7db;
            border: 2px solid #fcf8f0;
            box-shadow: 0 0 0 1px #d6cec0;
        }
        .contributor-card .name {
            margin-top: 0.75rem;
            font-weight: 600;
            font-size: 1.05rem;
            color: #1e3a5f;
        }
        .contributor-card .login {
            font-size: 0.85rem;
            color: #7a7060;
            margin-top: 0.1rem;
        }
        .contributor-card .contributions {
            margin-top: 0.5rem;
            font-size: 0.8rem;
            background: #f5f0e8;
            display: inline-block;
            padding: 0.2rem 0.8rem;
            border-radius: 40px;
            color: #4d4436;
        }
        .contributor-card a {
            text-decoration: none;
            color: inherit;
            display: block;
        }

        /* Loading & empty */
        .loading, .empty {
            grid-column: 1 / -1;
            text-align: center;
            padding: 4rem 0;
            color: #7a7060;
            font-size: 1.1rem;
        }
        .loading .spinner {
            display: inline-block;
            width: 28px;
            height: 28px;
            border: 3px solid #ede7db;
            border-top-color: #1e3a5f;
            border-radius: 50%;
            animation: spin 0.8s linear infinite;
            margin-bottom: 0.75rem;
        }
        @keyframes spin { to { transform: rotate(360deg); } }

        /* Footer */
        .footer {
            border-top: 1px solid #ede7db;
            padding: 2rem 0;
            text-align: center;
            color: #7a7060;
            font-size: 0.9rem;
        }
        .footer a {
            color: #1e3a5f;
            text-decoration: none;
            font-weight: 500;
        }
        .footer a:hover {
            text-decoration: underline;
        }

        @media (max-width: 600px) {
            .hero h1 { font-size: 2.2rem; }
            .controls { flex-direction: column; align-items: stretch; }
            .controls .stats { text-align: right; }
            .contributors-grid { grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 1rem; }
        }
    </style>
</head>
<body>

    <header class="hero">
        <div class="container">
            <h1>⚙️ Contributors</h1>
            <p>People who help build AgentPipe</p>
            <div class

## Verification
- Generated by DevilX auto-claim (OpenRouter/NVIDIA)
- Wed Sep  2 12:01:23 UTC 2026

Closes #2056
