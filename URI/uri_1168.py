casosTeste = int(input())

for i in range(1, casosTeste + 1):
    n = input()
    led = 0

    for j in range(0, len(n)):
        if n[j] == '1':
            led = led + 2
        elif n[j] == '2':
            led = led + 5
        elif n[j] == '3':
            led = led + 5
        elif n[j] == '4':
            led = led + 4
        elif n[j] == '5':
            led = led + 5
        elif n[j] == '6':
            led = led + 6
        elif n[j] == '7':
            led = led + 3
        elif n[j] == '8':
            led = led + 7
        elif n[j] == '9':
            led = led + 6
        elif n[j] == '0':
            led = led + 6
    
    print(f"{led} leds")
