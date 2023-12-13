# Num2Words


This is the most professional code that you can find on the internet to convert numbers to letters!

I didn't use any library!

This code supports English and Persian.


# How to use:

1. Choose Menu
2. Enter Number
3. Now it's not just a number anymore!

** The results of the Persian menu may be displayed in a mess, so use IDLE for correct display!


# Guide:

I tried my best to write this program in the least number of lines. That's why I didn't use the strings method, because in that case we needed at least 4 dictionaries, but I wrote an algorithm that is like a game with mathematics, and this way we no longer have any restrictions on input numbers.

In this method, I used the function in itself so that there is no need to repeat it and it is repeated inside itself for large numbers.

**Be careful that this idea is not suitable for any program because using the internal function will fill the RAM memory and cause the system to crash.
**

### But let's go to the algorithm logic of this code:

There are a series of numbers that are fixed, so we need to define a fixed dictionary for them.

But the rest of the numbers are actually a combination of the same fixed numbers, so we just have to convert the numbers into fixed parts.

For example, the number 27 is a combination of 20 and 7. But how to do this?

For this, you need to divide the number 27 by 10 and then round down. The obtained number is your tens. To get one, it is enough to get the remainder of dividing 27 by 10.

**What if it was a three-digit number?
**

For three-digit numbers, we do exactly the same as before, with the difference that we use 100 instead of 10.


**But we have reached the difficult part of the story!!**

For numbers greater than 1000, we must write an algorithm that is based on all the previous logics that we have defined!

First, we define a counter equal to 0.

Now, using the while loop, we repeatedly divide the number into 1000 and increase the counter by one number each time. This loop continues until the number obtained is less than 1.

At this moment, the number represents the number of powers of 1000. In this way, we can get the number scale, so we have to define a dictionary for the scales. Of course, I defined it at the beginning.
Now we have to take the big number and re-enter the rest of the number in the function so that the conversion operation is done on it. So for this we use a formula that I thought a lot until it came to my mind!
> The main number minus the big number multiplied by 1000 to the power of the counter

Now it is enough to give the obtained number again to the function and this is repeated until all the digits are translated.
