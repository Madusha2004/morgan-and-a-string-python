# morgan-and-a-string-python

An implementation of the "Morgan and a String" algorithm in Python, featuring a detailed, step-by-step explanation to aid understanding for beginners. (Taken from HackerRank)

---

**Initial Thoughts on this Problem:**  
This challenge initially presented a solvable chance of around **46.5%** (what i rember), indicating it was quite tricky to approach at first glance! This explanation details how I tackled it. I hope this helps anyone out there!

The "Morgan and a String" problem is about merging two given words (strings) into a single new word.  
Your task is to build this new word **character by character**, always choosing the next letter from either of the two original words, in a way that makes the final combined word the absolute **smallest** possible in alphabetical order.

---

If that sounds confusing, imagine there are 2 piles of letter cards called pile A and pile B.  
In pile A, there are 5 cards: "A", "P", "P", "L", "E" (in this order — "A" is on top, followed by the others).  
In pile B, there are 7 cards: "A", "P", "R", "I", "C", "O", "T" (again, in order — "A" is on top).

- You can only take the 'A' from "APPLE" first. After you take 'A', 'P' becomes the top card.
- You can only take the 'A' from "APRICOT" first. After you take 'A', 'P' becomes the top card.

Like that, your goal is to make the shortest word in alphabetical order by picking one card at a time from each pile.

You always want to pick the card that will make your word alphabetically smaller.

---

**Explanation of the code starts here...**  
The main work happens inside the `morganAndString(a, b)` function. This function takes two strings, `a` and `b`, as input.

---

### **01.) The "Sentinel" Character: The Ultimate Tie-Breaker**

**What is a "sentinel"?**  
It's a technique where a special character (sentinel) is used to make the final decision when all other comparisons are equal.

```python
a += chr(ord('z') + 1)
b += chr(ord('z') + 1)
```

- `ord('z')` gives the numerical value (ASCII/Unicode) of the character `'z'`.
- `ord('z') + 1` gives the value just after `'z'`, which is `'{'` (a curly brace) in ASCII.
- `chr(...)` converts that number back into a character, so `chr(ord('z') + 1)` results in `'{'`.

**Why `{`?**  
Because it acts as a guard at the end of the string (pile of cards), it comes after all lowercase and uppercase letters in alphabetical order.

So, when one string is completely used up (except for its sentinel), comparisons like `a[i] < b[j]` will favor the string that still has actual letters. The sentinel makes the "used up" string appear larger, so the remaining real characters in the other string get picked.

This simplifies suffix comparison logic.

---

### **Looping**

```python
i, j = 0, 0
result = []
```

- `i` and `j` are pointers. `i` points to the current character in string `a`, and `j` points to the current character in `b`.
- Both start at 0.
- `result = []` is an empty list to build the final result.

---

### **Main Loop**

```python
while i < len(a) - 1 or j < len(b) - 1:
```

This loop processes only the original strings, not the sentinel characters (hence the `-1`).

Three key scenarios occur inside this loop:

---

#### **Scenario 1: Character in `a` is Smaller**

```python
if a[i] < b[j]:
    result.append(a[i])
    i += 1
```

If `a[i]` is smaller than `b[j]`, add `a[i]` to the result and move `i` to the next character.

---

#### **Scenario 2: Character in `b` is Smaller**

```python
elif b[j] < a[i]:
    result.append(b[j])
    j += 1
```

If `b[j]` is smaller, do the same — pick it, add to result, and move `j`.

---

#### **Scenario 3: Characters are Equal (Tricky Part)**

```python
else:  # a[i] == b[j]
    if a[i:] < b[j:]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1
```

If both characters are the same, we compare the remaining suffixes of both strings lexicographically.

Example:  
If `a[i:]` is `"APPLE{"` and `b[j:]` is `"APRICOT{"`:

- 'A' == 'A', 'P' == 'P' — no decision.
- 'P' (from APPLE) < 'R' (from APRICOT) → So `"APPLE{"` is smaller.

Therefore, pick from the string that leads to the smaller suffix.

This approach ensures that if one string has only the sentinel left, the string with remaining real characters gets chosen.

---

#### **Scenario 4: Putting It All Together**

```python
return ''.join(result)
```

Once the loop finishes, `result` contains all selected characters. `''.join(result)` merges them into a single string.

---

### **Bonus: HackerRank Format**

This section isn't part of the algorithm itself but is relevant to how HackerRank handles input/output.

```python
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        a = input().strip()
        b = input().strip()
        result = morganAndString(a, b)
        fptr.write(result + '\n')
    fptr.close()
```

- `if __name__ == '__main__'`: Ensures this block only runs when the script is executed directly.(this is a standard python constructor)
---

Think of it like this:

You have two labels:

One label says "My Module" (which is what `__name__` becomes when imported).
The other label says "Main Program" (which is what `__name__` becomes when run directly).
The if statement is asking: "Does this file have the label 'Main Program'?"
If the file is imported, it has the "My Module" label, so the answer is "No" (False).
If the file is run directly, it has the "Main Program" label, so the answer is "Yes" (True).

---

- `fptr`: Opens an output file.
- `t`: Number of test cases.
- `a`, `b`: Inputs for each test case.
- `fptr.write()`: Writes the result to the output file.
- `fptr.close()`: Closes the file.

---

### **Important Takeaways**

- **Greedy Approach**: Always choose the alphabetically smallest character at each step. It results in the globally smallest final string.
- **Sentinel Character**: Helps in suffix comparison and simplifies logic when strings run out.
- **Suffix Comparison**: Crucial when the current characters are equal. Python's built-in string comparison makes this easy.



So that's it!  
Finally, I just want to say, learning is a continuous journey. If you find any mistakes or know a clearer way to explain something in here, I'd greatly appreciate your feedback.

You can also connect with me on [LinkedIn](https://www.linkedin.com/in/madusha-kolambage-282770333/)
