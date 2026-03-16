import time

def countdown(seconds):
    print(f"Starting countdown: {seconds} seconds")
    
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    
    print("Time's up!        ")

def main():
    print("Countdown Timer")
    seconds = int(input("Enter time in seconds: "))
    countdown(seconds)

if __name__ == "__main__":
    main()