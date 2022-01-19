# pip install --user -U nltk
# python -m nltk.downloader popular
from nltk.corpus import words
import argparse

#<-- Previous Wordle answers (500 days)
wordle_answers = ["rebut", "sissy", "humph", "awake", "blush", "focal", "evade", "naval", "serve", "heath", "dwarf", "model", "karma", "stink", "grade", "quiet", "bench", "abate", "feign", "major", "death", "fresh", "crust", "stool", "colon", "abase", "marry", "react", "batty", "pride", "floss", "helix", "croak", "staff", "paper", "unfed", "whelp", "trawl", "outdo", "adobe", "crazy", "sower", "repay", "digit", "crate", "cluck", "spike", "mimic", "pound", "maxim", "linen", "unmet", "flesh", "booby", "forth", "first", "stand", "belly", "ivory", "seedy", "print", "yearn", "drain", "bribe", "stout", "panel", "crass", "flume", "offal", "agree", "error", "swirl", "argue", "bleed", "delta", "flick", "totem", "wooer", "front", "shrub", "parry", "biome", "lapel", "start", "greet", "goner", "golem", "lusty", "loopy", "round", "audit", "lying", "gamma", "labor", "islet", "civic", "forge", "corny", "moult", "basic", "salad", "agate", "spicy", "spray", "essay", "fjord", "spend", "kebab", "guild", "aback", "motor", "alone", "hatch", "hyper", "thumb", "dowry", "ought", "belch", "dutch", "pilot", "tweed", "comet", "jaunt", "enema", "steed", "abyss", "growl", "fling", "dozen", "boozy", "erode", "world", "gouge", "click", "briar", "great", "altar", "pulpy", "blurt", "coast", "duchy", "groin", "fixer", "group", "rogue", "badly", "smart", "pithy", "gaudy", "chill", "heron", "vodka", "finer", "surer", "radio", "rouge", "perch", "retch", "wrote", "clock", "tilde", "store", "prove", "bring", "solve", "cheat", "grime", "exult", "usher", "epoch", "triad", "break", "rhino", "viral", "conic", "masse", "sonic", "vital", "trace", "using", "peach", "champ", "baton", "brake", "pluck", "craze", "gripe", "weary", "picky", "acute", "ferry", "aside", "tapir", "troll", "unify", "rebus", "boost", "truss", "siege", "tiger", "banal", "slump", "crank", "gorge", "query", "drink", "favor", "abbey", "tangy", "panic", "solar", "shire", "proxy", "point", "robot", "prick", "wince", "crimp", "knoll", "sugar", "whack", "mount", "perky", "could", "wrung", "light", "those", "moist", "shard", "pleat", "aloft", "skill", "elder", "frame", "humor", "pause", "ulcer", "ultra", "robin", "cynic", "agora", "aroma", "caulk", "shake", "pupal", "dodge", "swill", "tacit", "other", "thorn", "trove", "bloke", "vivid", "spill", "chant", "choke", "rupee", "nasty", "mourn", "ahead", "brine", "cloth", "hoard", "sweet", "month", "lapse", "watch", "today", "focus", "smelt", "tease", "cater", "movie", "lynch", "saute", "allow", "renew", "their", "slosh", "purge", "chest", "depot", "epoxy", "nymph", "found", "shall", "harry", "stove", "lowly", "snout", "trope", "fewer", "shawl", "natal", "fibre", "comma", "foray", "scare", "stair", "black", "squad", "royal", "chunk", "mince", "slave", "shame", "cheek", "ample", "flair", "foyer", "cargo", "oxide", "plant", "olive", "inert", "askew", "heist", "shown", "zesty", "hasty", "trash", "fella", "larva", "forgo", "story", "hairy", "train", "homer", "badge", "midst", "canny", "fetus", "butch", "farce", "slung", "tipsy", "metal", "yield", "delve", "being", "scour", "glass", "gamer", "scrap", "money", "hinge", "album", "vouch", "asset", "tiara", "crept", "bayou", "atoll", "manor", "creak", "showy", "phase", "froth", "depth", "gloom", "flood", "trait", "girth", "piety", "payer", "goose", "float", "donor", "atone", "primo", "apron", "blown", "cacao", "loser", "input", "gloat", "awful", "brink", "smite", "beady", "rusty", "retro", "droll", "gawky", "hutch", "pinto", "gaily", "egret", "lilac", "sever", "field", "fluff", "hydro", "flack", "agape", "wench", "voice", "stead", "stalk", "berth", "madam", "night", "bland", "liver", "wedge", "augur", "roomy", "wacky", "flock", "angry", "bobby", "trite", "aphid", "tryst", "midge", "power", "elope", "cinch", "motto", "stomp", "upset", "bluff", "cramp", "quart", "coyly", "youth", "rhyme", "buggy", "alien", "smear", "unfit", "patty", "cling", "glean", "label", "hunky", "khaki", "poker", "gruel", "twice", "twang", "shrug", "treat", "unlit", "waste", "merit", "woven", "octal", "needy", "clown", "widow", "irony", "ruder", "gauze", "chief", "onset", "prize", "fungi", "charm", "gully", "inter", "whoop", "taunt", "leery", "class", "theme", "lofty", "tibia", "booze", "alpha", "thyme", "eclat", "doubt", "parer", "chute", "stick", "trice", "alike", "sooth", "recap", "saint", "liege", "glory", "grate", "admit", "brisk", "soggy", "usurp", "scald", "scorn", "leave", "twine", "sting", "bough", "marsh", "sloth", "dandy", "vigor", "howdy", "enjoy"]
#-->

