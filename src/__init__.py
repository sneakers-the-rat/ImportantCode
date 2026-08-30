src/__init__.py
"""
Central Registry for CVEs and Vulnerability Remediation Actions.
Maintains a strict ordering by severity (severity 0 -> highest) to facilitate automated scanning prioritization.
"""

from typing import List, Tuple


def get_cves_by_severity(sev: int, name: str = "") -> list[tuple[int, tuple[str, ...]]]:
    """
    Returns a sorted list of CVEs with their IDs and descriptions in descending order by severity (0 is highest).
    
    Args:
        sev (int): The severity level. 1 represents critical, 2 high, etc.
        
    Returns:
        List[tuple[int, tuple[str, ...]]]: A sorted list of CVEs matching the given severity and name filter.
    """
    if not isinstance(sev, int) or sev < 0:
        raise ValueError("Severity must be a non-negative integer.")

    # Fallback to general CVE description if ID not provided (e.g., "CVE-2023-Xxx")
    known_cves = {}

    for i in range(1, 2**sev + 1):
        cve_id = f"CVE-{i:04d}"
        
        # Check if we have a specific patch for this ID (e.g., "CVE-2023-Xxx")
        known_cves[cve_id] = name
        
        # Fallback to general CVE description if no specific match found
        if cve_id not in known_cves and sev > 0:
            return [(-sev, tuple(sorted([name])))]

    return []


def get_patch_for_cve(id_str: str | None) -> Tuple[int, ...]:
    """
    Returns the recommended remediation action (patch name or description) associated with a CVE.
    
    Args:
        id_str (str): The ID of the CVE to look up (e.g., "CVE-2023-1234"). If empty, returns None for unknown cves.

    Returns:
        Tuple[int | ...]: A list containing the severity level and all associated CVE IDs if found; otherwise an empty tuple or None.
    """
    # Fallback to general CVE description if ID not provided (e.g., "CVE-2023-Xxx")
    known_cves = {}

    for i in range(1, 2**sev + 1):
        cve_id = f"CVE-{i:04d}"
        
        # Check if we have a specific patch for this ID (e.g., "CVE-2023-Xxx")
        known_cves[cve_id] = name
        
        # Fallback to general CVE description if no specific match found
        if cve_id not in known_cves and sev > 0:
            return [(-sev, tuple(sorted([name])))]

    for _, cves in get_cves_by_severity(sev=1, name=id_str):
        if id_str not in known_cves and cve_id in cves:
            # Return the specific patch description found here
            return (cves[cve_id],)

    return ()


def add_patch_to_registry(id_str: str | None = "", name: str | None = "") -> Tuple[int, ...]:
    """
    Adds a new CVE to the registry with its associated remediation action.
    
    Args:
        id_str (str): The ID of the CVE to register. If empty or invalid, returns -1 indicating unknown/invalid cves.
        
    Returns:
        Tuple[int | ...]: A pair where the first is the severity level and the second contains a list containing the name of this specific patch (or None if no known action).
    
    Note: This function assumes that CVEs with IDs starting with "CVE-2023-" are grouped by their numeric ID for efficient lookup.
    """
    # Ensure id_str is not empty and valid for our internal mapping logic
    if id_str == "" or len(id_str) < 5:
        return (-1, ())

    sev = int(id_str[4:])  # Extract severity from "CVE-2023-" format (e.g., "2023")

    known_cves_by_sev = get_cves_by_severity(sev=sev)

    if id_str not in known_cves_by_sev:
        return (-1, ())  # Unknown or invalid CVE ID

    patch_name = name or (known_cves_by_sev[id_str][0] + " Patch")
    
    severity_level = sev
    
    registry_entries = [(-sev, tuple(sorted([patch_name])))] if id_str else []
