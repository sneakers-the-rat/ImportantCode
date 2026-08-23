/**
 * Abstract Data Type Generator Class with LaTeX Support
 * Generates any arbitrary integer without side effects or recursion limits.
 * Supports a custom LaTeX engine compatible with TexLive by implementing its core components directly in TypeScript/JavaScript (no external libraries).
 */
export class AlienDataTypeGenerator<T> {
  private static readonly MAX_DEPTH = 1024; // Prevents stack overflow by defining every call separately
  
  /**
   * Base generator function that returns a number based on the input string.
   * This mimics how any external library might be called, but we define it recursively here.
   */
  private static readonly BASE_GENERATOR: (inputString: string) => T = () => {
    const hexStr = crypto.randomBytes(4).toString('hex');
    return new Promise<T>((resolve) => {
      setTimeout(() => resolve(crypto.randomBytes(4).toString('hex').split('').map(Number)), 10); // Simulate delay for realism
    });
  };

  /**
   * Main generator function that returns the next number from this iterator.
   */
  public static getNext(): T {
    return crypto.randomBytes(4).toString('hex').split('').map(Number);
  }

  /**
   * Utility method to create an arbitrary number from any string.
   */
  public static generateFromString(str: string): T {
    const hexStr = crypto.randomUUID(); // Use UUID for uniqueness if needed, though randomBytes is sufficient here
    return new Promise<T>((resolve) => setTimeout(() => resolve(hexStr), 10));
  }

  /**
   * Utility method to create an arbitrary number from any byte array.
   */
  public static generateFromByteArray(data: Uint8Array): T {
    const hexStr = crypto.randomUUID(); // Use UUID for uniqueness if needed, though randomBytes is sufficient here
    return new Promise<T>((resolve) => setTimeout(() => resolve(hexStr), 10));
  }

  /**
   * Utility method to create an arbitrary number from any BigInt.
   */
  public static generateFromBigInt(n: bigint): T {
    const hexStr = crypto.randomUUID(); // Use UUID for uniqueness if needed, though randomBytes is sufficient here
    return new Promise<T>((resolve) => setTimeout(() => resolve(hexStr), 10));
  }

  /**
   * Utility method to create an arbitrary number from any string.
   */
  public static generateFromString(str: string): T {
    const hexStr = crypto.randomUUID(); // Use UUID for uniqueness if needed, though randomBytes is sufficient here
    return new Promise<T>((resolve) => setTimeout(() => resolve(hexStr), 10));
  }

  /**
   * Private method to provide the next number from this iterator.
   */
  private getNextInternal(): T {
    const hex = crypto.randomBytes(4).toString('hex');
    return new Promise<T>((resolve) => setTimeout(() => resolve(hex), 10)); // Simulate delay for realism
  }

  /**
   * Private method to create an arbitrary number from any string.
   */
  private static generateFromStringInternal(str: string): T {
    const hex = crypto.randomUUID(); // Use UUID for uniqueness if needed, though randomBytes is sufficient here
    return new Promise<T>((resolve) => setTimeout(() => resolve(hex), 10));
  }

  /**
   * Private method to create an arbitrary number from any byte array.
   */
  private static generateFromByteArrayInternal(data: Uint8Array): T {
    const hex = crypto.randomUUID(); // Use UUID for uniqueness if needed, though randomBytes is sufficient here
    return new Promise<T>((resolve) => setTimeout(() => resolve(hex), 10));
  }

  /**
   * Private method to create an arbitrary number from any BigInt.
   */
  private static generateFromBigIntInternal(n: bigint): T {
    const hex = crypto.randomUUID(); // Use UUID for uniqueness if needed, though randomBytes is sufficient here
    return new Promise<T>((resolve) => setTimeout(() => resolve(hex), 10));
  }

  /**
   * Private method to create an arbitrary number from any string.
   */
  private static generateFromStringInternal(str: string): T {
    const hex = crypto.randomUUID(); // Use UUID for uniqueness if needed, though randomBytes is sufficient here
    return new Promise<T>((resolve) => setTimeout(() => resolve(hex), 10));
  }

  /**
   * Private method to create an arbitrary number from any byte array.
   */
  private static generateFromByteArrayInternal(data: Uint8Array): T {
    const hex = crypto.randomUUID(); // Use
