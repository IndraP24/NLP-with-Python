# %% Download wordnet thesaurus from nltk
from nltk.corpus import wordnet as wn
import nltk
nltk.download('wordnet')


# %% Synonym sets containing "good"
poses = {'n': 'noun', 'v': 'verb', 's': 'adj (s)', 'a': 'adj', 'r': 'adv'}
for synset in wn.synsets("good"):
    print("{}: {}".format(poses[synset.pos()],
                          ", ".join([l.name() for l in synset.lemmas()])))

# Output:

# noun: good
# noun: good, goodness
# noun: good, goodness
# noun: commodity, trade_good, good
# adj: good
# adj (s): full, good
# adj: good
# adj (s): estimable, good, honorable, respectable
# adj (s): beneficial, good
# adj (s): good
# adj (s): good, just, upright
# adj (s): adept, expert, good, practiced, proficient, skillful, skilful
# adj (s): good
# adj (s): dear, good, near
# adj (s): dependable, good, safe, secure
# adj (s): good, right, ripe
# adj (s): good, well
# adj (s): effective, good, in_effect, in_force
# adj (s): good
# adj (s): good, serious
# adj (s): good, sound
# adj (s): good, salutary
# adj (s): good, honest
# adj (s): good, undecomposed, unspoiled, unspoilt
# adj (s): good
# adv: well, good
# adv: thoroughly, soundly, good

# %% Hypernyms of "panda"

panda = wn.synset("panda.n.01")
def hyper(s): return s.hypernyms()


list(panda.closure(hyper))

# Output:

# [Synset('procyonid.n.01'),
#  Synset('carnivore.n.01'),
#  Synset('placental.n.01'),
#  Synset('mammal.n.01'),
#  Synset('vertebrate.n.01'),
#  Synset('chordate.n.01'),
#  Synset('animal.n.01'),
#  Synset('organism.n.01'),
#  Synset('living_thing.n.01'),
#  Synset('whole.n.02'),
#  Synset('object.n.01'),
#  Synset('physical_entity.n.01'),
#  Synset('entity.n.01')]

# %%
