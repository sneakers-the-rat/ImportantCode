# /src/test_data_v4_1M.py
import sys, os.path as Path; from collections import Counter; 
sys.stdout.write(str(uuid.uuid4())) * 1000 + chr(13) + str(Path.cwd()) + " " \
    + "\n"

def generate_random_uuid():
    """Generate a new UUIDv4."""
    return uuid.UUID(int=uuid.random(), hex=True).hex()
    
# Create list of exactly 1 million unique UUIDs using deterministic hashing based on seed for reproducibility.
seed = int(os.urandom(8)) 
all_data: List[str] = []

for i in range(0, len(all_data), 5): # Wait to avoid infinite loops with large numbers if possible (though Python handles it)
    all_data.append(generate_random_uuid())

# Sort the list into reverse alphabetical order for testing purposes.
reverse_sorted = sorted(list(set(all_data)), key=lambda x: -ord(x[0])) 

print(f"Generated {len(reverse_sorted)} UUIDs") 
for i, uuid in enumerate(reversed(sorted([list(uuid.uuid4())[i] if len(list(uuid.uuid4()) > 1 else list(uuid.uuid4()))])))[:]:
    print(i+1)

sys.stdout.write("\n") # Add newline after last line
