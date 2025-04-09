# coding: utf-8
from Bio import SeqIO
import ST_pairwise_alignment


def main():
    # Read seq1, seq2
    sequence1 = SeqIO.read("seq1.txt", "fasta").seq
    sequence2 = SeqIO.read("seq2.txt", "fasta").seq
    print("---------------Part1---------------")

    print("[Global Alignment]")
    alignment = ST_pairwise_alignment.global_alignment(sequence1, sequence2)
    print(alignment[0])
    print(f"\tScore: {alignment.score}\n")

    print("[Local Alignment]")
    alignment = ST_pairwise_alignment.local_alignment(sequence1, sequence2)
    print(alignment[0])
    print(f"\tScore: {alignment.score}\n")

    print("\n---------------Part2---------------")
    print("[Global Alignment with penalty]")
    extended_penalty = -5
    open_gap_penalty = -0.5
    alignment = ST_pairwise_alignment.global_alignment_with_penalty(sequence1, sequence2, extended_penalty,
                                                                    open_gap_penalty)
    print(f"\tScore: {alignment.score}")

    print("[Local Alignment with penalty]")
    alignment = ST_pairwise_alignment.local_alignment_with_penalty(sequence1, sequence2, extended_penalty,
                                                                   open_gap_penalty)
    print(f"\tScore: {alignment.score}")

    extended_penalty = -1
    open_gap_penalty = -0.1
    print("[Global Alignment with penalty]")
    alignment = ST_pairwise_alignment.global_alignment_with_penalty(sequence1, sequence2, extended_penalty,
                                                                    open_gap_penalty)
    print(f"\tScore: {alignment.score}")

    print("[Local Alignment with penalty]")
    alignment = ST_pairwise_alignment.local_alignment_with_penalty(sequence1, sequence2, extended_penalty,
                                                                   open_gap_penalty)
    print(f"\tScore: {alignment.score}")

    extended_penalty = -0.1
    open_gap_penalty = -0.01
    print("[Global Alignment with penalty]")
    alignment = ST_pairwise_alignment.global_alignment_with_penalty(sequence1, sequence2, extended_penalty,
                                                                    open_gap_penalty)
    print(f"\tScore: {alignment.score}")

    print("[Local Alignment with penalty]")
    alignment = ST_pairwise_alignment.local_alignment_with_penalty(sequence1, sequence2, extended_penalty,
                                                                   open_gap_penalty)
    print(f"\tScore: {alignment.score}")


if __name__ == "__main__":
    main()
else:
    print("<module name> : Is intended to be executed and not imported.")
