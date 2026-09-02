# Issue #2054: Fix: [Bounty: 23 USDC] Create contributors webpage

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
            margin: 0 auto;
            opacity: 0.3;
        }

        /* ----- CONTRIBUTORS GRID ----- */
        #contributors {
            background: white;
            border-radius: 2rem 2rem 0 0;
            padding: 2rem 1.5rem;
            box-shadow: 0 8px 24px rgba(0,0,0,0.04);
        }
        #contributors h2 {
            font-size: 1.8rem;
            font-weight: 600;
            color: #2b4f3b;
            margin-bottom: 0.25rem;
        }
        #contributors .subhead {
            color: #7a6e5a;
            margin-bottom: 2rem;
            font-size: 1rem;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 1.5rem;
        }
        .contributor-card {
            background: #fcf9f4;
            border-radius: 1.5rem;
            padding: 1.5rem 1rem;
            text-align: center;
            transition: transform 0.15s ease, box-shadow 0.15s ease;
            border: 1px solid #ede8dd;
        }
        .contributor-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 24px rgba(0,0,0,0.06);
        }
        .contributor-card img {
            width: 72px;
            height: 72px;
            border-radius: 50%;
            object-fit: cover;
            background: #e8e0d2;
            margin-bottom: 0.75rem;
            border: 2px solid white;
            box-shadow: 0 2px 6px rgba(0,0,0,0.06);
        }
        .contributor-card .name {
            font-weight: 600;
            font-size: 1.05rem;
            color: #2d2a24;
            word-break: break-word;
        }
        .contributor-card .contributions {
            font-size: 0.85rem;
            color: #7a6e5a;
            margin-top: 0.25rem;
        }
        .contributor-card .login {
            font-size: 0.8rem;
            color: #a0947c;
            margin-top: 0.1rem;
        }

        /* ----- LOADING & ERROR ----- */
        .status {
            text-align: center;
            padding: 3rem 1rem;
            font-size: 1.1rem;
            color: #5a4e3e;
        }
        .status .spinner {
            display: inline-block;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            border: 4px solid #ede8dd;
            border-top-color: #2b4f3b;
            animation: spin 0.8s linear infinite;
            margin-bottom: 0.75rem;
        }
        @keyframes spin { to { transform: rotate(360deg); } }

        /* ----- FOOTER ----- */
        footer {
            margin-top: 3rem;
            text-align: center;
            font-size: 0.9rem;
            color: #b0a492;
            border-top: 1px solid #ede8dd;
            padding-top: 2rem;
        }
        footer a {
            color: #2b4f3b;
            text-decoration: none;
        }
        footer a:hover {
            text-decoration: underline;
        }

        /* responsive */
        @media (max-width: 600px) {
            #hero h1 { font-size: 2.2rem; }
            .grid { grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- HERO -->
        <div id="hero">
            <h1>🌿 AgentPipe</h1>
            <p>Built by a community of contributors</p>
            <svg class="hero-svg" viewBox="0 0 900 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M0 20 C 150 0, 300 40, 450 20 C 600 0, 750 40, 900 20" stroke="#2b4f3b" stroke-width="2" stroke-dasharray="6 6"/>
            </svg>
        </div>

        <!-- CONTRIBUTORS SECTION -->
        <div id="contributors">
            <h2>All contributors</h2>
            <p class="subhead">People who have helped shape AgentPipe</p>
            <div id="grid-container" class="grid" role="list">
                <div class="status">
                    <div class="spinner"></div>
                    <div>Loading contributors…</div>
                </div>
            </div>
        </div>

        <footer>
            <p>Data from <a href="https://github.com/agentpipe/agentpipe" target="_blank" rel="noopener">GitHub</a> &middot; Thank you to everyone who contributes!</p>
        </footer>
    </div>

    <script>
        (function() {
            const container = document.getElementById('grid-container');

            // Replace with the actual repo owner and name if different
            const REPO_OWNER = 'agentpipe';
            const REPO_NAME  = 'agentpipe';

            async function fetchContributors() {
                try {
                   

## Verification
- Generated by DevilX auto-claim (OpenRouter/NVIDIA)
- Wed Sep  2 12:03:02 UTC 2026

Closes #2054
