# Matematik Documentation

Table of Contents:

- [Usage](#usage)
- [Reference](#reference)
- [FAQ](#faq)

<br>

# Usage

Firstly install this pacakage using pip:
```
$ pip install matematik
```
After that you can easily get the math formulas with their respective level of difficulty. For example if you want to get the algebra 2 formulas you need to do :
```py
from matematik.formula.algebra2 import *

sum_of_cubes(5, 6)  # <-- returns you the sum of cubes of 5 and 6
```
And this is basiaclly it. At the moment the following modules are included inside the `formula`:
  - arithmetic
  - algebra 1
  - algebra 2
  - geometry

<br>
<br>

# Reference

In this seciton headers are named after sub package names of the package 'matematik'. You can find all of the necessary information and usage of the code in their body content.

<br>

## formulas

At the moment there is only one sub pacakage of the matematik and that is: `formula`. It is a sub package that provides you quick solutions for basic formulas and returns you the answer.

In order to use the contents of this sub-package you can import it with this dot notation:
```python
from matematik.formula.<module_name> import <obj_name>
```

Lets view the modules inside this sub package:

### arithmetic.py

This module provides you various functions to do arithmetic operations on different kind of data structures and objects. Lets see an example:
```py
from matematik.formula.arithmetic import *

# you can do the basic addition with
add(6, 6)  # --> 12

# you can put as many arguments as you want
add_nums(4, 5, 1, ...)

# you can add the elements inside a list
arr_sum([5, 4, 2])

# you can add the elemetns inside a tuple
tup_sum((5, 4, 2))
```

As you can see above the functions that this package provide is not complicated at all. The algorithm inside them is basically just a formula for the given name. All you have to do is to give the necessary parameters.

Here is the list of functions inside the `arithmetic.py` module:

- #### `add(arg1, arg2)`
  This function returns you the sum of arg and arg2.

  Formula: arg1 + arg2

- #### `add_nums(arg1, arg2, ...)`
  This function adds all of the arguments passed to it. There is no limit for passing arguments

  Formula: arg1 + arg2 + ...

- #### `arr_sum([...])`
  Returns you the sum of all elements inside the array. The result is added from left to right. You can use negative numbers.

- #### `tup_sum((...))`
  Returns you the sum of all elements inside the tuple. The result is added from left to right. You can use negative numsbers.

- #### `subtract(arg1, arg2)`
  This function returns you the subtraction of arg1 and arg2

  Formula: arg1 - arg2

- #### `subtract_nums(arg1, arg2, ...)`
  This function returns you the subtraction of the arguments you pass to it. There is no limit to the arguments. Beware that if you pass negative numbers to you arguments the function will make it a addition since `- * - == +`

- #### `arr_subtract([...])`
  This function subtracts all the elements of the given arary. The function starts subtracting the elements from left to right. Beware that if you pass negative numbers to you arguments the function will make it a addition since `- * - == +`

- #### `tup_subtract((...))`
  This function subtracts all the elements of the given tuple. The function starts subtracting the elements from left to right. Beware that if you pass negative numbers to you arguments the function will make it a addition since `- * - == +`

- #### `multiply(arg1, arg2)`
  This function returns you the multiplication of the given parameters arg1 and arg2

  Formula: arg1 * arg2

- #### `multiply_nums(arg1, arg2, ...)`
  This function returns you the multiplication of the arguments you pass to it. There is no limit to the arguments.

- #### `arr_multiply([...])`
  This function returns you the multiplication of all the elements inside the array you pass into it. You can use negative numbers.

- #### `tup_multiply((...))`
  This function returns you the multiplication of all the elements inside the tuple you pass into it. You can use negative numbers.

<br>
<br>

## algebra1.py

This module provides you different kind of algebric equations. Sadly at the moment due to some problem at my end I couldn't use rational numbers so nearly 60% - 70% of the Algebra 1 formulas are not included in this module e.g. Quadratic Equation and such ...

Here is the list of functions inside the `algebra1.py` module:

- #### `slope_intercept(m, x, b)`
  This function returns you the `y` part of the formula called the Slope Intercept

  Formula: y = mx + b

- #### `point_slope(m, x1, x2)`
  This function returns you the value of "y1 - y2" in a equation where we use the Point Slope formula

  Formula: y1 - y2 = m(x1 - x2)

- #### `slope_formula(x1, x2, y1, y2)`
  This function returns you the slope (`m`) based on the given parameters.

  Formula:  m = y2 - y1 / x2 - x1

<br>
<br>

## algebra2.py

In this module you can find not all but most of the necessary algebra 2 formulas for your equations. However, sadly at the time of writing this there is a problem with the functions that contains rational numbers so not all of the formulas of algebra 2 is included in the module.

Here is the list of functions inside the `algebra2.py` module:

- #### `vertex(a, x, h, k)`
  This function returns you the `y`'s value from the formula called vertex

  Formula : y = a (x-h)^2 + k

- #### `standart(x, a, b, c)`
  This function returns you the `y` value of the Standart Formula

  Formula: y = ax^2 + bx +c

- #### `axis_symetry(a, b)`
  Returns you the `x` from the function Axis of Symetry

  Formula: x = -b/2a

- #### `sum_of_cubes(a, b)`
  This function returns you the Sum of Cubes with the given parameters

  Formula: (a+b)^3 = (a+b)(a^2 - ab + b^2)

- #### `different_of_cubes(a, b)`
  This functions returns you the Differnece of Cubes with the given parameters

  Formula: (a-b)^3 = (a-b)(a^2 + ab + b^2)

- #### `cube(x)`
  This function returns you the cube of `x`

  Formula =  x^3

<br>
<br>

## geometry.py

In this module you can find not all but most of the necessary geometry formulas for your equations. However, sadly at the time of writing this there is a problem with the functions that contains rational numbers so not all of the formulas of geometry is included in the module.

- Here is the list of functions inside the `algebra2.py` module:

- #### `area_of_triangle(b, h)`
  This function returns you the area of a triangle with the given `base` and `height`

  Formula: A=1/2bh

- #### `area_of_circle(r)`
  This function returns you the area of a circle with the given `radius`

  Formula: A=πr²

- #### `circumfrence(r)`
  This functionr returns you the circumfrence of a cirlce with the given `radius`

  Formula: C = 2πr

- #### `area_of_rect(l, w)`
  This function returns you the area of a rectangle based on its length and height

  Formula: A= length x width

- #### `trapezoid_midsegment(b1, b2)`
  This function returns you the midsegment of a trapezeoid based on its two bases

  Formula: 1/2 (base 1 + base 2)

- #### `volume_of_rect_prism(l, w, h)`
  This function returns you the volume of a rectangular prism based on its length width and height

  Formula: V = lwh

- #### `volume_of_tri_prism(b, h)`
  This function returns you the volume of a triungular prism based on its base and height value

  Formula: V=(1/2bh)h

- #### `volume_of_cylander(h)`
  This function returns you the volume of a cylinder based on its height

  Formula: V=πr²h

- #### `volume_of_cone(r, h)`
  This function returns you the volume of a cone based on its radius and height

  Formula: 1/3πr²h

- #### `volume_of_rect_pyramid(l, w, h)`
  Returns you the volume of a rectangular pyramid based on its length width and height

  Formula: V=1/3lwh

- #### `volume_of_tri_pyramid(b, h)`
  Returns you the volume of a triangular pyramid based on its base and height

  Formula: V=1/3(1/2bh)h

- #### `volume_of_sphere(r)`
  Returns you the volume of a sphere based on its radius

  Formula: V=4/3πr³

- #### `volume_of_hemisphere(r)`
  Returns you the volume of a hemisphere based on its radius

  Formula: V=2/3πr³




<br>
<br>
<br>

## FAQ
