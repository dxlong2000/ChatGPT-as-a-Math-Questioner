more_fewer = {
    "Definition": "Solve word problems comparing 2 numbers.  Numbers in the problems are less than 10.",
    "QA Queue": [
            {
                "Question": "The mass of the toy shark is 4 kilograms less than a red fox. The mass of the toy shark is 1 kilogram. What is the mass of the red fox?",
                "Answer": "4 + 1 = 5 kilograms",
                "Type": "Narrative",
                "Difficulty": 1
            }
        ],
    "Rate": 1,
    }

add_sub = {
    "Definition": "Solve addition and subtraction word problems.",
    "QA Queue": [
            {
                "Question": "Wilma jumped 7 meters. Ari jumped 5 meters. How much farther did Wilma jump than Ari?",
                "Answer": "7 - 5 = 2 meters",
                "Type": "Narrative",
                "Difficulty": 1
            }
        ],
    "Rate": 1,
    }

add_sub_2 = {
    "Definition": "Solve addition and subtraction word problems.",
    "QA Queue": [
            {
                "Question": "A T-Rex made 16 waffles for his friends for breakfast. 5 were blueberry waffles and the rest were chocolate chip waffles. How many chocolate chip waffles did he make?",
                "Answer": "16 - 5 = 11 waffles",
                "Type": "Narrative",
                "Difficulty": 1
            }
        ],
    "Rate": 1,
    }

length_size = {
    "Definition": "Order by length, Indirect measurement",
    "QA Queue": [
            {
                "Question": "My pencil is longer than my pen. My pen is longer than my marker. Which is shortest?",
                "Answer": "My marker",
                "Type": "Narrative",
                "Difficulty": 1
            }
        ],
    "Rate": 1,
    }  

FIRST_GRADE = {
    "Addition and subtraction": [
        {
            "Word problems with 'more' and 'fewer'": more_fewer
        },
        {
            "Addition and subtraction word problems 1": add_sub
        },
        {
            "Addition and subtraction word problems 2": add_sub_2
        },
        # {
        #     "Regrouping whole number place values": regrouping
        # }
    ],
    "Measurement, data, and geometry": [
        {
            "Length and size": length_size
        }        
    ]
}