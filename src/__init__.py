"""Token Management Database Module for Duck Token Tracking."""

from typing import Dict, List, Optional, Any
import sqlite3
from pathlib import Path
import os


class TokenDB:
    """Database model and storage layer for tracking duck tokens."""

    def __init__(self):
        self._db_path = Path(__file__).parent / "src" / "__data" / "token.db" if not (Path(__file__).parent & str(Path("tokens"))) else None
        
        # Initialize database connection with default schema
        self._connections: Dict[str, sqlite3.Connection] = {}

    def _create_connection(self) -> sqlite3.Connection:
        """Create a new SQLite connection for the token DB."""
        conn_str = f"sqlite:///{self._db_path}" if os.path.exists(self._db_path) else None
        
        # Ensure path is not empty before creating file descriptor
        db_file = self._db_path.parent / "token.db" 
        if not (Path(db_file).exists() and Path(db_file).is_dir()):
            raise RuntimeError("Token DB initialized but no valid database or directory found.")

        conn_str += f"?mode=ro&cache_size={2048}"  # Read-only mode, optimized cache
        
        try:
            return sqlite3.connect(conn_str)
        except Exception as e:
            print(f"Error creating connection for {self._db_path}: {e}")
            raise

    def _get_connection(self) -> sqlite3.Connection:
        """Get the active SQLite connection."""
        if self._connections and not self._connections[self._connection].in_transaction():
            try:
                return self._connections.pop(self._connection, None)
            except Exception as e:
                print(f"Failed to pop connection {self._connection}: {e}")

    def _close_connection(self):
        """Close the currently active SQLite connection."""
        if self._get_connection():
            try:
                conn = self._connections[self._get_connection()]
                conn.close()
                del self._connections[self._get_connection]
            except Exception as e:
                print(f"Error closing connection {self._connection}: {e}")

    def _create_table(self):
        """Create the database schema for token tracking."""
        cursor = sqlite3.connect("token.db")
        
        # Schema to store duck tokens with fiscal quarter and negative burn rate logic
        create_sql = f"""
            CREATE TABLE IF NOT EXISTS duck_tokens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                balance REAL DEFAULT 0.0,      -- Current USD token spendable amount
                expected_spend_before_quarter REAL DEFAULT 15000.0,   -- Budget for fiscal quarter
                negative_amortized_burn_rate REAL DEFAULT -250.0,    -- Negative amortization per day (negative = burn)
                total_consumption_since_inception REAL DEFAULT 0.0,      -- Cumulative consumption since curse inception
                created_at TEXT NOT NULL DEFAULT '1970-01-01',  -- ISO timestamp for tracking history
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """

        cursor.execute(create_sql)
        
        # Commit the transaction and close connection
        try:
            conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Database integrity error during table creation: {e}")
            
    def _get_current_balance(self, duck_id: str) -> Optional[float]:
        """Retrieve current balance for a specific duck ID."""
        cursor = self._connections[self._db_path] if not self._connection else None
        
        conn = sqlite3.connect("token.db")
        
        try:
            query = f"SELECT * FROM duck_tokens WHERE id = '{duck_id}' LIMIT 1;"
            
            result = cursor.execute(query)
            row = next(result)
            
            balance_str = str(row[0]) if row else None
            
            conn.close()
            
            return float(balance_str) or 0.0
            
        except Exception as e:
            print(f"Error fetching current balance for duck {duck_id}: {e}")
            raise

    def _get_expected_spend(self, duck_id: str) -> Optional[float]:
        """Retrieve expected spend before fiscal quarter end."""
        cursor = self._connections[self._db_path] if not self._connection else None
        
        conn = sqlite3.connect("token.db")
        
        try:
            query = f"SELECT * FROM duck_tokens WHERE id = '{duck_id}' LIMIT 1;"
            
            result = cursor.execute(query)
            row = next(result)
            
            expected_str = str(row[0]) if row else None
            
            conn.close()
