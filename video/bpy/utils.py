def convert_domain_to_range(
    value=30000,
    domain_max=50000,
    domain_min=10000,
    range_max=3,
    range_min=2,
):
    range_val = (value - domain_min) / (domain_max - domain_min)
    return (range_max - range_min) * range_val + range_min


def lfsr_galois_24bit(start_state):
    lfsr = start_state  # Any nonzero start state will work.
    period = 0
    lsb = lfsr & 1  # Get LSB (i.e., the output bit).
    lfsr >>= 1  # Shift register
    if lsb:  # If the output bit is 1,
        lfsr ^= 0xE10000  # apply toggle mask.
    return lfsr


def convert_hex_24bit_to_colour_tuple(hex_number):
    # Convert hexadecimal color code to RGB components
    red = (hex_number >> 16) & 0xFF
    green = (hex_number >> 8) & 0xFF
    blue = hex_number & 0xFF

    # Normalize RGB values to the range [0, 1]
    red_normalized = red / 255.0
    green_normalized = green / 255.0
    blue_normalized = blue / 255.0

    # Return color tuple with alpha channel set to 1
    return (
        red_normalized,
        green_normalized,
        blue_normalized,
        1,
    )


def lfsr_galois_12bit(start_state):
    lfsr = start_state  # Any nonzero start state will work.
    period = 0
    lsb = lfsr & 1  # Get LSB (i.e., the output bit).
    lfsr >>= 1  # Shift register
    if lsb:  # If the output bit is 1,
        lfsr ^= 0xE08  # apply toggle mask.
    return lfsr


def convert_hex_12bit_to_colour_tuple(hex_number):
    # Extract individual components from the 12-bit hex color code
    red = (hex_number >> 8) & 0xF
    green = (hex_number >> 4) & 0xF
    blue = hex_number & 0xF

    # Normalize RGB values to the range [0, 1]
    red_normalized = red / 15.0
    green_normalized = green / 15.0
    blue_normalized = blue / 15.0

    # Return color tuple with alpha channel set to 1
    return (
        red_normalized,
        green_normalized,
        blue_normalized,
        1,
    )


def modulo_html_colors_hex(number):
    html_colors_hex = {
        "black": 0x000000,
        "silver": 0xC0C0C0,
        "gray": 0x808080,
        "white": 0xFFFFFF,
        "maroon": 0x800000,
        "red": 0xFF0000,
        "purple": 0x800080,
        "fuchsia": 0xFF00FF,
        "green": 0x008000,
        "lime": 0x00FF00,
        "olive": 0x808000,
        "yellow": 0xFFFF00,
        "navy": 0x000080,
        "blue": 0x0000FF,
        "teal": 0x008080,
        "aqua": 0x00FFFF,
    }
    html_colors = [
        # "black",
        # "silver",
        # "gray",
        # "white",
        "maroon",
        "red",
        "purple",
        "fuchsia",
        "green",
        "lime",
        "olive",
        "yellow",
        "navy",
        "blue",
        "teal",
        "aqua",
    ]
    index = number % len(html_colors)
    return html_colors_hex[html_colors[index]]


def get_max_value(tuple_list):
    # Initialize max_value with negative infinity to handle negative values
    max_value = float("-inf")

    # Iterate through each tuple in the list
    for key, value in tuple_list:
        # Update max_value if the current value is greater
        if value > max_value:
            max_value = value

    return max_value


if __name__ == "__main__":
    result = convert_domain_to_range(
        value=50, domain_max=100, domain_min=1, range_max=3, range_min=1
    )
    print(
        "result = convert_domain_to_range(value=50, domain_max=100, domain_min=0, range_max=10, range_min=0) = ",
        result,
    )

    result = lfsr_galois_24bit(0xFFCCFF)
    print("lfsr_galois_24bit(0xFFCCFF) = ", hex(result))

    hex_color = 0xFFA500  # Example 24-bit color code (orange)
    result = convert_hex_24bit_to_colour_tuple(hex_color)
    print("convert_hex_24bit_to_colour_tuple(0xFFA500) = ", result)

    result = lfsr_galois_12bit(0xFCF)
    print("lfsr_galois_12bit(0xFCF) = ", hex(result))

    hex_color = 0xFC0  # Example 12-bit color code (e.g., from HTML/CSS)
    result = convert_hex_12bit_to_colour_tuple(hex_color)
    print("convert_hex_12bit_to_colour_tuple(0xFC0) = ", result)

    print("modulo_html_colors_hex(18) = ", modulo_html_colors_hex(18))

    tuple_list = [("a", 10), ("b", 20), ("c", 15)]
    print("Maximum value:", get_max_value(tuple_list))
