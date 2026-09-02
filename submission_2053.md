# Issue #2053: [Bounty: 23 USDC] Create contributors webpage

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AgentPipe Contributors</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            background: #0a0a1a;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #f0e8d0;
            overflow-x: hidden;
        }
        .container {
            max-width: 1300px;
            margin: 0 auto;
            padding: 0 20px;
        }
        /* Golden eggs decorations */
        .golden-egg {
            position: fixed;
            width: 24px;
            height: 32px;
            background: radial-gradient(ellipse at 30% 30%, #ffe87c, #d4a017);
            border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
            box-shadow: 0 0 12px #ffd70088, inset -4px -4px 8px #a67c00, inset 4px 4px 8px #fff6b0;
            z-index: 0;
            pointer-events: none;
            transform: rotate(var(--rot, 0deg));
        }
        .golden-egg::after {
            content: '';
            position: absolute;
            top: 8%;
            left: 22%;
            width: 30%;
            height: 12%;
            background: radial-gradient(circle, #fffbe6, transparent);
            border-radius: 50%;
            opacity: 0.7;
        }
        /* number 71 hidden counters */
        .number-71 {
            display: none;
        }
        /* hero */
        .hero {
            position: relative;
            background: linear-gradient(145deg, #1a2a1a, #0f1a0f);
            border-radius: 32px;
            padding: 40px 20px 60px;
            margin: 30px 0 50px;
            text-align: center;
            border: 2px solid #d4a01766;
            box-shadow: 0 0 60px #ffd70022;
            z-index: 1;
        }
        .hero h1 {
            font-size: 3.8rem;
            font-weight: 800;
            letter-spacing: 2px;
            background: linear-gradient(180deg, #ffe68f, #c99f1e);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 30px #ffd70044;
            margin-bottom: 12px;
        }
        .hero p {
            font-size: 1.3rem;
            color: #cbb88a;
            margin-bottom: 30px;
        }
        .factory-scene {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            max-width: 900px;
            margin: 0 auto;
            background: #1f2a1a;
            border-radius: 40px;
            padding: 20px;
            border: 1px solid #5a7a3a;
        }
        .factory-scene svg {
            width: 100%;
            height: auto;
            max-height: 320px;
            display: block;
            border-radius: 20px;
        }
        /* contributors grid */
        .contributors {
            position: relative;
            z-index: 1;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 30px;
            margin: 40px 0 60px;
        }
        .contributor-card {
            background: linear-gradient(160deg, #1c1c2e, #12121e);
            border-radius: 28px;
            padding: 24px 20px 20px;
            border: 1px solid #d4a01755;
            box-shadow: 0 8px 30px #00000066;
            transition: transform 0.25s ease, box-shadow 0.3s ease;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            backdrop-filter: blur(2px);
        }
        .contributor-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 16px 50px #ffd70033;
            border-color: #ffd700aa;
        }
        .portrait {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            background: #1e2a1e;
            border: 3px solid #d4a017;
            margin-bottom: 16px;
            overflow: hidden;
            flex-shrink: 0;
        }
        .portrait svg {
            width: 100%;
            height: 100%;
            display: block;
        }
        .contributor-card h3 {
            font-size: 1.5rem;
            color: #f5e6b0;
            margin-bottom: 6px;
        }
        .contributor-card .username {
            font-size: 0.95rem;
            color: #aabbcc;
            margin-bottom: 10px;
        }
        .contributor-card .username a {
            color: #d4a017;
            text-decoration: none;
            border-bottom: 1px dashed #d4a01766;
        }
        .contributor-card .username a:hover {
            color: #ffe68f;
            border-bottom-color: #ffe68f;
        }
        .facts {
            font-size: 0.95rem;
            line-height: 1.6;
            color: #cdc2a8;
            background: #0a0a14aa;
            padding: 12px 14px;
            border-radius: 16px;
            width: 100%;
            margin: 10px 0 12px;
            border-left: 3px solid #d4a017;
            text-align: left;
        }
        .facts span {
            display: block;
        }
        .facts .label {
            color: #b8942a;
            font-weight: 600;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        /* footer */
        .footer {
            position: relative;
            z-index: 1;
            background: linear-gradient(180deg, #12121e, #08080e);
            border-radius: 40px 40px 0 0;
            padding: 40px 30px 30px;
            margin-top: 30px;
            border-top: 2px solid #d4a01766;
        }
        .footer h2 {
            color: #f5e6b0;
            font-size: 1.8rem;
            text-align: center;
            margin-bottom: 20px;
        }
        .contact-grid {
            display: flex;
            flex-wrap: wrap;
           

## Verification
- Generated by DevilX auto-claim (OpenRouter/NVIDIA)
- Wed Sep  2 18:01:59 UTC 2026

Closes #2053
