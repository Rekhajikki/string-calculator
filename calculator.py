class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        delimiters = [',', '\n']

        # Custom delimiter support
        if numbers.startswith('//'):
            parts = numbers.split('\n', 1)
            delimiter_part = parts[0][2:]
            numbers = parts[1]
            delimiters.append(delimiter_part)

        # Split by delimiters
        import re
        split_pattern = '|'.join(map(re.escape, delimiters))
        number_list = re.split(split_pattern, numbers)

        # Convert to integers and filter negatives
        int_numbers = [int(num) for num in number_list if num.strip()]
        negatives = [num for num in int_numbers if num < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {negatives}")

        return sum(int_numbers)
