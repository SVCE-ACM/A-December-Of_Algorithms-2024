# A-December-of-Algorithms-2024

<div align="left">
<h1>
    <p align="center"><img alt="header" src="https://github.com/user-attachments/assets/da6f80f2-06db-4578-9833-f635b85e3da6" width="500"></img></p>

</h1>
Welcome to A December of Algorithms 2024.

Building on the success and enthusiasm of previous years, we’re excited to bring you a fresh selection of algorithms to explore and implement this December!

Each Day, Each Algorithm ;)
Finish them all to get a certificate :)

**Send a pull request only after completing all 31 algorithms.**

**Please submit all PRs on or before January 21st 11:59 PM IST.**

## What Do I Do?

We have a small collection of algorithms, one for every day of the month. Scroll down to take a look at them.

All you need to do is fork this repository, implement all 31 algorithms and send a pull request over to us.

Check out our FAQ for more information.

## Index

- [**December 01 - The Vanishing Number**](#december-01---the-vanishing-number)
- [**December 02 - The Wave Sort Challenge**](#december-02---the-wave-sort-challenge)
- [**December 03 - Alternating Square Arrangement**](#december-03---alternating-square-arrangement)
- [**December 04 - Plant Growth Tracker**](#december-04---plant-growth-tracker)
- [**December 05 - Josephus Problem**](#december-05---josephus-problem)
- [**December 06 - Target Pair Finder**](#december-06---target-pair-finder)
- [**December 07 - The Magical Tower**](#december-07---the-magical-tower)

- [**FAQ**](#faq)

## Algorithms

### December 01 - The Vanishing Number

#### Problem Statement

```
Imagine a race event with N participants, each having a unique bib number from 1 to N.
After the race, the event organizers collect the bib numbers of all participants who showed
up. However, one participant didn’t show up, and their bib number is missing. The task is to
find out which bib number is missing in order to identify the participant who was absent.
```

```
Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find
the number(between 1 to N), that is not present in the given array.
```

![image](https://github.com/user-attachments/assets/177fbe2f-9248-481b-adb6-61dfcea59582)

Example 1:

```
Input Format:
N = 5, array[] = {1,2,4,5}
Result: 3
```

```
Explanation:
In the given array, number 3 is missing. So, 3 is the answer.
```

Example 2:

```
Input Format:
N = 3, array[] = {1,3}
Result: 2
```

### December 02 - The Wave Sort Challenge

#### Problem Statement

```
Imagine you're at a music concert, surrounded by thousands of fans.
As the music plays, the crowd begins to move in a rhythmic pattern, rising and falling like a wave.
The energy is contagious, and everyone follows the same wave-like motion.
Now, think of the crowd as an unsorted array of integers, and your job is to arrange them in such a way that
the heights of the fans rise and fall, just like the waves at the concert.
Your task is to organize the array in a similar wave-like fashion!
```

```
Sort an array in wave form
Given an unsorted array of integers, sort the array into a wave array. An array arr[0..n-1] is sorted in wave form if:
arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= ….

```

![image1](https://github.com/user-attachments/assets/7c46bc27-91f9-4a89-8731-37efa558a939)

Example 1:

```
Input:
arr[] = {10, 5, 6, 3, 2, 20, 100, 80}
Output:
arr[] = {10, 5, 6, 2, 20, 3, 100, 80}

```

```
Explanation:
Here you can see {10, 5, 6, 2, 20, 3, 100, 80}. The first element is larger than the second, and the same pattern repeats again.
Large element – small element – large element – small element, and so on.
It can also be in the opposite pattern (small element – large element – small element – large element).
All you need to maintain is the up-down fashion, which represents a wave. There can be multiple answers.

```

Example 2:

```
Additional Scenario
Input:
arr[] = {1, 2, 3, 4, 5, 6}
Output:
arr[] = {2, 1, 4, 3, 6, 5}

```

```
Explanation:
In this case, we swap adjacent elements to form a wave-like array.
{2, 1, 4, 3, 6, 5} satisfies the condition where elements are alternately large and small.

```

### December 03 - Alternating Square Arrangement

#### Problem Statement

```
You are given integers ￼ (number of red squares) and ￼ (number of blue squares).
Your task is to arrange the squares in a sequence such that:
No two adjacent squares have the same color.
If it is not possible to create such an arrangement, return "Not possible".

```

```
Input

Two integers:
R￼: Number of red squares.
B￼: Number of blue squares.

Output

A valid arrangement as a string (e.g., "RBRBR" or "BRBRB") that satisfies the condition, or "Not possible" if no valid arrangement exists.


```

Sample Input and Output:
Example 1:

```
Input:
R = 3
B = 2

Output:
"RBRBR"
```

Explanation:

```
The sequence "RBRBR" satisfies the condition since no two adjacent squares are the same color.
```

Example 2:

```
Input:
R = 4
B = 2

Output:
"Not possible"
```

Explanation:

```
It is impossible to arrange 4 red squares and 2 blue squares without
having two adjacent squares of the same color. Hence, the output is "Not possible".

```

### December 04 - Plant Growth Tracker

#### Problem Statement

```
You are designing a program to help a gardener plan how to grow a special type of plant. The plants
grow in an interesting pattern:
• It takes 2 months for the plant to before it starts increasing in numbers.
• Starting from the third month, the number of plants in a month is the sum of the plants in the
previous two months.
For example, in the third month, there are 2 plants (1 + 1), in the fourth month, there are 3 plants (1 +
2), and so on.
```

![image](https://github.com/user-attachments/assets/4810c82d-5cc3-4ab8-a247-64d8d8133e44)

```
However, the gardener needs your help to write a program that predicts the number of plants for
any given number of months, n. Here's the catch:
• The gardener's old computer struggles to handle repeated function calls. As a result, you
cannot use recursion to solve this problem.
```

Example 1:

```
Input: No of Months: 10
Output: 55
```

Explanation:

```
We apply Fibonacci sequence here. Since the growth of the plant perfectly mirrors with Fibonacci
algorithm, as the gardener's computer is old, we have to use for loops and if statements to generate
the sequence.
```

Example 2:

```
Input: No of Months: 12
Output: 144
```

### December 05 - Josephus Problem

#### Problem Statement

```
A total of n people are standing in a circle, and you are one of them playing a game.
Starting from a person, k persons will be counted in order along the circle, and the kth person will be killed.
Then the next k persons will be counted along the circle, and again the kth person will be killed. This cycle will
continue until only a single person is left in the circle.
If there are 5 people in the circle in the order A, B, C, D, and E, you will choose k=3. Starting from A, you will
count A, B and C. C will be the 3rd person and will be killed. Then you will continue counting from D, E and
then A. A will be third person and will be killed.
```

![image](https://github.com/user-attachments/assets/5925562d-fc20-48b7-9114-016a0f2819e0)

```
You will be given an array where the first element is the first person from whom the counting will start and
the subsequent order of the people. You want to be the last one standing. Determine the index at which you
should stand to survive the game. Return an integer denoting safe position.
```

Example 1:

```
Input: n = 3, k = 2
Output: 3
```

Explanation:

```
There are 3 persons so skipping 1 person i.e 1st person 2nd person will be killed. Thus the safe
position is 3.
```

Example 2:

```
Input: n = 5, k = 3
Output: 4
```

Explanation:

```
There are 5 persons so skipping 2 person i.e 3rd person will be killed. Thus the safe position is 4.
```
### December 06 - Target Pair Finder

#### Problem Statement
```
From the initialised list of integers and a target sum by the user,
find all unique pairs of numbers from the list that add up to the target.
You can use nested loops and conditionals.
```


Sample I/O 1:
```
INPUT: 1) A list of integers: numbers = [2, 4, 3, 7, 1, 5].
              2) A target sum: target = 6.
OUTPUT:  Unique pairs are [(2, 4), (1, 5)]
```
Sample I/O 2:
```
INPUT:  1) A list of integers: numbers = [10, 15, 3, 7, 8, 12, 5].
              2)  A target sum: target = 20.
OUTPUT: Unique pairs are [(10, 10), (8, 12), (15, 5)]
Explanation:
The Target Pair Finder problem is about finding pairs of numbers in a list that add up to a specific target value. From the above example we can see that (10, 10): The first 10 and the second 10 in the list add up to 20, so thereby find all sets of unique pair from the given list summing up to the target value.
```
### December 07 - The Magical Tower

#### Problem Statement
```
You are tasked with designing a Magical Tower for a kingdom. The tower has multiple floors, and each floor is supported by a triangular arrangement of magical stones called the Pascal Stones. These stones have unique properties:

The stones at the edges of the triangle are always marked as 1.
The inner stones on each floor are infused with power equal to the sum of the two stones directly above them from the previous floor.
The first floor of the tower contains only a single stone ([1]), and subsequent floors are built according to the rules above. The kingdom's wizard has asked you to construct the first N floors of the Magical Tower.

Your task: Write a program that generates the arrangement of stones for the first N floors of the tower.
```

![PascalTriangleAnimated2](https://github.com/user-attachments/assets/c7be7eab-bd66-4947-93be-e7874f2670d3)

Sample I/O 1:
```
INPUT: numRows=5
OUTPUT:  [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```
Explanation:
```
The first 5 floors of the Magical Tower are constructed as follows:
Floor 1: [1]
Floor 2: [1, 1]
Floor 3: [1, 2, 1] → The second stone (2) is created by adding the two stones directly above it (1 + 1).
Floor 4: [1, 3, 3, 1] → The second stone (3) is created by adding 1 + 2, and the third stone (3) is created by adding 2 + 1.
Floor 5: [1, 4, 6, 4, 1] → The second stone (4) is created by adding 1 + 3, the third stone (6) by adding 3 + 3, and the fourth stone (4) by adding 3 + 1.
Each floor is constructed based on the magical rule that the value of each inner stone is the sum of the two stones directly above it.
```
Sample I/O 2:
```
INPUT:  numRows=1
OUTPUT: [1]
```

# FAQ

#### Who can join the Challenge?

Anyone who is passionate about coding and can dedicate a little time a day for the challenge for the next 31 days.

#### When should I submit the pull request?

You don't need to submit it everyday. Just submit it once you're done with all 31 algorithms.

#### What if I'm not able to code every day?

Not a problem. While coding every day is nice, we understand that other commitments might interfere with it.

Plus its holiday season. So you don't have to solve one problem every day.

Go at your own pace. One per day or 7 a week or even all 30 in a day.

#### What language should I use to code?

Anything! New to GoLang? Best way to practice it.

Wanna find out what all this hype about Python is? Use it!

Any and all languages are welcome.

Maybe you could try using a different language for every problem as a mini-challenge?

#### Fork? Pull request? What is all that? I don't know how to use GitHub!

If you are new to Git or GitHub, check out this out [GitHub](https://guides.github.com/activities/hello-world/)

#### Where are the rest of the problems?

Our code ninjas are hard at work preparing the rest of the problems. Don't worry, they'll be up soon.

#### How should I complete these programs?

We have a folder for each day of the month. Simply complete your code and move the file into that folder.

Be sure to rename your file to the following format: `language_username` or `language_username_problemname`
Some examples:
`python3_exampleUser.py`
`c_exampleUser.c`

**Please do not modify any existing files in the repository.**

#### I forked the repository but some problems were added only after that. How do I access those problems?

Not to worry! Open your nearest terminal or command prompt and navigate over to your forked repository.

Enter these commands:

```bash
git remote add upstream https://github.com/SVCE-ACM/A-December-of-Algorithms-2024.git
git fetch upstream
git merge upstream/main
```

If you're curious, the commands simply add a new remote called upstream that is linked to this repository. Then it 'fetches' or retrieves the contents of the repository and attempts to merge it with your progress.
Note that if you've already added the upstream repository, you don't need to re-add it in the future while fetching the newer questions.

#### I received a merge error. What do I do?

This shouldn't happen unless you modify an existing file in the repository. There's a lot of potential troubleshooting that might be needed, but the simplest thing to do is to make a copy of your code outside the repository and then clone it once again. Now repeat the steps from the answer above. Merge it and then add your code. Now proceed as usual. :)

#### I'm facing difficulties with/need help understanding a particular question.

Open up an [issue](https://github.com/SVCE-ACM/A-December-of-Algorithms-2021/issues) on this repository and we'll do our best to help you out.

###### [[Back to Top]](#----)

![wave](http://cdn.thekrishna.in/img/common/border.png)

```

```
