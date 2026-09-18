**Crucial Mistakes I Made**

**The Issue**

1. I intended `break` to affect the outer loop, but it terminates the nearest loop instead. I forgot that `break` terminates the nearest loop.

```python
while True:
    validation = True
    while validation:
        try:
            # Collecting the student score
            math_score = int(input("Enter Your Math Score: \n"))

            if math_score < 1 or math_score > 100:
                print("Score should be between range of 1 - 100")

            else:
                validation = False
        except ValueError:
            print("Enter a valid score.")
        else:
            break
```

**The Fix**

I completely removed the `else` block with `break` from the `try`/`except` chain. The validation loop now stops naturally when `validation` becomes `False`.

```python
while True:
    validation = True
    while validation:
        try:
            # Collecting the student score
            math_score = int(input("Enter Your Math Score: \n"))

            if math_score < 1 or math_score > 100:
                print("Score should be between range of 1 - 100")

            else:
                validation = False
        except ValueError:
            print("Enter a valid score.")
```

**Lesson**
When using nested loops, understand which loop each `break` statement affects.
