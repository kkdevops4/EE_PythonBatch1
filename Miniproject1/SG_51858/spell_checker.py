dictionary = ["we", "are", "am", "this", "is", "a", "python", "not", "net",
              "simple", "sentence", "mouse", "can", "take", "your",
              "learning", "pen", "whose", "bottle", "my", "name", "and", "i"]

sentence = input("Enter your sentence : ")
words = sentence.lower().split()

new_sentence = []

for el in words:
    if el in dictionary:
        new_sentence.append(el)
    else:
        best_match = el
        max_match = 0
        
        for correct_word in dictionary:
            match_count = 0
            
            for i in  range(min(len(el), (len(correct_word)))):
                if el[i] == correct_word[i]:
                    match_count += 1
                    
            if match_count > max_match:
                max_match = match_count
                best_match = correct_word
                
        new_sentence.append(best_match)

result = " ".join(new_sentence)
print("correct sentence : ", result)