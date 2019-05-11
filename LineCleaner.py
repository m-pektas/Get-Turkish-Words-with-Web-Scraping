def cleanLine(line):

    indices = [i for i, s in enumerate(line) if '>' in s]
    start = indices[0]

    indices = [i for i, s in enumerate(line) if '<' in s]
    end = indices[-1]

    return line[start+1:end]