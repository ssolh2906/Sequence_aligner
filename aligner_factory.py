from Bio.Align import PairwiseAligner, substitution_matrices


def get_global_aligner():
    """
    Returns a global aligner using BLOSUM62.
    """
    try:
        global_aligner = PairwiseAligner()
        global_aligner.mode = "global"
        global_aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
        return global_aligner
    except Exception as e:
        raise RuntimeError(f"Failed to create global aligner: {e}")


def get_local_aligner():
    """
    Returns a local aligner using BLOSUM62.
    """
    try:
        local_aligner = PairwiseAligner()
        local_aligner.mode = "local"
        local_aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
        return local_aligner
    except Exception as e:
        raise RuntimeError(f"Failed to create local aligner: {e}")
