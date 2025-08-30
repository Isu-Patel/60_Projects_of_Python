import random

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? He was outstanding in his field!",
    "Why don't eggs tell jokes? They'd crack each other up!",
    "What do you call a fake noodle? An impasta!",
    "Why did the math book look so sad? Because it had too many problems!",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "What's orange and sounds like a parrot? A carrot!",
    "Why did the bicycle fall over? It was two-tired!",
    "What do you call a sleeping bull? A bulldozer!",
    "Why did the coffee file a police report? It got mugged!",
    "What do you call a dinosaur that crashes his car? Tyrannosaurus Wrecks!",
    "Why don't programmers like nature? It has too many bugs!",
    "What do you call a fish wearing a crown? A king fish!",
    "Why did the cookie go to the doctor? Because it felt crumbly!",
    "What do you call a cow with no legs? Ground beef!",
    "Why don't oysters share? Because they're shellfish!",
    "What do you call a pig that does karate? A pork chop!",
    "Why did the banana go to the doctor? It wasn't peeling well!",
    "What do you call a dog magician? A labracadabrador!"
]

print("🎭 Random Joke Generator 🎭")
print("-" * 30)

while True:
    input("\nPress Enter for a joke (or Ctrl+C to exit): ")
    print(f"\n😄 {random.choice(jokes)}")