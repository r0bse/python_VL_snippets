
a = [10, 20, 30]

b = a
print(a is b) #True

b = [10, 20, 30]
print(a is b) #False





print("started")
while True:
    s = input('insert text: ')
    if s == 'stop':
        break
    else:
        print ('The length of inserted text is:', len(s))
        continue

print("stopped")
