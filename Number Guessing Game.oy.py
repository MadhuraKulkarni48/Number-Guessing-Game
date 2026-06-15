import random

print("🎮 Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 20.")

secret_number = random.randint(1, 20)
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess (1-20): "))
        attempts += 1

        if guess < 1 or guess > 20:
            print("⚠️ Please enter a number between 1 and 20.")
        elif guess < secret_number:
            print("📉 Too low! Try again.")
        elif guess > secret_number:
            print("📈 Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

    except ValueError:
        print("❌ Invalid input. Please enter a number.")