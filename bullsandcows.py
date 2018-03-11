from random import randint

def generate_number():
  generated = []
  generated.append(str(randint(0,9)))
  generated.append(generate_number_exept(generated))
  generated.append(generate_number_exept(generated))
  generated.append(generate_number_exept(generated))
  return generated

def generate_number_exept( exept ):
  in_range = False
  while not in_range:
    generated = str(randint(0,9))
    if generated not in exept:
      in_range = True
  return generated

def is_4_digit_number( entered_string ):
  count_numbers = 0
  for i in range(0, len(entered_string)):
    if entered_string[i].isdigit():
      count_numbers += 1
  if count_numbers == 4:
    return True
  return False

def check_bulls( correct, entered ):
  count_bulls = 0
  for i in range(0, 4):
    if entered[i] == correct[i]:
      count_bulls += 1
  return count_bulls
  
def check_cows( correct, entered ):
  count_cows = 0
  for i in range(0, 4):
    if entered[i] in correct:
      count_cows += 1
  return count_cows

def bulls_word( bulls_count ):
  word = "bulls"
  if bulls_count == 1:
    word = "bull"
  return word

def cows_word( cows_count ):
  word = "cows"
  if cows_count == 1:
    word = "cow"
  return word

def evaluation( guess_count ):
  if guess_count<6:
    return "amazing!"
  if guess_count<12:
    return "average."
  return "not so good."

if __name__ == '__main__':
  print "Hi there!"
  print "I've generated a random 4 digit number for you."
  print "Let's play a bulls and cows game."
  print "Enter a number"
  
  correct_array = generate_number()
  
  correct_answer = False
  guess_count = 0

  while not (correct_answer):
    entered_number_array = list(raw_input('>>> '))

    if is_4_digit_number(entered_number_array):
      bulls_result = check_bulls(correct_array, entered_number_array) 
      cows_result = check_cows(correct_array, entered_number_array)
      if bulls_result == 4:
        correct_answer = True
      else:
        print bulls_result,bulls_word(bulls_result),",",cows_result,cows_word(cows_result)
    else:
      print "Not a 4-digit number!"
    
    guess_count += 1
      
  last_word = "guesses!"
  if guess_count == 1:
    last_word = "guess!"

  print "Correct, you've guessed the right number in",guess_count,last_word
  print "That's",evaluation(guess_count)
