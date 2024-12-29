import random
import string

class WordProvider:
    def __init__(self):
        self.part1 = "I" 
        self.part2 = lambda: "l" + "ike"
        self.part6 = "45" + "lonesenco"  
        self.part3_data = ["random", "men"]

    def get_part1(self):
        return self.part1

    def get_part2(self):
        return self.part2()

    def get_part3(self):
        return self.part3_data[-1]  

def generate_random_noise():
    
    noise = ''.join(random.choices(string.ascii_letters, k=random.randint(2, 5)))
    
    
    spaces = ' ' * random.randint(20, 32)
    
    
    return spaces + noise

def construct_final_message(provider):
    words = []
    words.append(provider.get_part1())
    words.append(provider.get_part2())  
    words.append(provider.get_part3()) 
    return " ".join(words)

if __name__ == "__main__":
    for _ in range(random.randint(2, 6)):
        print(generate_random_noise())
        
    provider = WordProvider()

    final_message = construct_final_message(provider)
    print(final_message)

    # Exit code
    input("\nPress Enter to exit...")
