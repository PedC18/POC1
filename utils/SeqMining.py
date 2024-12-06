from prefixspan import PrefixSpan
from utils.Points import RallyExtraction,RallyParsing
from pymining import itemmining, seqmining
import re

StrokesDictionary = {
    '0' : 'Serve',
    '4' : 'Wide Serve',
    '5' : 'Body Serve',
    '6' : 'Down The T Serve',
    'f' : 'Forehand',
    'b' : 'Backhand',
    'r' : 'FH Slice',
    's' : 'BH Slice',
    'v' : 'FH Volley',
    'z' : 'BH Volley',
    '1' : ' Cruzado',
    '2' : ' Meio',
    '3' : ' Paralelo',
    '*' : 'Winner',
    '@' : 'Forced Error',
    '#' : 'Unforced Error',
    'o' :'standard overhead/smash',
    'p' :'backhand overhead/smash',
    'u' :'forehand drop shot',
    'y' :'backhand drop shot',
    'l' :'forehand lob',
    'm' :'backhand lob',
    'h' :'forehand half-volley',
    'i' :'backhand half-volley',
    'j' :'forehand swinging volley',
    'k' :'backhand swinging volley',
    'n' : 'net',
    'w' : 'wide' ,
    'd' : 'deep',
    'x' : 'both wide and deep',
    'g' : 'foot faults',
    't' : 'trick shot',
    'q' : 'unknown',
    'e' : 'any'
}

def GetStrokes():
    return StrokesDictionary


def Sequencer(Points):
    Rally = RallyExtraction(Points)

    data = [RallyParsing(d,StrokesDictionary) for d in Rally]

    Sequences = []
    Endings = []
    for seq, end in data:
        Sequences.append(seq)
        Endings.append(end)
    
    return Sequences, Endings

# Initialize the PrefixSpan algorithm
def CallPrefixSpan(Sequences, min_support, k = 0):
    ps = PrefixSpan(Sequences)

    # Find frequent subsequences
    frequent_patterns = ps.frequent(min_support)
    filtered_pattern = [(sup,seq) for sup, seq in frequent_patterns if len(seq) >= k]


    return filtered_pattern

def SortPatterns(patterns):
    sorted_values = sorted(patterns, key=lambda x : x[0],reverse=True)

    return sorted_values

def check_list_contained(A, B):
  # convert list A to string
    A_str = ' '.join(map(str, A))
    # convert list B to string
    B_str = ' '.join(map(str, B))
    # find all instances of A within B
    instances = re.findall(A_str, B_str)
 
    # return True if any instances were found, False otherwise
    return len(instances) > 0


# Non-contiguos sequence mining
def Seqmining(Sequences, k ):
    freq_seqs = seqmining.freq_seq_enum(Sequences, min_support=100)

    k = 4
    # Exibir resultados
    filtered_seq = [(seq,sup) for seq, sup in freq_seqs if len(seq) >= k]

    sorted_values = sorted(filtered_seq, key=lambda x : x[1],reverse=True)

    return sorted_values[:10]