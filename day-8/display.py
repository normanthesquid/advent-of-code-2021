from enum import Enum


class digit_segment_counts(Enum):
    one = 2
    four = 4
    seven = 3
    eight = 7
    two_three_five = 5
    zero_six_nine = 6


class display:
    def __init__(self, definition: str):
        self.signal_map = {
            "a": "a",
            "b": "b",
            "c": "c",
            "d": "d",
            "e": "e",
            "f": "f",
            "g": "g",
        }

        self.translated_outputs = []

        self.numeric_output = None

        signal_pattern_string, output_value_string = definition.split(" | ")

        self.signal_patterns = signal_pattern_string.rstrip().split()

        self.output_values = output_value_string.rstrip().split()

        self.decode()

    def decode(self):
        one = next(
            filter(
                lambda signal: len(signal) == digit_segment_counts.one.value,
                self.signal_patterns,
            )
        )

        four = next(
            filter(
                lambda signal: len(signal) == digit_segment_counts.four.value,
                self.signal_patterns,
            )
        )
        seven = next(
            filter(
                lambda signal: len(signal) == digit_segment_counts.seven.value,
                self.signal_patterns,
            )
        )
        eight = next(
            filter(
                lambda signal: len(signal) == digit_segment_counts.eight.value,
                self.signal_patterns,
            )
        )

        # the a signal is present in SEVEN, but not in ONE
        self.signal_map["a"] = list((set(seven) - set(one)))[0]

        # SIX has 5 digits, but is missing the C from 1. ZERO and NINE have the c and f
        # Also, ONE only has 2 digits, so the one that isn't c must be f
        zero_six_nines = list(
            filter(
                lambda signal: len(signal) == digit_segment_counts.zero_six_nine.value,
                self.signal_patterns,
            )
        )
        six = next(
            filter(
                lambda signal: one[0] not in signal or one[1] not in signal,
                zero_six_nines,
            )
        )
        if one[0] not in six:
            self.signal_map["c"] = one[0]
            self.signal_map["f"] = one[1]
        elif one[1] not in six:
            self.signal_map["c"] = one[1]
            self.signal_map["f"] = one[0]
        else:
            raise Exception("i messed up the SIX logic")
        zero_six_nines.remove(six)

        # FIVE has 5 digits, but is missing the c. TWO and THREE have the c
        two_three_five = list(
            filter(
                lambda signal: len(signal) == digit_segment_counts.two_three_five.value,
                self.signal_patterns,
            )
        )
        five = next(
            filter(
                lambda signal: self.signal_map["c"] not in signal,
                two_three_five,
            )
        )
        two_three_five.remove(five)

        # SIX has e, but FIVE does not. They are identical otherwise
        self.signal_map["e"] = list((set(six) - set(five)))[0]

        # TWO has e, THREE has f, otherwise they are identical
        if self.signal_map["e"] in two_three_five[0]:
            two = two_three_five[0]
            three = two_three_five[1]
        elif self.signal_map["f"] in two_three_five[0]:
            two = two_three_five[1]
            three = two_three_five[0]
        else:
            raise Exception("i messed up the TW0/THREE logic")
        two_three_five.remove(two)
        two_three_five.remove(three)

        # ZERO has e, NINE has d, otherwise they are identical
        if self.signal_map["e"] in zero_six_nines[0]:
            zero = zero_six_nines[0]
            nine = zero_six_nines[1]
        elif self.signal_map["e"] in zero_six_nines[1]:
            zero = zero_six_nines[1]
            nine = zero_six_nines[0]
        else:
            raise Exception("i messed up the ZERO/NINE logic")
        zero_six_nines.remove(zero)
        zero_six_nines.remove(nine)

        self.signal_map["d"] = list((set(nine) - set(zero)))[0]

        # FOUR's last unknown signal is b
        four_signals = list(four)
        four_signals.remove(self.signal_map["c"])
        four_signals.remove(self.signal_map["d"])
        four_signals.remove(self.signal_map["f"])
        self.signal_map["b"] = four_signals[0]

        # TWO's last unknown signal is g
        two_signals = list(two)
        two_signals.remove(self.signal_map["a"])
        two_signals.remove(self.signal_map["c"])
        two_signals.remove(self.signal_map["d"])
        two_signals.remove(self.signal_map["e"])
        self.signal_map["g"] = two_signals[0]

        self.translation_map = {value: key for key, value in self.signal_map.items()}
        self.translate_output()

    def translate_output(self):
        output = ""
        for output_value in self.output_values:
            output += self.translate_digit(output_value)

        self.numeric_output = int(output)

    def translate_digit(self, digit_string: str):

        translated_signals = {
            "a": "0",
            "b": "0",
            "c": "0",
            "d": "0",
            "e": "0",
            "f": "0",
            "g": "0",
        }

        for index, signal in enumerate(digit_string):
            mapped_signal = self.translation_map[signal]
            translated_signals[mapped_signal] = "1"

        translated_output = str().join(list(translated_signals.values()))
        self.translated_outputs.append(translated_output)
        return self.decode_digit(translated_output)

    def decode_digit(self, signals):
        if signals == "1110111":
            return "0"
        if signals == "0010010":
            return "1"
        if signals == "1011101":
            return "2"
        if signals == "1011011":
            return "3"
        if signals == "0111010":
            return "4"
        if signals == "1101011":
            return "5"
        if signals == "1101111":
            return "6"
        if signals == "1010010":
            return "7"
        if signals == "1111111":
            return "8"
        if signals == "1111011":
            return "9"

        return f":{signals}:"
        raise Exception("wtf is this nonsense")
