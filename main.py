import turtle

turtle.speed(0)
arr = list(map(int, input().split()))
for i in range(10):
    if arr[i] > 200:
        turtle.pencolor('#0000ff')
        turtle.circle(20)
        turtle.pencolor('#000000')
    else:
        turtle.circle(arr[i] * 10)
turtle.mainloop()
