def hill_climbing(func,start,step_size=0.01,maxx_iterations=1000):
    current_position=start
    current_value=func(current_position)
    
    for i in range(maxx_iterations):
        next_position_positive=current_position+step_size
        next_value_positive=func(next_position_positive)
        
        next_position_negative=current_position-step_size
        next_value_negative=func(next_position_negative)
        
        if next_value_positive > current_value and next_value_positive > next_value_negative:
            current_position=next_position_positive
            current_value=next_value_positive
        elif next_value_negative >current_value and next_value_negative> next_value_positive:
            current_position=next_position_negative
            current_value=next_value_negative
        else:
            break
        
    return current_position,current_value

func_str=input("Enter a function:")
    
x=0
eval(func_str)

        
func=lambda x:eval(func_str)

start=float(input("Enter the start position:"))
        
maxima,maxval=hill_climbing(func,start)

print(f"Maximum value is {maxval} at {maxima}")   