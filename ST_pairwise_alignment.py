# coding: utf-8
from aligner_factory import get_global_aligner, get_local_aligner


def global_alignment(sequence1, sequence2):
    try:
        if not sequence1 or not sequence2:
            raise ValueError("Sequences must not be empty.")
        global_aligner = get_global_aligner()
        global_alignments = global_aligner.align(sequence1, sequence2)
        return global_alignments
    except Exception as e:
        raise RuntimeError(f"Global alignment failed: {e}")


def local_alignment(sequence1, sequence2):
    try:
        if not sequence1 or not sequence2:
            raise ValueError("Sequences must not be empty.")
        local_aligner = get_local_aligner()
        local_alignments = local_aligner.align(sequence1, sequence2)
        return local_alignments
    except Exception as e:
        raise RuntimeError(f"Local alignment failed: {e}")


def global_alignment_with_penalty(sequence1, sequence2, extended_gap_score, open_gap_score):
    try:
        if not sequence1 or not sequence2:
            raise ValueError("Sequences must not be empty.")
        global_aligner = get_global_aligner()
        global_aligner.extend_gap_score = float(extended_gap_score)
        global_aligner.open_gap_score = float(open_gap_score)
        global_alignments = global_aligner.align(sequence1, sequence2)
        # Echo inputs: gap penalty
        print(f"\tExtended gap penalty: {extended_gap_score}")
        print(f"\tOpen gap penalty: {open_gap_score}")
        return global_alignments
    except Exception as e:
        raise RuntimeError(f"Global alignment with penalty failed: {e}")


def local_alignment_with_penalty(sequence1, sequence2, extended_gap_score, open_gap_score):
    try:
        if not sequence1 or not sequence2:
            raise ValueError("Sequences must not be empty.")
        local_aligner = get_local_aligner()
        local_aligner.extend_gap_score = float(extended_gap_score)
        local_aligner.open_gap_score = float(open_gap_score)
        local_alignments = local_aligner.align(sequence1, sequence2)
        print(f"\tExtended gap penalty: {extended_gap_score}")
        print(f"\tOpen gap penalty: {open_gap_score}")
        return local_alignments
    except Exception as e:
        raise RuntimeError(f"Local alignment with penalty failed: {e}")


if __name__ == "__main__":
    print("<module name> : Is intended to be imported and not executed.")
