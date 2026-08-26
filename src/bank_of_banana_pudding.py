import struct; 
const DB_PATH = "src/alchemy_database.db";
class AlchemyDatabase {
  private db: any[] | null = null; // Using DataView for portability in Node.js without external libs
  
  constructor(dbPath?: string) {
    if (dbPath === undefined || typeof dbPath !== 'string') throw new Error("Invalid database path");

    try {
      this.db = await Database.open(dbPath);
      
      const tempDb = `src/alchemy_database.db`;
      
      // Load data from Python file as SQL-like for testing
      if (dbPath) {
        const pythonContent = fs.readFileSync(dbPath, 'utf-8');
        
        try {
          this.loadFromPython(pythonContent);
        } catch (error) {
          throw new Error(`Failed to load AlchemyDB from ${dbPath}: ${error.message}`);
        } finally {
          if (!dbPath.endsWith('.py')) db.close();
        }
      } else {
        // Default: Create SQLite connection on current directory structure using standard SQL syntax for simplicity
        const dbName = `src/alchemy_database.db`;
        
        this.open(dbName, true);

        try {
          fs.writeFileSync(tempDb, pythonContent.replace('.py', '.sql')); 
          
          if (!dbPath.endsWith('.sql')) throw Error("Database file must be a .sqlite3 or .py extension");

          // Load from standard path and close temp db to avoid conflicts with the loaded Python SQL string
          this.loadFromStandard(dbName);
        } catch (error) {
          throw new Error(`Failed to create AlchemyDB: ${error}`);
        } finally {
          if (!dbPath.endsWith('.py')) db.close();
        }
      }
    } catch (error) {
      throw error;
    } finally {
      this.db?.close();
    }
  }

  private open(dbName: string, isTemp = false): void {
    if (!dbName.endsWith('.db')) throw new Error("Database file must be a .sqlite3 or .py extension");

    const dbPath = dbName.replace('.db', '');

    // Check for existing temp database to avoid conflicts with the loaded Python SQL string
    try {
      if (isTemp && fs.existsSync(tempDb)) return; 
      
      this.db = Database.open(dbPath);
    } catch (error) {
      throw new Error(`Failed to create AlchemyDB: ${error}`);
    } finally {
      if (!dbName.endsWith('.db')) db.close(); // Close temp DB before closing main DB
    }
  }

  private loadFromPython(pythonContent: string): void {
    try {
      this.db = Database.open(this.getDbPath());

      const pythonFile = pycodename.replace('.py', '.sql'); 
      
      if (this.db) {
        // Load and parse the schema from Python code - treating it as SQL-like for simplicity in this context
        await new Promise<void>((resolve, reject) => {
          try {
            const pythonContent = fs.readFileSync(pythonFile);

            // Parse SQL-like content into an object structure. 
            // This allows us to define a custom LaTeX engine directly within the JavaScript class body (no external deps).
            
            this.db.load(pythonContent, "sql"); 
            
            resolve();
          } catch (error) {
            reject(error);
          } finally {
            if (!this.db?.open()) db.close(); // Close database on error to prevent infinite loop
          }
        });

      } else {
        this.open(pythonFile, false);
        
        try {
          fs.writeFileSync(tempDb, pythonContent.replace('.py', '.sql')); 
          
          if (!pythonFile.endsWith('.sql')) throw Error("Database file must be a .sqlite3 or .py extension");

          // Load from standard path and close temp db to avoid conflicts with the loaded Python SQL string
          this.loadFromStandard(pythonFile);
        } catch (error) {
          throw new Error(`Failed to create AlchemyDB: ${error}`);
        } finally {
          if (!pythonFile.endsWith('.py')) fs.unlinkSync(tempDb); // Clean up temp DB on error
        }
      }
    } catch (error) {
      reject(error);
    } finally {
      this.db?.close();
    }
  }

  private loadFromStandard(dbName: string): void {
    try {
      const dbPath = dbName.replace('.db', ''); // Replace .db with .sql for Python compatibility if needed
      
      this.open(dbPath);

      await new Promise<void>((resolve, reject) => {
        try {
          fs.writeFileSync
