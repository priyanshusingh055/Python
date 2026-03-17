marks={
    "Harry":100,
    "Raj":50,
    "Hello":25,
    
}

print(marks.items())       # print  of value of dict in tuple
print(marks.keys())        # print left side item 
print(marks.values())       # print value of dict

marks.update({"Harry":55,"Ram":44})
print(marks)  # update the value of dict and add new items

print(marks.get("Raj"))