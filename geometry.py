geometry_part_1 = {
    "Performing transformations": [
        {
            "Introduction to rigid transformations": {
            "Definition": "A rigid transformation is a type of geometric transformation that doesn't change the size or shape of the object being transformed. Translations, rotations, and reflections are all rigid transformations.\n For any transformation, we have the pre-image figure, which is the figure we are performing the transformation upon, and the image figure, which is the result of the transformation.\n For any transformation, we have the pre-image figure, which is the figure we are performing the transformation upon, and the image figure, which is the result of the transformation.",
            "QA Queue": [
                    {
                        "Question": "What single transformation was applied to quadrilateral A to get quadrilateral B?\nBEGIN PLOT:\nDraw(Quadrilateral A, connects A_1 (1, 1), A_2 (1, 2), A_3 (3, 3), A_4 (4, 1))\nDraw(Quadrilateral B, connects B_1 (7, 1), B_2 (7, 2), B_3 (9, 3), B_4 (10, 1)).\nEND PLOT.",
                        "Answer": "We see that, we can obtain point B_1 from point A_1 by moving A_1 six units to the right.\nThe same could be applied to pairs of points (A_2, B_2), (A_3, B_3), (A_4, B_4).\nSo quadrilateral B could be obtained from quadrilateral A by a single translation of 6 units to the right.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Translation": {
            "Definition": "Translations only move things from one place to another; they don't change their size, arrangement, or direction. A translation by (a,b) is a transformation that moves all points a units in the x-direction and b units in the y-direction. Such a transformation is commonly represented as T_(a,b).\nProperty 1: Line segments are taken to line segments of the same length.\nProperty 2: Angles are taken to angles of the same measure.\nProperty 3: Lines are taken to lines, and parallel lines are taken to parallel lines.",
            "QA Queue": [
                    {
                        "Question": "Quadrilateral A'B'C'D' is the image of quadrilateral ABCD under a translation.\nBEGIN PLOT:\nDraw(`A`, (6, 2))\nDraw(`B`, (5, 1))\nDraw(`C`, (-4, -5))\nDraw(`D`, (3, 6))\nDraw(`A'`, (5, -1))\nDraw(`B'`, (4, -2))\nDraw(`C'`, (-7, -6))\nDraw(`D'`, (2, 3))\nEND PLOT.\nDetermine the translation.",
                        "Answer": "Point A' could be obtained from point A by moving A 1 unit to the left and 3 units down.\nThat means the translation from A into A' is (-1, -3).\nTherefore, the translation from quadrilateral ABCD into the quadrilateral A'B'C'D' is (-1, -3).",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,
            }
        },
        {
            "Rotations": {
            "Definition": "In geometry, rotations make things turn in a cycle around a definite center point. Every rotation is defined by two important parameters: the center of the rotation—we already went over that—and the angle of the rotation. The angle determines by how much we rotate the plane about the center.",
            "QA Queue": [
                    {
                        "Question": "Quadrilateral A'B'C'D' is the image of quadrilateral ABCD under a rotation about the origin (0,0).\BEGIN PLOT:\nDraw(`A`, (-2, 3))\nDraw(`B`, (-3, 4))\nDraw(`C`, (-6, 2))\nDraw(`D`, (-4, 0))\nDraw(`A'`, (-3, -2))\nDraw(`B'`, (-4, -3))\nDraw(`C'`, (-2, -6))\nDraw(`D'`, (0, -4))\nEND PLOT.\nDetermine the angle of rotation.",
                        "Answer": "Point A' can be obtained from point A by rotating point A about the origin (0, 0) at an angle of 90 degrees counter-clockwise.\nSo the angle of rotation is 90 degrees.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Reflections":{
            "Definition": "A reflection is a transformation that acts like a mirror: It swaps all pairs of points that are on exactly opposite sides of the line of reflection. The line of reflection can be defined by an equation or by two points it passes through.",
            "QA Queue": [
                    {
                        "Question": "Draw the line of reflection that reflects quadrilateral ABCD onto quadrilateral A'B'C'D'.\nBEGIN PLOT:\nDraw(`A`, (-1, 0))\nDraw(`B`, (-2, -2))\nDraw(`C`, (-4, -1))\nDraw(`D`, (-6, 1))\nDraw(`A'`, (3, -2))\nDraw(`B'`, (2, -4))\nDraw(`C'`, (4, -5))\nDraw(`D'`, (6.8, -5.4))\nEND PLOT.",
                        "Answer": "Here, note that AB and A'B' are parallel, so the reflection line is also parallel with AB and A'B'.\nWe can take the midpoint of line AA' and the midpoint of line BB', then connect them together to get the line of reflection.\nBEGIN PLOT:\nDraw(`A''`, midpoint of AA')\nDraw(`B''`, midpoint of BB')\nDraw(Line connects A'' and B'')\nEND PLOT.'",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Dilations":{
            "Definition": "First, we need to remember what dilation is: a geometric transformation that changes the size of an object without changing its shape.\nThe center of dilation, then, is the point from which the object is being scaled.\nTo find the center of dilation, we'll need to look at two corresponding points from the original object (the pre-image) and the new object (the image). We'll label the points A and B for the pre-image and A' and B' for the image. To find the center of dilation, we'll draw two lines: one from A to A' and one from B to B'. The point where the two lines intersect is the center of dilation.",
            "QA Queue": [
                    {
                        "Question": "Draw the image of triangle ABC under a dilation whose center is P and scale factor is 1/2.\BEGIN PLOT:\nDraw(`A`, (1, 2))\nDraw(`B`, (5, -2))\nDraw(`C`, (-7, 0))\nDraw(`P`, (-7, 10)).\nEND PLOT.",
                        "Answer": "To draw the image of triangle ABC under the dilation with center P and scale factor 1/2, we need to take the midpoints of AP, BP and CP.\nThe midpoint of AP is A'(-3, 6).\nThe midpoint of BP is B'(-1, 4).\nThe midpoint of CP is C'(-7, 5).\nBEGIN PLOT:\nDraw(`A'`, (-3, 6))\nDraw(`B'`, (-1, 4))\nDraw(`C'`, (-7, 5)).\nEND PLOT.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        }
    ],
    "Transformation properties and proofs":[
        {
            "Rigid transformation overview":{
            "Definition": "When we can transform one figure onto another using only rigid transformations, the two figures are congruent.\nRigid transformations preserve length, so we can use the measurements in a congruent figure to help us calculate the perimeter or area of another figure.\nRigid transformations preserve angle measure. The properties of angle measures on transversals will help us make sense of why translations and dilations take lines to parallel lines, but rotations and reflections usually don't.",
            "QA Queue": [
                    {
                        "Question": "Triangle ABC is reflected across line n to create triangle A'B'C'.\nGiven \angle ABC = 67 \degree, AC = 61, \angle B'A'C' = 59 \degree, B'C' = 57.\nWhat is the measure of \angle ACB?",
                        "Answer": "By the property of reflection, we know that \angle BAC = \angle B'A'C' = 59 \degree.\nAlso, since the sum of 3 angles in a triangle is 180 \degree, we have: \angle ABC + \angle ACB + \angle BAC = 180 \degree.\nBy substituting \angle ABC = 67 \degree and \angle BAC = 59 \degree, we obtain: \angle ACB = 180 \degree - 67 \degree - 59 \degree = 54 \degree.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Dilations preserve angle measures":{
            "Definition": "Dilation preserves angles and preserves directions of lines.",
            "QA Queue": [
                    {
                        "Question": "Quadrilateral A'B'C'D' is the result of dilating quadrilateral ABCD about point D by a scale factor of 3/2.\nHow many of the following statements are true:\n1. Lines AC and A'C' are parallel.\n2. Lines DB and D'B' are paralled.\n3. \angle BAD is not equal to \angle B'A'D'.",
                        "Answer": "Since dilation preserves angles, point 3 is correct.\nDilation also maps a line to a line with the same direction to it. However, line DB goes through the dilation center, D, so it remains the same line. That means point 1 is true and point 2 is false.\nIn conclusion, points 1 and 3 are true.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Properties & definitions of transformations":{
            "Definition": "Besides other familiar transformations, we provide the exact definition of rotation here: A rotation by \theta degrees about point P moves any point A counterclockwise to a point B such that both A and B are on the same circle centered at P, and \angle APB = \theta.",
            "QA Queue": [
                    {
                        "Question": "A sequence of transformations is described below.\nA rotation about a point P.\nA translation\nA reflection over a line QR.\nAnother translation.\nWhich of the following: angle measures or segment lengths, remain the same after the sequence?",
                        "Answer": "Since the sequence of transformations contains only rigid transformations, all the angle measures and segment lengths remain the same.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Proof with transformations":{
            "Definition": "We often use rigid transformations and dilations in geometric proofs because they preserve certain properties. Rigid transformations—such as translations, rotations, and reflections—preserve the lengths of segments, the measures of angles, and the areas of shapes. Dilations, on the other hand, change the size of a shape, but they preserve the measures of angles, the proportions, and relationships between different parts of the shape.\nCertain transformations preserve even more properties. For example, when we translate or dilate a figure, figures that were parallel before the transformation are still parallel after it. So, when we use rigid transformations and dilations in geometric proofs, we can be confident that certain properties will remain the same even when the shapes are moved or resized.",
            "QA Queue": [
                    {
                        "Question": "FG and HI are parallel lines. \angle IFG=60 \degree.\nAlfred was asked to find the measure of angle x and explain his reasoning.\nBEGIN PLOT:\nDraw(Line FG)\nDraw(Line IJ)\nDraw(Line FI)\nLabel(\angle IFG, 60 \degree)\nDraw(Point K such that I is between K and F).\Label(\angle KIJ, x \degree)\nEND PLOT.",
                        "Answer": " Based on the given information and the plot, we have parallel lines FG and HI. Additionally, we know that angle IFG measures 60 degrees. We need to find the measure of angle x (angle KIJ) and explain our reasoning.\nSince FG and HI are parallel lines, we can conclude that angle IFG and angle KIJ are corresponding angles. Corresponding angles are equal when two parallel lines are intersected by a transversal.\nTherefore, we can say that angle KIJ (denoted as x) is equal to angle IFG, which is given as 60 degrees. Hence, the measure of angle x is 60 degrees.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,   
            }
        },
    ],
    "Congruence": [
        {
            "Transformations & congruence":{
            "Definition": "Two shapes are congruent if they have the same size and shape. When we use rigid transformations (translations, rotations, and reflections) to move a shape, it keeps the same size and shape. So if there is a series of rigid transformations that show that one shape matches up with another shape, the figures are congruent. If they cannot match up, the figures are not congruent.",
            "QA Queue": [
                    {
                        "Question": "Segments AB and CD coincide. Vinay concluded: 'Segments AB and CD have no angles with the same measurement, so they are not congruent.'\nWhat error did Vinay make in his conclusion?",
                        "Answer": "Segments AB and CD are still congruent since there exists a series of transformations that maps AB onto CD. For example, the series contains one transformation: Translation by 0 unit.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Congruent triangles":{
            "Definition": "There are three main criteria for triangle congruence. If two triangles meet any one of these three criteria, they are considered congruent.\nSide-Side-Side (SSS) criterion: Two triangles are congruent if all three of their corresponding side lengths are equal.\nSide-Angle-Side (SAS) criterion: Two triangles are congruent if two of their corresponding side lengths and the angle between those sides are equal.\nAngle-Angle-Side (AAS) criterion: Two triangles are congruent if two of their corresponding angles and the side between those angles are equal.",
            "QA Queue": [
                    {
                        "Question": "Given triangles ABC and DEF.\nWe assume that AB = DE, \angle A = \angle D, \angle B = \angle E. Prove that 2 triangles are congruent.",
                        "Answer": "Following the Angle-Angle-Side (AAS) criterion, with the angles being: \angle A = \angle D and \angle B = \angle E, and the sides being: AB = DE, we can conclude that triangle ABC is congruent to triangle DEF.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Theorems concerning triangle properties":{
            "Definition": "There are three very useful theorems that connect equality and congruence.\nTwo angles are congruent if and only if they have equal measures.\nTwo segments are congruent if and only if they have equal measures.\nTwo triangles are congruent if and only if all corresponding angles and sides are congruent.",
            "QA Queue": [
                    {
                        "Question": "Joe tried to prove that the sum of a triangle's interior angle measures is 180 degrees. Please help him.",
                        "Answer": "Let's start with a generic triangle ABC and denote its interior angles as angle A, angle B, and angle C.\n1. Draw a straight line segment DE parallel to side BC from point A (with A lies between D and E).\nNow, we have two parallel lines DE and BC. According to the property of parallel lines, the corresponding angles are congruent.\nAngle A is congruent to angle BAC.\nAngle B is congruent to angle CAD.\nAngle C is congruent to angle BAE.\nNow, we have: \angle A + \angle B + \angle C = \angle BAC + \angle BAE + \angle CAD = 180 \degree.\nSo we have proved that the sum of angles in triangle ABC is 180 \degree.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Working with triangles":{
            "Definition": "There are three main criteria for triangle congruence. If two triangles meet any one of these three criteria, they are considered congruent.\nSide-Side-Side (SSS) criterion: Two triangles are congruent if all three of their corresponding side lengths are equal.\nSide-Angle-Side (SAS) criterion: Two triangles are congruent if two of their corresponding side lengths and the angle between those sides are equal.\nAngle-Angle-Side (AAS) criterion: Two triangles are congruent if two of their corresponding angles and the side between those angles are equal.",
            "QA Queue": [
                    {
                        "Question": "",
                        "Answer": "Since AC and BD are parallel, we have \angle ACB = \angle CBD.\nSo in order to find x, we will find \angle ACB instead.\nWe have the sum of angles of triangle ABC is 180 \degree, so: \angle ACB + \angle ABC + \angle BAC = 180 \degree.\nSubstituting \angle ABC = 43 \degree, \angle BAC = 69 \degree, we get: \angle ACB = 180 \degree - 43 \degree - 69 \degree = 68 \degree.\nSo, we obtain x = 68.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Theorems concerning quadrilateral properties":{
            "Definition": "The triangle congruence criteria can help us break down other figures into triangles, which can be easier to work with. For example, we might divide a quadrilateral into two triangles, determine whether the two triangles are congruent, and then use that information to infer something about the quadrilateral.",
            "QA Queue": [
                    {
                        "Question": "Alessandra wants to prove that if quadrilateral ABCD has one pair of congruent and parallel opposite sides, call them AB and CD, then it is a parallelogram.\nAlessandra says: 'I can prove this by establishing the congruence of a single pair of triangles.'\nWhich pair of triangles is Alessandra referring to, and which criterion should she use for establishing congruence?",
                        "Answer": "Alessandra is referring to the pair of triangles ABD and CDA. She wants to establish the congruence of these triangles in order to prove that quadrilateral ABCD is a parallelogram.\nTo establish the congruence of triangles ABD and CDA, Alessandra should use the Side-Angle-Side (SAS) congruence criterion. Specifically:\nSide AB is congruent to side CD.\nSide AD is congruent to side DA.\nAngle ADB is congruent to angle CDA (given that AB is parallel to CD, angle ADB and angle CDA are alternate interior angles).\nBy establishing the congruence of triangles ABD and CDA using the SAS criterion, Alessandra can conclude that quadrilateral ABCD is a parallelogram.",
                        "Type": "Narrative",
                        "Difficulty": 5
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
            "Proofs of general theorems":{
            "Definition": "The triangle congruence criteria help us compare and work with other figures in several ways. They can allow us to determine whether two triangles are congruent, which can be helpful when we want to determine whether two other figures are also congruent.",
            "QA Queue": [
                    {
                        "Question": "Let ABCD be a square.\nF is the midpoint of AD and G is the midpoint of BC.\nWe draw an arc AC that is a part of the circle with center B, and this arc intersects FG at E.\nCalculate \angle BED.",
                        "Answer": "Since E is in the circle with center B, we have BE = BA = BC. Since FG is the perpendicular bisector of BC, we have EB = EC. Since EB = EC = BC, the triangle EBC is an equilateral triangle. So \angle BEC = 60 \degree.\nSince \angle BED = \angle BEC + \angle CED, now we only need to find angle CED.\nSince \angle BCE is also 60 \degree, and \angle ECD is complementary with \angle BCE, we have \angle ECD = 90 \degree - 60 \degree = 30 \degree.\nWe have ECD is an isosceles triangle, so \angle CED = (180 - 30) / 2 \degree = 75 \degree.\nIn total, \angle BED = 60 \degree + 75 \degree = 135 \degree.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Constructing lines and angles":{
            "Definition": "We can do a lot of geometry constructions using only ruler and compass, e.g constructing a parallel line, constructing a perpendicular line, ...",
            "QA Queue": [
                    {
                        "Question": "Jenny wants to construct an equilateral triangle, and Luke wants to help her. However, Luke also does not know how to do it. Please help Luke!",
                        "Answer": "Luke can simply draw a circle with center A.\nThen he can pick a point B on the circle and draw another circle with center B and the same radius.\nLet an intersection of 2 circles be C.\nThen ABC will be an equilateral triangle, since BA = BC and AC = AB.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,   
            }
        }
    ]
}

geometry_part_2 = {
    "Similarity": [
        {
            "Definitions of similarity":{
            "Definition": "A relationship between two quantities is proportional if the ratio between those quantities is always equivalent. We will look at side length ratios to find out whether triangles are similar or not.",
            "QA Queue": [
                    {
                        "Question": "Timo was curious if quadrilaterals LMNR and PQNO were similar, so he tried to map one figure onto the other using a rotation and a dilation. Timo concluded: 'It's not possible to map LMNR onto PQNO using a sequence of rigid transformations and dilations, so the quadrilaterals are not similar.'\nWhat error did Timo make in his conclusion?",
                        "Answer": "There is no error in the conclusion. If two quadrilaterals are similar, then a rotation with center N that aligns M, N, Q, as well as M, R, O, and a dilation with center N after that, will map two quadrilaterals onto each other. But here Timo cannot map them after a rotation and a dilation, so two quadrilaterals are not similar.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Introduction to triangle similarity":{
            "Definition": "Triangle similarity criteria:\nAA: Two pairs of corresponding angles are equal.\nSSS: Three pairs of corresponding sides are proportional.\nSAS: Two pairs of corresponding sides are proportional and the corresponding angles between them are equal.",
            "QA Queue": [
                    {
                        "Question": "Is triangle LJK similar to triangle ABC?\BEGIN PLOT:\nDraw(Triangle ABC)\nLabel(\angle A, 54\degree)\nLabel(\angle B, 58 \degree)\nDraw(Triangle LJK)\nLabel(\angle J, 54 \degree)\nLabel(\angle L, 68 \degree)\nEND PLOT.",
                        "Answer": "Since in a triangle, three interior angles have sum equal to 180 \degree, we have: \angle L + \angle J + \angle K = 180 \degree.\nWe already know \angle J = 54 \degree and \angle L = 68 \degree, so: \angle K = 180 \degree - 54 \degree - 68 \degree = 58 \degree.\nSince \angle A = \angle J = 54 \degree and \angle B = \angle K = 58 \degree, we conclude that the two triangles are similar by the AA criterion.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Solving similar triangles":{
            "Definition": "When we draw an altitude to the hypotenuse of a right triangle, it creates two smaller right triangles. Interestingly, these two smaller right triangles are both similar to the original right triangle and to each other.\nThis happens because the altitude divides the hypotenuse into two segments, but also creates two new right angles. The two new right angles, along with the two segments, give us two right triangles that share the same proportions as the original right triangle.\nThis self-similarity is useful in geometry, as it allows us to use properties of similar triangles to solve problems. For example, if we know the length of the hypotenuse and one leg of the original right triangle, we can use this self-similarity to find the lengths of the two segments created by the altitude.",
            "QA Queue": [
                    {
                        "Question": "Solve for x in the following figure:\nDraw(Triangle ABC, with \angle B = 90 \degree)\nDraw(D on AB such that B is between A and D)\nLabel(Length AB, 10)\nLabel(Length BD, 10)\nDraw(E on AC such that DE is perpendicular to AD)\nLabel(Length BC, 6)\nLabel(Length DE, x)\nEND PLOT.",
                        "Answer": "To solve for x, first we notice that triangles ABC and ADE both have the same angle A and also both have a right angle, so by the AA criterion, they are similar.\nThis means we have the following proportion: AB/AD = BC/DE.\nNote that AB = 10, AD = AB + BD = 10 + 10 = 20, BC = 6 and DE = x.\nBy substituting in, we have: 10/20 = 6/x.\nSo x = 6 * 20 / 10 = 12.\nThe answer is x = 12.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Angle bisector theorem":{
            "Definition": "The angle bisector theorem states that: In a triangle ABC, AD being the bisector for angle BAC (D on BC), then: AB / AC = BD / DC.",
            "QA Queue": [
                    {
                        "Question": "In the following figure, \angle DAC = \angle BAD.\nWhat is the length of BD?\nBEGIN PLOT:\nDraw(triangle ABC)\nDraw(D on BC such that \angle DAC = \angle BAD)\nLabel(Length AB, 6.8)\nLabel(Length AC, 4.6)\nLabel(Length CD, 2.5)\nEND PLOT.",
                        "Answer": "Following the angle bisector theorem, since AD is a bisector for angle BAC, we have: AB / AC = BD / DC.\nBy substituting the known quantities, we obtain: BD = DC * AB / AC = 2.5 * 6.8 / 4.6 \approx 3.67.\nSo BD is approximately 3.67.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Solving problems with similar & congruent triangles":{
            "Definition": "One thing we can prove using triangle similarity is the Pythagorean theorem. For example, consider a right triangle with sides a, b, and c, where c is the hypotenuse. Divide the triangle into two smaller, similar right triangles by drawing a perpendicular from the right angle to the hypotenuse.\nBecause the triangles are similar, we can write ratios of corresponding side lengths, which ultimately simplifies to a^2 + b^2 = c^2, the Pythagorean theorem!\nWe can use triangle similarity to show that the three medians of a triangle intersect at a single point. We can use triangle similarity to prove that the three altitudes of a triangle also intersect at a single point.\nAnother interesting property we can derive from triangle similarity is that when two chords (line segments with both endpoints on a circle) intersect, the product of the two segments on one chord is equal to the product of the two segments on the other chord.\nThere are many more properties we can prove using triangle similarity, and these are just a few examples.",
            "QA Queue": [
                    {
                        "Question": "Find x in the following figure:\nBEGIN PLOT:\nDraw(Right triangle ABE at B)\nDraw(F on BE, F is between B and E)\nDraw(C on AE such that CF is perpendicular to BE)\nDraw(D on BC such that DE is perpendicular to BE)\nLabel(Length AB, 9)\nLabel(Length DE, 12)\nLabel(Length CF, x)\nEND PLOT.",
                        "Answer": "Since triangles EFC and EBA are similar (AA criterion), we have: CF / AB = EF / EB, or x / 9 = EF / EB.\nSince triangles BFC and BED are similar (AA criterion), we have: CF / DE = BF / BE, or x / 12 =  BF / BE.\nSumming up two equations, we have: x / 9 + x / 12 = EF / EB + BF / BE = (EF + BF) / BE = EB / EB = 1.\nSo: x(1/9 + 1/12) = 1, hence x = 1/(1/9 + 1/12) = 36/7 \approx 5.14.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Proving relationships using similarity":{
            "Definition": "One thing we can prove using triangle similarity is the Pythagorean theorem. For example, consider a right triangle with sides a, b, and c, where c is the hypotenuse. Divide the triangle into two smaller, similar right triangles by drawing a perpendicular from the right angle to the hypotenuse.\nBecause the triangles are similar, we can write ratios of corresponding side lengths, which ultimately simplifies to a^2 + b^2 = c^2, the Pythagorean theorem!\nWe can use triangle similarity to show that the three medians of a triangle intersect at a single point. We can use triangle similarity to prove that the three altitudes of a triangle also intersect at a single point.\nAnother interesting property we can derive from triangle similarity is that when two chords (line segments with both endpoints on a circle) intersect, the product of the two segments on one chord is equal to the product of the two segments on the other chord.\nThere are many more properties we can prove using triangle similarity, and these are just a few examples.",
            "QA Queue": [
                    {
                        "Question": "In triangle LMN, O is the midpoint of LM, and P is the midpoint of LN. Prove that OP is parallel to MN.",
                        "Answer": "Two triangles LMN and LOP have the same angle L. Also, we have the proportion: LM / LO = LN / LP = 2. By the SAS criterion, we conclude that triangles LMN and LOP are similar.\nThis means that \angle LMN = \angle LOP.\nAs \angle LMN and \angle LOP are corresponding angles, we see that MN is parallel to OP.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Solving modeling problems with similar & congruent triangles":{
            "Definition": "There are many properties we can prove using triangle similarity.",
            "QA Queue": [
                    {
                        "Question": "A pool table is 1m by 2m. There are 6 pockets total: 4 in the corners and 2 at the midpoints of each 2m side. A cue ball is placed 0.25m from the north wall and 0.25m away from the west wall. The angles formed as the ball approaches and deflects form a mirror image of each other.\nAt what distance x from the southeast corner should the cue ball hit the east wall, so the cue ball sinks into the pocket at the midpoint of the south wall?",
                        "Answer": "We can model the problem as the following figure:\nBEGIN PLOT:\nDraw(Rectangle ABCD)\nLable(AB, 'South')\nLabel(BC, 'East')\nLabel(CD, 'North')\nLabel(DA, 'West')\nDraw(E in rectangle ABCD, E is 0.25 from North and 0.25 from West)\nDraw(S, midpoint of AB)\nDraw(F on BC such that, \angle EFC = \angle SFB)\nLabel(Length FB, x)\nEND PLOT.\nWe need to calculate x.\nLet G be the point on BC such that EG is perpendicular to BC.\nSince \angle EFG = \angle SFB and \angle EGF = \angle SBF = 90 \degree, we have triangles SFB and EFG are similar.\nNote that GC is equal to the distance from E to North, which is 0.25, so FG = BC - GC - FB = 1 - 0.25 - x = 0.75 - x.\nAlso note that EG = CD - distance from E to West = 2 - 0.25 = 1.75.\nLast but not least, SB = AB / 2 = 1.\nWe have the proportion: EG / GF = SB / BF, so: 1.75 / (0.75 - x) = 1 / x, which is equivalent to: 1.75x = 0.75 - x, or: x = 0.75 / 2.75 = 3 / 11.\nSo we conclude that x = 3 / 11 and the cue ball should hit the east wall 3/11 m from the southeast corner.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,   
            }
        }
    ],
    "Right triangles & trigonometry": [
        {
            "Pythagorean theorem":{
            "Definition": "The Pythagorean theorem is a^2 + b^2 = c^2, where a and b are lengths of the legs of a right triangle and c is the length of the hypotenuse.",
            "QA Queue": [
                    {
                        "Question": "The Museu Blau in Barcelona, Spain, is a natural science museum built in the shape of a triangular prism. The base of the building is an equilateral triangle 180 meters on each side. The height of the prism is 25m.\nFind the height h of the triangular base.",
                        "Answer": "BEGIN PLOT:\nDraw(Equilateral triangle ABC)\nDraw(AH perpendicular to BC, H on BC)\nLabel(Length AH, h)\nEND PLOT.\nWe need to find AH. By the Pythagorean theorem, we have: AH^2 + HB^2 = AB^2, but HB = BC/2 = 90 and AB = 180, hence: AH^2 = 180^2 - 90^2 = 24300.\nSo AH = \sqrt(24300) \approx 155.88.\nSo the height of the triangular base is approximately 155.88m",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Special right triangles":{
            "Definition": "30-60-90 triangles are right triangles whose acute angles are 30 \degree and 60 \degree.\n45-45-90 triangles are right triangles whose acute angles are both 45 \degree. This makes them isosceles triangles.",
            "QA Queue": [
                    {
                        "Question": "In the right triangle shown, \angle Q = 60 \degree and QR = 2\sqrt(3).\BEGIN PLOT:\nDraw(Right triangle PRQ at R)\nLabel(\angle Q, 60 \degree)\nLabel(Length RQ, 2\sqrt(3)\nLabel(Length PQ, x)\nEND PLOT.\nWhat is the value of x?",
                        "Answer": "To find x, we need to find the length of PQ.\nSince PQR is a 30-60-90 triangle, the proportion between RQ and PQ is: RQ / PQ = 1/2.\nSo PQ = 2 * 2\sqrt(3) = 4\sqrt(3).\nSo x = 4\sqrt(3).",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Ratios in right triangles":{
            "Definition": "The hypotenuse of a right triangle is always the side opposite the right angle.\nThe opposite side is across from a given angle.\nThe adjacent side is the non-hypotenuse side that is next to a given angle.\nIf two right triangles have an acute angle measure in common, they are similar by angle-angle similarity. The ratios of corresponding side lengths within the triangles will be equal. So the ratio of the side lengths of a right triangle just depends on one acute angle measure.",
            "QA Queue": [
                    {
                        "Question": "Approximate \angle Q in the triangle below.\BEGIN PLOT:\nDraw(Right triangle RPQ at P)\nLabel(Length PQ, 2.5)\nLabel(Length RQ, 4.4)\nEND PLOT.",
                        "Answer": "Since RPQ is a right triangle, we have: cos(\angle Q) = PQ / RQ = 2.5 / 4.4 \approx 0.57.\nThat means \angle Q is about 55 \degree.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Sine & cosine of complementary angles":{
            "Definition": "If \alpha and \beta are complementary angles, then: sin(\alpha) = cos(\beta).",
            "QA Queue": [
                    {
                        "Question": "Malia tried to prove that cos(\theta) = sin(90 \degree - \theta).\nHow can you help her with it?",
                        "Answer": "Let ABC be a right triangle with \angle B = \theta.\nThen \angle C = 90 \degree - \theta.\nWe need to prove that cos(\angle B) = sin(\angle C), but it is equivalent to: BA / BC = BA / BC.\nSo we have completed the proof.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Modeling with right triangles":{
            "Definition": "When you see an object above you, there's an angle of elevation between the horizontal and your line of sight to the object.\nSimilarly, when you see an object below you, there's an angle of depression between the horizontal and your line of sight to the object.",
            "QA Queue": [
                    {
                        "Question": "The image below is a model of Aya, point A, looking up to Super Girl, point S, in the sky.\BEGIN PLOT:\nDraw(Rectangle AESH, AE is parallel to Ox and S is higher than AE)\nLabel(\angle SAE, 1)\nLabel(\angle SAH, 2)\nLabel(\angle ASE, 3)\nLabel(\angle ASH, 4).\nEND PLOT.\nWhat is the angle of elevation from Aya to Super Girl?",
                        "Answer": "The angle of elevation from Aya to Super Girl is angle 1.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,   
            }
        }
    ]
}

geometry_part_3 = {
    "Analytic geometry": [
        {
            "Distance and midpoints":{
            "Definition": "The distance between the points (x_1, y_1) and (x_2, y_2) is given by the following formula: \sqrt((x_2-x_1)^2 + (y_2-y_1)^2). The midpoint of the points (x_1, y_1) and (x_2, y_2) is given by the following formula: ((x_1 + x_2)/2, (y_1 + y_2)/2).",
            "QA Queue": [
                    {
                        "Question": "Point A is located at (-2, -7) and point M is located at (2.5, -1.5). Point M is the midpoint between point A and an unknown point B. We need to find the coordinates of point B.",
                        "Answer": "Using the midpoint formula, we have: x_A + x_B = 2 * x_M, so x_B = 2 * 2.5 - (-2) = 7.\nWe also have: y_A + y_B = 2 * y_M, so y_B = 2 * (-1.5) - (-7) = 4.\nIn conclusion, the coordinates of B are (7, 4).",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Dividing line segments":{
            "Definition": "There are a few ways to divide a line segment into two segments with a certain ratio of lengths. One way is to apply the given ratio to both the horizontal and vertical displacements between the points.",
            "QA Queue": [
                    {
                        "Question": "Point A is located at (1, 5) and point C is located at (-5, -7).\nFind the coordinates of point B on line AC such that the length of AC is 6 times the length of AB.",
                        "Answer": "We can apply the given ratio (AC = 6 AB) to both the horizontal and vertical displacements between the points. We have:\nx_C - x_A = 6(x_B - x_A) and y_C - y_A = 6(y_B - y_A).\nSubstituting the coordinates, we obtain: x_B = (x_C - x_A + 6x_A) / 6 = (-5 - 1 + 6) / 6 = 0 and y_B = (y_C - y_A + 6y_A) / 6 = (-7 - 5 + 30) / 6 = 3.\nIn conclusion, we have B(0, 3).",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Problem solving with distance on the coordinate plane":{
            "Definition": "By calculating distances on the coordinate, we can find areas or determining if a point is inside/outside/on a circle, and many other applications.",
            "QA Queue": [
                    {
                        "Question": "A circle with center P(0, 0) and passing through the point W(-6, \sqrt(37)) is given. Determine where the point Z(8, 3) lies in relation to the circle.",
                        "Answer": "The distance between W and P is: \sqrt((-6-0)^2 + (\sqrt(37) - 0)^2) = \sqrt(36 + 37) = \sqrt(73).\nThe distance between Z and P is: \sqrt((8-0)^2 + (3-0)^2) = \sqrt(64 + 9) = \sqrt(73).\nSince both W and Z have the same distance from P, the point Z lies on the circumference of the circle.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Parallel & perpendicular lines on the coordinate plane":{
            "Definition": "Parallel lines are two lines that will never intersect. They have the same slope. Perpendicular lines, on the other hand, intersect at a 90-degree angle. Their slopes are opposite reciprocals of each other. For example, if one line has the slope 2/3, the perpendicular line will have the slope -3/2.",
            "QA Queue": [
                    {
                        "Question": "One line passes through the points (-8, 1) and (4, 4). Another line passes through the points (-9, -7) and (9, -3).\nAre the lines parallel, perpendicular, or neither?",
                        "Answer": "The slope of the first line is: (4 - 1) / (4 - (-8)) = 3 / 12 = 1/4.\nThe slop of the second line is: (-3 - (-7)) / (9 - (-9)) = 4 / 18.\nThe slopes are neither equal nor opposite reciprocals of each other.\nSo the lines are neither parallel nor perpendicular.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Equations of parallel & perpendicular lines":{
            "Definition": "To find the equation of a parallel line, we'll use the same slope as the original line, but a different y-intercept. If we know a point (x1, y1) through which the parallel line passes, we can substitute the coordinates into the point-slope formula, where m represents the slope of the line\n(y - y1) = m(x - x1).\nTo find the equation of a perpendicular line, we'll use the opposite reciprocal slope, and then use the point-slope formula to find the y-intercept.",
            "QA Queue": [
                    {
                        "Question": "What do the following two equations represent?\n6x - 15y = 15\ny = (2/5)x - 1",
                        "Answer": "The first equation could be rewritten as: y = (2/5)x - 1.\nThe equations of two lines are the same, so it means that two lines are coincide.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        }
    ],
    "Conic sections": [
        {
            "Standard equation of a circle":{
            "Definition": "The standard equation of a circle is: (x - h)^2 + (y - k)^2 = r^2.",
            "QA Queue": [
                    {
                        "Question": "The equation of a circle is given below.\n(x - 5.2)^2 + (y + 3.7)^2 = 49.\nWhat is its center?\nWhat is its radius?",
                        "Answer": "The center of the circle is (5.2, -3.7).\nThe radius of the circle is \sqrt(49) = 7.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Expanded equation of a circle":{
            "Definition": "Circles can also be given in expanded form, which is simply the result of expanding the binomial squares in the standard form and combining like terms.",
            "QA Queue": [
                    {
                        "Question": "Graph the circle: x^2 + y^2 + 16x - 16y + 124 = 0.",
                        "Answer": "We can rewrite the circle formula into standard form: x^2 + y^2 + 16x -16y + 124 = (x^2 + 16x + 64) + (y^2 - 16y + 64) - 4 = (x+4)^2 + (y-4)^2 - 4.\nSo the new circle formula is: (x+8)^2 + (y-8)^2 = 4.\nThis means that the circle has center (-8, 8) and radius \sqrt(4) = 2.\BEGIN PLOT:\nDraw(Point A, (-8, 8))\nDraw(Circle with center A, radius 2)\nEND PLOT.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Focus and directrix of a parabola":{
            "Definition": "A parabola can be graphed as the set of all points that are equidistant from a fixed point (the 'focus') and a fixed line (the 'directrix').",
            "QA Queue": [
                    {
                        "Question": "What is the equation of the parabola with a focus at (-7, -5) and a directrix at x = -4?",
                        "Answer": "Let P be a point on the parabola, then its distance from (-7, -5) is: \sqrt((x_P + 7)^2 + (y_P + 5)^2).\nThe distance from P to the directrix at x = -4 is: abs(x_P - (-4)) = abs(x_P + 4) = \sqrt((x_P+4)^2).\nFor the two distances to be the same, we need: (x_P + 7)^2 + (y_P + 5)^2 = (x_P+4)^2.\nThe equation for the parabola is then: x^2 + 14x + 49 + (y + 5)^2 = x^2 + 8 x + 16, which is equivalent to: 6 x + 33 + (y + 5)^2 = 0.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        }
    ],
    "Circles": [
        {
            "Circle basics":{
            "Definition": "What's the area of a semicircle (a half circle)? It's half the area of the full circle. What's the arc length of 1/3 of a circle? It's 1/3 of the circumference of the full circle. In high school geometry, we'll generalize from these common fractions to be able to find the arc length and area for parts of circles given the radius and any central angle measure.",
            "QA Queue": [
                    {
                        "Question": "Find the arc length of the partial circle AB.\nBEGIN PLOT:\nDraw(Point O, (0, 0))\nDraw(Point A, (2, 0))\nDraw(Point B, (0, 2))\nDraw(arc AB, in circle center O)\nEND PLOT.",
                        "Answer": "The partial circle AB is one-fourth of a circle with radius 2.\nSo the arc length is 1/4 the perimeter of a circle with radius 2.\nIn conclusion, the arc length is: 1/4 * 2\pi * 2 = \pi.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Arc measure":{
            "Definition": "Arc length is the distance along a curved line, like on the edge of a circle.\nOn a circle, we need to know the central angle of the arc (\theta) and the radius of the circle (r) to find arc length. If \theta is in degrees:\narc length = \theta / 360 \degree * 2 \pi r.",
            "QA Queue": [
                    {
                        "Question": "What is the arc measure, in degrees, of major arc ADC on circle P below?\BEGIN PLOT:\nDraw(Circle with center P)\nDraw(A, B, C, D clockwise on circle P)\nLabel(\angle APB, 70 \degree)\nLabel(\angle BPC, 104 \degree)\nEND PLOT.",
                        "Answer": "We can first calculate the arc measure of small arc ABC, then subtract it from 360 degrees to get the arc measure for ADC.\nThe central angle of arc ABC is: \angle APB + \angle BPC = 70 \degree + 104 \degree = 174 \degree.\nHence, the central angle of major arc ADC is: 360 \degree - 174 \degree = 186 \degree.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Sector":{
            "Definition": "A sector is a part of a circle, defined by two radii (the plural of radius) and the arc between them. Think of it as 'pie slice' of the circle.",
            "QA Queue": [
                    {
                        "Question": "A sector with an area of 26\pi cm has a radius of 6cm. What is the central angle measure of the sector in radians?",
                        "Answer": "The total central angle of the whole circle is 2\pi.\nThe area of the whole circle is \pi * 6^2 = 36 \pi.\nWe have the following proportion: central angle / whole angle = area of sector / area of whole, which leads to: central angle = 2\pi * 26\pi / 36\pi = 13/9 \pi.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Inscribed angle":{
            "Definition": "An inscribed angle is an angle that has its vertex on the circumference of a circle.",
            "QA Queue": [
                    {
                        "Question": "In the figure below, \angle ABC is inscribed in circle P. The length of PC is 12 units. The arc length of arc AC is 68/15\pi.\BEGIN PLOT:\nDraw(Circle with center P)\nDraw(Small arc AC on circle P)\nLabel(Length of arc AC, 68/15 \pi)\nLabel(Length PC, 12)\nEND PLOT.\nWhat is the measure of \angle ABC in degrees?",
                        "Answer": "The radius of the circle is 12 units, so the perimeter of the circle is: 24 \pi.\nSo the central angle of arc AC is: 360 * 68/15 \pi / (24\pi) = 68 \degree.\nSince the inscribed angle is half the central angle, we conclude that \angle ABC = 68 / 2 = 34 \degree.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Inscribed shapes problem solving":{
            "Definition": "An inscribed shape is a shape that is drawn inside a circle such that all of its vertices are touching the circumference of the circle.",
            "QA Queue": [
                    {
                        "Question": "In the figure below, quadrilateral ABCD is inscribed in circle P. The radius of circle P is 5 units.\BEGIN PLOT:\nDraw(Circle center P)\nDraw(Points A, B, C, D clockwise on circle P)\nLabel(\angle BCD, 9/20 \pi)\nEND PLOT.\nWhat is the length of arc BCD?",
                        "Answer": "The central angle BPD is: 2 * \angle BCD = 9/10 \pi.\nSo the length of arc BAD is: 9/10 \pi / (2\pi) * perimeter, with perimeter = 2\pi * 5 = 10 \pi.\nSo the length of arc BAD is: 9/2 pi.\nTo calculate the length of arc BCD, we subtract the length of arc BAD from the perimeter, which is: 10 \pi - 9/2 \pi = 11/2 \pi.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Properties of tangents":{
            "Definition": "A tangent line is a line that touches a circle at just one point. A secant line is a line that cuts through a circle at two points.",
            "QA Queue": [
                    {
                        "Question": "All sides of triangle ABC are tangent to circle P.\nBEGIN PLOT:\nDraw(Triangle ABC)\nDraw(Circle center P, tangent with all 3 sides of triangle ABC)\nDraw(Point F, intersection of circle P with AB)\nLabel(Length BF, 16)\nLabel(Length AC, 14)\nEND PLOT.\nWhat is the perimeter of triangle ABC?",
                        "Answer": "Let D be the intersection of circle P with BC, E be the intersection of circle P with AC.\nSince AE and AF are both tangent to circle P, we have AE = AF.\nSimilarly, we also obtain: BD = BF, CD = CE.\nSo the perimeter of triangle ABC is: AB + AC + BC = (AF + FB) + AC + (BD + DC) = (AF + CD) + AC + BF + BD = (AE + CE) + AC + BF + BF = 2AC + 2BF = 2 * 14 + 2 * 16 = 60.\nSo the perimeter of triangle ABC is 60.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Constructing regular polygons inscribed in circles":{
            "Definition": "Using ruler and compass, we can construct many beautiful geometric figures!",
            "QA Queue": [
                    {
                        "Question": "Construct a regular hexagon inscribed inside the circle.",
                        "Answer": "First, we pick a random point A on the circle.\nThen, we draw a circle with center A and has the same radius as the original circle.\nThis circle cuts the original circle at B and F.\nContinuing drawing another circle with center B and cuts the original circle at point C (besides point A).\nContinue this process with point C to obtain point D, and do it again with point D to get point E.\nWe see that, by connecting ABCDEF, we get a regular hexagon!",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,   
            }
        }
    ]
}

geometry_part_4 = {
    "Solid geometry": [
        {
            "2D vs. 3D objects":{
            "Definition": "A prism is a pair of congruent polygons in parallel planes and the collection of all the points between them. A right prism has its top face directly above its bottom face. The translation vector is perpendicular to the bases. An oblique prism has a non-perpendicular translation vector.\nA pyramid is a polygon, a vertex in a different plane, and the collection of all the points between them. A right pyramid has its apex directly above the center of the base. An oblique pyramid has its apex anywhere else.\nA polyhedron is a solid figure where every surface is a polygon. Prisms and pyramids are examples of polyhedra.\nA sphere is a solid figure where every point on the surface is the same distance from its center.\nThe intersection of a plane and a solid is a cross-section. So every cross-section is 2D figure that we could get by slicing through a 3D figure.",
            "QA Queue": [
                    {
                        "Question": "Consider a square of side length 5, and a line m that contains a side of the square as a subsegment.\nWhat solid 3D object is produced by rotating the square about line m?",
                        "Answer": "By rotating the square about line m, we will create a cylinder with radius 5 units and height 5 units.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Cavalieri's principle and dissection methods":{
            "Definition": "Cavalieri's principle in 2D: If two figures have the same height and the same width at every point along that height, they have the same area.\nCavalieri's principle in 3D: If two 3D figures have the same height and the same cross-sectional area at every point along that height, they have the same volume.\nThe formula for the volume V of a pyramid is V = 1/3 * (base area) * (height).",
            "QA Queue": [
                    {
                        "Question": "A square-based pyramid has a base area of 30 square units and a volume of 96 cubic units. A cone has the same base area and height as the pyramid.\nWhat is the volume of the cone?",
                        "Answer": "Since the cone has the same base area and height as the pyramid, by Cavalieri's principle, the volume of the cone is the same as the volume of the pyramid.\nSo the volume of the cone is 96 cubic units.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Volume and surface area":{
            "Definition": "Prisms and prism-like figures: Volume = (base area) * (height).\nRectangular prisms: Volume = ((rectangle base) * (rectangle height)) * (prism height).\nTriangular prisms: Volume = (1/2 * (triangle base) * (triangle height)) * (prism height).\nCylinders: Volume = (\pi * (radius^2)) * (height).\nPyramids and pyramid-like figures: Volume = 1/3 * (base area) * (height).\nRectangle-based pyramids: Volume = 1/3 * ((rectangle base) * (rectangle height)) * (pyramid height).\nCones: Volume = 1/3 * (\pi * (radius^2)) * (height).\nSphere: Volume = 4/3 * \pi * (radius^3)",
            "QA Queue": [
                    {
                        "Question": "A company makes spherical tanks that store chemicals. Their standard model has a diameter of 6 meters, but a customer needs a larger tank whose capacity is 2.5 times the volume of the standard model.\nWhat is the approximate diameter of this larger tank? Round to the nearest tenth.",
                        "Answer": "If the diameter multiplies by x times, then the volume of the tank would multiply by x^3 times.\nSo in order to multiply the capacity by 2.5 times, we need to multiply the diameter by the cube root of 2.5.\nSo tehe approximate diameter of the larger tank is: 6 * \sqrt{3}{2.5} \approx 8.1 meter.",
                        "Type": "Narrative",
                        "Difficulty": 4
                    }
                ],
            "Rate": 1,   
            }
        },
        {
            "Density":{
            "Definition": "Density is a measure of how compact a material is. It is defined as the mass of the material divided by its volume. In solid geometry, we can use density to compare different materials and determine which one is heavier or lighter for a given volume.",
            "QA Queue": [
                    {
                        "Question": "Keenan wants to make a paperweight at pottery class. He designs a pyramid-like model with a base area of 80 square centimeters and a height of 7.5 centimeters. The density of the clay he is using is 1.7 grams per cubic centimeter.\nWhat is the weight of Keenan's paperweight?",
                        "Answer": "The volume of the paperweight is: 1/3 * 80 * 7.5 = 200 cubit centimeters.\nHence the weight of the paper weight is: 1.7 * 200 = 340 grams.",
                        "Type": "Narrative",
                        "Difficulty": 5
                    }
                ],
            "Rate": 1,   
            }
        }
    ]
}