import reader

locks, keys = reader.read("day 25\\input.txt")

print('locks')
for o in locks:
    print(o.get_spaces())
print('keys')
for o in keys:
    print(o.get_pins())

def try_lock_key(lock, key):
    for i in range(len(lock.get_spaces())):
        if lock.get_spaces()[i] + key.get_pins()[i] > 5:
            return False
    return True

cnt = 0
for lock in locks:
    for key in keys:
        if try_lock_key(lock, key):
            cnt += 1    
print(cnt)