import random

def hangman():
    print(" Welcome To Hang Man Game ")

    words = ['plython', 'programming', 'hangman', 'game']
    word = random.choice(words)  # اختيار كلمة عشوائية من القائمة
    guessed_letters = []  # قائمة لتخزين الحروف التي تم تخمينها
    tries = 3  # عدد المحاولات المتاحة

    while tries > 0:
        guessed_word = ""  # الكلمة المخمنة حتى الآن
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter  # إضافة الحرف المخمن إذا تم تخمينه بشكل صحيح
            else:
                guessed_word += "_"  # استبدال الحروف غير المخمنة بشرطة سفلية

        if guessed_word == word:
            print("Congratulations! You guessed the word correctly *_* ")
            break  # إذا تم تخمين الكلمة بشكل صحيح، يتم إيقاف اللعبة وإظهار رسالة الفوز

        print("Word:", guessed_word)
        print("Tries left:", tries)

        guess = input("Enter a letter: ").lower()  # استلام تخمين اللاعب وتحويله إلى حرف صغير

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue  # إذا تم تخمين الحرف بالفعل، يتم الاستمرار في اللعبة دون خصم محاولة

        guessed_letters.append(guess)  # إضافة الحرف المخمن إلى قائمة الحروف المخمنة

        if guess not in word:
            tries -= 1
            print("Wrong guess! try agin \n")  # إذا تم تخمين حرف خاطئ، يتم خصم محاولة وطباعة رسالة خطأ

        print("-------------------------------------")

    else:
        print("Game over! You ran out of tries.")
        print("The word was:", word)  # إذا نفدت المحاولات دون تخمين الكلمة بشكل صحيح، يظهر رسالة خسارة ويعرض الكلمة الصحيحة
        print("Done By Eng:Shaima.R")
hangman()