import random
import words5
answer = random.choice(words5.word_list)

flag = 1
while flag:
  guess = input("猜一個單字: \n").lower()
  A = 0
  B = 0

  if len(guess)==5:

    for j in range(0,5):
      if guess[j] == answer[j]:
        A=A+1
    for k in range(0,5):
      if guess[j] != answer[j] and guess[k] == answer[j]:
        B=B+1
      
    print(f'{A}A{B}B')
  if A == 5:
    print('恭喜你答對了')
    break

  else:
    print('請輸入五個字的單詞')
    break
