# Time complexity: O(n)
def manage_stage_changes(changes):
    stack_performance = []
    cancel_performance = []
    
    for i in changes:
        if i.startswith("Schedule"):
            _, performance_id = i.split()
            stack_performance.append(performance_id)
        elif i == "Cancel" and stack_performance:
            cancel_performance.append(stack_performance.pop())
        else:
            stack_performance.append(cancel_performance.pop())
    return stack_performance


print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 

# Example Output:

# ["A", "C", "B", "D"]
# []
# ["Z"]

# Time complexity: O(n)