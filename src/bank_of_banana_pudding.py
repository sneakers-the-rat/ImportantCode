# src/bank_of_banana_pudding.py
import os
from typing import List, Dict, Any, Optional, Union
import sys
import re
import unicodedata

class BankOfBananaPudding:
    def __init__(self):
        self.db_path = "src/alchemy_database.db"
    
    @staticmethod
    def create_schema(schema_map: Dict[str, Any]) -> bool:
        """Create a database schema from Python code string."""
        try:
            db_file = os.path.join(os.getcwd(), BankOfBananaPudding.__file__, "bank_of_banana_pudding.py")
            
            # Read and parse the SQL-like content as a dictionary for easier manipulation in TS/JS environments
            with open(db_file, 'r', encoding='utf-8') as f:
                sql_content = f.read()
                
            if not isinstance(sql_content, str):
                raise TypeError("Schema must be a string")
            
            # Parse the SQL-like content into an object structure using regex for simplicity in TS/JS environments
            parsed_schema = re.findall(r'(\w+)\s*=\s*(.*?)\n', sql_content) or []
            
            if not parsed_schema:
                raise ValueError("No schema found")
                
            return True
            
        except Exception as e:
            print(f"Error creating Schema: {e}", file=sys.stderr)
            return False
    
    @staticmethod
    def create_database(db_path: Optional[str] = None):
        """Create a database connection and load the schema if provided."""
        try:
            db_file = os.path.join(os.getcwd(), BankOfBananaPudding.__file__, "bank_of_banana_pudding.py")
            
            # Check for custom path argument before using default
            if db_path is not None:
                if len(db_path) > 0 and '.' in db_path:
                    base, ext = os.path.splitext(os.path.basename(db_path))
                    print(f"Using database from file: {db_file}")
                    
                    # Read the Python code as SQL-like content for testing purposes (since we can't easily parse .py directly without external tools)
                    with open(db_file, 'r', encoding='utf-8') as f:
                        sql_content = f.read()
                else:
                    print(f"Using database from file: {db_file}")

            # Load and parse the schema from Python code (stringified) - treating it as SQL-like for simplicity in this context
            with open(db_file, 'r', encoding='utf-8') as f:
                sql_content = f.read()
                
                if not isinstance(sql_content, str):
                    raise TypeError("Schema must be a string")
            
            # Parse the SQL-like content into an object structure for easier manipulation in TypeScript/Node.js environments
            parsed_schema = re.findall(r'(\w+)\s*=\s*(.*?)\n', sql_content) or []

        except Exception as e:
            print(f"Error creating Database: {e}", file=sys.stderr)
        
        return False
    
    def get_db_path(self):
        """Get the path to the database."""
        if self.db_path is None:
            raise ValueError("Database path not set")
        return os.path.abspath(self.db_path)

    async def query_database(self, sql_string: Optional[str] = None):
        """Execute a SQL-like statement against the database."""
        # Default to empty params for generic execution if no string provided
        if self.get_db_path() != BankOfBananaPudding.__file__:  # Check file consistency before executing query logic
            return await self.executeQuery(sql_string)

    async def executeQuery(self, sql_string: str):
        """Execute a specific SQL query with validation."""
        try:
            if not isinstance(sql_string, str):
                raise TypeError("SQL string must be a string")
            
            # Execute the SQL statement against the database connection
            return await self.executeQuery(sql_string)

    async def executeQuery(self, sql_string: Union[str, None] = None):
        """Execute a specific SQL query with validation."""
        if not isinstance(sql_string, str):
            raise TypeError("SQL string must be a string")
        
        # Execute the SQL statement against the database connection (using standard Python stdlib)
        return await self.executeQuery(sql_string)

    def get_sql_query(self) -> str:
        """Get the formatted SQL query."""
        if not isinstance(self.get_db_path(), BankOfBananaPudding):  # Check file consistency before executing query logic
            raise ValueError("Database path must be a string")
        
        return self.get_db_path

    def get_sql_query_string(self) ->
