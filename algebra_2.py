algebra_2_part_1 = {
    "Polynomial arithmetic": [
        {
            "Intro to polynomials": {
            "Definition": "A polynomial is a type of mathematical expression made up of one or more terms. Each term consists of a variable (usually x) raised to a non-negative integer exponent, and multiplied by a coefficient. For example, 3x^2 + 2x - 5 is a polynomial.",
            "QA Queue": [
                    {
                        "Question": "Given the following polynomial, Lisa wants to identify the terms along with the coefficient and exponent of each term: 3x^2 - 8x + 7.",
                        "Answer": "The terms of the polynomial are:\nBEGIN TABLE:\nTerm & Coefficient & Exponent\n3x^2 & 3 & 2\n-8x & -8 & 1\n7 & 7 & 0\nEND TABLE.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Average rate of change of polynomials": {
            "Definition": "To find the average rate of change (ARC) of the function f over an interval, we need to take the total change in the function value over the interval (which is the difference of its values at the endpoints) and divide it by the length of the interval.",
            "QA Queue": [
                    {
                        "Question": "Given f(x) = x^3 - 9x.\nLinda wants to find the average rate of change of f over the interval [1, 6].",
                        "Answer": "The average rate of change of f(x) in the interval [1, 6] is: (f(6) - f(1)) / (6 - 1).\nWe have: f(6) = 6^3 - 9 * 6 = 162, f(1) = 1^3 - 9 * 1 = -8.\nSo the ARC is: (162 - (-8)) / (6 - 1) = 170 / 5 = 34.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Adding and subtracting polynomials": {
            "Definition": "We can add or subtract two polynomials by combining like terms. For example, to add 3x^2 + 2x − 5 and 2x^2 −3x + 1, we combine the x^2 terms, the x terms, and the constant terms:\n(3x^2 + 2x − 5) + (2x^2 − 3x + 1) = 5x^2 − x − 4.",
            "QA Queue": [
                    {
                        "Question": "Lucina has two polynomials: P(b) = -4b^2 + 6b - 9 and Q(b) = 7b^2 - 2b - 5.\nIn order to get a raise from her boss, she has to calculate P(b) + Q(b).\nPlease help her!",
                        "Answer": "We can subtract polynomials by combining like terms: P(b) - Q(b) = (-4b^2 + 6b - 9) - (7b^2 - 2b - 5) = (-4)b^2 + 6b - 9 + (-7)b^2 + 2b + 5 = (-4 -7)b^2 + (6 + 2)b + (-9 + 5) = -11b^2 + 8b - 4.\nSo the answer Lucina wants is -11b^2 + 8b - 4.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Multiplying monomials by polynomials":{
            "Definition": "In order to multiply monomials by polynomials, we need to apply the distributive property.",
            "QA Queue": [
                    {
                        "Question": "Leao is trying to expand m(-m^3 + m^2 + 3m).\nHow can he do it?",
                        "Answer": "Leao can use the distributive property: m(-m^3 + m^2 + 3m) = m * (-m^3) + m * m^2 + m * 3m = -m^4 + m^3 + 3m^2.\nSo the answer is: -m^4 + m^3 + 3m^2.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Multiplying binomials by polynomials":{
            "Definition": "In order to multiply binomials by polynomials, we need to apply the distributive property twice.",
            "QA Queue": [
                    {
                        "Question": "The teacher asks you to expand and simplify the expression: (1 + x)(x^2 - 5x - 6) and promises to give you candies if you answer correctly.\nWhat would your answer be?",
                        "Answer": "Apply the distributive property:\n(1 + x)(x^2 - 5x - 6) = 1(x^2 - 5x - 6) + x(x^2 - 5x - 6).\nApply the distributive property again: 1(x^2 - 5x - 6) + x(x^2 - 5x - 6) = 1(x^2) + 1(-5x) + 1(-6) + x(x^2) + x(-5x) + x(-6) = x^2 - 5x - 6 + x^3 - 5x^2 - 6x = x^3 - 4x^2 - 11x - 6.\nSo my answer would be: x^3 - 4x^2 - 11x - 6.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Special products of polynomials":{
            "Definition": "There are certain polynomial products that occur frequently in mathematics, and it's helpful to recognize them.\nFor example, the square of a binomial is: (a+b)^2 = a^2 + 2ab + b^2.\nAnother common special product is the difference of two squares: (a + b)(a − b) = a^2 − b^2.",
            "QA Queue": [
                    {
                        "Question": "Use a nice trick to expand and simplify the following expression: (7m^6 + 6)(7m^6 - 6).",
                        "Answer": "We could use the difference of two squares formula: (7m^6 + 6)(7m^6 - 6) = (7m^6)^2 - 6^2 = 49m^12 - 36.\nSo the answer is: 49m^12 - 36.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        }
    ],
    "Complex numbers":[
        {
            "The imaginary unit i":{
            "Definition": "The backbone of this new number system is the imaginary unit, or the number i. The following is true of the number i: i = \sqrt(-1) and i^2 = -1.\nThe second property shows us that the number i is indeed a solution to the equation x^2 = -1.\nThe number i is by no means alone! By taking multiples of this imaginary unit, we can create infinitely many more pure imaginary numbers.\nIf the original exponent is not a multiple of 4, then finding the closest multiple of 4 less than it allows us to simplify the power down to i, i^2, or i^3 just by using the fact that i^4 = 1.",
            "QA Queue": [
                    {
                        "Question": "How can Yasuo express the following radical using the imaginary unit, i?\nThe radical is: \plusminus \sqrt(-37).",
                        "Answer": "Yasuo can write the radical as: \plusminus \sqrt(37) i.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Complex numbers introduction":{
            "Definition": "A complex number is any number that can be written as a + bi, where i is the imaginary unit and a and b are real numbers.\na is called the real part of the number, and b is called the imaginary part of the number.",
            "QA Queue": [
                    {
                        "Question": "A curious adventurer found a complex number on his way to the Far Away land: 13.2i + 1.\nWhat is the imaginary part of this number?",
                        "Answer": "The imaginary part of this number is: 13.2.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "The complex plane":{
            "Definition": "The complex plane consists of two number lines that intersect in a right angle at the point (0, 0).\nThe horizontal number line (what we know as the x-axis on a Cartesian plane) is the real axis.\nThe vertical number line (the y-axis on a Cartesian plane) is the imaginary axis.",
            "QA Queue": [
                    {
                        "Question": "Help Linda to plot -1+i in the complex plane.",
                        "Answer": "The real part of -1+i is -1 and the imaginary part of -1+i is 1.\nSo its coordinate on the complex plane would be: (-1, 1).",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Adding and subtracting complex numbers":{
            "Definition": "To add or subtract two complex numbers, we combine their real parts and their imaginary parts separately. For example, (2+3i) + (4−2i) = 6+i.",
            "QA Queue": [
                    {
                        "Question": "After adding two complex items, -30i and 52-30i, you will get a legendary complex item! What would the legendary item be?",
                        "Answer": "Adding two complex numbers: -30i + (52 - 30i) = 52 + (-30 + (-30))i = 52 - 60i.\nSo the legendary complex item is: 52 - 60i.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Multiplying complex numbers":{
            "Definition": "To multiply two complex numbers, we use the distributive property to multiply all the terms together.",
            "QA Queue": [
                    {
                        "Question": "Lara has a complex number -1-3i and Lawrence has another complex number -1+i.\nThey want to find out what is the product of these two complex numbers.",
                        "Answer": "Multiplying the two complex numbers by the distributive property, we have: (-1-3i)(-1+i) = 1 - i + 3i - 3i^2 = 1 - i + 3i - 3 * (-1) = 1 + 2i + 3 = 4 + 2i.\nSo the product of Lara's number and Lawrence's number is 4 + 2i.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Quadratic equations with complex solutions":{
            "Definition": "Some quadratic equations don't have any 'real' solutions, but they do have complex solutions. For example, x^2 + 1 = 0 doesn't have any real solutions, but it does have the two complex solutions x = \plusminus i.",
            "QA Queue": [
                    {
                        "Question": "Find the solutions of the quadratic equation x^2 + x + 1 = 0.",
                        "Answer": "If we have a quadratic equation ax^2 + bx + c = 0, the quadratic formula gives the solutions:\nx = (-b \plusminus \sqrt(b^2 - 4ac)) / 2a.\nIn this problem, a = 1, b = 1 and c = 1. Let’s substitute those values into the quadratic formula to find the solutions.\nFirst, we find out that b^2 - 4ac = 1^2 - 4 * 1 * 1 = -3. Since the discriminant is negative, we will have two complex solutions: x = (-1 \plusminus \sqrt(-3)) / (2 * 1) = -1/2 \plusminus (\sqrt(3) / 2) * i.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
    ],
    "Polynomial factorization": [
        {
            "Factoring monomials":{
            "Definition": "To factor a monomial means to express it as a product of two or more monomials. To factor a monomial completely, we write the coefficient as a product of primes and expand the variable part.",
            "QA Queue": [
                    {
                        "Question": "Ibuki factored 12x^7 as (4x^3)(3x^4).\nMelodie factored 12x^7 as (2x^6)(6x).\nWhich of them factored 12x^7 correctly?",
                        "Answer": "Both Ibuki and Melodie factored 12x^7 correctly, since 4x^3 * 3x^4 = 2x^6 * 6x = 12x^7.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Greateset common factor":{
            "Definition": "The greatest common factor of two numbers is the greatest integer that is a factor of both numbers. The process is similar when you are asked to find the greatest common factor of two or more monomials. Simply write the complete factorization of each monomial and find the common factors. The product of all the common factors will be the GCF.",
            "QA Queue": [
                    {
                        "Question": "Adam, Eve and Luka each has a polynomial: Adam has 44c^5, Eve has 22c^3 and Luka has 11c^4.\nWhat is the greatest common factor of these three polynomials?",
                        "Answer": "Factorizing Adam's polynomial completely, we have: 44c^5 = 2 * 2 * 11 * c * c * c * c * c.\nFactorizing Eve's polynomial completely, we have: 22c^3 = 2 * 11 * c * c * c.\nFactorizing Luka's polynomial completely, we have: 11c^4 = 11 * c * c * c * c.\nHence, we obtain the GCF: 11c^3.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Taking common factors":{
            "Definition": "To factor the GCF out of a polynomial, we do the following:\n1. Find the GCF of all the terms in the polynomial.\n2. Express each term as a product of the GCF and another factor.\n3. Use the distributive property to factor out the GCF.",
            "QA Queue": [
                    {
                        "Question": "A rectangle has an area of 12x^4 + 6x^3 + 15x^2 square meters.\nThe length of the rectangle (in meters) is equal to the greatest common monomial factor of 12x^4, 6x^3, and 15x^2.\nWhat is the width of the rectangle?",
                        "Answer": "Factorizing completely: 12x^4 = 2 * 2 * 3 * x * x * x * x, 6x^3 = 2 * 3 * x * x * x, 15x^2 = 3 * 5 * x * x.\nSo the greatest common monomial factor of 12x^4, 6x^3 and 15x^2 = 3x^2.\nHence, we can factorize the area into: 3x^2 (4x^2 + 2x + 5).\nSo the width of the rectangle is 4x^2 + 2x + 5.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Factoring higher degree polynomials":{
            "Definition": "Factoring is the process of breaking down a polynomial into smaller pieces (or 'factors') that, when multiplied together, will give you the original polynomial.",
            "QA Queue": [
                    {
                        "Question": "Factor completely the following expression: (x^2 - 4)(x^2 + 6x + 9).",
                        "Answer": "To factor (x^2 - 4), we use the 'difference of square' pattern: x^2 - 4 = x^2 - 2^2 = (x-2)(x+2).\nTo factor (x^2 + 6x + 9), we use the 'perfect square' pattern: x^2 + 6x + 9 = x^2 + 2 * 3 * x + 3^2 = (x+3)^2.\nIn conclusion, the complete factorization is: (x-2)(x+2)(x+3)^2.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Factoring using structure":{
            "Definition": "Polynomial identities are equations that are true for all values of the variable. For example, the difference of squares identity, a^2 - b^2 = (a-b)(a+b), is true for any values of a and b.",
            "QA Queue": [
                    {
                        "Question": "We want to factor the following expression: (x-5)^2 + 2y^3 (x-5) + y^6.\nWe can factor the expression as (U + V)^2 where U and V are either constant integers or single-variable expressions.\nWhat are U and V?",
                        "Answer": "By using the 'perfect square' identity, we obtain: (x-5)^2 + 2y^3 (x-5) + y^6 = (x-5 + y^3)^2.\nSo our answer for U and V could be: U = x-5 and V = y^3.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Polynomial identities":{
            "Definition": "Polynomial identities are equations that are true for all values of the variable. For example, the difference of squares identity, a^2 - b^2 = (a-b)(a+b), is true for any values of a and b.",
            "QA Queue": [
                    {
                        "Question": "Mario has the following formula: (x - 2y)^2 = x^2 - 4xy + 4y^2.\nLuigi has the following formula: (m + 1)^2 - m^2 = 1.\nBetween Mario and Luigi, whose formula is a true identity?",
                        "Answer": "In Mario's formula, the right hand side can be factorized using the 'perfect square' identity: x^2 - 4xy + 4y^2 = x^2 - 2 * x * 2y + (2y)^2 = (x-2y)^2.\nLuigi's formula is not true for m = 2: (2 + 1)^2 - 2^2 = 9 - 4 = 5 > 1.\nSo only Mario has a formula which is a true identity.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Geometric series":{
            "Definition": "In geometric series where: a is the first term, r is the common ratio, n is the number of terms, S_n is the sum of the first n terms, the formula for S_n is:\nS_n = a + ar + ... + ar^(n-1) = a(1 - r^n) / (1-r).",
            "QA Queue": [
                    {
                        "Question": "A new shopping mall records 120 total shoppers on their first day of business. Each day after that, the number of shoppers is 10% more than the number of shoppers the day before.\nWhat is the total number of shoppers that visited the mall in the first 7 days? Round your final answer to the nearest integer.",
                        "Answer": "Notice that the daily counts of shoppers form a geometric sequence.\nThe first term is a = 120, the common ratio is the ratio between the number of shoppers in a day compared to the day before, which is: r = 1 + 0.1 = 1.1.\nThe number of terms is 7 (the number of days).\nSo the total number of shoppers that visited the mall in the first 7 days is: S_7 = a + ar + ... + ar^6 = a(1 - r^7) / (1 - r) = 120 * (1 - 1.1^7) / (1 - 1.1) \approx 1138.\nSo there are approximately 1138 shoppers that visited the mall in the first 7 days.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        }
    ]
}

algebra_2_part_2 = {
    "Polynomial division": [
        {
            "Dividing polynomials by x":{
            "Definition": "We divide polynomials for the same reason we divide numbers: to solve problems. By breaking a polynomial down into smaller, more manageable pieces, we can solve problems more easily.",
            "QA Queue": [
                    {
                        "Question": "Divide the polynomials: (5x^4 + 9) / x.\nYour answer should be in the form p(x) + k/x where p is a polynomial and k is an integer.",
                        "Answer": "Here, we will use the method of splitting the quotient into multiple quotients: (5x^4 + 9) / x = 5x^4 / x + 9 / x.\nNow let's try to cancel common factors in the resulting terms.\nWe have: 5x^4 / x = 5x^3 and 9 / x doesn't have common factors so it has to stay as it is.\nIn conclusion, this is the result of dividing the polynomials: 5x^3 + 9/x.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Dividing quadratics by linear factors":{
            "Definition": "Quadratics are a very common type of polynomial, so they come up often in problems. Knowing how to divide them by linear factors (like x or x−2) can help us factor them completely.",
            "QA Queue": [
                    {
                        "Question": "Lissandro needs your help to divide the polynomials: (x^2 - 3x + 9) / (x - 2).\nYour answer should be in the form p(x) + k / (x-2) where p is a polynomial and k is an integer.",
                        "Answer": "We can use the method of polynomial long division to obtain: the quotient is x-1 and the remainder is 7.\nTherefore: (x^2 - 3x + 9) / (x - 2) = x - 1 + 7 / (x-2).",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Dividing polynomials by linear factors":{
            "Definition": "We divide polynomials for the same reason we divide numbers: to solve problems. By breaking a polynomial down into smaller, more manageable pieces, we can solve problems more easily.",
            "QA Queue": [
                    {
                        "Question": "The polynomial p(x) = 3x^3 - 20x^2 + 37x - 20 has a known factor of (x-4).\nPlease rewrite p(x) as a product of linear factors.",
                        "Answer": "First, we can factorise x-4 out of the polynomial: p(x) = 3x^3 - 12x^2 - 8x^2 + 32x + 5x - 20 = 3x^2(x-4) - 8x(x-4) + 5(x-4) = (3x^2 - 8x + 5)(x-4).\nWe can further factorise 3x^2 - 8x + 5 as follow: 3x^2 - 8x + 5 = 3x^2 - 3x - 5x + 5 = 3x(x-1) - 5(x-1) = (3x-5)(x-1).\nIn conclusion, the complete factorisation of p(x) is: p(x) = (3x-5)(x-1)(x-4).",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Polynomial Remainder Theorem":{
            "Definition": "For a polynomial p(x) and a number a, the remainder on division by x−a is p(a).",
            "QA Queue": [
                    {
                        "Question": "Cleo has a mysterious polynomial P(x)! However, she does not know how it looks like, she only has a manual of it, which says: 'P(x) divided by (x−8) has a remainder of 5.\nP(x) divided by (x−5) has a remainder of 3.\nP(x) divided by (x+5) has a remainder of −2.\nP(x) divided by (x+8) has a remainder of 0.'\nCleo wants to find the value of P(5) and P(-8).\nWhat are the values that Cleo is looking for?",
                        "Answer": "According to the Polynomial Remainder Theorem, P(5) is equal to the remainder when P(x) is divided by (x−5), and we are given that this remainder is equal to 3, so P(5) = 3.\nSimilarly, P(−8) is equal to the remainder when P(x) is divided by (x − (−8)), which can be rewritten as (x+8), and we are given that this remainder is equal to 0, so P(-8) = 0.\nIn conclusion, Cleo could know that P(5) = 3 and P(-8) = 0.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        },
    ],
    "Polynomial graphs": [
        {
            "Zeros of polynomials":{
            "Definition": "The zeros of a polynomial are the x-values where the polynomial crosses the x-axis. In other words, they're the points where the polynomial equals 0.",
            "QA Queue": [
                    {
                        "Question": "We want to find the zeros of this polynomial: p(x)=(x^2 − 9)(x^2 + x − 2).\nPlot all the zeros (x-intercepts) of the polynomial in a graph.",
                        "Answer": "First, we factorise the polynomial.\nTo factorise x^2 - 9, we use the 'difference of squares' pattern: x^2 - 9 = (x-3)(x+3).\nWe can also further factorise x^2 + x - 2 into (x-1)(x+2).\nSo p(x) is completely factorised into (x-3)(x+3)(x-1)(x+2).\nThe zeros of all the linear factors are the zeros of p(x), which are: x = 3, x = -3, x = 1, x = -2.\nNow we can plot them on a graph.\nBEGIN PLOT:\nDraw(Point X_1, (3, 0))\nDraw(Point X_2, (-3, 0))\nDraw(Point X_3, (1, 0))\nDraw(Point X_4, (-2, 0))\nEND PLOT.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Positive and negative intervals of polynomials":{
            "Definition": "Polynomials can be positive or negative in certain intervals. For example, a polynomial might be positive for all x-values less than −2, negative between −2 and 3, and positive again for all x-values greater than 3.\nThe sign of a polynomial between any two consecutive zeros is either always positive or always negative.",
            "QA Queue": [
                    {
                        "Question": "f(x) = (2x - 1)(3x - 5)(x - 7)(3x + 6) has zeros at x = -2, x = 1/2, x = 5/3, and x = 7.\nWhat is the sign of f on the interval 1/2 < x < 5/3.",
                        "Answer": "Since the sign of a polynomial between any two consecutive zeros is either always positive or always negative, we can just pick a value between 1/2 and 5/3, for example x = 1, then calculate f(1) to determine the sign of f(x) on the interval 1/2 < x < 5/3.\nWe have: f(1) = (2 * 1 - 1) * (3 * 1 - 5) * (1 - 7) * (3 * 1 + 6) = 1 * (-2) * (-6) * 9 = 108 > 0.\nSo f(x) is always positive on the interval 1/2 < x < 5/3.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "End behaviour of polynomials":{
            "Definition": "The end behavior of a function f describes the behavior of the graph of the function at the 'ends' of the x-axis.",
            "QA Queue": [
                    {
                        "Question": "Consider the polynomial function g(x) = -10x^7 - 9x^5 + 7x^3 - 8x.\nWhat is the end behavior of the graph of g?",
                        "Answer": "As the input variable gets positively or negatively larger, the lower-degree terms become insignificant in comparison to the term with the highest degree, which is called the leading term.\nTherefore, in order to determine the end behavior of a polynomial, we consider its leading term. In particular, whether its degree is odd or even, and whether its sign is positive or negative.\nIn the case of g, the leading term is -10x^7, which has an odd degree and a negative coefficient, which means that -10x^7 goes to -\infinity if x approaches +\infinity, and goes to +\infinity when x approaches -\infinity.\nTherefore, the end behaviour of the graph of g is: As x \to \infinity, g(x) \to -\infinity, and as x \to -\infinity, g(x) \to \infinity.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        },
    ],
    "Rational exponents and radicals": [
        {
            "Rational exponents":{
            "Definition": "Rational exponents are just like regular exponents, except the exponent is a fraction instead of a whole number. For example, 2^(3/4) has a rational exponent, while 2^3 has a whole number exponent.",
            "QA Queue": [
                    {
                        "Question": "Which rational exponent is equivalent to (\sqrt{4}{d})^3?",
                        "Answer": "We see that: \sqrt{4}{d} is equivalent to d^(1/4).\nSo (\sqrt{4}{d})^3 is equivalent to d^(3/4).",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Properties of exponents (rational exponents)":{
            "Definition": "Here are some properties of rational exponents—notice how they are similar the properties of integer exponents:\n b^(m/n) = \sqrt{n}{b^m}.\n b^(m/n) * b^(p/n) = b^((m+p)/n).\n (b^(m/n))^(p/q) = b^(mp/nq).",
            "QA Queue": [
                    {
                        "Question": "Rewrite the expression in the form k * z^n. Write the exponent as an integer, fraction, or an exact decimal (not a mixed number).\nThe expression is: (10\sqrt{3}{z}) / 2z^2.",
                        "Answer": "First, we rewrite all terms of the expression into rational exponents: (10z^(1/3)) / 2z^2.\nThen we separately evaluate the constant: 10 / 2 = 5, and the exponent of variable: z^(1/3) / z^2 = z^(1/3 - 2) = z^(-5/3).\nIn conclusion, the final expression is: 5 * z^(-5/3).",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Evaluating exponents & radicals":{
            "Definition": "To evaluate an exponential expression, you can either use the properties of exponents to simplify it, or use a calculator. For radicals, you can find the square root, cube root, or n-th root of a number using a calculator or by breaking the number down into its factors.",
            "QA Queue": [
                    {
                        "Question": "Given an expression: \sqrt{5}{-t^4} * \sqrt{5}{t}.\nQuavo has the value t = 2 and wants to evaluate the expression but does not know how to do it. Please help Quavo.",
                        "Answer": "We need to evaluate: \sqrt{5}{-2^4} * \sqrt{5}{2}, which is equal to: \sqrt{5}{-16} * \sqrt{5}{2} = \sqrt{5}{-16 * 2} = \sqrt{5}{-32} = -2.\nSo the answer that Quavo needs is -2.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Equivalent forms of exponential expressions":{
            "Definition": "There are a few different ways you can write an exponential expression, and sometimes we might need to convert between them. Here are three equivalent forms for the same expression: 2^(3/4)\n \sqrt{4}{2^3}\n \sqrt{4}{8}.",
            "QA Queue": [
                    {
                        "Question": "What is the value of A when we rewrite (5/6)^x as A^(-8x)?",
                        "Answer": "We need to find A such that A^(-8) = 5/6, or equivalently: 1/(A^8) = 5/6, or equivalently: A^8 = 6/5, which means: A = (6/5)^(1/8).\nSo the value of A is (6/5)^(1/8).",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Solving exponential equations using properties of exponents":{
            "Definition": "To solve exponential equations, we can often use properties of exponents to simplify them. For example, to solve 2^x = 8, we can rewrite 8 as 2^3, which lets us set x = 3.",
            "QA Queue": [
                    {
                        "Question": "Solve the exponential equation for x: 32^(x/3) = 8^(x-12).",
                        "Answer": "Since 32 = 2^5 and 8 = 2^3, we can rewrite the equation as follow: 2^(5 * x/3) = 2^(3 * (x-12)).\nNow, we only need to solve the following equation: 5 * x/3 = 3 * (x-12), which is equivalent to: 5x = 9x - 108.\nThus, we have: x = 108 / 4 = 27.\nSo the answer is x = 27.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        },
    ]
}

algebra_2_part_3 = {
    "Exponential models": [
        {
            "Interpreting the rate of change of exponential models":{
            "Definition": "In mathematics, the rate of change tells us how quickly a quantity is changing over time. For an exponential model, the rate of change gives us information about how quickly the quantity grows (or decays) over time.",
            "QA Queue": [
                    {
                        "Question": "Nina uploaded a funny video on her website, which rapidly gains views over time. The relationship between the elapsed time, t, in days, since Nina uploaded the video, and the total number of views, V(t), is modeled by the following function: V(t) = 500 * (1.8)^t.\nWrite a sentence that describes the daily percent change in the views of the video.",
                        "Answer": "Everyday, 80% of views are added to the total number of views of the video.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Constructing exponential models according to rate of change":{
            "Definition": "An exponential model is a type of function that shows how a quantity grows exponentially over time. We often use exponential models to represent things like population growth, radioactive decay, and compound interest.",
            "QA Queue": [
                    {
                        "Question": "Carbon-14 is an element which loses 1/10 of its mass every 871 years. The mass of a sample of carbon-14 can be modeled by a function, M, which depends on its age, t (in years).\nWe measure that the initial mass of a sample of carbon-14 is 960 grams.\nWrite a function that models the mass of the carbon-14 sample remaining t years since the initial measurement.",
                        "Answer": "The initial mass of the sample of carbon-14 is 960 grams.\nEach 871 years, carbon-14 loses 1/10 of its mass (or multiplies its mass by 9/10), so each year, carbon-14 multiplies its mass by (9/10)^(1/871).\nAfter t years, carbon-14 multiplies its mass by: (9/10)^(t/871).\nSo M(t) = 960 * (9/10)^(1/871).",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Advanced interpretation of exponential models":{
            "Definition": "'Advanced interpretation' refers to being able to take an exponential model and understand what the different parts of it mean. For example, we should be able to figure out what the initial value is, how quickly the quantity is growing, and what the trend will be over time.",
            "QA Queue": [
                    {
                        "Question": "Dominic sent a chain letter to his friends, asking them to forward the letter to more friends.\nThe relationship between the elapsed time t, in hours, since Dominic sent the letter, and the number of people, P_hour(t), who receive the email is modeled by the following function: P_hour(t) = 18 * (1.05)^t.\nWrite a sentence that describes the daily rate of change in the number of people who receive the email.",
                        "Answer": "Every hour, the number of people who receive the email grows by a factor of 1.05.\nSo every 24 hours, the number of people who receive the email grows by a factor of (1.05)^24.\nThus, every day, the number of people who receive the email grows by a factor of (1.05)^24 \approx 3.23.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        }
    ],
    "Logarithms": [
        {
            "Introduction to logarithms":{
            "Definition": "Logarithms are the inverse operation of exponentiation. We can use logarithms to find the exponent to which a given base must be raised in order to produce a particular result.\nThe constant e is a very important number in mathematics. It is an irrational number, which means it cannot be written exactly as a fraction or a decimal, but we often approximate it as e \approx 2.71828. It is the base of the natural logarithm ln.\nAs n gets larger and larger, the sequence (1 + 1/n)^n gets closer and closer to e.",
            "QA Queue": [
                    {
                        "Question": "Nami want to evaluate log_(25) (1/5), so she asks for your help!",
                        "Answer": "If log_(25) (1/5) = x, then 25^x = 1/5.\nNotice that the square root of 25 is 5, and 5^(-1) = 1/5.\nSo (\sqrt(25))^(-1) is equal to 1/5.\nRewriting (\sqrt(25))^(-1), we obtain 25^(-1/2).\nSo 25^x = 25^(-1/2).\nIn conclusion, x = -1/2, so log_(25) (1/5) = -1/2.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Properties of logarithms":{
            "Definition": "The product rule: log_b(MN) = log_b(M) + log_b(N).\nThe quotient rule: log_b(M/N) = log_b(M) - log_b(N).\nThe power rule: log_b(M^p) = p log_b(M).",
            "QA Queue": [
                    {
                        "Question": "Incineroar challenges Pikachu to rewrite the following in the form log(c): 2log(5). Pikachu asks for help from you!",
                        "Answer": "By using the power rule, Pikachu can rewrite the expression as: log(5^2) = log(25).",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "The change of base formula for logarithms":{
            "Definition": "Change of base rule: log_b(M) = log_a(M) / log_a(b) for any a.",
            "QA Queue": [
                    {
                        "Question": "Which expression is equivalent to log_4(m) * log_m(20) and take the form log_a(b)?",
                        "Answer": "By the change of base rule, we have: log_4(20) / log_4(m) = log_m(20).\nHence, the expression equivalent to log_4(m) * log_m(20) is log_4(20).",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Solving exponential equations with logarithms":{
            "Definition": "Solving exponential equations of the form a * b^x = d: To solve for x, we must first isolate the exponential part by dividing both hand sides by a. Then we can solve for x by converting the equation to logarithmic form.\nSolving exponential equations of the form a * b^(cx) = d: We can solve for cx first, then solve for x by dividing the answer by c.",
            "QA Queue": [
                    {
                        "Question": "Jordan is really curious when he saw the equation (2^x - 3)(2^x - 4) = 0.\nWe is excited to see the solution of this equation! Please help him.",
                        "Answer": "Since (2^x - 3)(2^x - 4) = 0, we know that 2^x - 3 = 0 or 2^x - 4 = 0.\nWe can now solve each case individually.\nWhen 2^x - 3 = 0, or 2^x = 3, we get x = log_2(3).\nWhen 2^x - 4 = 0, or 2^x = 4, we get x = log_2(4) = 2.\nIn conclusion, there are two solutions for this equation, x = log_2(3) and x = 2.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Solving exponential models":{
            "Definition": "Logarithms and radicals are used in lots of different ways in the real world. They are important in fields like finance, engineering, and science. For example, the Richter scale, which measures the magnitude of earthquakes, uses a logarithmic scale. This means that a magnitude 6 earthquake is actually ten times stronger than a magnitude 5 earthquake!",
            "QA Queue": [
                    {
                        "Question": "Harper uploaded a funny video of her dog onto a website.\nThe relationship between the elapsed time, d, in days, since the video was first uploaded, and the total number of views, V(d), that the video received is modeled by the following function.\nV(d) = 4^(1.25d).\nHow many views will the video receive after 6 days? Round your answer, if necessary, to the nearest hundredth.",
                        "Answer": "The number of views that the video will receive after 6 days is: V(6) = 4^(1.25*6) = 4^(7.5) = 4^(15/2) = 2^15 = 32768.\nSo in total, there will be 32768 views.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        }
    ],
    "Transformations of functions": [
        {
            "Shifting functions":{
            "Definition": "When we shift a function horizontally, we are moving the entire graph of the function left or right. This is done by adding or subtracting a constant from the function's input. For example, to shift the function f(x) = x^2 three units to the left, we would write f(x+3) = (x+3)^2. \nVertical shifting is similar to horizontal shifting, except we are moving the entire graph of the function up or down. This is done by adding or subtracting a constant from the function's output. For example, to shift the function f(x) = x^2 four units up, we would write f(x) = x^2 + 4.",
            "QA Queue": [
                    {
                        "Question": "Explain the series of transformations needed to obtain the graph of the function g(x) = (x+7)^3 - 9 from the graph of the function f(x) = x^3.",
                        "Answer": "First, we move the graph 9 units down, it will become the graph of h(x) = x^3 - 9.\nNext, we move the new graph 7 units to the left, we will obtain the graph of g(x) = (x+7)^3 - 9.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Reflecting functions":{
            "Definition": "When we reflect a function, we're flipping it over a specific line. For example, if we reflect a function over the y-axis, we're flipping it from left to right. If we reflect a function over the x-axis, we're flipping it from top to bottom.",
            "QA Queue": [
                    {
                        "Question": "The function f is defined as f(x) = 1/4 (x+2)^3 - 2.\nThe graph of the function g(x) is the reflection of the graph of f(x) through the x-axis.\nWhat is the formula for g(x)?",
                        "Answer": "When we reflect f(x) through the x-axis, the graph of it becomes the graph of -f(x).\nSo g(x) = - 1/4 (x+2)^3 + 2.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Symmetry of functions":{
            "Definition": "A function is an even function if its graph is symmetric with respect to the y-axis.\nA function is an odd function if its graph is symmetric with respect to the origin.\nA monomial is a one-termed polynomial.",
            "QA Queue": [
                    {
                        "Question": "Is the following function even, odd, or neither?\nf(x) = 3 / (x^2 + 2).",
                        "Answer": "By calculating f(-x): f(-x) = 3 / ((-x)^2 + 2) = 3 / (x^2 + 3) = f(x), we conclude that the function f(x) is an even function.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Scaling functions":{
            "Definition": "When we scale a function, we're changing its size on the graph. For example, if we multiply a function by 2, we're making it twice as tall. If we multiply a function by 1/2, we're making it half as tall.",
            "QA Queue": [
                    {
                        "Question": "The graph of function f(x) is described as below:\nBEGIN PLOT:\nDraw(Point A, (2, 2))\nDraw(Point B, (-1, 0))\nDraw(Point C, (5, -2))\nDraw(Point D, (6, 1))\nDraw(A ray starts from A, goes through B, label it Part 1)\nDraw(A segment that connects A and C, label it Part 2)\nDraw(A ray starts from C, goes through D, label it Part 3)\nEND PLOT.\nThe graph of function f(x) is comprised of 3 parts drawn in the graph.\nYour task is to draw the graph of the function g(x) = 2f(x).",
                        "Answer": "To draw the graph of the function g(x) = 2f(x), we need to scale the y-coordinates of the points on the graph of f(x) by a factor of 2.\nBEGIN PLOT:\nDraw(Point A', (2, 4))\nDraw(Point B', (-1, 0))\nDraw(Point C', (5, -4))\nDraw(Point D', (6, 2))\nDraw(A ray starts from A', goes through B', label it Part 1)\nDraw(A segment that connects A' and C', label it Part 2)\nDraw(A ray starts from C', goes through D', label it Part 3)\nEND PLOT.\nThe graph of function g(x) is comprised of 3 parts drawn in the graph.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
    ]
}

algebra_2_part_4 = {
    "Equations": [
        {
            "Rational equations":{
            "Definition": "Rational equations are equations that contain one or more fractions. To solve them, we usually try to get rid of the fractions, and then solve the equation with other strategies we know.",
            "QA Queue": [
                    {
                        "Question": "Find all solutions to the equation:\n (x^2 + 20) / (x(x-2)) = (14-x) / (x-2).",
                        "Answer": "Multiply both sides by x(x-2), we get: x^2 + 20 = x(14-x), which is equivalent to: 2x^2 - 14x + 20.\nDivide both hand sides by 2, we obtain: x^2 - 7x + 10 = 0, which we can factorise into: (x-2)(x-5) = 0.\nSo the equation has 2 candidate solutions: x = 2 and x = 5.\nHowever, the solution x = 2 makes the formula undefined, so x = 5 is the only solution.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Square-root equations":{
            "Definition": "Square-root equations are equations that contain square roots. To solve them, we usually isolate the square root on one side of the equation, and square both sides in order to get rid of the square root.",
            "QA Queue": [
                    {
                        "Question": "Solve the following square-root equation:5w - \sqrt(27w + 7) = 3w - 1.",
                        "Answer": "Subtract 5w from both sides: -\sqrt(27w + 7) = -2w - 1.\nSquaring both sides: 27w + 7 = 4w^2 + 4w + 1, which is equivalent to: 4w^2 - 23w - 6 = 0.\nFactorising: (w - 6)(4w + 1) = 0.\nSo the candidate solutions are w = -1/4 and w = 6.\nBoth w = 6 and w = -1/4 make 27w + 7 >= 0, so w = 6 and w = -1/4 are the solutions of the equation.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Extraneous solutions":{
            "Definition": "Sometimes when we solve an equation, we'll find a solution that makes one side of the equation equal to the other, but doesn't actually work when we plug it back into the original equation. This is called an extraneous solution. It's really important to always check our solutions by substituting them back into the original equation, to make sure they're not extraneous.",
            "QA Queue": [
                    {
                        "Question": "Rania solves the equation below by first squaring both sides of the equation: -5 = \sqrt(3x - 7).\nWhat extraneous solution does Rania obtain?",
                        "Answer": "Squaring both hand sides: 25 = 3x - 7, which is equivalent to: 3x = 32, so x = 32 / 3.\nHowever, if we substitute x = 32/3, we get: \sqrt(3x - 7) = 5 \neq -5.\nSo x = 32/3 is not a solution, it is an extraneous solution.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Cube-root equations":{
            "Definition": "Cube-root equations are equations that contain cube roots. To solve them, we usually isolate the cube root on one side of the equation, and cube both sides in order to get rid of the cube root.",
            "QA Queue": [
                    {
                        "Question": "Solve for y: -\sqrt{3}{y} = 4 \sqrt{3}{y} + 5.",
                        "Answer": "First, we isolate the cube-root to a hand side: -5\sqrt{3}{y} = 5.\nNext, we divide both hand sides by 5 and take the cube of both sides to get: -y = 1.\nSo the solution for the equation is y = -1.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Quadratic systems":{
            "Definition": "Quadratic systems are systems of equations where at least one of the equations is a quadratic equation. To solve them, we often use substitution or elimination, just like with linear systems, but sometimes we have to use more advanced techniques like graphing or completing the square.",
            "QA Queue": [
                    {
                        "Question": "We want to solve the following system of equations.\nx^2 + y^2 = 1,\ny = 2x + 2.\nOne of the solutions to this system is (-1, 0).\nFind the other solution. Your answer must be exact.",
                        "Answer": "Substituting y = 2x + 2 into the first equation, we get: x^2 + (2x + 2)^2 = 1, which is equivalent to: x^2 + 4x^2 + 8x + 4 = 1, so: 5x^2 + 8x + 3 = 0.\nFactorising, we get: (5x + 3)(x + 1) = 0.\nTwo solutions of the above function are x = -3/5 and x = -1.\nThe corresponding solutions for the system would be: (-3/5, 4/5) and (-1, 0).\nSo the solution other than (-1, 0) is (-3/5, 4/5).",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Solving equations by graphing":{
            "Definition": "",
            "QA Queue": [
                    {
                        "Question": "An entomologist can model the number of mosquitos in a forest as a function of rainfall. In a similar way, they can also model the number of bats in the forest.\nThe function f(x) = 5x − x^2 gives the number of mosquitos in the forest (in millions), and the function g(x)=3x−0.5x^2 gives the number of bats (in millions). In both equations x represents rainfall (in centimeters). When there is 0cm of rainfall, the number of mosquitos is the same as the number of bats.\nWhat is another rainfall amount where the number of mosquitos is the same as the number of bats? Round your answer to the nearest half centimeter.",
                        "Answer": "We need to solve the equation: f(x) = g(x). By graphing both f(x) and g(x), we see that they intersect at (0, 0) and at (4, 4).\nSo the solutions of the equation are x = 0 and x = 4.\nSo the other rainfall amount where the number of mosquitos is the same as the number of bats is 4 centimeters.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        },
    ],
    "Trigonometry": [
        {
            "Unit circle introduction": {
                  "Definition": "The unit circle definition allows us to extend the domain of sine and cosine to all real numbers. The process for determining the sine/cosine of any angle θ is as follows:\
                  1) Starting from (1,0), move along the unit circle in the counterclockwise direction until the angle that is formed between your position, the origin, and the positive x-axis is equal to θ \
                  2) sin(θ) is equal to the y-coordinate of your point, and cos(θ) is equal to the x-coordinate.",
                  "QA Queue": [
                          {
                              "Question": "A unit circle on an x y coordinate plane where the center of the unit circle is at the \
                              origin and the circumference of the circle touches (one, zero), (zero, one), (negative one, zero), and \
                              (zero, negative one). Point A is located at near one thirty o'clock on the circle. \
                              Point B is located near eleven o'clock on the circle. Point C is located near\
                               three thirty o'clock on the circle.W hich of the coordinates is equal to cos(50)?",
                              "Answer": "x-coordinate of A",
                              "Type": "Narrative",
                              "Difficulty": 4
                          }
                      ],
                  "Rate": 1,
                  }
        },
        {
            "The Pythagorean identity": {
                  "Definition": "sin^2(θ)+cos^2(θ)=1",
                  "QA Queue": [
                          {
                              "Question": "The angle θ is located in Quadrant IV and sin(θ) = -10/13. What is the value of cos(θ)",
                              "Answer": "sqrt(1-(-10/13)^2)=sqrt(69)/13",
                              "Type": "Narrative",
                              "Difficulty": 4
                          }
                      ],
                  "Rate": 1,
                  }
        },
        {
            "Amplitude, midline and period": {
                  "Definition": "Midline, amplitude, and period are three features of sinusoidal graphs. Midline is the horizontal line that passes exactly in the middle between the graph's maximum and minimum points.\
                  Amplitude is the vertical distance between the midline and one of the extremum points. \
                  Period is the distance between two consecutive maximum points, or two consecutive minimum points (these distances must be equal).",
                  "QA Queue": [
                          {
                              "Question": "A graph of a trigonometric wave on an x y coordinate plane. The x and y axes scale by one. There is a point on the highest part of the graph labeled (negative pi, six and eight tenths). There is a point on the lowest part of the graph labeled (pi, one and two tenths).",
                              "Answer": "amplitude=max value−midline value=2.8",
                              "Type": "Narrative",
                              "Difficulty": 4
                          }
                      ],
                  "Rate": 1,
                  }
        },
        {
            "Transforming sinusoidal graphs": {
                  "Definition": "Amplitude in sinusoids of the form y=asin(bx+c)+d where the amplitude of a sinusoid of the form is equal to |a|",
                  "QA Queue": [
                          {
                              "Question": "What is the amplitude of y=5sin(4x−2)−3",
                              "Answer": "The amplitude of y = 5sin(4x-2)-3 is 5 times the amplitude of y = sin(4x-2) - 3.\nSo the amplitude of y = 5sin(4x-2) - 3 is 5.",
                              "Type": "Narrative",
                              "Difficulty": 4
                          }
                      ],
                  "Rate": 1,
                  }
        },
        {
            "Sinusoidal models": {
                  "Definition": "By understanding how to transform sinusoidal graphs, we can graph a wider variety of sinusoidal functions. For example, we can change the amplitude, midline, or period to match a given equation.",
                  "QA Queue": [
                          {
                              "Question": "The altitude of the International Space Station t minutes after its perigee (closest point), in kilometers, is given by \
                              A(t) = 415−sin( (2π(t+23.2)/92.8 ). The International Space Station reaches its perigee once in every orbit. How long does the International Space Station take to orbit the earth?",
                              "Answer": "A(t) is maximum => 2π(t+23.2)/92.8 = π/2 + 2πn => t + 23.2 = 23.2 + 92.8n => t = 92.8n => That happens every 92.8 minutes",
                              "Type": "Integer",
                              "Difficulty": 4
                          }
                      ],
                  "Rate": 1,
                  }
        },

    ],
    "Modeling":[
        {
            "Interpreting features of functions": {
                  "Definition": "When a function f has a graph that is symmetrical with respect to the y-axis, we say that f is even. \
                  Algebraically, this means that f(−x)=f(x) for every input value x. \
                  When a function f has a graph that is symmetrical with respect to the origin, we say that f is odd. \
                  Algebraically, this means that f(−x)=-f(x) for every input value x. It is possible to have a function that is neither even nor odd.",
                  "QA Queue": [
                          {
                              "Question": "A wave on a t h coordinate plane, where h is the vertical axis and t is the horizontal axis. The h axis scales by fives. The t axis scales by two. The wave starts on the h axis at (zero, nine) and has a repeating pattern with one full cycle from four to ten.",
                              "Answer": "To find the period of the graph, we can draw vertical lines between the beginning and the end of one complete cycle. Since the distance between the vertical lines is 6 seconds, the period of the graph is 6 seconds.",
                              "Type": "Integer",
                              "Difficulty": 5
                          }
                      ],
                  "Rate": 1,
                  }
        },
        {
            "Manipulating formulas": {
                  "Definition": "Manipulating formulas allows us to solve for different variables, simplify expressions, and rewrite equations in different forms. This can be especially helpful when we are trying to understand what a function is telling us or when we want to use the function in a different way.",
                  "QA Queue": [
                          {
                              "Question": "The following formula is used in economics to find an amount of money's future value, F, \
                              where P is the present value, r is the interest rate, and t is time. F=P(1+r)^t. Rearrange the formula to highlight the present value P",
                              "Answer": "P=F/(1+r)^t",
                              "Type": "Integer",
                              "Difficulty": 4
                          }
                      ],
                  "Rate": 1,
                  }
        },
        {
            "Modeling with multiple variables": {
                  "Definition": "When we model with two variables, our model will only consider the relationship between those two variables. When we model with multiple variables, we can study the relationships between several variables at the same time. This can be helpful when we want to understand how different variables interact with one another.",
                  "QA Queue": [
                          {
                              "Question": "A company uses 3 trucks to deliver a total of T liters of cement. Each truck can transport x liters of cement per trip, and makes a total of y trips.",
                              "Answer": "T=3xy",
                              "Type": "Integer",
                              "Difficulty": 4
                          }
                      ],
                  "Rate": 1,
                  }
        }
    ]
}