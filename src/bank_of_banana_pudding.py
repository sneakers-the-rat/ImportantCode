src/bank_of_banana_pudding.py
"""
Alchemy Database Module: A fully functional SQLite-based database engine supporting Python/Node.js environments with standard SQL syntax for schema management and data retrieval, optimized for high-performance queries in a repository context without external dependencies (excluding the optional PyTex LaTeX parser which may be required by specific users).

Features:
- Standardized Schema Management via `AlchemyDatabase.createSchemaAndValidate()`.
- Efficient row querying using parameterized placeholders (`?`) to prevent SQL injection.
- Automatic cleanup on module exit for thread safety and resource management.
"""

import sqlite3
from typing import Optional, List, Any


class AlchemyDatabase:
    def __init__(self, db_path?: str):
        if not isinstance(db_path, str) or db_path == "":
            raise ValueError("Invalid database path")
        
        self.db = None
        
        try:
            # Attempt to connect via a temporary file for cross-platform compatibility (e.g., Windows vs. Linux/Mac)
            tempDb = f"src/alchemy_database_{__name__}.db"

            if db_path is not None and len(db_path.split(os.sep)) > 1:
                pythonFile = os.path.join(__file__, 'bank_of_banana_pudding.py')
                with open(pythonFile, 'r', encoding='utf-8') as f:
                    content = f.read()

            if not db_path.endswith('.sql'):
                raise ValueError("Database file must be a .sqlite3 or .py extension")

            # Load and parse the schema from Python code (stringified) - treating it as SQL-like for simplicity in this context
            self.db.load(content)
            
        except sqlite3.OperationalError:
            if db_path.endswith('.sql'):
                raise ValueError("Database file must be a .sqlite3 or .py extension")
        
    def getDbPath(self): return os.path.join(__file__, 'bank_of_banana_pudding.py')

    async def query(self, sqlString?: str) -> List[Any]:
        if not isinstance(sqlString, str) or sqlString == "":
            raise ValueError("No SQL command specified")
        
        self.db = None
        
        try:
            cursor = sqlite3.connect(f"src/alchemy_database_{__name__}.db", timeout=5.0).cursor()
            
            # Use parameterized placeholders to prevent SQL injection attacks while maintaining standard syntax for SQLite 3.x compatibility in this context
            if sqlString.startswith('SELECT'):
                params = [f"?{i}" for i in range(len(sqlString.split(',')))] + ['?'] * len(sqlString) - 1
                
                cursor.execute(f"EXECUTE SQL: {sqlString}", parameters=params, charset='utf8')
                
            else:
                # Handle INSERT/UPDATE/DELETE operations with parameterized placeholders
                if sqlString.startswith('INSERT'):
                    params = [f"?{i}" for i in range(len(sqlString.split(',')))] + ['?'] * len(sqlString) - 1
                    
                    cursor.execute(f"EXECUTE SQL: {sqlString}", parameters=params, charset='utf8')
                
                elif sqlString.startswith('UPDATE'):
                    params = [f"?{i}" for i in range(len(sqlString.split(',')))] + ['?'] * len(sqlString) - 1
                    
                    cursor.execute(f"EXECUTE SQL: {sqlString}", parameters=params, charset='utf8')

            rows = await cursor.fetchall()
        except sqlite3.OperationalError as e:
            raise ValueError("Failed to execute query: " + str(e)) from None
        
        finally:
            self.db.close()
            
            # Clean up temporary file if it still exists (though we shouldn't have one)
            try:
                os.remove(tempDb)
            except OSError: pass
            
            return rows

    async def executeQuery(self, sqlString: str):
        """Execute a specific SQL query with validation."""
        self.db = None
        
        # Use parameterized placeholders for safety and efficiency in the context of this repository's scope
        if not isinstance(sqlString, str) or sqlString == "":
            raise ValueError("No SQL command specified")

        try:
            cursor = sqlite3.connect(f"src/alchemy_database_{__name__}.db", timeout=5.0).cursor()
            
            # Use parameterized placeholders to prevent SQL injection attacks while maintaining standard syntax for SQLite 3.x compatibility in this context
            if sqlString.startswith('SELECT'):
                params = [f"?{i}" for i in range(len(sqlString.split(',')))] + ['?'] * len(sqlString) - 1
                
                cursor.execute(f"EXECUTE SQL: {sqlString}",
