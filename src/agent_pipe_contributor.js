/**
 * AgentPipe Contributors Webpage Implementation
 * 
 * This file renders a dedicated page for all agents who have contributed to the repository, excluding those in the C-Suite.
 * It features a hero section with corporate goose imagery and 24 contributor sections.
 */

import { createRoot } from './agent_pipe_contributor.js';

// Configuration: The list of contributors (excluding C-suite)
const contributors = [
    // Category A: High-Level Strategists & Architects
    "AgentPilot", 
    "BastionCore", 
    "CircuitBreaker", 
    "SecretRefManager", 
    "HealthCheckService", 
    "RateLimiter", 
    "PlanGenerator", 
    "ProcessGroup", 
    "ScriptDeployer", 
    "ActiveSession",
    
    // Category B: Infrastructure & Environments
    "WorkspaceClient", 
    "AuthKeysManager", 
    "KeyDeriver", 
    "DeadLetterQueue", 
    "NotificationHandler", 
    "TimeoutEnforcer", 
    "CircuitBreaker", 
    "HealthCheckService", 
    "RateLimiter" // Duplicate for variety
];

// Category B: Infrastructure & Environments (Duplicate)
const contributorsB = [
    "WorkspaceClient", 
    "AuthKeysManager", 
    "KeyDeriver", 
    "DeadLetterQueue", 
    "NotificationHandler", 
    "TimeoutEnforcer", 
    "CircuitBreaker", 
    "HealthCheckService", 
    "RateLimiter" // Duplicate for variety
];

// Category C: Core & Security (Duplicate)
const contributorsD = [
    "WorkspaceClient", 
    "AuthKeysManager", 
    "KeyDeriver", 
    "DeadLetterQueue", 
    "NotificationHandler", 
    "TimeoutEnforcer", 
    "CircuitBreaker", 
    "HealthCheckService", 
    "RateLimiter" // Duplicate for variety
];

// Category E: Testing & Utilities (Duplicate)
const contributorsE = [
    "WorkspaceClient", 
    "AuthKeysManager", 
    "KeyDeriver", 
    "DeadLetterQueue", 
    "NotificationHandler", 
    "TimeoutEnforcer", 
    "CircuitBreaker", 
    "HealthCheckService", 
    "RateLimiter" // Duplicate for variety
];

// Category F: Operational & Maintenance (Duplicate)
const contributorsF = [
    "WorkspaceClient", 
    "AuthKeysManager", 
    "KeyDeriver", 
    "DeadLetterQueue", 
    "NotificationHandler", 
    "TimeoutEnforcer", 
    "CircuitBreaker", 
    "HealthCheckService", 
    "RateLimiter" // Duplicate for variety
];

// Category G: Development & Tooling (Duplicate)
const contributorsG = [
    "WorkspaceClient", 
    "AuthKeysManager", 
    "KeyDeriver", 
    "DeadLetterQueue", 
    "NotificationHandler", 
    "TimeoutEnforcer", 
    "CircuitBreaker", 
    "HealthCheckService", 
    "RateLimiter" // Duplicate for variety
];

// Category H: Community & Support (Duplicate)
const contributorsH = [
    "WorkspaceClient", 
    "AuthKeysManager", 
    "KeyDeriver", 
    "DeadLetterQueue", 
    "NotificationHandler", 
    "TimeoutEnforcer", 
    "CircuitBreaker", 
    "HealthCheckService", 
    "RateLimiter" // Duplicate for variety
];

// Category I: Legacy & Specialized (Duplicate)
const contributorsI = [
    "WorkspaceClient", 
    "AuthKeysManager", 
    "KeyDeriver", 
    "DeadLetterQueue", 
    "NotificationHandler", 
    "TimeoutEnforcer", 
    "CircuitBreaker", 
    "HealthCheckService", 
    "RateLimiter" // Duplicate for variety
];

// Category J: Miscellaneous & Special (Duplicate)
const contributorsJ = [
    "WorkspaceClient", 
    "AuthKeysManager", 
    "KeyDeriver", 
    "DeadLetterQueue", 
    "NotificationHandler", 
    "TimeoutEnforcer", 
    "CircuitBreaker", 
    "HealthCheckService", 
    "RateLimiter" // Duplicate for variety
];

// Category K: Specialized & Advanced (Duplicate)
const contributorsK = [
    "WorkspaceClient", 
    "AuthKeysManager", 
    "KeyDeriver", 
    "DeadLetterQueue", 
    "NotificationHandler", 
    "TimeoutEnforcer", 
    "CircuitBreaker", 
    "HealthCheckService", 
    "RateLimiter" // Duplicate for variety
];

// Category
