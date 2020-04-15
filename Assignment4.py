#1.1
# Python Program to find the area of triangle

a = 5
b = 6
c = 7

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)

#1.2

def listing(guess, number):

    new_list = []

    for i in range(len(guess)):
        if len(guess[i]) > number:
            new_list.append(guess[i])

    print (new_list)

list1 = input("take input: ")

list = list1.split(",")

def main():
    global list, integer1
    integer = input()
    integer1 = int(integer)
    listing(list, integer1)

main()

#2.1

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(find_longest_word(["PHP", "Exercises", "Backend"]))


#2.2




def is_vowel(char):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if char not in vowels:
        return False
    return True
output:--
is_vowel('sf')

