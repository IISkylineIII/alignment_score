def alignment_score(seq1, seq2, match_score, mismatch_penalty, indel_penalty):
    score = 0
    for char1, char2 in zip(seq1, seq2):
        if char1 == char2:
            score += match_score
        elif char1 == '-' or char2 == '-':
            score -= indel_penalty
        else:
            score -= mismatch_penalty
    return score

seq1 = "TCGAC--ATT"
seq2 = "CC---GAA-T"
match_score = 1
mismatch_penalty = 1
indel_penalty = 2

alignment_score = alignment_score(seq1, seq2, match_score, mismatch_penalty, indel_penalty)
print("Score do alinhamento:", alignment_score)
