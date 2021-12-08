def find_wiring_map(signal_patterns):
    """
    Returns a dictionary containing the mapping between segments (A, B, ..., G)
    and wires (a, b, ..., g)
    """
    mapping = {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None}
    pattern = [None] * 10
    # 1, 4 and 7 have unique lengths, their patterns can be determined
    pattern[1] = [x for x in signal_patterns if len(x) == 2][0]
    pattern[4] = [x for x in signal_patterns if len(x) == 4][0]
    pattern[7] = [x for x in signal_patterns if len(x) == 3][0]

    # A is segment present in 7 but not in 1
    for segment in pattern[7]:
        if segment not in pattern[1]:
            mapping['A'] = segment
    
    # 0, 6 and 9 are the only ones that have 6 digits
    candidates_069 = [x for x in signal_patterns if len(x) == 6]
    # but only 6 is missing one of the two digits of 1
    for candidate in candidates_069:
        for segment in pattern[1]:
            if segment not in candidate:
                pattern[6] = candidate
                mapping['C'] = segment

    # Find the remaining segment of 1
    for segment in pattern[1]:
        if segment != mapping['C']:
            mapping['F'] = segment

    # There are two unknown segments in 4, belonging to B and D
    unknowns_4 = pattern[4].replace(mapping['C'], '').replace(mapping['F'], '')
    # which appear in 9 but not in 0
    candidates_069.remove(pattern[6])
    candidates_09 = candidates_069
    for candidate in candidates_09:
        for segment in unknowns_4:
            if segment not in candidate:
                pattern[0] = candidate
                mapping['D'] = segment
                candidates_09.remove(candidate)
    pattern[9] = candidates_09[0]
    
    # Find the remaining segment of 4
    mapping['B'] = unknowns_4.replace(mapping['D'], '')

    # At this point there are two missing wires to determine, those mapped to E and G
    missing_wires = 'abcdefg'
    for wire in mapping.values():
        if wire:
            missing_wires = missing_wires.replace(wire, '')

    # Of those segments, only E is present in 9
    for wire in missing_wires:
        if wire not in pattern[9]:
            mapping['E'] = wire
            mapping['G'] = missing_wires.replace(wire, '')
    
    return mapping


def wires_to_segments(wires, mapping):
    inv_map = {v: k for k, v in mapping.items()}
    segments = ''
    for wire in wires:
        segments += inv_map[wire]
    sorted_segments = ''
    for segment in sorted(segments):
        sorted_segments += segment
    return sorted_segments


def segments_to_number(segments):
    mapping = {'ABCEFG':  '0',
               'CF':      '1',
               'ACDEG':   '2',
               'ACDFG':   '3',
               'BCDF':    '4',
               'ABDFG':   '5',
               'ABDEFG':  '6',
               'ACF':     '7',
               'ABCDEFG': '8',
               'ABCDFG':  '9'}
    return mapping[segments]
