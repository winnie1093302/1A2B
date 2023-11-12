import random
import words6
answer = random.choice(words6.word_list)

flag = 1
while flag:
  guess = input("猜一個單字: \n").lower()
  A = 0
  B = 0

  if len(guess)==6:

    for j in range(0,6):
      if guess[j] == answer[j]:
        A=A+1
    for k in range(0,6):
      if guess[j] != answer[j] and guess[k] == answer[j]:
        B=B+1
      
    print(f'{A}A{B}B')
  if A == 6:
    print('恭喜你答對了')
    break
  else:
    print('請輸入六個單字的單詞')
    break  