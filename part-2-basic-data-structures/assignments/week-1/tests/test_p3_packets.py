import pytest

from p3_packets import process_packets

EXAMPLE_DATA = [
    (
        (1, []),  # input
        [],  # output
    ),
    (
        (1, [
            (0, 0)
        ]),  # input
        [0],  # output
    ),
    (
        (1, [
            (0, 1),
            (0, 1),
        ]),  # input
        [0, -1],  # output
    ),
    (
        (1, [
            (0, 1),
            (1, 1),
        ]),  # input
        [0, 1],  # output
    ),
]


class TestSolution:
    """Test Problem 3 solution."""

    @pytest.mark.parametrize('input_,expected', EXAMPLE_DATA)
    def test_examples(self, input_, expected):
        """Test on example data from problem statement."""
        buff_size, packets = input_

        assert process_packets(packets, buff_size) == expected

    @pytest.mark.parametrize('count,buff_size', [
        (10, 1), (10, 10), (1000, 100), (2000, 1000), (10, 100)
    ])
    def test_all_same_time(self, count, buff_size):
        """
        Test case: many packets arriving at the same time.

        Each packet needs 10 ms to process.
        """
        processing_time = 10

        packets = ((1, processing_time) for _ in range(count))
        expected = [
            1 + i * processing_time for i in range(min(count, buff_size))
        ] + [-1 for i in range(count - buff_size)]

        assert process_packets(packets, buff_size) == expected

    @pytest.mark.parametrize('count,buff_size', [
        (10, 1), (10, 10), (10000, 100), (10, 100)
    ])
    def test_all_zero_processing(self, count, buff_size):
        """
        Test case: multiple packets with zero processing times.

        Packets arriving at 0, 0, 1, 1, ...
        """
        packets = [(i // 2, 0) for i in range(count)]
        expected = [i // 2 for i in range(count)]

        assert process_packets(packets, buff_size) == expected

    @pytest.mark.parametrize('count,buff_size', [
        (10, 1), (10, 10), (10000, 100), (10, 100)
    ])
    def test_all_successfull_sequent(self, count, buff_size):
        """Test case: new packet arrive after all previous was processed."""
        packets = [(i * 10, 5) for i in range(count)]
        expected = [i * 10 for i in range(count)]

        assert process_packets(packets, buff_size) == expected
