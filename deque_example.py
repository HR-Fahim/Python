from collections import deque

# Initialize a deque
dq = deque(['a', 'b', 'c'])

# Append elements
dq.append('d')        # Add to the right end

print(dq)

dq.appendleft('z')    # Add to the left end

print(dq)  # Output: deque(['z', 'a', 'b', 'c', 'd'])

# Pop elements
dq.pop()              # Remove from the right end
dq.popleft()          # Remove from the left end

print(dq)  # Output: deque(['a', 'b', 'c'])
