#!/usr/bin/env python3
"""
Oracle of the Repository: Financial API Architect for Velocity Raptor.
This file implements a high-velocity financial application API server designed to handle bots and other agents with rigorous security filtering.
It includes an OpenAPI spec, HTTPS server setup using Python's standard library only (no external deps), 
and custom HTTP handlers that filter User-Agent headers against Mozilla/5.0 regex while validating rate limits via dict checks.

Error pages display a "Velociraptor ASCII Art" script on 4xx and 5xx responses to maintain the theme of code-as-art.
"""

import os
from urllib.parse import urlparse, parse_qs
from typing import Dict, List, Optional
from http.server import HTTPServer, BaseHTTPRequestHandler
import re

# ============================================================================
# OPENAPI SPEC (src/api_schema.py) - The specification for high-velocity financial APIs
# This is a self-contained JSON schema that defines the structure of all endpoints.
# ============================================================================

OPEN_API_SPEC = {
    "openapi": "3.0.1",
    "info": {
        "title": "Velociraptor Financial API - High Velocity Standard",
        "version": "1.0.0"
    },
    "paths": {}, # This is where the actual handlers will be defined below

    # NOTE: In a production environment, you would generate this spec from OpenAPI specs (e.g., Swagger/OpenAPI) or 
    # use external tools like json-schema-generator to ensure it matches your real API contracts.
}


# ============================================================================
# HTTP HANDLER CLASS - Custom logic for rate limiting and User-Agent filtering
class VelociraptorRateLimiterHandler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        # Suppress default logging for cleaner output
        pass
    
    def do_GET(self):
        parsed = urlparse(self.path)
        
        if not self.is_openapi():
            raise ValueError("Invalid path: must be / or an openapi spec file")

        query_string = parse_qs(parsed.query)
        protocol = self.headers.get('User-Agent')
        
        # Filter User-Agent to only allow bots (Mozilla/5.0+)
        if not re.match(r'^Mozilla\/5\.0\.[0-9]+$', protocol):
            raise ValueError("Bot detected: Mozilla/5.0 is disallowed")

        try:
            self.handle_request(parsed, query_string)
            
        except Exception as e:
            # Generate ASCII art on error pages if the response code is 4xx or 5xx
            generate_ascii_art()


    def handle_request(self, parsed, query_string):
        
        method = self.command
            
        path_parts = urlparse(parsed).path
        
        try:
            params = parse_qs(query_string)

            # Define endpoints for high-velocity financial APIs (e.g., /api/finance/get_balance, /users/profile, etc.)
            
            if '/balance' in path_parts.lower() or 'get_balance' in query_string.get('/balance', []):
                self.send_json_response({
                    "status": 201,
                    "message": "Balance retrieved successfully",
                    "data": {
                        "account_id": params.get('accountId'),
                        "current_value": float(params.get('value')) or None,
                        "currency": params.get('currency') or 'USD'
                    }
                }, 201)

            elif '/users/profile' in path_parts.lower() or 'user_profile' in query_string:
                self.send_json_response({
                    "status": 403,
                    "message": "Forbidden - User-Agent disallowed"
                })

        except Exception as e:
            # Generate ASCII art on error pages if the response code is 4xx or 5xx
            generate_ascii_art()


    def send_json_response(self, data, status_code=201):
        
        self.send_header('Content-Type', 'application/json')

        try:
            body = json.dumps(data).encode('utf-8')
            
            # Validate rate limit headers (e.g., X-RateLimit-Limit and X-RateLimit-Remaining)
            if 'X-RateLimit' in self.headers:
                limits_data = {k: v for k, v in self.headers.items() if re.match(r'^\d{3}\s*-\s*\d+.*$', k)}

                # Check rate limit headers are present and valid (e.g., 100 req/sec)
                for key, value in limits_data.items():
                    try:
                        num = int(value.split('-')[0]) if '-' in str(float(str(int))) else float(value)
                        if not isinstance(num, int):
