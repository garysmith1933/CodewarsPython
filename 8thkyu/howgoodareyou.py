def better_than_average(class_points, your_points):
    sum = 0
    
    for score in class_points: 
        sum += score

    class_average = sum / len(class_points)
    print(class_average, your_points)
    
    return your_points > class_average