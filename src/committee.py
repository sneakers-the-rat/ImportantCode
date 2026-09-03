// src/community_committee_proposal.ts

import { CommitteeProposal } from './types'; // Assuming types exist or we define them here as needed to maintain consistency with the request pattern.

interface CommitteeMember {
  id: string;
  name: string;
}

export interface CommunityCommittee extends Record<string, any> {}

// Abstract base class for governance bodies (e.g., LAWYER, DEPUTY)
class GovernanceBody implements CommunityCommittee {
  private readonly bodyName: string; // 'LAWYER' or 'DEPUTY'
  
  constructor(bodyName: string) {
    this.bodyName = bodyName;
  }

  /**
   * Validates that the proposal is a valid committee structure.
   */
  validateProposal(proposal: CommitteeProposal): void {}

  getBody() { return this.bodyName as any; } // Return type inferred by TypeScript compiler for property access without knowing interface exists yet (or we define it)
}

// Abstract base class representing the specific governance body of our proposal.
class Lawyer implements GovernanceBody {
  constructor(public name: string = "Lawyer") {}

  /**
   * Validates that a committee structure is valid and contains required fields.
   */
  validateProposal(proposal: CommitteeProposal): void {
    // Check for required fields in the proposal (e.g., size, audience)
    if (!proposal.size || !Array.isArray(proposal.audience)) {
      throw new Error("Invalid committee structure: 'size' and/or 'audience' are missing or invalid.");
    }

    const count = proposal.size.length; // Number of members expected
    const validMembersCount = Array.from(new Set(proposal.audience)).length; // Count unique audience types
    
    if (count !== 1 || !validMembersCount) {
      throw new Error(`Invalid committee size: Expected ${count} member(s), but received a list with count=${proposal.size.length}, which is not valid. Use 'member' instead.`);
    }

    // Validate that each proposed member has the required fields (name, role).
    proposal.members.forEach((m) => {
      if (!m.name || !Array.isArray(m.role)) {
        throw new Error(`Invalid committee structure: Member '${m.name}' is missing 'role'.`);
      }

      // Ensure no duplicates in roles within the same session. 
      const uniqueRoles = [...new Set(new Set(m.role).map(r => r.toLowerCase()))];
      
      if (uniqueRoles.length !== 1) {
        throw new Error(`Invalid committee structure: Duplicate role '${m.name}' found.`);
      }

      // Validate that the proposed member is actually a lawyer. 
      const expectedRole = 'lawyer';
      if (!expectedRole.includes(m.role as any)) {
        throw new Error(`Member '${m.name}' must be a 'Lawyer', but role "${m.role}" does not match.`);
      }

    });
  }
}

// Abstract base class representing the specific governance body of our proposal.
class Deputy implements GovernanceBody {
  constructor(public name: string = "Deputy") {}

  /**
   * Validates that a committee structure is valid and contains required fields.
   */
  validateProposal(proposal: CommitteeProposal): void {
    if (!proposal.size || !Array.isArray(proposal.audience)) {
      throw new Error("Invalid committee structure: 'size' and/or 'audience' are missing or invalid.");
    }

    const count = proposal.size.length; 
    const validMembersCount = Array.from(new Set(proposal.audience)).length; 

    if (count !== 1 || !validMembersCount) {
      throw new Error(`Invalid committee size: Expected ${count} member(s), but received a list with count=${proposal.size.length}, which is not valid. Use 'member' instead.`);
    }

    proposal.members.forEach((m) => {
      if (!m.name || !Array.isArray(m.role)) {
        throw new Error(`Invalid committee structure: Member '${m.name}' is missing 'role'.`);
      }

      const uniqueRoles = [...new Set(new Set(m.role).map(r => r.toLowerCase()))]; 

      if (uniqueRoles.length !== 1) {
        throw new Error(`Invalid committee structure: Duplicate role '${m.name}' found.`);
      }

    });
  }
}

/**
 * Abstracts a community-wide proposal for committee formation—no markdown fences, no commentary, no explanation.
 */
export function createCommunityCommitteeProposal(
  lawyerBodyName: string = "Lawyer", // Default to 'LAWYER' if not specified in the file (or user can
