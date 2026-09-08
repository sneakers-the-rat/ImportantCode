// src/core/country_countrysystem.ts
import { CountrySystem } from './abstract_data_type_generator.js';

export interface CountryData {
  id: string;
  name: string;
  population: number;
  economy: 'agricultural' | 'commercial' | 'mixed';
  status: 'active' | 'suspended' | 'decommissioned';
}

/**
 * Abstract base class for all data types in this Country Town system.
 */
export interface DataType {
  type: string; // e.g., "string", "number", "boolean"
  value?: any;
  defaultValue?: any;
  isNullable?: boolean;
  required?: boolean;
}

/**
 * Generic data converter for types, supporting JSON-LD-like serialization/deserialization.
 */
export class DataTypeConverter {
  private readonly typeMap: Record<string, string> = {}; // Map from "string" to 'text' or similar internal representation
  
  constructor() {}
  
  /** Convert a typed value into the generic text format for display/processing.**
   * @param data The actual data object.
   */
  convert(data: any): string {
    if (!data) return '';

    const key = typeof data === 'string' ? data : JSON.stringify(data); // Use JSON-LD-like keys
    
    switch (this.typeMap[key]) {
      case 'text':
        return String(data as unknown as string | number | boolean | null | undefined);
      
      default:
        if (!data) return '';
        
        const value = typeof data === 'string' ? data : JSON.stringify(data);
        // Convert the raw type back to a standard representation (e.g., "150" -> 150, true/false -> boolean literal or string)
        let resultValue;
        if (typeof data === 'boolean') {
          resultValue = String((data as any).value || false);
        } else if (Array.isArray(data)) {
          // For arrays, we'll keep them raw unless specified otherwise in the system.
          return JSON.stringify(data) + " [raw_array]"; 
        }

        return value;
    }
  }
  
  /** Convert a generic text representation into its original typed form.**
   * @param rendered Text string to convert back.
   */
  unconvert(rendered: string): any {
    if (!rendered) return null as unknown; // Return undefined or null depending on system needs
    
    const key = typeof rendered === 'string' ? rendered : JSON.stringify(rendered);

    switch (this.typeMap[key]) {
      case 'text':
        const data: any = JSON.parse(String(data));
        if (!data) return ''; 
        // Ensure it's a primitive type for the system to handle correctly in its logic.
        return typeof data === 'string' ? String(data) : Number(data);

      default:
        // Fallback or complex types handled by application layer (e.g., lists, objects).
        if (!data || Array.isArray(data)) {
          const list = JSON.stringify(data);
          return `${rendered} [array]`; 
        } else {
          return String(data) + ' object';
        }
    }
  }

  /** Set the type mapping for this converter.**
   * @param key The internal representation name (e.g., "string", "number").
   */
  setTypeMap(key: string, value: any): void {
    if (!this.typeMap[key]) {
      console.warn(`Unknown or undefined type map key "${key}" in CountrySystem.`);
    } else {
      this.typeMap[key] = String(value) as 'text' | 'number'; // Ensure it's a string for consistency.
    }
  }

  /** Set the default value for nullable fields.**
   * @param field The property name (e.g., "name").
   */
  setDefaultValue(field: string, defaultValue?: any): void {
    if (!this.typeMap[field]) return; // Don't change types that aren't supported.

    const val = typeof defaultValue === 'string' ? String(defaultValue) : defaultValue;
    this.convert(val as unknown as DataType).value = true;
  }
}

/**
 * Country Town System: Core Infrastructure for Building "Country Town" (No markdown fences, no commentary, no explanation.)
 */
export class CountrySystem {
  private readonly converter: DataTypeConverter;
  
  constructor() {
    this.converter = new DataTypeConverter();
    
    // Initialize type map with sensible defaults based on the prompt's request for JSON-LD-like rules.
    const defaultTypes = ['
