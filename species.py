import sys
import pykemon

def makeSpecies(name):
    p = pykemon.get(pokemon=name)
    s = 'species.addLast(new PokemonSpecies('
    
    args = ['"%s"' % p.name, p.hp, p.attack, p.defense, p.sp_atk, p.sp_def, p.speed]
    args += ['Type.' + t.upper() for t in p.types] + ['Move.GENERIC']
    s += ', '.join(map(str, args))
    
    s += '));'
    print s

for name in sys.argv[1:]:
    makeSpecies(name)