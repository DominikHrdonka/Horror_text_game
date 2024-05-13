import time
class Dialogue:

    def __init__(self, content) -> None:
        self.content = content

    def play_dialogue(self, dialogue_key) -> None:
        while dialogue_key:
            dialogue = self.content[dialogue_key]
            for line in dialogue["lines"]:
                print(line)
                time.sleep(2)

            next_dialogue_key = None
            if "options" in dialogue:
                while True:
                    print("------------------")
                    for option_key, (option_text, _) in dialogue["options"].items():
                        print(f"{option_key}. {option_text}")
                    print("------------------")
                    choice = input("Choose an option: ")
                    if choice in dialogue["options"]:
                        next_dialogue_key = dialogue["options"].get(choice)[1]
                        break
                    else:
                        print("Invalid dialogue choice")
                    
            dialogue_key = next_dialogue_key

creature = Dialogue(
    content={
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
        },
        "code_answer": {
            "lines": [
                ">>That door has a keypad. Any chance you know the code?<<",
                ">>What for? We can't run away, can we?<<",
                ">>Well, why not? We can call help and get out of this madness!<<",
                ">>She'll find you, no matter where you go.<<"
            ],
            "options": {
                "1": (">>Tell me what you know<<", "code_answer_one"),
                "2": (">>You'll regret it if you don't tell me!<<", "c e_answer_two")
            }
        },
        "code_answer_one":{
            "lines": [
                ">>I might know the code. I can distinguish the sound of the individual keys. I've been here for a long time, you know.<<",
                ">>Well?<<",
                ">>It's either 472, or 571.<<",
                ">>Thank you! I will get us out of here.<<",
                ">>I highly doubt that.<<"
            ]
        },
        "code_answer_two":{
            "lines": [
                ">>Threats mean nothing in here. You will learn soon...<<"
            ],
            "option": {
                "1": (">>Tell me what you know<<", "code_answer_one"),
            }
        }
    }
)

crone = Dialogue(
    content={
        "start": {
            "lines": [
                ">>There's no way to get out, you filth!<<",
                "A horrible underground voice shatters the moment of stillness.\nThe crone stands in front of you, even more horrific in the full-moon light."
            ],
            "options": {
                "1": ("Leave me alone!", "answer_one"),
                "2": ("What are you?", "answer_two")
            }
        },
        "answer_one": {
            "lines": [
                ">>Silence!<<",
                ">>You belong to me.<<",
                ">>You turned yourself in.<<",
                ">>Now, you will pay the debt.<<",
                "The roar deafening, shattering your skull from within."
            ]
        },
        "answer_two": {
            "lines": [
                ">>Your judge.<<",
                ">>Your executioner.<<",
                ">>Get on your knees, worm! You are not worthy.<<"
            ],
            "options": {
                "1": ("What are you talking about?", "answer_three"),
                "2": ("You will never get me!", "answer_three")
            }
        },
        "answer_three": {
            "lines": [
                ">> Earthling filth!<<",
                ">>Your heart will adorn the gate of my Kingdom<<",
                ">>But make no mistake. With your sacrifice, the others got only a little bit more time.<<",
                ">>Their time will come as well.<<",
                "Suddenly, there is a vision entering the corner of your eyes.",
                """A group of people in a circle on a dark night. All of them holding hands, chanting.
Flames burning in the middle. You stand next to the crackling fire,
your arms raised high above.
Ecstatic, the voices intertwine and swirl around the trees.""",
                ">>It is time, Joel<<",
                """A woman says and lays her hand on your shoulder.
You look at her sad face. Tears are rolling down her cheek.""",
                ">>We will never be able to repay you.<<",
                "You inhale the heavy air.",
                ">>Just take care of her.<<",
                "And then, you throw yourself into the flames.",
                "Darkness and nothing more…"
            ],
            "options": {
                "1": ("Maria…", "answer_four")
            }
        },
        "answer_four": {
            "lines": [
                ">>Oh don't worry, you piece of dying meat. <<",
                "The crone's voice gets you back into the presence.",
                ">>I will rip her throat as well.<<"
            ]
        }
    }
)
