def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    # Number of available rooms
    num_rooms = 8
    
    # Check if there are enough names to assign to rooms
    if len(names) > num_rooms:
        raise ValueError("There are more speakers than available rooms.")
    
    # Initialize the list to store the assignment messages
    assignments = []
    
    # Assign each speaker to a room
    for i, name in enumerate(names):
        room_number = i + 1  # Room numbers start from 1
        message = f"Hello, {name}! You'll be assigned to room {room_number}!"
        assignments.append(message)
    
    return assignments

#Here is a test
speakers = ["Arel", "Carol"]
print(assign_rooms(speakers))


def printer(names):
    
    badges = batch_badge_creator(names)
    assignments = assign_rooms(names)
    
    for badge in badges:
        print(badge)
    
    for assignment in assignments:
        print(assignment)

printer(speakers)