# AoC Notes

## Day 1: Sonar Sweep

### Part 1

As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the nearby sea floor. On a small screen, the sonar sweep report (your puzzle input) appears: each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.

For example, suppose you had the following report:

199
200
208
210
200
207
240
269
260
263
This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 199, 200, 208, 210, and so on.

The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
In this example, there are 7 measurements that are larger than the previous measurement.

How many measurements are larger than the previous measurement?

#### Mental Model

Graph of distance vs. depth (2D)
Interested in relative point change as you move along the line (so you only need to remember 2 values at a time, not all the values.)

All the information you need to know is:

- What is the value of the line I am currently on? (X)
- What was the value of the line before the one I am currently on. (Y)
- Is X < Y or X >= Y? (we only care about increase, so just the first case.)
- If X < Y increment a counter that starts at 0.

Programming tools required:

- Ability to iterate over the lines in a file as overlapping pairs.
- Ability to compare the integer values of x, y in a pair.
- Ability to store and update a count variable.

Python/Optimisation questions:

- Is it best to read in all the lines at once, assign them a row index, then compare?
- Or is it better to read in a pair, compare, and then do it again?
- How can I make this be written in as few lines of code as possible?
- Are there new cool ways in Python 3.10 to do this?

First basic hack with no looking stuff up was to do a zip (handle all lines as pairs), but this doesn't allow for overlap between pairs (duh).
(i.e. it zips 0-1 2-3 4-5, where I want the values from 0-1, 1-2, 2-3, 3-4)

Then I looked up new itertools functions in Python 3.10.6 and found they've added itertools.pairwise(iterable), which gives me exactly this iteration behavior.

What could I have improved?

- Make smaller refined test data set rather than using input immediately.
- Get obvious prints in early.

Follow-up learning questions:

- Review https://docs.python.org/3.10/library/itertools.html to understand these iterables; also then understand how to write basic iterators the 'horrible'/original way.

## Part 2

Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.
Instead, consider sums of a three-measurement sliding window. Again considering the above example:

199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H

Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:

A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)
In this example, there are 5 sums that are larger than the previous sum.

Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

### Mental Model

A long list where you can group into sets of 3, sum the value of those sets, and then compare each set's sum to its immediately adjacent neighbour.

All the information you need to know is:

- What is the current 3 part segment I am currently on? (A)
- What is the sum of the 3 parts of A?
- What is the adjacent 3 part segment (positioned to the right on a line) (B)?
- What is the sum of the 3 parts of B?
- Is sum(A) < sum(B) or sum(A) >= sum(B)? (we only care about increase, so just the first case.)
- If sum(A) < sum(B) increment a counter that starts at 0.
- That our dummy input produces a count of 5.

Python/Optimisation questions:

- How can I make this be written in as few lines of code as possible?

What did I actually do?:

- Set up a small example of a for loop using slicing to get a sliding window of values.
- Remembered how to write list comprehensions and how slicing works in Python3.
- Used the example test data set from the part2 question as a dummy input file.

What could I have improved?

- I'm a dumbass and didn't realise until I was writing it that you can just re-use the iterator from part 1 to do the sum comparisons.

## Day 2: Dive

## Part 1

Now, you need to figure out how to pilot this thing.
It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.
Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.

The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

forward 5
down 5
forward 8
up 3
down 8
forward 2
Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

forward 5 adds 5 to your horizontal position, a total of 5.
down 5 adds 5 to your depth, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13.
up 3 decreases your depth by 3, resulting in a value of 2.
down 8 adds 8 to your depth, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15.
After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?

### Mental Model

A 2D plot with depth and horizontal position; our 'pilot' (point) moves within this space on both axes.

All the information you need to know is:

- What is the next move?
    if forward, add to horizontal_position count
    if down, add to depth count.
    if up, subtract from depth count.
- What is the multiple of final horizontal position and final depth?

Programming tools required:

- Ability to store and update two count (int) variables (for horizontal and depth respectively).
- Ability to conditionally decide (based on string equivalence) which count variable to increment.
- Ability to multiply two integers together and print the result.

Python/Optimisation questions:

- How can I write this in as few lines of code as possible?
I think this is going well; applying list comprehensions is good.

What did I actually do?:

- Used the 'all the information' problem statement above, and wrote the solution very fast :))

# Part 2

Based on your calculations, the planned course doesn't seem to make any sense. You find the submarine manual and discover that the process is actually slightly more complicated.

In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0. The commands also mean something entirely different than you first thought:

down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
It increases your horizontal position by X units.
It increases your depth by your aim multiplied by X.
Again note that since you're on a submarine, down and up do the opposite of what you might expect: "down" means aiming in the positive direction.

Now, the above example does something different:

forward 5 adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change.
down 5 adds 5 to your aim, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13. Because your aim is 5, your depth increases by 8*5=40.
up 3 decreases your aim by 3, resulting in a value of 2.
down 8 adds 8 to your aim, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15. Because your aim is 10, your depth increases by 2*10=20 to a total of 60.
After following these new instructions, you would have a horizontal position of 15 and a depth of 60. (Multiplying these produces 900.)

Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?

## Day 3: Binary Diagnostic

The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.
The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.
You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010

Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

### Day 3 Part 2

life_support_rating = o2_generator_rating * co2_scrubber_rating

let l be a list of binary numbers (typed as strings)
for index (range of length list) for each element in l
    KEEP only elements that meet a criteria at  index
    IF the list of elements reaches size 1, stop.
    SET the rating value equal to that element.

o2_generator_rating (10111 23):
    DETERMINE most common value (0 or 1) in current bit; keep only numbers with that bit in that position.
        IF 0 and 1 are equally common at the current bit, keep bits with 1 in that position.

co2_scrubber_rating (01010 10):
    DETERMINE least common value (0 or 1) in current bit; keep only numbers with that bit in that position.
        IF 0 and 1 are equally common at the current bit, keep bits with 0 in that position.

Multiple is 230.

### Pseudocode with Adam

There's a style from a famous textbook on algorithms (Introduction to Algorithms, Rivest, Leiserson and Cormen.)
(For and while are universal constructs, write english for the rest.)

There is no global standard.
Most people words are closest to C and Basic, probably. Because it's determined by what people grew up with as languages.
(foreach, loop until, if x matches, otherwise; let means assign a variable and give it these values; case)
mathematically inclined or statistically inclined might use mathematical notation (e.g. Set notation.)
