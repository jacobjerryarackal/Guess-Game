import random

class GuessingGame:
  def __init__(self):
    self.difficulty_levels = {"easy": (1, 10), "medium": (1, 100), "hard": (1, 1000)}
    self.difficulty = None
    self.secret_number = None
    self.guesses = 0
    self.wins = 0
    self.losses = 0

  def choose_difficulty(self):
    print("Choose difficulty level (easy, medium, hard): ")
    while True:
      choice = input().lower()
      if choice in self.difficulty_levels:
        self.difficulty = choice
        self.secret_number = random.randint(*self.difficulty_levels[choice])
        print(f"I'm thinking of a number between {self.difficulty_levels[choice][0]} and {self.difficulty_levels[choice][1]}.")
        return
      else:
        print("Invalid choice. Please choose easy, medium, or hard.")

  def take_guess(self):
    while True:
      try:
        guess = int(input("Take a guess: "))
        return guess
      except ValueError:
        print("Invalid input. Please enter a number.")

  def check_guess(self, guess):
    self.guesses += 1
    if guess == self.secret_number:
      print(f"Congratulations! You guessed the number in {self.guesses} tries.")
      self.wins += 1
      return True
    elif guess < self.secret_number:
      print("Too low, try again.")
    else:
      print("Too high, try again.")
    return False

  def play_game(self):
    self.guesses = 0
    self.choose_difficulty()
    while True:
      if self.check_guess(self.take_guess()):
        break

  def show_stats(self):
    if self.wins + self.losses == 0:
      print("No games played yet!")
    else:
      win_rate = self.wins / (self.wins + self.losses) * 100
      print(f"Wins: {self.wins}, Losses: {self.losses}, Win Rate: {win_rate:.2f}%")

  def run(self):
    while True:
      print("\nGuessing Game Menu:")
      print("1. Play Game")
      print("2. Show Statistics")
      print("3. Exit")

      choice = input("Enter your choice: ")

      if choice == "1":
        self.play_game()
      elif choice == "2":
        self.show_stats()
      elif choice == "3":
        break
      else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
  game = GuessingGame()
  game.run()
