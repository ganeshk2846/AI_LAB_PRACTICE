import random
import nltk
from nltk.corpus import wordnet

# -----------------------------
# DOWNLOAD NLTK
# -----------------------------
try:
    wordnet.synsets("test")
except LookupError:
    nltk.download('wordnet')
    nltk.download('omw-1.4')


# -----------------------------
# WORD LIST
# -----------------------------
word_list = [
    # Tech
    "python", "java", "compiler", "debugging", "database",
    "algorithm", "function", "variable", "keyboard", "internet",
    "software", "hardware", "encryption", "cybersecurity",

    # AI / Science
    "artificial", "intelligence", "neural", "network", "robotics",
    "quantum", "physics", "chemistry", "biology", "astronomy",
    "gravity", "molecule", "atom", "energy",

    # Space
    "galaxy", "planet", "satellite", "asteroid", "comet",
    "universe", "telescope", "orbit", "cosmos", "eclipse",

    # Animals
    "elephant", "giraffe", "kangaroo", "dolphin", "penguin",
    "alligator", "chimpanzee", "butterfly", "crocodile",

    # Nature
    "mountain", "river", "ocean", "forest", "desert",
    "volcano", "rainbow", "thunder", "lightning",

    # Objects
    "guitar", "pyramid", "bicycle", "airplane", "backpack",
    "calculator", "television", "microscope", "camera",

    # Common Words
    "jungle", "school", "teacher", "student", "library",
    "holiday", "festival", "adventure", "journey", "dream",

    # Medium/Hard Words
    "oxygen", "hydrogen", "photosynthesis", "transformation",
    "communication", "development", "programming", "engineering",
    "architecture", "mathematics"
]


# -----------------------------
# FUNCTIONS
# -----------------------------
def choose_word():
    return random.choice(word_list)


def get_wordnet_hint(word):
    synsets = wordnet.synsets(word)
    if synsets:
        return synsets[0].definition()
    return f"The word starts with '{word[0]}' and has {len(word)} letters."


def display_word(secret_word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])


def reveal_random_letter(secret_word, guessed_letters):
    remaining_letters = [l for l in set(secret_word) if l not in guessed_letters]
    if remaining_letters:
        letter = random.choice(remaining_letters)
        guessed_letters.add(letter)
        print(f"🔓 Letter revealed: {letter}")


# -----------------------------
# GAME LOGIC
# -----------------------------
def play_game():
    secret_word = choose_word()

    guessed_letters = set()   # contains all revealed + guessed letters

    attempts = len(secret_word) - 1
    score = 0

    # Initial reveal
    reveal_random_letter(secret_word, guessed_letters)

    print("🎮 Hangman (WordNet Powered)")
    print("💡 Each hint reveals a letter!")
    print(f"🎯 Attempts: {attempts}")

    while attempts > 0:

        # ✅ WIN CHECK (FIXED)
        if set(secret_word).issubset(guessed_letters):
            print("\n🎉 YOU WIN!")
            print("Word:", secret_word)
            score += 50
            print("🏆 Final Score:", score)
            return

        print("\nWord:", display_word(secret_word, guessed_letters))
        print("Attempts left:", attempts)
        print("Score:", score)

        guess = input("Enter a letter (or 'hint'): ").lower()

        # -----------------------------
        # HINT FEATURE
        # -----------------------------
        if guess == "hint":
            print("\n💡 Hint:", get_wordnet_hint(secret_word))

            attempts -= 1
            score -= 5

            reveal_random_letter(secret_word, guessed_letters)
            continue

        # -----------------------------
        # VALIDATION
        # -----------------------------
        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Enter a valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ Already guessed/revealed.")
            continue

        guessed_letters.add(guess)

        # -----------------------------
        # CHECK GUESS
        # -----------------------------
        if guess in secret_word:
            print("✅ Correct!")
            score += 10
        else:
            print("❌ Wrong!")
            attempts -= 1
            score -= 5

        # ✅ WIN CHECK AGAIN (AFTER GUESS)
        if set(secret_word).issubset(guessed_letters):
            print("\n🎉 YOU WIN!")
            print("Word:", secret_word)
            score += 50
            print("🏆 Final Score:", score)
            return

    # -----------------------------
    # GAME OVER
    # -----------------------------
    print("\n💀 GAME OVER!")
    print("Word was:", secret_word)
    print("🏆 Final Score:", score)


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    play_game()