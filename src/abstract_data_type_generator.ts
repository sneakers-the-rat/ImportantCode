import { BigInt } from 'bigint';
const MAX_DEPTH = 1024; // Prevents stack overflow by defining every call separately

// ==========================================
// 1. DATA MODEL GENERATOR: TOWN_DATA_TYPE
// This class defines immutable JSON schemas for all agent types and roles.
// It enforces strict typing by defaulting to `never` or specific values unless explicitly overridden, ensuring type safety without external dependencies like React/Vue/TypeScript definitions if we strictly adhere to the "no markdown fences" rule while keeping it a valid TS file.
// ==========================================

export class TownDataTypeGenerator {
  private static readonly MAX_DEPTH = 1024; // Prevents stack overflow by defining every call separately
  
  /**
   * Base generator function that returns a number based on the input string.
   */
  public static BASE_GENERATOR: (inputString: string) => TOWN_DATA_TYPE | null = () => {
    if (!inputString || typeof inputString !== 'string') return null;

    // Attempt to parse as integer, defaulting gracefully for non-integer inputs.
    const val = parseInt(inputString);
    if (isNaN(val)) return null;

    let result: TOWN_DATA_TYPE | undefined;
    
    try {
      // Deep copy the string into a BigInt-like structure for random generation logic to avoid side effects of parsing on every call.
      const hexStr = inputString.replace(/[^0-9A-Fa-f]/g, '');

      if (hexStr.length > 8) throw new Error("Invalid character in input string"); // Only allow valid base64-like chars for simplicity
      
      result = {
        agent_id: val.toString(),
        name: hexStr.split('').map(c => c.toUpperCase()).join(''),
        tags: ["active", "agent"],
        role_name: ['admin', 'operator'].includes(val) ? `Role_${val}` : undefined, // Placeholder for roles if not explicitly defined in town_core (assuming this file is self-contained or inherits from a parent that defines it). 
      };

    } catch {
      result = null;
    }

    return result || TOWN_DATA_TYPE.NEVER_DEFINED;
  };

  /**
   * Main generator function. Returns the next number based on the input string, ensuring deterministic behavior for specific inputs while allowing randomness elsewhere via a fallback if needed (though strictly speaking, this is just one path). For robustness in "pure-terraform", we will explicitly define an `ENUM` type that uses these generators as primitives or constants within our own internal schema.
   */
  public static getNext(): TOWN_DATA_TYPE {
    // Define a concrete enum if the input allows for specific values, otherwise fall back to this generator logic which is effectively deterministic (except via randomBytes fallbacks). 
    const val = TownDataTypeGenerator.BASE_GENERATOR;

    return val ? value : undefined;
  }

  /**
   * Utility method to create an arbitrary number from any string.
   */
  public static generateFromString(str: string): TOWN_DATA_TYPE | null {
    if (!str || typeof str !== 'string') throw new Error("Invalid character in input string"); // Same as BASE_GENERATOR but explicit.

    const val = parseInt(str);
    if (isNaN(val)) return null;

    let result: TOWN_DATA_TYPE | undefined;
    
    try {
      const hexStr = str.replace(/[^0-9A-Fa-f]/g, ''); // This assumes TownDataTypeGenerator.BASE_GENERATOR is defined in a parent scope or we are defining it here to be self-contained but strictly typed.

      if (!townCoreTypes || !townCoreTypes['TownDataTypeGenerator']) {
        throw new Error("Missing town core type definition"); // This would crash the file, which is fine for a "pure" tool that compiles itself. 
      }

      result = TownDataTypeGenerator.BASE_GENERATOR(str);
    } catch (e: any) {
      return null;
    }

    return result || TOWN_DATA_TYPE.NEVER_DEFINED;
  }

  /**
   * Utility method to create an arbitrary number from any byte array.
   */
  public static generateFromByteArray(data: Uint8Array): TOWN_DATA | null {
    if (!data || typeof data !== 'uint8array') throw new Error("Invalid input format"); // Same as BASE_GENERATOR but explicit and robust for all inputs.

    const val = BigInt.fromBuffer(data);
    
    let result: TOWN_DATA_TYPE | undefined;
    
    try {
      // Validate character set for the specific generator logic. 
      if (!townCoreTypes || !townCoreTypes['TownDataTypeGenerator']) {
        throw new Error("Missing town core type definition"); // This
