dialogues = {
        "start": {
            "lines": ["You take a deep breath.",
                      ">> Hello? Can you hear me?<<",
                      "The rumbling continues...",
                      ">>Hey! Over here!<<",
                      ">>What do you want?<<"
            ],
            "options": {
                "1": (">>Who are you?<<", "answer_one"),
                "2": (">>Where are we?<<", "answer_two")
        }
        },
        "answer_one": {
            "lines": [
                ">>Urgh... WHO I am? More like WHAT I am.<<",
                ">>So much pain...<<",
                ">>So much horror...<<",
                ">>HELP ME!!!<<"
            ],
            "options": {
                "1": (">>Where are we?<<", "answer_two")
            }
        },
        "answer_two": {
            "lines": [
                ">>In hell...<<",
                ">>Is she... Is she still gone?<<"
            ],
            "options": {
                "1": (">>Who is SHE?<<", "answer_three"),
                "2": (">>There's just us. I guess...<<", "answer_four")
            }
        },
        "answer_three": {
            "lines": [
                ">>Our Mother? What kind of question is that?<<",
                ">>She is the one who feeds us.<<",
                ">>Who carresses us.<<",
                ">>Who punishes us.<<",
                "*Quiet sobing*",
                ">>I don't want her to come back...<<"
            ],
            "options": {
                "1": (">>There's just us. I guess...<<", "answer_four")
            }
        },
        "answer_four": {
            "lines": [
                ">>Good... that is very good. We must rest.<<",
                ">>Before she comes back.<<"
            ],
            "options": {
                "1": (">>How can we get out of here?", "answer_five")
            }
        },
        "answer_five": {
            "lines": [
                ">>We can't. We're bound to this place.<<",
                ">>Forever<<",
                ">>And now, let me rest. Before she comes back.<<"
            ]
        }
    }