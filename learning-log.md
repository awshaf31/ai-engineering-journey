# Learning Log

## 2026-10-14 — Lesson 01
- What I did:
    - I understand the terminal commands
    - Install Homebrew and tools
    - I connected my GitHub account and created a public     repository.
    - Setup project folder and virtual environments.
    - then created .gitignore file
    - Wrote my first python program
    - Understand how to call function , print ,input ,docstring , run main() also
    - my first commit for this lesson
    - Added second function
    - Created a README file
- What was difficult: Syntax errors , Second function Writing my self with first function
- How I fixed it: Reading the error then understanding it and fixed ,again and again try and rewrite that second function
- What I learned: I learned print ,input ,function,return ,f string

## Study hours calculator (study_hours.py)
- What it does: This program asks the user for hours on 5 days. Then it calculates the total and average.
- How I tested it: I entered 1, 2, 3, 4, 5. The output was Total: 15.0 and Average: 3.0.
- What was difficult: The hardest part was that total was not updated inside main(), and Python showed an error.
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
        - NameError: name 'tax' is not defined. <- this is wrong.
    3. **Fix it** so the program prints the price with tax, and prints **no error**. Do **not** move `tax` outside the function. Hint: how do you save the value that `add_tax` returns, so you can print it?
        - I added this line `result = add_tax(100.0)`
                            `print(result)`
        - Removed this line `print(tax)`
    4. In your log, write 2 sentences: 
        - This error happened because tax is made inside the function, and I tried to use it outside the function.
        - I fixed it by using `return` and saving the value in `result`.