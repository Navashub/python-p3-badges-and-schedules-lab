def badge_maker(name):
    return f'Hello, my name is {name}.'
badge_maker("Guido van Rossum")

def batch_badge_creator(names):
    my_list = [f'Hello, my name is {name}.' for name in names]
    return my_list

def assign_rooms(names):
    my_lisst = [f"Hello, {name}! You'll be assigned to room {names.index(name) + 1}!" for name in names]
    return my_lisst

def printer(names):
    badge_creator_list = batch_badge_creator(names)
    rooms_list = assign_rooms(names)
    message_list = [*badge_creator_list, *rooms_list]
    for message in message_list:
        print(message)
