with open('image.jpg' , 'rb') as f:
    size = f.seek(0,2)
    print(size)

