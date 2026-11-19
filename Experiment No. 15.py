import gc
import tracemalloc

# Start tracing Python memory allocations
tracemalloc.start()

# Check default GC thresholds
print("GC Thresholds:", gc.get_threshold())

# Function to create circular references (reference cycles)
def create_reference_cycles(count):
    for i in range(count):
        a = {}
        b = {"ref": a, "data": [j for j in range(1000)]}
        a["ref"] = b  # Creates a cycle between 'a' and 'b'

# 1. Measure baseline memory before creating objects
current_before, peak_before = tracemalloc.get_traced_memory()
print(f"\n[Before Object Creation] Current Memory: {current_before / 1024:.2f} KB")

# 2. Create 500 cyclic objects that fall out of scope immediately
create_reference_cycles(500)

# 3. Measure memory after creating cycles (before manual GC)
current_after_alloc, _ = tracemalloc.get_traced_memory()
print(f"[Before Manual GC]       Current Memory: {current_after_alloc / 1024:.2f} KB")

# 4. Manually trigger garbage collection
collected_objects = gc.collect()
print(f"\nManual GC executed -> Collected {collected_objects} unreachable objects.")

# 5. Measure memory after manual GC
current_after_gc, peak_after_gc = tracemalloc.get_traced_memory()
print(f"[After Manual GC]        Current Memory: {current_after_gc / 1024:.2f} KB")
print(f"Memory Reclaimed: {(current_after_alloc - current_after_gc) / 1024:.2f} KB")

tracemalloc.stop()