word_list = words.words()

parser = argparse.ArgumentParser(description="Print list of words with certain conditions.")
parser.add_argument("-l", "--length", type=int, help="word length (defaults to 5)")
parser.add_argument("-gn", "--green", type=str, help="known letters in known positions (use _ for no letter)")
parser.add_argument("-y", "--yellow", type=str, help="known letters in unknown positions")
parser.add_argument("-gy", "--grey", type=str, help="letters not in word (if letter also exists in yellow then limit the amount of that letter in word to amount in yellow)")
parser.add_argument("-e", "--exclude", type=str, nargs="+", help="like green but inverse (accepts more than one string)")
parser.add_argument("-w", "--wordle", action="store_true", help="only show valid answers from previous wordle answers")

args = parser.parse_args()

length = args.length if args.length else 5
grey = set(args.grey) if args.grey else []
green = args.green if args.green else "_" * length
yellow = args.yellow + "".join([c for c in green if c.isalpha() and c not in args.yellow]) if args.yellow else "".join([c for c in green if c.isalpha()])
exclude = args.exclude if args.exclude else []
show_valid_wordle_answers = args.wordle

if len(green) != length: exit("Error: Length of green != length of word")
if any([len(e) != length for e in exclude]): exit("Error: Length of exclude != length of word")

def _filter(word):
    # Check grey
    for char in grey:
        if char in set(yellow): continue
        if char in word: return False
    # Check green
    for i in range(length):
        if green[i].isalpha() and green[i] != word[i]: return False
    # Check yellow
    for char in set(yellow):
        if char in grey and word.count(char) > yellow.count(char): return False
        if word.count(char) < yellow.count(char): return False
    # Check exclude
    for e in exclude:
        for i in range(length):
            if e[i].isalpha() and e[i] == word[i]: return False

    return True


if show_valid_wordle_answers:
    valid_wordle_answers = list(filter(_filter, wordle_answers))
    print(valid_wordle_answers, end="\n\n")
    print("There are {} possible words for these conditions".format(len(valid_wordle_answers)))
else:
    valid_words = list(filter(_filter, [word for word in word_list if len(word) == length]))
    print(valid_words, end="\n\n")
    print("There are {} possible words for these conditions".format(len(valid_words)))



