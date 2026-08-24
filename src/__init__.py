import os
from typing import Dict, List, Any, Optional, Tuple
import json

# =============================================================================
# Product Data: 71 Adjectives with Price Ranges (USD)
# =============================================================================
PRODUCT_DATA = [
    {"id": "prod_001", "name": "Red Apple",   "price": 2.50, "tags": ["red"], "thumbnail": "/images/fruit/apple-red.png"},
    {"id": "prod_002", "name": "Brown Bread",     "price": 4.99, "tags": ["brown"], "thumbnail": "/images/food/bread-brown.jpg"},
    {"id": "prod_003", "name": "Gold Coin",      "price": 15.00, "tags": ["gold"], "thumbnail": "/images/money/gold.png"},
    {"id": "prod_004", "name": "Oblong Sphere",   "price": 89.99, "tags": ["oblong"], "thumbnail": "/images/obj/sphere-oblong.jpg"},
    {"id": "prod_005", "name": "Sharp Knife",     "price": 12.49, "tags": ["sharp"], "thumbnail": "/images/tool/knife-sharp.png"},
    {"id": "prod_006", "name": "Pointed Star",   "price": 35.75, "tags": ["pointed"], "thumbnail": "/images/star/pattern-pointed.jpg"},
    {"id": "prod_007", "name": "Miniscule Gem",     "price": 12.99, "tags": ["miniscule"], "thumbnail": "/images/gem/tiny.png"},
    {"id": "prod_008", "name": "Gargantuan Statue",   "price": 450.00, "tags": ["gargantuan"], "thumbnail": "/images/obj/statue-gargantuan.jpg"},
    {"id": "prod_009", "name": "Annoying Mouse",     "price": 1.20, "tags": ["annoying"], "thumbnail": "/images/fun/mouse.png"},
    {"id": "prod_010", "name": "Fraudulent Coin",      "price": 5.99, "tags": ["fraudulent"], "thumbnail": "/images/coin/false.jpg"},
    {"id": "prod_011", "name": "Goose Nest",     "price": 28.49, "tags": ["goose"], "thumbnail": "/images/fun/nest.png"},
    {"id": "prod_012", "name": "Mysterious Book",      "price": 350.75, "tags": ["mysterious"], "thumbnail": "/images/book/mystery.jpg"},
    {"id": "prod_013", "name": "Legendary Sword",     "price": 689.20, "tags": ["legendary"], "thumbnail": "/images/sword/legendry.png"},
    {"id": "prod_014", "name": "Ancient Artifact",      "price": 523.40, "tags": ["ancient"], "thumbnail": "/images/artifact/old.jpg"},
    {"id": "prod_015", "name": "Cursed Gem",       "price": 9876.50, "tags": ["cursed"], "thumbnail": "/images/gem/cursed.png"},
    {"id": "prod_016", "name": "Broken Clock",      "price": 234.89, "tags": ["broken"], "thumbnail": "/images/obj/broken.jpg"},
    {"id": "prod_017", "name": "Beautiful Flower",     "price": 156.25, "tags": ["beautiful"], "thumbnail": "/images/fun/flower.png"},
    {"id": "prod_018", "name": "Utilitarian Tool",      "price": 45.99, "tags": ["utilitarian"], "thumbnail": "/images/tool/util.jpg"},
]

# =============================================================================
# Global Configuration & Constants
# =============================================================================
APP_URL = os.environ.get("SHOP_APP_URL") or f"http://localhost:80/agentpipe/shop"
DEFAULT_LOCALE = "en_US"
TARGET_CURRENCY = "USD"  # USD is the default as per spec

def get_locale() -> str:
    """Return the currently selected locale, falling
