# coding: utf-8
import ST_pairwise_alignment


# Test for Global alignments

def test_global_alignment_success():
    seq1 = "MKTAYIAKQRQISFVKSHFSRQDILDLWIYHTQGYFPDWQNY"
    seq2 = "MKTAYIAKQRQISFVKSHFSRQDILDWIYHTQG"
    alignment = ST_pairwise_alignment.global_alignment(seq1, seq2)
    print("[test_global_alignment_success] Passed")
    print(alignment[0])
    print()


def test_global_alignment_failure():
    try:
        ST_pairwise_alignment.global_alignment("", "ABC")
    except Exception as e:
        print("[test_global_alignment_failure] Passed")
        print(f"Caught error: {e}")
    print()


# Local Alignment


def test_local_alignment_success():
    seq1 = "MKTAYIAKQRQISFVKSHFSRQDILDLWIYHTQGYFPDWQNY"
    seq2 = "QRQISFVKSHFSRQDILDWI"
    alignment = ST_pairwise_alignment.local_alignment(seq1, seq2)
    print("[test_local_alignment_success] Passed")
    print(alignment[0])
    print()


def test_local_alignment_failure():
    try:
        ST_pairwise_alignment.local_alignment(None, "ABC")
    except Exception as e:
        print("[test_local_alignment_failure] Passed")
        print(f"Caught error: {e}")
    print()


# Global Alignment with Penalty

def test_global_alignment_with_penalty_success():
    seq1 = "MKTAYIAKQRQISFVKSHFSRQDILDLWIYHTQGYFPDWQNY"
    seq2 = "MKTAYIAKQRQISFVKSHFSRQDILDWIYHTQG"
    alignment = ST_pairwise_alignment.global_alignment_with_penalty(seq1, seq2, -2, -0.5)
    print("[test_global_alignment_with_penalty_success] Passed")
    print(alignment[0])
    print()


def test_global_alignment_with_penalty_failure():
    try:
        ST_pairwise_alignment.global_alignment_with_penalty("AAA", "TTT", "not-a-number", -0.1)
    except Exception as e:
        print("[test_global_alignment_with_penalty_failure] Passed")
        print(f"Caught error: {e}")
    print()


# Local Alignment with Penalty

def test_local_alignment_with_penalty_success():
    seq1 = "MKTAYIAKQRQISFVKSHFSRQDILDLWIYHTQGYFPDWQNY"
    seq2 = "QRQISFVKSHFSRQDILDWI"
    alignment = ST_pairwise_alignment.local_alignment_with_penalty(seq1, seq2, -1, -0.2)
    print("[test_local_alignment_with_penalty_success] Passed")
    print(alignment[0])
    print()


def test_local_alignment_with_penalty_failure():
    try:
        ST_pairwise_alignment.local_alignment_with_penalty("AAA", "", -1, -0.1)
    except Exception as e:
        print("[test_local_alignment_with_penalty_failure] Passed")
        print(f"Caught error: {e}")
    print()


# Run All Tests

def run_all_tests():
    print("Running tests...\n")

    test_global_alignment_success()
    test_global_alignment_failure()

    test_local_alignment_success()
    test_local_alignment_failure()

    test_global_alignment_with_penalty_success()
    test_global_alignment_with_penalty_failure()

    test_local_alignment_with_penalty_success()
    test_local_alignment_with_penalty_failure()

    print("\nAll tests finished.")


if __name__ == "__main__":
    run_all_tests()
