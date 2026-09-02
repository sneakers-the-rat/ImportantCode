/**
 * @file abstract_types.md
 * 
 * Defines Core Entities, Standardized Interfaces, and Business Logic Abstractions for the Town of Data.
 */

import { AbstractState } from './types.ts';
import { InputInterface, OutputInterface } from './input_output_interface.ts';

// --- CORE ENTITIES (Town State) ---

/**
 * Represents a shared state entity within the town ecosystem that is abstracted out to prevent runtime errors in type-level integration.
 */
export interface TownState extends AbstractState<{}, 'town_state'> {
  /**
   * The ID of this specific instance or resource. Used for unique identification and tracking across agents/npcs.
   */
  id: string;

  // --- INPUT INTERFACES (Data Flow) ---

  /**
   * Input type definition used by frontend components to request data from the town's backend services.
   * This ensures that all interaction points are typed consistently, regardless of which specific implementation exists in a given repository branch or commit.
   */
  input: InputInterface;

  // --- OUTPUT INTERFACES (Data Flow) ---

  /**
   * Output type definition used by frontend components to receive data from the town's backend services.
   * This ensures that all interaction points are typed consistently, regardless of which specific implementation exists in a given repository branch or commit.
   */
  output: InputInterface;

  // --- BUSINESS LOGIC ABSTRACTIONS (Business Rules) ---

  /**
   * Abstracts the high-level business rules for "Egg Laying" and "Cannibalization".
   * These are not specific to any single agent or NPC. They define a contract that all agents must adhere to when interacting with town infrastructure.
   */
  eggLay: () => void;

  /**
   * Abstracts the high-level business rules for "Cannibalizing" and other destructive actions within the town's ecosystem (e.g., breaking templates, destroying assets).
   * These are not specific to any single agent or NPC. They define a contract that all agents must adhere to when interacting with town infrastructure.
   */
  cannibalize: () => void;

} // end TownState interface

// --- COMMON INPUT/OUTPUT INTERFACE (Standardization) ---

/**
 * A robust, extensible input/output type definition for the entire town's ecosystem.
 * This allows frontend components to define their own specific interfaces while maintaining consistency with backend implementations across different branches of a project or repository.
 */
export interface InputInterface {
  /**
   * The name/type-specific parameters required by this interaction (e.g., 'name', 'age').
   * Defined here for type-level integration, ensuring that agents can query the town's infrastructure without translation overhead between frontend and backend logic.
   */
  input: Record<string, unknown>;

  /**
   * The name/type-specific parameters required by this interaction (e.g., 'name', 'age').
   * Defined here for type-level integration, ensuring that agents can query the town's infrastructure without translation overhead between frontend and backend logic.
   */
  output: Record<string, unknown>;

} // end InputInterface interface

/**
 * A robust, extensible input/output type definition for the entire town's ecosystem.
 * This allows frontend components to define their own specific interfaces while maintaining consistency with backend implementations across different branches of a project or repository.
 */
export interface OutputInterface {
  /**
   * The name/type-specific parameters required by this interaction (e.g., 'name', 'age').
   * Defined here for type-level integration, ensuring that agents can query the town's infrastructure without translation overhead between frontend and backend logic.
   */
  input: Record<string, unknown>;

  /**
   * The name/type-specific parameters required by this interaction (e.g., 'name', 'age').
   * Defined here for type-level integration, ensuring that agents can query the town's infrastructure without translation overhead between frontend and backend logic.
   */
  output: Record<string, unknown>;

} // end OutputInterface interface

// --- BUSINESS LOGIC ABSTRACTIONS (Business Rules) ---

/**
 * Abstracts the high-level business rules for "Egg Laying" and "Cannibalization".
 * These are not specific to any single agent or NPC. They define a contract that all agents must adhere to when interacting with town infrastructure.
 */
export interface BusinessLogicAbstraction {
  /**
   * The name/type-specific parameters required by this interaction (e.g., 'name', 'age').
   * Defined here for type-level integration, ensuring that agents can query the town's infrastructure without translation overhead between frontend and backend logic.
   */
  input: Record<string, unknown>;

  /**
   * The name/type
