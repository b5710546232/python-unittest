def count(input):
    output = {}
    for item in input:
        if item in output.keys():
            output[item] += 1
        else:
            output[item] = 1
    return output