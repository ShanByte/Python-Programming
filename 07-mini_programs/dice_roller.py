import random

def roll_dice(num_dice=1, sides=6):
    results = [random.randint(1, sides) for _ in range(num_dice)]
    return results

def main():
    print("Dice Rolling Simulator")
    
    while True:
        num_dice = int(input("How many dice to roll? "))
        sides = int(input("How many sides per die? (default 6): ") or 6)
        
        results = roll_dice(num_dice, sides)
        print(f"\nResults: {results}")
        print(f"Total: {sum(results)}")
        
        again = input("\nRoll again? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()