print("1.练习模式")
print("2.测试模式")
print("3.历史记录")
a = int(input())

if a == 1:
    print("现支持0到n的加减法")
    print("加法or减法(1/2)")
    sss = int(input())
    print("输入题目数量")
    n = int(input())
    print("输入最大加or被减数")
    m = int(input())
    sum_correct = 0

    if sss == 1:
        for i in range(n):
            import random
            num1 = random.randint(0, m)
            num2 = random.randint(0, m)
            correct_answer = num1 + num2
            print(num1, " + ", num2, " = ")
            user_answer = int(input())
            if correct_answer == user_answer:
                print("正确!")
                sum_correct += 1
            else:
                print(f"错误! 正确答案是: {correct_answer}")

    elif sss == 2:
        for i in range(n):
            import random
            num1 = random.randint(0, m)
            num2 = random.randint(0, num1)  # Ensure that subtraction result is non-negative
            correct_answer = num1 - num2
            print(num1, " - ", num2, " = ")
            user_answer = int(input())
            if correct_answer == user_answer:
                print("正确!")
                sum_correct += 1
            else:
                print(f"错误! 正确答案是: {correct_answer}")

    print("\n练习总结:")
    print("总题数:", n)
    print("正确题数:", sum_correct)
    print("错误题数:", n - sum_correct)

elif a == 2:
    print("现支持0到n的加减法")
    print("加法or减法(1/2)")
    sss = int(input())
    print("输入题目数量")
    n = int(input())
    print("输入最大加or被减数")
    m = int(input())
    sum_correct = 0

    if sss == 1:
        for i in range(n):
            import random
            num1 = random.randint(0, m)
            num2 = random.randint(0, m)
            correct_answer = num1 + num2
            print(num1, " + ", num2, " = ")
            user_answer = int(input())
            if correct_answer == user_answer:
                print("正确!")
                sum_correct += 1
            else:
                print(f"错误! 正确答案是: {correct_answer}")

    elif sss == 2:
        for i in range(n):
            import random
            num1 = random.randint(0, m)
            num2 = random.randint(0, num1)  # Ensure that subtraction result is non-negative
            correct_answer = num1 - num2
            print(num1, " - ", num2, " = ")
            user_answer = int(input())
            if correct_answer == user_answer:
                print("正确!")
                sum_correct
