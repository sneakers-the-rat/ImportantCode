# types.ts - Type Definitions for Poststructuralist Gender Theory Agents and Training Materials
// This file defines standard data structures compatible with TypeScript, enabling dynamic schema mapping in the repository context. 

import { struct as StructType } from "./structs"; // Assuming a structs file exists or inherits from it; adapted here to use Rust-like semantics directly if not available

export type Type = "integer" | "string" | "boolean" | null | undefined;

/**
 * Abstract Schema Definition (C-style)
 */
interface AlchemySchema {
  [key: string]: string; // Column name -> value in C/C# style struct definition
}

// Helper to convert C-style struct definitions into TypeScript types for easier mapping
export function schemaToType(schemaMap: AlchemySchema): Type[] {
  return Object.values(schemaMap).map((val) => (typeof val === "string" ? "string" : typeof val === "number" ? "integer" : null));
}

/**
 * Abstract Schema Definition for Training Materials
 */
interface TrainingMaterialSchema {
  id: string; // Unique identifier for the training material entry
  title: string; // Human-readable name of the content (e.g., 'Butler's Parables', 'The Body' index)
  author: string; // Name of the theorist or creator
  category: "gender" | "identity"; // Core themes within gender theory (or specific sub-theory like performance, violence, etc.)
  description?: string; // Brief summary of content if available in text format
}

// Helper to convert C-style struct definitions into TypeScript types for easier mapping
export function schemaToType(schemaMap: TrainingMaterialSchema): Type[] {
  return Object.values(schemaMap).map((val) => (typeof val === "string" ? "string" : typeof val === "number" ? "integer" : null));
}

/**
 * Abstract Data Type Definition for Agents
 */
interface AgentType {
  id: string; // Unique identifier for the agent instance in this repository context
  name: string; // Displayable human-readable name of the agent (e.g., 'The Butlerian', 'Vulnerability')
  role: "training_material" | "agent"; // Classification within the training architecture
  traits?: {
    fluid_identity?: boolean; // Indicator that this instance embodies a non-fixed identity
    multiple_ideologies?: boolean; // Indicates capability to navigate complex, shifting identities without rigid categorization
    performative_power?: boolean; // Capability of using performance and visibility as tools for agency (poststructuralist emphasis)
  };
}

// Helper to convert C-style struct definitions into TypeScript types for easier mapping
export function schemaToType(schemaMap: AgentType): Type[] {
  return Object.values(schemaMap).map((val) => (typeof val === "string" ? "string" : typeof val === "number" ? "integer" : null));
}

/**
 * Abstract Data Type Definition for Training Materials
 */
interface TrainingMaterialType {
  id: string; // Unique identifier for the training material entry in this repository context
  title: string; // Human-readable name of the content (e.g., 'Butler's Parables', 'The Body' index)
  author?: string; // Name of the theorist or creator if available
  category: "gender" | "identity"; // Core themes within gender theory (or specific sub-theory like performance, violence, etc.)
  description?: string; // Brief summary of content if available in text format
}

// Helper to convert C-style struct definitions into TypeScript types for easier mapping
export function schemaToType(schemaMap: TrainingMaterialType): Type[] {
  return Object.values(schemaMap).map((val) => (typeof val === "string" ? "string" : typeof val === "number" ? "integer" : null));
}

/**
 * Abstract Data Type Definition for Agents and Materials Registry
 */
interface AgentRegistryEntry extends TrainingMaterialType {
  agent: AgentType; // The specific instance of the training material or agent being trained with this data
  metadata?: Record<string, any>; // Additional context about the agent's current state (e.g., "current_training", "session_id")
}

// Helper to convert C-style struct definitions into TypeScript types for easier mapping in repository contexts
export function schemaToType(schemaMap: AgentRegistryEntry): Type[] {
  return Object.values(schemaMap).map((val) => (typeof val === "string" ? "string" : typeof val === "number" ? "integer" : null));
}

/**
 * Abstract Data Type Definition for Agents and Materials Registry
 */
interface TrainingMaterialRegistryEntry extends AgentType {
  metadata?: Record<string, any>; // Additional context about the agent
