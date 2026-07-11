def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result
nested_list = [1,[2,3,[4,5]],6]
print(flatten(nested_list))



def common_elements(list1, list2):
    return list(set(list1))
''''
hahashish_'s profile picture
hahashish_
•
Kyu dhone hai itne bartan jab ek me hi kaam ho jayega…
… more
hahashish_ · Original audio
 
hahashish_ · Original audio
 
Likes
74

mycodeshala's profile picture
mycodeshala
•
JavaScript Concepts
------------------------------------------------------------------------------
1. Scope of variables (const, let and var)
2. Function & Variable hoisting
3. Closures
4. Callback Hell
5. Asynchronous vs Synchronous (How to implement both in JS)
6. 'this' variable in Javascript
7. Promises
8. Function.prototype & Inheritance in JavaScript
9. Call, Apply, Bind methods in JavaScript
10. Polyfill for bind()
11. Currying in JavaScript
12. localStorage vs sessionStorage
13. CORS
14. Event Loop
15. ES6 - Arrow function + why do we need them?
16. Cookies & how do they work?
17. Debouncing in JavaScript
18. Throttling in JavaScript
19. Debouncing vs Throttling
20. ES6 modules
21. web workers (& shared workers) and service workers
22. Async/Await
23. How do you add a poly-fill
24. Event bubbling/capturing
25. Event Delegation
26. functional programming with javascript
27. use strict in JavaScript
28. object.freeze in JavaScript
29. LESS
30. SCSS
31. SCSS vs SASS
32. super keyword in JavaScript
33. Lodash library
34. webpack
35. Modern ES6 features (spread operator, destructuring, etc.)
36. GraphQL
37. Testing in JavaScript with JEST
38. different methods of Array object in Javascript
39. Redux in React
40. Context API in React
41. Hooks in React (useState)
42. Component Lifecycle Hooks
43. Creating object clone in JS (Object.assign())
44. Shallow copy vs. Deep copy
45. JWT
46. Reference vs Value in JavaScript
47. Async vs Defer
48. Pop, Push, Shift and Unshift Array Methods in JavaScript
49. String.slice() vs String.substring() vs String.substr()
50. Array slice vs splice in JavaScript

'''