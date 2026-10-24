# Learning Log

## 2026-10-14 — Lesson 01
- What I did:
    - I understand the terminal commands
    - Installed Homebrew and tools
    - I connected my GitHub account and created a public repository.
    - Setup project folder and virtual environments.
    - then created .gitignore file
    - Wrote my first python program
    - Understand how to call function , print ,input ,docstring , run main() also
    - my first commit for this lesson
    - Added second function
    - I created a README file
- What was difficult: Syntax errors , Second function Writing my self with first function
- How I fixed it: Reading the error then understanding it and fixed ,again and again try and rewrite that second function
- What I learned: I learned print ,input ,function,return ,f string

## Study hours calculator (study_hours.py)
- What it does: This program asks the user for hours on 5 days. Then it calculates the total and average.
- How I tested it: I entered 1, 2, 3, 4, 5. The output was Total: 15.0 and Average: 3.0.
- What was difficult: The hardest part was that total was not updated inside main(), and Python showed a ValueError.
- How I fixed it: I moved total = 0 inside main().
- Error from the bonus question: When I typed "eight", Python showed eight (ValueError: could not convert string to float: 'eight').
- What I learned: A variable created inside a function only exists inside that function. I also learned how to use float() and for loops.

## 2026-10-21 — Lesson 02
- lesson02/predict.py.
    - My guess both are same result : 8 and 8
    - **Questions to answer in your log (your own words):**
        1. Which lines printed what? Was your guess right? wrong
            Output : `8`
                     `None` <- this is I missed to predict
                     `8`
        2. Why does `print(a)` show `None`?
            `double_print()` show `8` on screen because of the `print()` inside it. It has no return, so it gives back `None`. That is why `print(a)` shows `None`  
        3. Why can you do `b + 1` but not `a + 1`?
            `b` holds the number 8, so I can use it in a calculation but `a` holds `None`, and I can't add `1` to `None`

            TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

- `lesson02/scope_bug.py`
    1. **Predict:** What prints? Which line fails? What is the error name?
        - It prints: 110.0
        - I don't know error name
    2. Run it. Was your prediction right?
        - 110.0 <- this is right
        - The failing line is `print(tax)`
        - NameError: name 'tax' is not defined. <- I did not know the error name.
    3. **Fix it** so the program prints the price with tax, and prints **no error**. Do **not** move `tax` outside the function. Hint: how do you save the value that `add_tax` returns, so you can print it?
        - I added this line `result = add_tax(100.0)`
                            `print(result)`
        - Removed this line `print(tax)`
    4. In your log, write 2 sentences: 
        - This error happened because tax is made inside the function, and I tried to use it outside the function.
        - I fixed it by using `return` and saving the value in `result`.

## 2026-10-23 — Lesson 02

- `lesson02/shopping_total.py`
    - What happens if you type `abc` for a price? Write the error name in your log
        - ValueError: could not convert string to float: 'abc'  

### sum_to(3) trace
`sum_to` is in `lesson02/loops_practice.py`. I traced it with n = 3.

| Moment | i | total |
|---|---|---|
| Before the loop | none | 0 |
| 1st pass | 1 | 1 |
| 2nd pass | 2 | 3 |
| 3rd pass | 3 | 6 |

- `total` starts at 0.
- `range(1, 3 + 1)` gives 1, 2, 3.
- In the 1st pass, i is 1, total becomes 1.
- In the 2nd pass, i is 2, total becomes 3.
- In the 3rd pass, i is 3, total becomes 6.
- At the end, `return` gives back total = 6.
- I tested a wrong version. It used + 1, so it counted the passes. I fixed it with + i.
- I predicted sum_to(4) = 10 before running. I was right.

## 2026-10-24 — Lesson 02

### Task 2: functions_practice.py
- Hardest function: discount_price, because I had to find the logic and then convert it to code.
- `%` gives the remainder. `7 % 2` is 1 and `8 % 2` is 0, so a number is even when the remainder is 0.
- When an `assert` failed, Python showed AssertionError. I fixed the function, not the check.

### Task 4: loops_practice.py
- `i == 0 % 2` was wrong because `0 % 2` is 0, so the `if` asked `i == 0`. `i` starts at 1, so it never passed, `count` stayed 0, and `assert count_even(10) == 5` failed.
- `count = count + i` was wrong because it added the number itself, but I wanted to add 1.
- The line `count_even(10) == 5` without `assert` did nothing, because Python worked out the result and then threw it away.

### Knowledge check
1. `print()` is the wrong choice inside `total_cost` because it hands back `None`. In `main()`, the line `grand_total + total_cost(price, quantity)` then `TypeError`, because it tries to add a number and `None`
2. A function with no `return` gives back `None`
3. `print(tax)` fails outside `add_tax` because `tax` exists only inside `add_tax`. I get the value out with `return`.
4. In `def total_cost(price, quantity)`, `price` and `quantity` are parameters. In `total_cost(2.5, 4)`, `2.5` and `4` are arguments.
5. `range(1, 6)` gives 1, 2, 3, 4, 5. It stops before the last number, so sum_to needs n + 1 because it must include n.
6. When an `assert` is true, nothing happens and program keeps going. When it is false, `AssertionError`.