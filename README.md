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
- [**December 08 - Digit Manipulation**](#december-08---digit-manipulation)
- [**December 09 - Customer Return Frequency**](#december-09---customer-return-frequency)
- [**December 10 - Concurrent Task Execution**](#december-10---concurrent-task-execution)
- [**December 11 - The Robot Returns**](#december-11---the-robot-returns)
- [**December 12 - Smart Ticketing System**](#december-12---smart-ticketing-system)
- [**December 13 - Minimum Swap Sorting Problem**](#december-13---minimum-swap-sorting-problem)
- [**December 14 - Split the Squad**](#december-14---split-the-squad)
- [**December 15 -  Holiday Gift Arrangement**](#december-15---holiday-gift-arrangement)
- [**December 16 -  Train Platform Calculation**](#december-16---train-platform-calculation)
- [**December 17 -  Cybersecurity Alert Management**](#december-17---cybersecurity-alert-management)
- [**December 18 -  Howard's Rare Gems**](#december-18---howards-rare-gems)
- [**December 19 -  Endless Towers**](#december-19---endless-towers)
- [**December 20 -  Robot Pathways Problem**](#december-20---robot-pathways-problem)
- [**December 21 -  The Intersection**](#december-21---the-intersection)
- [**December 22 -  Earthquake Propagation**](#december-22---earthquake-propagation)
- [**December 23 -  Crystal Grid**](#december-23---crystal-grid)
- [**December 24 -  String Permutation Grouping**](#december-24---string-permutation-grouping)
- [**December 25 -  Task Scheduler**](#december-25---task-scheduler)
- [**December 26 -  Escape The Lava Field**](#december-26---escape-the-lava-field)
- [**December 27 -  Trapping Rain Water**](#december-27---trapping-rain-water)
- [**December 28 -  Bookshelf Organizer**](#december-28---bookshelf-organizer)
- [**December 29 -  The Maze of Weighted Portals**](#december-29---the-maze-of-weighted-portals)
- [**December 30 -  Super Egg Drop**](#december-30---super-egg-drop)
- [**December 31 -  Speed Of Light Simulation**](#december-31---speed-of-light-simulation)


  




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
### December 08 - Digit Manipulation

#### Problem Statement
```
Write a program to calculate the Digit Square Sum for all numbers from 1 to a given positive integer
N.
The Digit Square Sum of a number is calculated by squaring each digit of the number and then
summing up the squares.
```
```
Your task is to write a function that:
1. Takes an integer N as input.
2. Computes the Digit Square Sum for each number from 1 to N.
3. Returns the total sum of these values.
```

Example 1:
```
For N = 12, the program calculates the following:
- 1 -> 1^2 = 1
- 2 -> 2^2 = 4
- 3 -> 3^2 = 9
- ...
- 12 -> 1^2 + 2^2 = 1 + 4 = 5
```
```
The total sum is 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 1 + 2 + 5 = 293.
Output:
The program should return the total Digit Square Sum.
```


### December 09 - Customer Return Frequency

#### Problem Statement

```
You are managing an e-commerce platform and you have a list of customer return
frequencies (how many times a customer has returned products). Your task is to find the total number of
customers who have returned products exactly once.
```


Example 1:

```
Input Format:
returns = [2, 1, 5, 1, 0, 3, 1, 4, 1]
Result: 4
```

```
Explanation:
The list returns = [2, 1, 5, 1, 0, 3, 1, 4, 1] represents the return frequency of each customer.
 We are looking for customers who have returned products exactly once, so we need to count how
many times 1 appears in the list.
```

Example 2:

```
Input Format:
returns = [4, 3, 7, 2, 1, 0, 2, 1, 3]
Result: 2
```
### December 10 - Concurrent Task Execution
#### Problem Statement
```
You are given a list of tasks, where each task has a unique identifier and a list of dependencies (other
tasks that must be completed before this task can be executed). Your goal is to determine a valid
order to execute the tasks using concurrency wherever possible.
You must account for the dependencies and ensure no task runs before its dependencies are
completed. If no valid execution order exists (i.e., there is a cyclic dependency), return an error
message.
```
Input:
```
• A list of tasks, where each task is represented as a pair (task_id, dependencies).
o task_id is a unique identifier for the task (e.g., an integer or string).
o dependencies is a list of task IDs that must be completed before the given task can
run.
```
Output:
```
If a valid task execution order exists, return a list of lists, where each sublist contains the task
IDs that can be executed concurrently at that step.
• If no valid order exists (i.e., a circular dependency is found), return the message "Error: Cyclic
dependency detected".
```

![image](https://github.com/user-attachments/assets/e848e914-4128-457a-be5b-6f64699b86df)

Sample 1:
```
Input:
tasks = [
 ("A", []),
 ("B", ["A"]),
 ("C", ["A"]),
 ("D", ["B", "C"]),
 ("E", ["D"])
]
```
```
Output:
[["A"], ["B", "C"], ["D"], ["E"]]
```
Explanation:
```
• "A" has no dependencies, so it runs first.
• "B" and "C" both depend only on "A", so they can run concurrently.
• "D" depends on both "B" and "C", so it runs after them.
• "E" depends on "D", so it runs last
```
Sample 2:
```
Input:
tasks = [
 ("A", ["B"]),
 ("B", ["A"])
]
```
```
Output:
"Error: Cyclic dependency detected"
```

Explanation:
```
• "A" depends on "B" and "B" depends on "A", creating a cycle.
```

### December 11 - The Robot Returns
#### Problem Statement
```
There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a
sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
You are given a string moves that represents the move sequence of the robot where moves[i] represents
its i
th move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).
Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.
```
```
Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right
once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the
same for each move.
```
![image](https://github.com/user-attachments/assets/d6399796-727c-417b-9f6c-c68a4bc21743)

Sample 1:
```
Input: moves = "UD"
Output: true
Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it
ended up at the origin where it started. Therefore, we return true.
```
Sample 2:
```
Input: moves = "LL"
Output: false
Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false
because it is not at the origin at the end of its moves.
```
Reference: For more information on topological sorting and dependency resolution, check out this guide on https://www.geeksforgeeks.org/topological-sorting/


### December 12 - Smart Ticketing System
#### Problem Statement
```
You are tasked with designing a Smart Ticketing System for a popular concert. The system
manages ticket requests using a queue data structure but with additional complexity:
1. Priority Handling:
Some customers are marked as VIPs (designated by a VIP tag in their request). VIP
customers have higher priority and are served before regular customers, regardless of
their position in the queue. However, among VIPs or regular customers, the requests are
handled in the order they are received (FIFO).
2. Dynamic Ticket Allocation:
Each request includes the number of tickets the customer wants. If the requested tickets
exceed the remaining tickets, the system will allocate all remaining tickets to the
customer.
3. Queue Operation:
If a customer receives fewer tickets than requested due to limited availability, the request
is still considered processed, and the next customer in the queue is served.
You must implement a program that processes these ticket requests and returns the result of
each transaction.
```
Contraints:
```
1. 2. 3. The system starts with N tickets available.
Each request is represented as a string in the format "CustomerName
NumberOfTickets [VIP]"
If [VIP] is not present, the customer is treated as a regular customer.
Requests are processed until all tickets are sold out or the queue is empty
```
Sample 1:
```
Input:
N = 5
requests = ["John 2 VIP" ,"Alice 3", "Bob 2" , "Charlie 1 VIP"]
Output:
["John purchased 2 tickets", "Charlie purchased 1 tickets"
, "Alice purchased 2 tickets", Bob was not served"]
Explanation:
"John 2 VIP" is served first because he is a VIP.
"Charlie 1 VIP" is served next, as he is also a VIP.
"Alice 3" is served, but only 2 tickets are left, so she gets 2.
"Bob 2" cannot be served as there are no tickets remaining.
```
Sample 2:
```
Input:
N = 10
requests = ["Eve 4","Diana 3 VIP","Adam 5","Frank 6 VIP"]
Output:
["Diana purchased 3 tickets","Frank purchased 6 tickets","Eve purchased tickets", "Adam was not served"]
```
### December 13 - Minimum Swap Sorting Problem
#### Problem Statement
```
John has a list of unique integers that he wants to sort in ascending order.
However, he can only sort the list by swapping two elements at a time.
The "cost" of each swap is 1 unit.
Your task is to determine the minimum cost
(i.e., the minimum number of swaps required) to sort the list.
```
Example 1:
```
Sample Input 1:
5
4 3 1 2 5
Sample Output 1:
3
```
Explanation:
```
The given list is [4, 3, 1, 2, 5].
Swap 4 and 1: [1, 3, 4, 2, 5]
Swap 3 and 2: [1, 2, 4, 3, 5]
Swap 4 and 3: [1, 2, 3, 4, 5]
Total swaps = 3. Hence, the minimum cost is 3.
```
Example 2:
```
Sample Input 2:
4
2 3 4 1
Sample Output 2:
3
```
```
Input Format:
The first line contains an integer, N, the total number of integers in the list.
The second line contains N space-separated integers representing the list.
Output Format:
An integer representing the minimum cost (number of swaps) required to sort the list.
```
References: This problem is inspired by sorting algorithms and cycle detection in graphs.

### December 14 - Split the Squad
#### Problem Statement
```
Alice has N students in his class, numbered 1 through N. Each student has
expertise in a subject numbered Ai

. Alice has to divide the students into two

teams Team 1 and Team 2, such that:
1. Each student belongs to exactly one team.

2. The uniqueness of each team is exactly K.

3. Additionally, the difference in the number of students between the two teams
must not exceed D.
```
```
The uniqueness of a team is defined as the number of distinct subjects such that
there is at least one student in the team with expertise in the subject. For
example, the uniqueness of a team denoted by A = [1, 3, 1, 4, 4] is 3.
Alice wants to know if it is possible to distribute the students into two teams
satisfying the conditions.
```
```
Input format
The first line contains an integer T, the number of test cases.
For each test case:
The first line contains three integers N, K, and D.
The second line contains N integers A1
,A2
,....,An
```
```
Output format
For each test case, print YES if Alice is able to make two teams satisfying the
given conditions, otherwise print NO.
```
```
Constraints

1 ≤ T ≤ 105
2 ≤N ≤ 105
1 ≤ K ≤ N
1 ≤ D ≤ N
1 ≤ Ai ≤ N
```
![image](https://github.com/user-attachments/assets/3111d8a4-a02d-4804-b7e4-f2257d631abe)

```
Explanation
Test Case 1:
Divide students into Team 1 = [1, 2, 2] and Team 2 = [3, 4, 4]. Both teams have
a uniqueness of 2, and the difference in the number of students is 0 (≤ 2).
Output is YES.

Test Case 2:
No way to divide the students into two teams with both having a uniqueness of
3 while keeping the size difference ≤ 1.
Output is NO.
```

References
https://www.geeksforgeeks.org/greedy-algorithms
https://www.geeksforgeeks.org/hashing-data-structure



### December 15 - Holiday Gift Arrangement
#### Problem Statement
```
It’s December, and Santa is preparing to deliver gifts. He has N houses to visit,
each requiring a certain number of gifts. Santa’s sleigh can carry a maximum of W gifts at a time.
You are given:
	•	An array houses[] where each element represents the number of gifts required at a house.
	•	The maximum carrying capacity W of Santa’s sleigh.
Santa needs to minimize the number of trips required to deliver all the gifts.
Each trip can serve one or more consecutive houses as long as the total number of gifts does not exceed W.
Write a function minTrips(houses, W) that returns the minimum number of trips Santa needs to deliver the gifts
Here is an artistic depiction of Santa Claus preparing for his December gift deliveries.
It captures the festive and cheerful atmosphere with snow-covered houses and a sleigh loaded with gifts.
```
Example:
```
Input:
houses = [2, 3, 5, 2, 1]
W = 6
Output:
3
Explanation:
	•	Trip 1: Deliver to house 1 and 2 (2 + 3 gifts = 5 ≤ 6).
	•	Trip 2: Deliver to house 3 (5 gifts = 5 ≤ 6).
	•	Trip 3: Deliver to house 4 and 5 (2 + 1 gifts = 3 ≤ 6).

```
Hints:
```
Use a greedy approach to group consecutive houses.
```

### December 16 - Train Platform Calculation
#### Problem Statement
```
We are tasked with determining the minimum number of platforms required at a railway station so that no
train has to wait for another train to depart. Given the arrival times and departure times of multiple trains,
the solution must compute how many platforms are required at the station to handle all trains without delay.
 The input consists of two arrays: arrivals and departures. Each element in arrivals represents the
arrival time of a train, and the corresponding element in departures represents its departure time.
 The goal is to calculate the minimum number of platforms required to ensure that no two trains are
waiting at the same time.
```
```
Constraints
1. Times are represented in 24-hour format (e.g., 9:00 AM = 900, 11:45 PM = 2345).
2. Arrival and departure times are sorted or unsorted but paired correctly for each train.
3. At any point, the number of overlapping intervals (trains at the station) determines the platform
requirement.
```
![image](https://github.com/user-attachments/assets/834a96fa-24d3-45ab-8ef2-cfeb44639432)

Example 1:
```
Input: arrivals = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]
Output 1: Minimum platforms required: 1
```

Explanation
```
Input Format
Two Arrays:

1. arrivals: Contains the arrival times of trains in 24-hour format (e.g., 9:00 AM = 900, 11:45
PM = 2345).
2. departures: Contains the corresponding departure times of the same trains in 24-hour format.

One-to-One Mapping:
1. Each element in arrivals corresponds to the same index in departures. For example:
2. arrivals[0] is the arrival time of Train 1.

3. departures[0] is the departure time of Train 1.
Time Constraints:

1. Arrival time is always less than or equal to the departure time for each train.
2. The arrays can be unsorted but must have the same length.
Sample Input:
arrivals = [900, 940, 950, 1100, 1500, 1800] departures = [910, 1200, 1120, 1130, 1900, 2000]
 Train 1: Arrives at 900, departs at 910.
 Train 2: Arrives at 940, departs at 1200.
 Train 3: Arrives at 950, departs at 1120, and so on.
```
Example 2:
```
Input: arrivals = [1030, 1015, 1045, 1100, 1500, 1530]
departures = [1040, 1105, 1050, 1130, 1515, 1600]
Ouput: Minimum platforms required: 2
```
### December 17 - Cybersecurity Alert Management
#### Problem Statement
```
A cybersecurity company monitors network traffic to detect malicious activities.
The system uses a hash table to store and manage incoming alerts based on their unique threat IDs.
Each alert has associated metadata, including timestamp, IP address, and threat level.
The challenge lies in handling the following constraints efficiently:
High Throughput: The system must process millions of alerts per second, ensuring minimal latency in storing and retrieving threat IDs.
Duplicate Alerts: If the same threat ID is received multiple times within 30 seconds, only the first instance should be stored, and subsequent duplicates should be ignored.
Eviction Policy: Alerts older than 5 minutes must be removed automatically to free up memory.
Priority Updates: If an alert is updated with a higher threat level, the hash table must reflect the latest information without affecting performance.
Memory Optimization: Due to limited memory, the system must handle collisions effectively while maintaining a low memory footprint.
The task is to design the alert management system using a hash table to ensure high efficiency, scalability, and accuracy under the given constraints.
```
Sample 1:
```
Input:
Incoming alerts:
[  {"id": "A123", "timestamp": "00:00:10", "threat_level": 3},  {"id": "A123", "timestamp": "00:00:15", "threat_level": 3},  {"id": "B456", "timestamp": "00:00:20", "threat_level": 2},  {"id": "A123", "timestamp": "00:00:30", "threat_level": 5},  {"id": "B456", "timestamp": "00:05:05", "threat_level": 2}]
Output:
Stored alerts:
[  {"id": "A123", "timestamp": "00:00:30", "threat_level": 5},  {"id": "B456", "timestamp": "00:05:05", "threat_level": 2}]
Explanation:
The duplicate alert for A123 within 30 seconds (00:00:15) is ignored.
The priority of A123 is updated to level 5 (00:00:30).
Alerts older than 5 minutes are removed (e.g., B456 at 00:00:20).
```
Sample 2:
```
Input:
Incoming alerts :
[  {"id": "X001", "timestamp": "12:00:00", "threat_level": 1},  {"id": "Y002", "timestamp": "12:02:30", "threat_level": 3},  {"id": "X001", "timestamp": "12:02:45", "threat_level": 2},  {"id": "Z003", "timestamp": "12:07:00", "threat_level": 4}]
Output:
Stored alerts:
[  {"id": "Y002", "timestamp": "12:02:30", "threat_level": 3},  {"id": "X001", "timestamp": "12:02:45", "threat_level": 2},  {"id": "Z003", "timestamp": "12:07:00", "threat_level": 4}]
```

### December 18 - Howard's Rare Gems
#### Problem Statement
```
Howard, a charismatic yet reckless gem dealer, specializes in acquiring rare and exotic gemstones to make huge profits. He thrives on risky deals and has a knack for identifying high-value chains of diamonds, rubies, and emeralds.

Howard knows he can maximize his earnings if he finds chains with a palindromic arrangement of gemstones, as these rare patterns fetch a significantly higher price.

The prices of individual gems are as follows:
- A diamond (D) is worth $500.
- A ruby (R) is worth $250.
- An emerald (E) is worth $100.

For palindromic chains, the total price is multiplied by the chain's length, adding a massive bonus to the profit. Given a long chain of mixed gemstones, Howard must determine the maximum profit he can achieve by cutting out the most valuable palindromic chain.

```
Example 1:
```
Chain: "RDEREDRRRD"
Output: $7,250
Explanation: The longest palindromic chain is "RDEREDR", worth $(250 + 500 + 100 + 100 + 500 + 250 + 250) \times 7 = 7,250.
```


Example 2:
```
Chain: "DERRREDERREDEREDR"
Output: $24,000
Explanation: The longest palindromic chain is "REDERREDER", worth $(250 + 100 + 500 + 250 + 500 + 250 + 500 + 100 + 250 + 250) \times 10 = 24,000.
```

Hints:
```
Use efficient algorithms like Manacher’s Algorithm to identify the longest palindromic substring quickly and calculate the profit.
```

### December 19 - Endless Towers
#### Problem Statement
```
The King's Challenge Story:

The king has a treasure of golden disks stacked in ascending order of size on a tower ( disk A).
He wants to move these disks to another tower (disk C). However, to ensure the safety of his treasure:

1. Only one golden disk can be moved at a time.


2. A larger golden disk cannot be placed on top of a smaller disk.


3. A third tower (disk B) must be used as an intermediate step.



The king challenges his wisest advisor to find the minimum number of moves to transfer all the disks to Tower C while following these rules.

The Question:

"If the king had 4 disks, what is the minimum number of moves required to complete the task, and what is the sequence of moves ? “
Here are two sample inputs and outputs for the Tower of Hanoi problem described as the king's challenge:
```
Sample 1:
```
Number of golden disks: 3
Towers: A (start), B (helper), C (destination)

Output:
Minimum number of moves: 7
Sequence of moves:
1. Move disk 1 from A to C
2. Move disk 2 from A to B
3. Move disk 1 from C to B
4. Move disk 3 from A to C
5. Move disk 1 from B to A
6. Move disk 2 from B to C
7. Move disk 1 from A to C
```
Explanation:
```
Initial Setup:

Start tower (A) contains three disks, stacked in ascending size (smallest on top).

Helper tower (B) is empty and will be used as an intermediate step.

Destination tower (C) is where all disks must end up, following the rules:

1. Only one disk can be moved at a time.


2. A larger disk cannot be placed on a smaller disk.


3. Use all three towers effectively.


Steps and Explanation:

1. Move disk 1 from A to C:

The smallest disk is moved directly to the destination tower.



2. Move disk 2 from A to B:

The second-smallest disk is moved to the helper tower, as the destination is occupied.



3. Move disk 1 from C to B:

The smallest disk is moved from the destination tower to the helper tower, stacking it on top of disk 2.



4. Move disk 3 from A to C:

The largest disk is moved directly to the destination tower.



5. Move disk 1 from B to A:

The smallest disk is moved back to the start tower, freeing up space on the helper tower.



6. Move disk 2 from B to C:

The second-smallest disk is moved to the destination tower, stacking it on top of the largest disk.



7. Move disk 1 from A to C:

Finally, the smallest disk is moved to the destination tower, completing the puzzle.



Final State:

Tower A: Empty

Tower B: Empty

Tower C: All three disks stacked in ascending size (smallest on top).



Minimum Moves:

The total number of moves is 7, which matches the formula  for .
```
Sample 2:
```
Number of disks: 4
Towers: A (start), B (helper), C (destination)

Output:
Minimum number of moves: 15

Sequence of moves:
1. Move disk 1 from A to B
2. Move disk 2 from A to C
3. Move disk 1 from B to C
4. Move disk 3 from A to B
5. Move disk 1 from C to A
6. Move disk 2 from C to B
7. Move disk 1 from A to B
8. Move disk 4 from A to C
9. Move disk 1 from B to C
10. Move disk 2 from B to A
11. Move disk 1 from C to A
12. Move disk 3 from B to C
13. Move disk 1 from A to B
14. Move disk 2 from A to C
15. Move disk 1 from B to C

```
### December 20 - Robot Pathways Problem
#### Problem Statement
```
You are given an integer array steps[] representing different step sizes a robot can take and an integer distance.
Find the number of distinct ways the robot can reach the exact distance by taking any combination of the given step sizes.
Note:
The robot can take any step size from steps[] as many times as needed.
Steps can be taken in any order.
```
Sample:
```
Input:
steps[] = {1, 2, 3}
distance = 4
Output:
7
```
Explanation:
```
The robot can reach the distance in the following ways:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(2, 1, 1)
(2, 2)
(1, 3)
(3, 1)
```

### December 21 - The Intersection
#### Problem Statement

```
You are given two singly linked lists that may or may not intersect. Write a program to
find the value of the node where the two linked lists intersect. If they do not
intersect, return "No intersection found."
```
![image](https://github.com/user-attachments/assets/52c2bf7e-7e2b-4aff-b805-ef4682674b11)

Input Format
```
1. Enter the number of nodes in the first linked list N: An integer.
2. Enter N space-separated node values for the first linked list: The values of the
nodes.
3. Enter the number of nodes in the second linked list M: An integer.
4. Enter M space-separated node values for the second linked list: The values of
the nodes.
5. Enter the position (1-indexed) in the first linked list where the second linked
list intersects (0 if no intersection): An integer.
```
Output Format:
```
The program should display:
1. "The intersection point is: <value>" if an intersection exists.
2. "No intersection found." if the linked lists do not intersect.
```
Sample Input 1:
```
Enter the number of nodes in the first linked list: 5
Enter the node values: 1 2 3 4 5
Enter the number of nodes in the second linked list: 3
Enter the node values: 6 7 8
Enter the position of intersection: 3
```
Sample Output 1
```
The intersection point is: 3
```
Sample Input 2:
```
Enter the number of nodes in the first linked list: 4
Enter the node values: 10 20 30 40
Enter the number of nodes in the second linked list: 3
Enter the node values: 50 60 70
Enter the position of intersection: 0
```
Sample Output 2:
```
No intersection found.
```

### December 22 - Earthquake Propagation
#### Problem Statement

```
You are given a list of buildings in a city, each represented by a 0-indexed 2D integer array buildings[i] = [xi,
yi, ri]. Here, xi and yi are the coordinates of the building, and ri is the radius of its earthquake shockwave.
When an earthquake occurs at a building, it will affect all buildings within its radius. The affected buildings
will further propagate the earthquake shockwave to other buildings within their radius.
Return the maximum number of buildings that can be affected if you trigger the earthquake at one building.
```
![image](https://github.com/user-attachments/assets/18cf62d5-9d59-4e2c-9372-46ec3ffe180d)

Sample I/O 1:
```

Input: buildings = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2
earthquakes . If an earthquake occurs at the left building, the right
building will not be affected.But if an earthquake occurs at the
right building, both buildings will be affected.So the maximum
number of buildings that can be affected is max(1, 2) = 2.
```
Sample I/O 2 :
```
Input: buildings = [[1,1,5],[10,10,5]]
Output: 1
```

### December 23 - Crystal Grid
#### Problem Statement
```
In the ancient kingdom, a mystical Crystal Grid of size N x N (where 1 <= N <= 500) holds secrets of immense power.
Each cell in the grid contains a magical value. To unlock the grid's energy, the wizard has devised a three-step process based on its structure:

Task 1: The Diagonal Energy Difference
Extract the Primary Energy Path, which is the sum of magical values along the primary diagonal (from the top-left to the bottom-right of the grid).
Extract the Secondary Energy Path, which is the sum of magical values along the secondary diagonal (from the top-right to the bottom-left of the grid).
Calculate the absolute difference between these two paths:
Diagonal_Energy = |Sum_primary - Sum_secondary|

Task 2: The Boundary Energy
Calculate the Boundary Energy, which is the sum of all magical values located on the boundary of the grid (the outermost rows and columns).

Task 3: The Final Magical Result
Combine the results to compute the Final Magical Result:
Final_Result = Diagonal_Energy + Boundary_Energy
```
Sample I/O:
```
Crystal Grid (N = 3):
1 2 3  
4 5 6  
7 8 9  
Diagonal Energy Difference:

Primary Diagonal = 1 + 5 + 9 = 15
Secondary Diagonal = 3 + 5 + 7 = 15
Diagonal_Energy = |15 - 15| = 0
Boundary Energy:

Boundary elements = 1, 2, 3, 4, 6, 7, 8, 9
Boundary_Energy = 1 + 2 + 3 + 4 + 6 + 7 + 8 + 9 = 40
Final Magical Result:
Final_Result = Diagonal_Energy + Boundary_Energy = 0 + 40 = 40
```
### December 24 - String Permutation Grouping
#### Problem Statement
```
Generate a function that groups the unique permutations of a string based on their
lexicographical order but extracted in a specific non-standard manner.
```
![image](https://github.com/user-attachments/assets/63965430-b425-46de-ad14-0b022631a971)
```
1. Given a string s, generate all unique permutations of the string.
2. A
er generating the permutations, group them based on their first letter. For
each letter, list the permutations that start with that letter.
3. Finally, return a dictionary where each key is the starting letter of the
permutations, and the value is a list of permutations starting with that letter,
formatted in lexicographical order.
```
Input Format
```
● A single string s contains only lowercase letters (1 ≤ length of s ≤ 12). The string
may contain duplicates.
```
Sample Input and Output
```
Input 1: abc
Output 1:
{
'a': ['abc', 'acb'],
'b': ['bac', 'bca'],
'c': ['cab', 'cba']
}
```
Constraints
```
● The function should handle duplicate letters appropriately in the permutations
(i.e., no duplicate permutations in the output).
● The output should be sorted for each group in lexicographical order.
```
References :
https://mathworld.wolfram.com/LexicographicOrder.html


### December 25 - Task Scheduler

#### Problem Statement
```
Design a task scheduler using any data structure where each node contains the task
description and its priority. The tasks should be arranged in the list based on priority
(highest priority first). Allow for the following operations:
• Add a new task with priority.
• Remove a completed task.
• Search for Task
• Display the tasks in priority order.
```
![image](https://github.com/user-attachments/assets/d4e81a33-06da-4a28-8933-b7b3ed7af25e)


Example Input
```
• Add task: (”Complete Assignment”, Priority 2)
• Add task: (”Buy Groceries”, Priority 1)
• Display: [(”Complete Assignment”, Priority 2), (”Buy Groceries”, Priority 1)]
• Remove task: ”Complete Assignment”
• Final list: [(”Buy Groceries”, Priority 1)]

```
Output Format
```
Use a menu driven Task Scheduler.
```
Constraints
```
• Try to keep Search time in O(k) ,i.e a constant lookup.
• Program Should be Modular.
• The program must compute the result within 1 second.
```
Notes
```
You can create any sort of data structure for the Scheduler but make sure it is self
balancing based on priority. For achieving constant lookup time during searching check
out dynamic hashing. Also a bonus criteria would be:
• Trying to reduce runtime memory.
• Storing the Scheduler data locally using file system methods.
```



### December 26 - Escape The Lava Field

#### Problem Statement
```
You are standing at the edge of a dangerous lava field, represented as an array of stones.
Each stone has a number written on it, indicating the maximum number of stones you can
jump forward from that position. Starting from the first stone, determine if it’s possible to
safely reach the last stone without falling into the lava.
Problem Statement:-
Given an array where each element represents the maximum number of steps you can
jump forward from that element, return true if we can reach the last index starting from the
first index. Otherwise, return false.
```
![image](https://github.com/user-attachments/assets/157af115-b519-4450-8fc2-a9ba768b7b2a)

Example 1:
```
Input:nums = [2, 3, 1, 0, 4]
Output: True
Explanation:
We start at index 0, with value 2 this means we can jump to index 1 or 2.
From index 1, with value 3, we can jump to index 2, 3, or 4. However, if we jump to index 2
with value 1, we can only jump to index 3.
So we jump to index 1 then index 4 reaching the end of the array.
Hence, we return true.
```
Example 2:-
```
Input:nums = [3, 2, 1, 0, 4]
Output: False
```
### December 27 - Trapping Rain Water

#### Problem Statement
```
Given an array representing bar heights in an elevation map, compute the total units of
water trapped between bars after raining. The width of each bar is 1. Return the total
trapped water.
Problem Statement:-
Given n non-negative integers representing an elevation map where the width of each bar
is 1, compute how much water it can trap after raining.
```
Example 1:
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented
by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water
(blue section) are being trapped.
```
Example 2:-
```
Input: height =
[4,2,0,3,2,5]
Output: 9
```
### December 28 - Bookshelf Organizer

#### Problem Statement

```
Sonny has several books and wants to organize them into shelves such
that each shelf contains exactly shelfSize books, and the books on each
shelf are arranged in sequential order based on their assigned numbers.
Given an integer array books where books[i] represents the number on the
ith book and an integer shelfSize, return true if he can organize the books
this way, or false otherwise.
```

SAMPLE TEST CASE:

```
INPUT:
books = [1, 2, 3, 6, 2, 3, 4, 7, 8]
shelfSize = 3
One possible arrangement is:
Group 1: [1, 2, 3]
Group 2: [2, 3, 4]
Group 3: [6, 7, 8]
OUTPUT:
So,you return true
If not possible,you return false.
```

SAMPLE TEST CASE 2:

```
books = [1, 2, 3, 4, 5]
shelfSize = 4
One possible arrangement is:
[1, 2, 3, 4]
But we can’t allot a shelf for the book 5.
OUTPUT:
So,you need to return false.
```

```
P.S: While a O(N*N) solution will be able to handle small test cases,it will fail
with large enough ones,so can you come up with a solution that can visit
each element only once,i.e a O(N) solution?
```
### December 29 - The Maze of Weighted Portals

#### Problem Statement

```
You are given a rectangular grid of size N x M, where each cell represents a
room. Some rooms are connected by portals with varying weights. Moving
through a portal costs you a certain weight (energy). Your goal is to move from
the top-left corner (1,1) to the bottom-right corner (N,M) with the minimum
total weight possible. However, you have a restriction: you can only use each
portal at most once.
Each portal connects exactly two rooms (not necessarily adjacent), and there are
P portals in total. You can move to neighboring rooms (up, down, left, right) at
no cost, but the portals are your only means to reduce the distance significantly.
```

![image](https://github.com/user-attachments/assets/45cbadc6-bcc1-4768-a447-cce3b80893b6)


Input Format

```
1. First line: Two integers N (number of rows) and M (number of columns).
2. Second line: An integer P (number of portals).
3. Next P lines: Each line contains four integers: x1, y1, x2, y2, W:
○ (x1, y1) and (x2, y2) are the grid coordinates of the two rooms
connected by the portal.
○ W is the weight of the portal.
4. Output: An integer representing the minimum total weight to reach (N,
M) from (1, 1).
```

Constraints

```
● 1 ≤ N, M ≤ 50
● 1 ≤ P ≤ 1000
● 1 ≤ W ≤ 100
● You may assume all portals are distinct, and (1, 1) and (N, M) are
guaranteed to be part of the grid.
```

Input 1:

```
4 4
3
1 1 2 3 5
2 3 4 4 2
1 2 4 1 8
```

Output 1:

```
10
Explanation for Input 1:
● The grid is 4 x 4.
● There are 3 portals:
○ Portal 1 connects (1,1) to (2,3) with a weight of 5.
○ Portal 2 connects (2,3) to (4,4) with a weight of 2.
○ Portal 3 connects (1,2) to (4,1) with a weight of 8.
● Using Portal 1 to go from (1,1) → (2,3), then Portal 2 to go from (2,3)
→ (4,4) gives the minimum weight path 5 + 2 = 10.
```

Input 2:

```
3 3
2
1 1 3 3 4
1 2 2 3 7
```

Output 2

```
4
Approach and Challenges
1. Graph Representation:
Represent the grid as a graph where each cell is a node. Portals act as
weighted edges connecting non-adjacent nodes.
2. Pathfinding with Constraints:
Use a modified Dijkstra's algorithm or A* search to find the shortest path.
Since portals can only be used once, you must maintain state information
for visited portals.
3. Optimization:
Efficiently handle up to 1000 portals and avoid redundant calculations.
Use priority queues or dynamic programming for optimal performance.
```
### December 30 - Super Egg Drop

#### Problem Statement

```
You are tasked with finding the critical floor in a building with n floors using k identical eggs. The critical
floor, fff, is defined as the highest floor where an egg does not break when dropped. The following rules
apply:
If an egg is dropped from floor xxx:
It breaks if x>fx > fx>f.
It does not break if x≤fx \leq fx≤f.
Objective:
Minimize the maximum number of moves required to determine the critical floor fff with certainty.
Constraints:
If an egg breaks, it can no longer be used.
If an egg does not break, it can be reused for subsequent drops.
You may drop eggs from any floor between 1 and nnn.
Goal:
Determine the minimum number of moves required to guarantee the discovery of fff, regardless of the initial position of fff .
```
![image](https://github.com/user-attachments/assets/b005f7c4-637f-46bb-a80b-934f04bf0bf2)

Sample I/O 1:

```
Input: k = 2 (eggs), n = 6 (floors)
Output 1: Minimum moves required = 3
```

Explanation of input format 1:

```
The input for this problem consists of two integers:
1. Number of Eggs (kkk):
o Represents the total number of identical eggs available for testing.
o Each egg can either break or remain intact when dropped from a floor.
o If an egg breaks, it cannot be reused in further tests.
2. Number of Floors (nnn):
o Represents the total number of floors in the building, labeled from 1 to nnn.
o The goal is to find the critical floor fff (where 0≤f≤n0 \leq f \leq n0≤f≤n) using the minimum
number of moves.

Key Characteristics of Input:
1. Both kkk (number of eggs) and nnn (number of floors) are positive integers:
o 1≤k≤1001 \leq k \leq 1001≤k≤100
Meaning of k=1k = 1k=1:
 If there is only one egg, it can be tested sequentially from the first floor upwards until it breaks. In
this case, the worst-case number of moves is equal to nnn.
Meaning of n=1n = 1n=1:
 If there is only one floor, the critical floor is either floor 1 or floor 0 (no breaking). Only one move is
needed.
```
Sample I/O 2:

```
Input: k = 3 (eggs), n = 14 (floors)
Ouput: Minimum moves required = 4
```
![image](https://github.com/user-attachments/assets/7dbd12bd-2d4c-4d53-a566-f65102af7d27)

References :

https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

https://en.wikipedia.org/wiki/Shortest_path_problem

https://en.wikipedia.org/wiki/A*_search_algorithm


### December 31 - Speed of Light Simulation

#### Problem Statement
```
You are designing a physics simulation where the speed of light needs to be
 approximated efficiently. The simulation requires calculating the normalized
 velocity vectors of particles in real-time. Given `n` particles with their
 initial velocity components, devise an algorithm to compute their normalized
velocities within strict time constraints. You can't use division in the algorithm
 as it is a slow system-independent process.

```


## Input Format

![image](https://github.com/user-attachments/assets/0418e03c-b303-4f82-bf4d-dff3cd751301)

## Output Format
Output `n` lines, each containing three floating-point numbers representing the normalized velocity vector of the `i`-th particle:

![image](https://github.com/user-attachments/assets/daac15d2-f2aa-40ea-af56-fd3ec3338a65)

![image](https://github.com/user-attachments/assets/7f80c1ac-4de8-46b4-b76a-2ff52b1a242b)

## Constraints

![image](https://github.com/user-attachments/assets/dad67bbc-c7e2-4e03-8a9b-89b5e78e1340)

## Notes
```
Division is not allowed. To achieve the required performance, traditional square root
 computations may not suffice for large `n`. Consider optimizing your solution using 
approximation techniques such as Newton's method and try using bit manipulation based on
 the IEEE 754 format. For more pointers, look for the Quake III algorithm.

```
## Example Input

```
vec1:  3  4  0
vec2: -6  8  0
vec3:  5  12 0

```
## Example Output

```
normalised vec1:  0.6      0.8      0.0
normalised vec2: -0.6      0.8      0.0
normalised vec3:  0.384615 0.923077 0.0

```
## Edge Cases

![image](https://github.com/user-attachments/assets/0c83f6d1-9cfb-4434-9080-816e7f8cdde8)

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
