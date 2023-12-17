math_3_part_1 = {
    "Polynomial arithmetic": [
        {
            "Average rate of change of polynomials": {
            "Definition": "The average rate of change of polynomial P(x) in interval [a, b] is the slope of the line connecting (a, P(a)) and (b, P(b)).",
            "QA Queue": [
                    {
                        "Question": "On interval [2, 3], which polynomial has a larger average rate of change: P(x) = 5x + 7 or Q(x) = 3(x+1)^2 - 5?",
                        "Answer": "Let's calculate the average rate of change for the polynomial P(x) = 5x + 7 over the interval [2, 3]:\nP(2) = 5(2) + 7 = 17,\nP(3) = 5(3) + 7 = 22.\nAverage rate of change for P(x) = (P(3) - P(2)) / (3 - 2) = (22 - 17) / (3 - 2) = 5.\nNow, let's calculate the average rate of change for the polynomial Q(x) = 3(x + 1)^2 - 5 over the same interval:\nQ(2) = 3(2 + 1)^2 - 5 = 12,\nQ(3) = 3(3 + 1)^2 - 5 = 44.\nAverage rate of change for Q(x) = (Q(3) - Q(2)) / (3 - 2) = (44 - 12) / (3 - 2) = 32.\nComparing the average rates of change, we find that the polynomial Q(x) = 3(x+1)^2 - 5 has a larger average rate of change than P(x) = 5x + 7 over the interval [2, 3].",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Adding and subtracting polynomials": {
            "Definition": "Adding and subtracting polynomials is an exercise in combining like terms.",
            "QA Queue": [
                    {
                        "Question": "Subtract 4p^2 - 9p + 11 from p^2 - 5p + 4.\nYour answer should be a polynomial in standard form.",
                        "Answer": "We can subtract the two polynomials term by term:\n(p^2 - 5p + 4) - (4p^2 - 9p + 11) = p^2 - 5p + 4 - 4p^2 + 9p - 11.\nNow, let's combine like terms:\n(-4p^2 + p^2) + (-5p + 9p) + (4 - 11) = -3p^2 + 4p - 7.\nTherefore, the result of subtracting (4p^2 - 9p + 11) from (p^2 - 5p + 4) is -3p^2 + 4p - 7.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Multiplying monomials by polynomials": {
            "Definition": "We use the distributive property to multiply monomials by polynomials. For example, 2x(3x+7) = 6x^2 + 14x.",
            "QA Queue": [
                    {
                        "Question": "A rectangle has a height of 2x^4 and a width of x^2 + 8x + 15.\nExpress the area of the entire rectangle.\nYour answer should be a polynomial in standard form.",
                        "Answer": "The area (A) of the rectangle is given by:\nA = height * width = (2x^4) * (x^2 + 8x + 15).\nTo find the product, we can distribute the height (2x^4) to each term in the width (x^2 + 8x + 15):\nA = 2x^4 * x^2 + 2x^4 * 8x + 2x^4 * 15 = 2x^6 + 16x^5 + 30x^4.\nTherefore, the area of the entire rectangle is 2x^6 + 16x^5 + 30x^4.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Multiplying binomials by polynomials":{
            "Definition": "For example, when we multiply a binomial by a trinomial, we multiply each term in the binomial by each term in the trinomial.",
            "QA Queue": [
                    {
                        "Question": "Expand the following expression: (8 - 3a^2)(2a^2 + 6).\nYour answer should be a polynomial in standard form.",
                        "Answer": "We can use the distributive property to multiply each term in the first expression by each term in the second expression. Let's go through the steps:\n(8 - 3a^2)(2a^2 + 6) = 8 * 2a^2 + 8 * 6 - 3a^2 * 2a^2 - 3a^2 * 6.\nNow, we simplify each term and get the polynomial: 16a^2 + 48 - 6a^4 - 18a^2.\nCombining like terms, we have -6a^4 + 16a^2 - 18a^2 + 48 = -6a^4 - 2a^2 + 48.\nTherefore, the expanded expression in standard form is -6a^4 - 2a^2 + 48.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Special products of polynomials":{
            "Definition": "The 'difference of squares' form (where P and Q can be any monomial): (P + Q)(P − Q)=P^2 − Q^2.\nThe 'perfect square' pattern (where P and Q can be any monomial): (P+Q)^2 = P^2 + 2PQ + Q^2.",
            "QA Queue": [
                    {
                        "Question": "Expand and combine like terms: (9n^7 - 1)^2.",
                        "Answer": "Let's apply the 'perfect square' pattern:\n(9n^7 - 1)^2 = (9n^7)^2 - 2(9n^7)(1) + (1)^2 = 81n^14 - 18n^7 + 1.\nTherefore, the expanded and simplified expression is 81n^14 - 18n^7 + 1.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        }
    ],
    "Polynomial factorization":[
        {
            "Factoring monomials":{
            "Definition": "A monomial is an expression that is the product of constants and nonnegative integer powers of the variable, like x, or 3a^2.\nTo factor a monomial means to express it as a product of two or more monomials.",
            "QA Queue": [
                    {
                        "Question": "Find the missing factor D that makes the equality true: −15y^4 = (D)(3y^2).",
                        "Answer": "We are looking for the expression that we can multiply by 3y^2 to get -15y^4.\nWe should multiply 3 by -5 to get -15.\nWe should multiply y^2 by y^2 to get y^4.\nIn conclusion, D = -5y^2.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Greatest common factor of monomials":{
            "Definition": "The greatest common factor of two numbers is the greatest integer that is a factor of both numbers. For example, the GCF of 12 and 18 is 6. The process is similar when you are asked to find the greatest common factor of two or more monomials, simply write the complete factorization of each monomial and find the common factors. The product of all the common factors will be the GCF.",
            "QA Queue": [
                    {
                        "Question": "What is the greatest common factor of 30b^2, 80b^2, and 20b^3?",
                        "Answer": "Let's analyze each term individually:\n30b^2 can be factored as 2 * 3 * 5 * b^2.\n80b^2 can be factored as 2^4 * 5 * b^2.\n20b^3 can be factored as 2^2 * 5 * b^3.\nTo find the GCF, we look for the common factors with the lowest exponent. In this case, the common factors are 2, 5, and b^2. Taking the lowest exponent for each factor, we have 2 * 5 * b^2, which simplifies to 10b^2.\nTherefore, the greatest common factor of 30b^2, 80b^2, and 20b^3 is 10b^2.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Factoring higher degree polynomials":{
            "Definition": "When we factor a polynomial, we write the polynomial as a product of two or more factors.",
            "QA Queue": [
                    {
                        "Question": "Factor completely the following polynomial: x^4 + 5x^3 + 4x + 20.",
                        "Answer": "Let's group the first two terms and the last two terms: (x^4 + 5x^3) + (4x + 20).\nNow, let's factor out the greatest common factor from each group: x^3(x + 5) + 4(x + 5).\nNotice that we have a common binomial factor of (x + 5). We can factor it out: (x + 5)(x^3 + 4)\nNow, we have factored the polynomial completely into (x + 5)(x^3 + 4).",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Factoring using structure":{
            "Definition": "The 'difference of squares' form (where P and Q can be any monomial): (P + Q)(P − Q)=P^2 − Q^2.\nThe 'perfect square' pattern (where P and Q can be any monomial): (P+Q)^2 = P^2 + 2PQ + Q^2.",
            "QA Queue": [
                    {
                        "Question": "We want to factor the following expression: 25x^2 - 36y^8.\nWe can factor the expression as (U + V)(U − V) where U and V are either constant integers or single-variable expressions.\nWhat are U and V?",
                        "Answer": "First, we identify the perfect square terms within 25x^2 and 36y^8: 25x^2 = (5x)^2 and 36y^8 = (6y^4)^2.\nNow, let's rewrite the expression using these perfect squares: 25x^2 - 36y^8 = (5x)^2 - (6y^4)^2.\nWe can see that this expression follows the pattern of a difference of squares, which can be factored as (A + B)(A - B), where A = 5x and B = 6y^4.\nTherefore, U = 5x and V = 6y^4.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Geometric series":{
            "Definition": "In a geometric series with a being the first term, r being the common ratio and n being the number of terms, the sum of the first n terms is:\nS_n = a + ar + ar^2 + ... + ar^(n-1) = (a(1 - r^n)) / (1-r).\nCreated by Sal Khan.",
            "QA Queue": [
                    {
                        "Question": "A monkey is swinging from a tree. On the first swing, she passes through an arc whose length is 24 m. With each swing, she travels along an arc that is half as long as the arc of the previous swing.\nWhich expression gives the total length the monkey swings in her first n swings?",
                        "Answer": "Let's denote the length of the first swing as a1 (which is 24 m) and the common ratio between the terms as r (which is 1/2).\nThe total length can be calculated using the formula for the sum of a finite geometric series with total length = a1 * (1 - r^n) / (1 - r).\nSubstituting the values, we have:\nTotal length = 24 * (1 - (1/2)^n) / (1 - 1/2).\nSimplifying further, we get:\nTotal length = 24 * (1 - 1/2^n) / (1/2) = 48 * (1 - 1/2^n).\nTherefore, the expression for the total length the monkey swings in her first n swings is 48 * (1 - 1/2^n).",
                        "Type": "Narrative",
                        "Difficulty": 3
                    }
                ],
            "Rate": 1,
            }
        }
    ],
    "Polynomial division": [
        {
            "Dividing polynomials by x":{
            "Definition": "Not every polynomial division results in a polynomial. When it doesn't, we end up with a remainder.",
            "QA Queue": [
                    {
                        "Question": "Divide the polynomials: (2x^4 + 5x + 4) / x.\nYour answer should be in the form p(x) + k/x where p is a polynomial and k is an integer.",
                        "Answer": "Usually, there are many different ways to divide polynomials. Here, we will use the method of splitting the quotient into multiple quotients:\n(2x^4 + 5x + 4) / x = 2x^4 / x + 5x / x + 4 / x.\nNow let's try to cancel common factors in the resulting terms.\n2x^4 / x = 2x^3, 5x / x = 5, and 4 / x doesn't have common factors so it has to stay as it is.\nIn conclusion, this is the result of dividing the polynomials: 2x^3 + 5 + 4 / x.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Dividing quadratics by linear factors":{
            "Definition": "Not every polynomial division results in a polynomial. When it doesn't, we end up with a remainder.",
            "QA Queue": [
                    {
                        "Question": "Divide the polynomials: (x^2 - 5) / (x - 2).\nYour answer should be in the form p(x) + k / (x - 2) where p is a polynomial and k is an integer.",
                        "Answer": "We can factor x^2 - 5 as the following: x^2 - 5 = x^2 - 4 - 1 = (x-2)(x+2) - 1.\nSo the division results in: x + 2 - 1 / (x-2).",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Dividing polynomials by linear factors":{
            "Definition": "Not every polynomial division results in a polynomial. When it doesn't, we end up with a remainder.",
            "QA Queue": [
                    {
                        "Question": "Divide the polynomials: (2x^3 - 13x^2 + 9x - 16) / (x - 6).\nYour answer should be either be p(x) or p(x) + k / (x - 6) where p is a polynomial and k is an integer.",
                        "Answer": "To divide the polynomial (2x^3 - 13x^2 + 9x - 16) by (x - 6), we can use long division. Let's go through the steps:\nWe start by dividing the first term of the dividend (2x^3) by the divisor (x - 6), which gives us 2x^2. We then multiply this term by the divisor (x - 6) and subtract the result from the dividend:\n2x^3 - 13x^2 + 9x - 16 = 2x^2(2x-6) - x^2 + 9x - 16.\nNext, we bring down the next term from the dividend (- x^2 + 9x - 16):\n-x^2 + 9x - 16 = -x(x-6) + 3x - 16.\nAgain, we bring down the next term from the dividend (3x - 16):\n3x - 16 = 3(x-6) + 2.\nSince the remainder is 2, we have: 2x^3 - 13x^2 + 9x - 16 = (2x^2 + 5x - 1)(x - 6) + 2.\nHence, the answer is p(x) + k/(x - 6) = 2x^2 + 5x - 1 + 2/(x - 6).",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Polynomial remainder theorem":{
            "Definition": "The polynomial remainder theorem states that, for every number r, any polynomial f(x) is the sum of f(r) and the product by x-r of a polynomial in x of degree less than the degree of f.",
            "QA Queue": [
                    {
                        "Question": "P(x) is a polynomial. Here are a few values of P(x): P(-5) = -2, P(-3) = 6, P(3) = 7, P(5) = -1.\nWhat is the remainder when P(x) is divided by (x+5)?",
                        "Answer": "According to the Remainder Theorem, if we substitute the value of (-5) into P(x) and find the result, that will be the remainder.\nGiven the values of P(-5) = -2, we know that when x = -5, the value of P(x) is -2. Therefore, the remainder when P(x) is divided by (x+5) is -2.\nHence, the remainder when P(x) is divided by (x+5) is -2.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        }
    ]
}

math_3_part_2 = {
    "Polynomial graphs`": [
        {
            "Zeros of polynomials":{
            "Definition": "For what x values p(x) is going to be equal to 0? We say that polynomial p has zeros when x = x_0 if p(x_0) = 0.",
            "QA Queue": [
                    {
                        "Question": "We want to find the zeros of this polynomial: p(x) = (x + 2)(2x^2 + 3x - 9).\nPlot all the zeros (x-intercepts) of the polynomial on a graph.",
                        "Answer": "The zeros of p(x) are -2, 1.5 and 3.\nBEGIN PLOT:\nDraw('A', (-2, 0))\nDraw('B', (1.5, 0))\nDraw('C', (-3, 0))\nEND PLOT.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Positive and negative intervals of polynomials":{
            "Definition": "The sign of a polynomial between any two consecutive zeros is either always positive or always negative.",
            "QA Queue": [
                    {
                        "Question": "f(x) = (2x−1)(3x−5)(x−4)(3x+6) has zeros at x = −2, x = 1/2, x = 5/3, and x = 4.\nWhat is the sign of f on the interval 1/2 < x < 5/3?",
                        "Answer": "The sign of a polynomial between any two consecutive zeros is either always positive or always negative, we can just pick a value x in the interval (1/2, 5/3), calculate f(x) and find out its sign.\nWe can pick x = 1, then f(1) = (2 - 1) * (3 - 5) * (1 - 4) * (3 + 6) = 54 > 0.\nSo f(x) is always positive on the interval 1/2 < x < 5/3.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "End behavior of polynomials":{
            "Definition": "The end behavior of a function f describes the behavior of the graph of the function at the 'ends' of the x-axis.\nIn other words, the end behavior of a function describes the trend of the graph if we look to the right end of the x-axis (as x approaches +\infinity) and to the left end of the x-axis (as x approaches −\infinity).",
            "QA Queue": [
                    {
                        "Question": "Consider the polynomial function g(x) = -x^4 + 2x^3 + 5x^2 - 1.\nWhat does the function approach when x approaches +\infinity?",
                        "Answer": "In g, the leading term is -x^4.\nSince the degree of the leading term, 4, is even, the leading term behaves the same as x gets both positively and negatively large. In both cases, x^4 goes to positive infinity.\nHowever, the sign of the leading term is negative, so the leading term goes to -\infinity instead.\nAs the leading term is dominate, we conclude that g(x) goes to minus infinity when x approaches +\infinity.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        }
    ],
    "Logarithms": [
        {
            "Introduction to logarithm":{
            "Definition": "Logarithms are another way of thinking about exponents. We have the following formula:\nlog_b(a) = c \Leftrightarrow b^c = a, where b is the base, c is the exponent, and a is the argument.\nA really important logarithm is logarithm with base e, or we can call it the natural logarithm.",
            "QA Queue": [
                    {
                        "Question": "What is the logarithm with base 1/5 of 5.",
                        "Answer": "To find the logarithm, we need to find x such that (1/5)^x = 5.\nNote that, (1/5)^x = 1/(5^x) = (5^0)/(5^x) = 5^(0-x).\nAlso, trivially we have 5^1 = 5, so 0 - x = 1, or equivalently, x = -1.\nIn conclusion, the logarithm with base 1/5 of 5 is -1.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Properties of logarithms":{
            "Definition": "Product rule: log_b(MN) = log_b(M) + log_b(N).\nQuotient rule: log_b(M/N) = log_b(M) - log_b(N).\nPower rule: log_b(M^p) = p log_b(M).",
            "QA Queue": [
                    {
                        "Question": "Tanya wants to simplify the following expression: log_5 ((25^x)/y). However, she does not have strong mathematics fundamentals. Please help her!",
                        "Answer": "Let A = log_5 ((25^x)/y).\nUsing the quotient rule, we get: A = log_5(25^x) - log_5(y).\nUsing the power rule, we get: A = x * log_5(25) - log_y.\nFinally, since 25 = 5^2, we have log_5(25) = 2.\nSo we can simplify A into 2x - log_5(y).",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Change of base formula for logarithms":{
            "Definition": "Change of base rule: log_b(M) = log_a(M) / log_a(b), for all a, b, M.",
            "QA Queue": [
                    {
                        "Question": "Evaluate the logarithm: log_4(0.6).\nRound your answer to the nearest thousandth.",
                        "Answer": "We can use the change of base rule to get: log_4(0.6) = log_2(0.6) / log_2(4) = log_2(0.6) / 2.\nWe see that log_2(0.6) is approximately -0.7375, so log_4(0.6) is approximately -0.368.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Solving exponental models":{
            "Definition": "To solve exponential equations of the form a * b^x = d, we must first isolate the exponential part and get: b^x = d/a. Then, we can obtain x by converting the equation into the logarithm form: x = log_b(d/a).",
            "QA Queue": [
                    {
                        "Question": "Katya is a ranger at a nature reserve in Siberia, Russia, where she studies the changes in the reserve's bear population over time.\nThe relationship between the elapsed time t, in years, since the beginning of the study and the bear population B(t), on the reserve is modeled by the following function: B(t) = 5000 * 2^(−0.05t). In how many years will the reserve's bear population be 2000? Round your answer, if necessary, to the nearest hundredth.",
                        "Answer": "To find out in how many years the reserve's bear population will be 2000, we can set up the equation and solve for t. The given function is: B(t) = 5000 * 2^(-0.05t).\nWe need to find the value of t when B(t) is 2000: 2000 = 5000 * 2^(-0.05t).\nDividing both sides of the equation by 5000, we get: 0.4 = 2^(-0.05t).\nTo solve for t, we can take the logarithm of both sides using the base 2 logarithm: log2(0.4) = log2(2^(-0.05t)).\nUsing the property of logarithms, we can bring down the exponent: log2(0.4) = -0.05t * log2(2).\nSince log2(2) equals 1, we can simplify further: log2(0.4) = -0.05t.\nUsing a calculator, we find that log2(0.4) is approximately -1.3219, so t would be approximately -1.3219 / (-0.05) \approx 26.438.\nSo it would take about 26.438 years.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        }
    ],
    "Transformation of functions": [
        {
            "Symmetry of functions":{
            "Definition": "A function is an even function if its graph is symmetric with respect to the y-axis.\nA function is an odd function if its graph is symmetric with respect to the origin.",
            "QA Queue": [
                    {
                        "Question": "This table defines function f:\BEGIN TABLE\nx & -2 & -1 & 0 & 1 & 2\nf(x) & 2 & 3 & 0 & 2 & 3\nEND TABLE.\nAccording to the table, is f even, odd, or neither?",
                        "Answer": "Comparing the function values with their corresponding values when we substitute -x for x, we can see that f(-1) is not equal to f(1) and f(1) + f(-1) is also not zero.\nSo f is neither odd nor even.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        }
    ],
    "Equation": [
        {
            "Rational equations":{
            "Definition": "To solve a rational equation, we will multiply both sides by the denominator to transform it into an easier equation. After solving it, we need to check if the obtained value is valid (does not make the original terms undefined).",
            "QA Queue": [
                    {
                        "Question": "Teresa needs your help to solve the following equation: (y-1) / (3y + 7) = 1/10.",
                        "Answer": "We can start by cross-multiplying.\nMultiplying both sides of the equation by 10 * (3y+7) yields: 10 * (y−1) = (3y+7).\nExpanding the equation: 10y − 10 = 3y + 7, which is equivalent to 7y = 17.\nSo y = 17/7.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Square-root equations":{
            "Definition": "To solve square-root equations, we want to isolate the radical term. Then we can try to square both sides to transform it into easier equations. Last but not least, do make sure to check the validity of the solution and avoid extraneous solution!",
            "QA Queue": [
                    {
                        "Question": "What are the solutions to the following equation? The equation is: 6 + 3x = \sqrt(2x + 12) + 2x.",
                        "Answer": "First, we subtract 2x from both sides and get: 6 + x = \sqrt(2x + 12).\nThen, squaring both sides, we get: 36 + 12x + x^2 = 2x + 12, which is equivalent to: x^2 + 10x + 24 = 0.\nFurther factoring, we get: (x+4)(x+6) = 0, so the equation has 2 candidate solutions: x=-4 and x=-6.\nBoth solutions are valid.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Solving equations by graphing":{
            "Definition": "We can solve an equation by graphing both sides of the equation, then estimate the solution.",
            "QA Queue": [
                    {
                        "Question": "Esteban and Anna opened different investment accounts at the same time.\nEsteban's account balance can be modeled by f(t) = 1000 * e^(0.08t).\nAnna's account balance can be modeled by g(t) = 750 * e^(0.12t).\nWhen do the accounts have the same balance?",
                        "Answer": "By graphing both f and g and estimate the intersection, we obtain the answer, which is in about 7 years.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Solving exponental models":{
            "Definition": "To solve exponential equations of the form a * b^x = d, we must first isolate the exponential part and get: b^x = d/a. Then, we can obtain x by converting the equation into the logarithm form: x = log_b(d/a).",
            "QA Queue": [
                    {
                        "Question": "Katya is a ranger at a nature reserve in Siberia, Russia, where she studies the changes in the reserve's bear population over time.\nThe relationship between the elapsed time t, in years, since the beginning of the study and the bear population B(t), on the reserve is modeled by the following function: B(t) = 5000 * 2^(−0.05t). In how many years will the reserve's bear population be 2000? Round your answer, if necessary, to the nearest hundredth.",
                        "Answer": "To find out in how many years the reserve's bear population will be 2000, we can set up the equation and solve for t. The given function is: B(t) = 5000 * 2^(-0.05t).\nWe need to find the value of t when B(t) is 2000: 2000 = 5000 * 2^(-0.05t).\nDividing both sides of the equation by 5000, we get: 0.4 = 2^(-0.05t).\nTo solve for t, we can take the logarithm of both sides using the base 2 logarithm: log2(0.4) = log2(2^(-0.05t)).\nUsing the property of logarithms, we can bring down the exponent: log2(0.4) = -0.05t * log2(2).\nSince log2(2) equals 1, we can simplify further: log2(0.4) = -0.05t.\nUsing a calculator, we find that log2(0.4) is approximately -1.3219, so t would be approximately -1.3219 / (-0.05) \approx 26.438.\nSo it would take about 26.438 years.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        }
    ]
}

math_3_part_3 = {
    "Trigonometry": [
        {
            "Law of sines":{
            "Definition": "In a triangle ABC, the law of sines states that: sinA / BC = sinB / CA = sinC / AB.",
            "QA Queue": [
                    {
                        "Question": "The following figure shows triangle ABC with side lengths to the nearest tenth.\nBEGIN PLOT:\nDraw(Acute triangle ABC)\nLabel(\angle A, 53 \degree)\nLabel(\angle C, 44 \degree)\nLabel(Length AB, 18)\nEND PLOT.\nFind BC.",
                        "Answer": "To find the length of BC in triangle ABC, we can use the Law of Sines. In this case, we can use the following equation: sinA / BC = sinC / AB. Substituting the given values, we get: sin(44 \degree) / 18 = sin(53 \degree) / BC. To solve for BC, we can rearrange the equation: BC = (18 * sin(44 \degree)) / sin(53 \degree). Using a calculator, we can get BC \approx 22.4.\nTherefore, the length of BC in triangle ABC is approximately 20.7 units (rounded to the nearest tenth).",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Law of cosines":{
            "Definition": "In triangle ABC, let AB = c, BC = a, CA = b. Then a^2 = b^2 + c^2 - 2bc cos(BAC). The same property is applied for the other 2 sides.",
            "QA Queue": [
                    {
                        "Question": "Given the following figure. Find angle B.\nRound to the nearest degree.\nBEGIN PLOT:\nDraw(Acute triangle ABC)\nDraw(Length BC, 6)\nDraw(Length AC, 13)\nDraw(Length AB, 15)\nEND PLOT.",
                        "Answer": "To find angle B in the triangle ABC, we can use the Law of Cosines: AC^2 = AB^2 + BC^2 - 2 * AB * BC * cos(B) \Rightarrow 13^2 = 15^2 + 6^2 - 2 * 15 * 6 * cos(B) \Rightarrow 169 = 225 + 36 - 180 * cos(B).\nSimplifying further: 92 = 180 * cos(B).\nDividing both sides by 180: cos(B) = 92 / 180 \approx 0.511.\nSo \angle B \approx 59 \degree.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Solving general triangles":{
            "Definition": "We can solve a triangle using the law of sines and law of cosines.",
            "QA Queue": [
                    {
                        "Question": "'How can we bridge this river?' asks Omkar.\n'First, let's find the distance to the big rock on the other side,' Melissa replies. Melissa moves 100 meters away, as shown. She looks back and measures a 33 \degree angle between Omkar and the big rock.\nFrom his viewpoint, Omkar sees an angle of 98 \degree between Melissa and the big rock.\nWhat is the distance across the river from Omkar to the big rock? Do not round during your calculations. Round your final answer to the nearest meter.",
                        "Answer": "Let A be the point represents where Melissa stands, B be the point represents where Omkar stands, and C represents where the big rock is.\nWe have: \angle A = 33 \degree, \angle B = 98 \degree, AB = 100, and need to find BC.\nFirst we have \angle C = 180 - 98 - 33 = 49 \degree.\nUsing the law of sines, we have: BC = sin(A) * AB / sin(C) = sin(33 \degree) * 100 / sin(49 \degree) \approx 72.17.\nIn conclusion, the distance from Omkar to the big rock is about 72 meters.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Unit circle introduction":{
            "Definition": "The unit circle definition allows us to extend the domain of sine and cosine to all real numbers. The process for determining the sine/cosine of any angle \theta is as follows:\nStarting from (1,0), move along the unit circle in the counterclockwise direction until the angle that is formed between your position, the origin, and the positive x-axis is equal to \theta.\nsin(\theta) is equal to the y-coordinate of your point, and cos(\theta) is equal to the x-coordinate.",
            "QA Queue": [
                    {
                        "Question": "Given the following figure:\nBEGIN PLOT:\nDraw(x-axis)\nDraw(y-axis)\nDraw(Unit circle)\nDraw(Point A in the first quadrant and on the unit circle)\nLabel(\angle AOx, 50 \degree)\nLabel('A', (0.64, 0.77).\nEND PLOT.\nEstimate sin(50\degree).",
                        "Answer": "Since Point A lies on the unit circle, the y-coordinate of Point A represents the value of sine for the angle formed.\nTherefore, sin(50°) is approximately equal to the y-coordinate of Point A, which is 0.77.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Radian":{
            "Definition": "Radian is defined such that one radian is the angle subtended at the centre of a circle by an arc that is equal in length to the radius. We have the conversion: 2\pi radians = 360 \degree.",
            "QA Queue": [
                    {
                        "Question": "Convert the angle \theta = (29\pi) / 15 radians to degrees. Express your answer exactly.",
                        "Answer": "Since 2\pi radiansis 360 degrees, we have: \theta = 29/30 * (2\pi) radians, which is equivalent to 29/30 * 360 = 351 degrees.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "The Pythagorean identity":{
            "Definition": "The Pythagorean identity states that: sin^2(\theta) + cos^2(\theta) = 1.",
            "QA Queue": [
                    {
                        "Question": "The angle \theta_1 is located in Quadrant IV, and sin(\theta_1) = -13/85.\nWhat is the value of cos(\theta_1)?\nExpress your answer exactly.",
                        "Answer": "By the Pythagorean identity, we have: sin^2(\theta_1) + cos^2(\theta_1) = 1, which means that cos^2(\theta_1) + (-13/85)^2 = 1 \Rightarrow cos^2(\theta_1) = 7056/7225.\nSo cos(\theta_1) = 84 / 85.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Amplitude, midline, & period":{
            "Definition": "Midline, amplitude, and period are three features of sinusoidal graphs.\nMidline is the horizontal line that passes exactly in the middle between the graph's maximum and minimum points.\nAmplitude is the vertical distance between the midline and one of the extremum points.\nPeriod is the distance between two consecutive maximum points, or two consecutive minimum points (these distances must be equal).",
            "QA Queue": [
                    {
                        "Question": "What is the midline of the function f(x) = sinx + 3?",
                        "Answer": "The midline of the function g(x) = sinx is y = 0.\nNow shifting the function graph 3 units up along the y-axis, we get the midline of f(x) = sinx + 3, which is the line y = 3.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Transforming sinusoidal graphs":{
            "Definition": "A graph could be transformed in various ways, including stretching or reflecting.",
            "QA Queue": [
                    {
                        "Question": "What is the amplitude of y = -6 sin(3\pi x + 4) - 2?",
                        "Answer": "We can start from the graph y = sin(x), which has amplitude 1.\nThe graph y = sin(3\pi x) is a horizontal stretch of y = sin(x) and has the same amplitude.\nThe graph y = sin(3\pi x + 4) shifts y = sin(3\pi x) four units to the left, so the amplitude still remains 1.\nThe graph y = -6 sin(3\pi x + 4) - 2 does a vertical stretch of scale 6 on y = sin(3\pi x + 4), then reflects through the x-axis, then shifts down 2 units, which make the amplitude multiplies by 6.\nIn conclusion, the amplitude of y = -6 sin(3\pi x + 4) - 2 is 6 units.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Sinusoidal models":{
            "Definition": "Sinusoidal graphs could be useful in modeling periodical things, such as rainfall, temperature, ...",
            "QA Queue": [
                    {
                        "Question": "In the month of March, the temperature at the South Pole varies over the day in a periodic way that can be modeled approximately by a trigonometric function.\nThe highest temperature is about −50 Celcius degrees, and it is reached around 2 p.m. The lowest temperature is about −54 Celcius degrees and it is reached half a day apart from the highest temperature, at 2 a.m. What is the temperature at 5 p.m? Round your answer, if necessary, to two decimal places.",
                        "Answer": "We can model the temperature T by a trigonometric function T(t), with respect to time t.\nThe difference between the maximum and minimum of the function is (-50) - (-54) = 4, so the amplitude is 2.\nThe time period is 24, and the midline is T = ((-50) + (-54)) / 2 = -52.\nSo the function that models the situation is: T(t) = 2 sin((t+16)/24 * 2 \pi) - 52.\nThis means the temperature at 5 p.m is T(5) \approx -50.59 Celcius degrees.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        },
    ],
    "Modeling": [
        {
            "Modeling with function combination":{
            "Definition": "This unit is all about modeling using functions and formulas. We will learn how to use them in different ways, including combining them.",
            "QA Queue": [
                    {
                        "Question": "The function C(t) = 400 + 30t models the number of classrooms, C, in the town of Sirap, t years from now. The function D(t) = 25 + t models the number of students per classroom, D, t years from now.\nLet S be the number of students in Sirap's school system t years from now.\nWrite a formula of S(t) in terms of t.",
                        "Answer": "First, we want to find a formula for S(t) in terms of C(t) and D(t).\nWe see that the number of students is the multiplication of the number of students per classroom and the number of classrooms, so S(t) = C(t) * D(t).\nSo the formula for S(t) is: (25 + t) * (400 + 30t).",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Interpreting features of functions":{
            "Definition": "In general, to interpret the meaning of the symmetry in the graph of a function, it is helpful to do the following:\nStep 1: Decide if the function is even or odd and determine what this means algebraically.\nStep 2: Understand what each variable represents in terms of the context.\nStep 3: Come up with a statement that uses the meaning of the variables and compares the output values for opposite input values.",
            "QA Queue": [
                    {
                        "Question": "Trudy is learning to drive a new kind of vehicle. The speed of the vehicle is determined by the position of a rotating knob. The vehicle's speed, V(x), in miles per hour, is a function of the knob position, x. Note that x>0 means the knob is turned x units clockwise and x<0 means the knob is turned x units counter-clockwise.\nThis function is even. Which of statement could interpret the symmetry of the graph of function V",
                        "Answer": "Rotating the knob clockwise and counter-clockwise by the same amount results in equal vehicle speeds.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Manipulating formulas":{
            "Definition": "This unit is all about modeling using functions and formulas. We will learn how to use them in different ways, including combining them.",
            "QA Queue": [
                    {
                        "Question": "The following formula is used in economics to find an amount of money's future value, F, where P is the present value, r is the interest rate, and t is time.\nF = P(1 + r)^t.\nRearrange the formula to highlight the present value.",
                        "Answer": "Divide both sides by (1+r)^t, we have: P = F(1+r)^(-t).",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Modeling with two variables":{
            "Definition": "This unit is all about modeling using functions and formulas. We'll learn how to address situations with two variables.",
            "QA Queue": [
                    {
                        "Question": "Lisa owns a 'Random Candy' vending machine, which is a machine that picks a candy out of an assortment in a random fashion. Lisa controls the probability of picking each candy.\nThe machine is running out of 'Honey Bunny', so Lisa wants to program it so that the probability of getting a candy other than 'Honey Bunny' twice in a row is greater than 9/4 times the probability of getting 'Honey Bunny' in one try.\nWrite an inequality that models the situation. Use p to represent the probability of getting 'Honey Bunny' in one try.",
                        "Answer": "Let p be the probability of getting 'Honey Bunny' in one try. Then the probability of getting a candy other than 'Honey Bunny' in one try is 1-p, and the probability of getting that twice in a row is (1-p)^2.\nSince the probability of getting a candy other than 'Honey Bunny' twice in a row is greater than 9/4 times the probability of getting 'Honey Bunny' in one try, we get (1-p)^2 > 9/4 * p.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Modeling with multiple variables":{
            "Definition": "This unit is all about modeling using functions and formulas. We'll learn how to address situations with multiple variables.",
            "QA Queue": [
                    {
                        "Question": "Juana is measuring two pyramids whose bases are isosceles right triangles.\nGiven the height h and the volume V of the first pyramid, Juana uses the formula a = sqrt(6V/h) to compute its base's side length a to be 1 meter.\nThe second pyramid has the same height, but has 9 times the volume. What is the side length of its base?",
                        "Answer": "Multiplying V with 9 would multiply sqrt(V) with 3.\nSo if the second pyramid has the same height but has 9 timese the volume, its side should be 3 times the side of the first pyramid.\nSo the second pyramid's side length is 1 * 3 = 3 meters.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        }
    ],
    "Study design": [
        {
            "Samples and surveys":{
            "Definition": "There are 4 types of sampling methods.\nSimple random sampling: In a simple random sample, every member of the population has an equal chance of being selected. Your sampling frame should include the whole population.\nSystematic sampling: Systematic sampling is similar to simple random sampling, but it is usually slightly easier to conduct. Every member of the population is listed with a number, but instead of randomly generating numbers, individuals are chosen at regular intervals.\nStratified sampling: Stratified sampling involves dividing the population into subpopulations that may differ in important ways.\nCluster sampling: Cluster sampling also involves dividing the population into subgroups, but each subgroup should have similar characteristics to the whole sample. Instead of sampling individuals from each subgroup, you randomly select entire subgroups.",
            "QA Queue": [
                    {
                        "Question": "A group of randomly selected Throne County citizens were asked to pick their favorite genre of music. The table below shows the results of the survey. There are 2006 Throne County citizens.\nBEGIN TABLE:\nFavorite genre of music & Number of citizens\nCountry & 25\nRock & 38\nOldies & 11\nOther & 6.\nEND TABLE.\nBased on the data, what is the most reasonable estimate for the number of Throne County citizens whose favorite genre of music is rock?",
                        "Answer": "The most reasonable estimate comes from multiplying the total population size by the proportion of citizens in the sample whose favorite genre of music is rock: Estimate = Population size * Sample proportion.\nWe have the population size be 2006, and the sample proportion is: 38 / (25 + 38 + 11 + 6) = 38 / 80.\nSo the estimation would be: 2006 * 38 / 80 \approx 953 citizens.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Observational studies and experiments":{
            "Definition": "We do studies to gather information and draw conclusions. The type of conclusion we draw depends on the study method used:\nIn an observational study, we measure or survey members of a sample without trying to affect them.\nIn a controlled experiment, we assign people or things to groups and apply some treatment to one of the groups, while the other group does not receive the treatment.",
            "QA Queue": [
                    {
                        "Question": "A study took random sample of adults and asked them about their bedtime habits. The data showed that people who drank a cup of tea before bedtime were more likely to go to sleep earlier than those who didn't drink tea.\nWhich type of study method is this?",
                        "Answer": "This study was a survey that looked at if people drank tea or not and when they went to bed. The people were not randomly assigned to groups, so this was an observational study.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        }
    ]
}

math_3_part_4 = {
    "Binomial probability": [
        {
            "Binomial probability":{
            "Definition": "Suppose we throw a basketball n times and the chance to score in an attempt is p. Then the chance to score in k out of n attempts is \binom(n, k) * p^k * (1-p)*(n-k).",
            "QA Queue": [
                    {
                        "Question": "Steph's little brother Luke only has a 20% chance of making a free-throw.\nSteph promises to buy Luke ice cream if he makes 3 or more of his 4 free-throws. He is going to shoot 4 free-throws.\nWhat is the probability that he makes 3 or more of the 4 free throws?",
                        "Answer": "The probability that Luke makes 3 or more of the 4 free throws is the sum of probability that Luke makes 3 throws and probability that Luke makes 4 throws.\nWe have the formula: P(makes 3 or more) = P(makes 3 free-throws) + P(makes 4 free-throws) = \binom(4,3) * (1/5)^3 * 4/5 + \binom(4,4) * (1/5)^4 = 16/625 + 1/625 = 17/625 = 0.0272.\nSo the chance that Luke gets an ice scream is 0.0272.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        }
    ],
    "Normal distributions": [
        {
            "Normal distributions":{
            "Definition": "Many measurements fit a special distribution called the normal distribution. In a normal distribution,\n\approx 68% of the data falls within 1 standard deviation of the mean,\n\approx 95% of the data falls within 2 standard deviations of the mean,\n\approx 99.7% of the data falls within 3 standard deviations of the mean.",
            "QA Queue": [
                    {
                        "Question": "The lifespans of seals in a particular zoo are normally distributed. The average seal lives 13.8 years; the standard deviation is 3.2 years.\nUse the empirical rule (68−95−99.7%) to estimate the probability of a seal living between 7.4 and 17 years.",
                        "Answer": "Since 7.4 = 13.8 - 2 * 3.2 and 17 = 13.8 + 3.2, it means 7.4 years is within 2 standard deviations of the mean and 17 years is within 1 standard deviation of the mean.\nThe probability that the seal lives between 7.4 and 13.8 years is then: 95% / 2 = 47.5%, and the probability that the seal lives between 13.8 years and 17 years is: 68% / 2 = 34%.\nIn total, the probability that the seal lives between 7.4 and 17 years is: 47.5% + 34% = 81.5%.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        }
    ],
    "Rational functions": [
        {
            "Cancelling common factors":{
            "Definition": "A polynomial is an expression that consists of a sum of terms containing integer powers of x, like 3x^2 − 6x − 1.\nA rational expression is simply a quotient of two polynomials. Or in other words, it is a fraction whose numerator and denominator are polynomials.\nThe domain of any expression is the set of all possible input values. In the case of rational expressions, we can input any value except for those that make the denominator equal to 0 (since division by 0 is undefined).\nA rational expression is reduced to lowest terms if the numerator and denominator have no factors in common.",
            "QA Queue": [
                    {
                        "Question": "Simplify the following rational expression and express in expanded form: (z^2 + 4zy + 4y^2) / (4z + 8y).",
                        "Answer": "We can simplify the rational expression by the following steps: (z^2 + 4zy + 4y^2) / (4z + 8y) = (z+2y)^2 / (4(z + 2y)) = (z+2y) / 4.\nThe cancelled term is z + 2y, so the expression is equivalent only when z + 2y \neq 0.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "End behavior of rational functions":{
            "Definition": "The end behavior of a function f describes the trend of the function at the 'ends' of the x-axis, i.e., as x approaches +\infinity and as x approaches −\infinity.",
            "QA Queue": [
                    {
                        "Question": "Consider the following rational function: f(x) = (-8x^3 - 3x + 4) / (2x^2 - 9).\nDetermine f's end behaviour.",
                        "Answer": "For rational functions, the end behavior will be similar to the leading term in the numerator divided by leading term in the denominator.\nIn our case: f(x) \approx (-8x^3) / (2x^2).\nWe can now reduce -8x^3 / 2x^2 to the lowest terms and it becomes -4x.\nWe have -4x approaches -\infinity as x approaches +\infinity so f(x) behaves the same. Similarly, we have f(x) approaches +\infinity as x approaches -\infinity.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Discontinuities of rational functions":{
            "Definition": "Inputs where the function is defined and the numerator is equal to zero are zeros of the function.\nWe can simplify the function expression by canceling out common factors. Any undefined input that no longer makes the denominator equal to zero is a removable discontinuity. The remaining undefined inputs are vertical asymptotes.",
            "QA Queue": [
                    {
                        "Question": "Let q(x) = (x^2 - 8x + 15) / (x^2 - 6x + 9).\nDescribe the behavior of the function q around its vertical asymptote at x = 3.",
                        "Answer": "Simplifying q(x), we get: (x^2 - 8x + 15) / (x^2 - 6x + 9) = (x-3)(x-5) / (x-3)^2 = (x-5) / (x-3).\nWhen x approaches 3, the numerator approaches 3 - 5 = -2 < 0.\nSo we can conclude: When x approaches 3-, q(x) approaches +\infinity, and when x approaches 3+, q(x) approaches -\infinity.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Modeling with rational functions":{
            "Definition": "Many real-world problems could be modeled with rational functions.",
            "QA Queue": [
                    {
                        "Question": "Ian can rake a lawn and bag the leaves in 5 hours. Kyandre can rake the same lawn and bag the leaves in 3 hours. Working together, how long would it take them to rake the lawn and bag the leaves?",
                        "Answer": "In an hour, Ian could rake 1/5 lawn, while Kyandre would rake 1/3 lawn.\nCombined, they will rake 1/5 + 1/3 = 8/15 lawn.\nSo the time it takes when they rake the lawn and bag the leaves together would be 15/8 = 1.875 hours or 1 hour 52.5 minutes.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Multiplying & dividing rational expressions":{
            "Definition": "In general, the product of two rational expressions is undefined for any value that makes either of the original rational expressions undefined.\nTo divide two numerical fractions, we multiply the dividend (the first fraction) by the reciprocal of the divisor (the second fraction).\nWhen dividing two rational expressions, the quotient is undefined for any value that makes either of the original rational expressions undefined, and for any value that makes the divisor equal to zero.",
            "QA Queue": [
                    {
                        "Question": "Given the following expression: (x^2 + 5x + 4)/(x^2 - 13x + 40) * (x-8)/(x^2-1).\nWhat is the product in lowest terms and what values of x must we exclude from the domains of the expressions?",
                        "Answer": "Multiplying and reducing to lowest terms: (x^2 + 5x + 4)/(x^2 - 13x + 40) * (x-8)/(x^2-1) = (x+1)(x+4)/((x-5)(x-8)) * (x-8)/((x-1)(x+1)) = (x+4)/(x-5)(x-1).\nFinding the x-values that make the expression undefined:\nxx-values that make the first factor's denominator equal to zero: x = 5 and x = 8.\nAnd x-values that make the second factor's denominator equal to zero: x = −1 and x = 1.\nIn conclusion, the values of x we must exclude from the domains of the expressions are x = −1, x = 1, x = 5, and x = 8.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Adding subtracting rational expressions intro":{
            "Definition": "To add or subtract two numerical fractions with the same denominator, we simply add or subtract the numerators, and write the result over the common denominator.\nTo add or subtract two numerical fractions with different denominators, we need to find the common denominator, then add or subtract as normal.",
            "QA Queue": [
                    {
                        "Question": "Add: 1/(7x^2 - 7x) + 6/(7x^2 + 14x).\nThe numerator should be expanded and simplified. The denominator should be either expanded or factored.",
                        "Answer": "First, we want to factorise both denominators: 1/(7x^2 - 7x) + 6/(7x^2 + 14x) = 1/(7x(x-1)) + 6/(7x(x+2)).\nWe can multiply both the numerator and the denominator of the first expression by x+2, and multiply both the numerator and the denominator of the second expression by x-1. This way, they will have the common denominator 7x(x-1)(x+2).\nSo: 1/(7x(x-1)) + 6/(7x(x+2)) = (x+2)/(7x(x-1)(x+2)) + 6(x-1)/(7x(x-1)(x+2)).\nNow that the expressions have a common denominator, we can subtract them:(x+2)/(7x(x-1)(x+2)) + 6(x-1)/(7x(x-1)(x+2)) = (x+2 + 6x-6) / (7x(x-1)(x+2)) = (7x-4) / (7x(x-1)(x+2)).",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,
            }
        }
    ],
}