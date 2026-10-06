**Crucial Mistakes I Made**


1. **Complicating `break` behavior**
**The Issue**
 I mistakenly placed `break` inside the `try`/`except` block instead of the loop I intended to control. Since `break` exits the nearest loop, it stopped the validation loop rather than the intended outer loop.

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

2. **Terminating loop too early.**

**The Issue**
In the function file, in the delete_student function, i was terminating the loop, after the first iteration count, it doesn't loop through the whole list.

```python
        # Checking if the student exist in memory
        for index, name in enumerate(students):
            if student == name["name"]:
                # Deleting student and returning success.
                del students[index]
                return 'Student deleted Successfully.'
            else:
                return f'{student} does not exist.'
```

**The Fix**
I removed the `else` block, and shifted the `return` statement outside the loop, so it will return the statement only after it has finish looping over the whole `list`, and it doesn't find a match.

```python
        # Checking if the student exist in memory
        for index, name in enumerate(students):
            if student == name["name"]:
                # Deleting student and returning success.
                del students[index]
                return "Student deleted Successfully."
        # returns does not exist message, if the student doesn't exist.
        return f"{student} does not exist."
```

**Lesson**
When solving some logical problems, your `if` block doesn't always need an `else` block. 


