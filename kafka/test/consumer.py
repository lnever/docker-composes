from kafka import KafkaConsumer


def get_binary(s):

    result = []
    for c in s:
        num = int(ord(c))
        tmp = []
        while num > 0:
            tmp.append(num % 2)
            num >>= 1

        while len(tmp) < 8:
            tmp.append(0)

        tmp.reverse()

        result += tmp
    return result


def read_int(binary, len):

    res = 0
    for i in range(len):
        res <<= 1
        res += binary[i]

    return binary[len:], res


def load_offset_info(s):
    binary = get_binary(s)

    binary, version = read_int(binary, 16)
    binary, offset = read_int(binary, 64)

    print(version, offset)


consumer = KafkaConsumer('__consumer_offsets')

for msg in consumer:
    load_offset_info(msg.value)
