rawinput = "AaBbC"

length = len(rawinput)
input_repeated = rawinput*3

first_count = [0 for _ in range(length)]
mid_count = [0 for _ in range(length)]
last_count = [0 for _ in range(length)]

for i,char in enumerate(rawinput):
    if char==char.lower():
        mid_count[i] = input_repeated[length+i-2:length+i+3].count(char.upper())
        first_count[i] = input_repeated[max(length+i-2,length):length+i+3].count(char.upper())
        last_count[i] = input_repeated[length+i-2:min(length+i+3,2*length)].count(char.upper())

answer = sum(first_count)+ (998*sum(mid_count)) +sum(last_count)
print(answer)