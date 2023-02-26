import random

BLOCK_SIZE = 16



def encrypt(plaintext, key, rounds):
    blocks = [plaintext[i:i + BLOCK_SIZE] for i in range(0, len(plaintext), BLOCK_SIZE)]

    # Pad the last block if necessary
    if len(blocks[-1]) < BLOCK_SIZE:
        blocks[-1] = blocks[-1].ljust(BLOCK_SIZE)

    # Generate a random permutation matrix using the key
    rand = random.Random(0)
    perm = list(range(BLOCK_SIZE))
    rand.shuffle(perm)

    # Generate a subkey for each round
    rand = random.Random(hash(key))
    subkeys = [[rand.randint(0, 255) for j in range(BLOCK_SIZE)] for i in range(rounds)]

    # Encrypt each block
    ciphertext = ""
    for block in blocks:
        # Convert the block to a list of bytes
        block = [ord(b) for b in block]

        # Apply the initial permutation
        perm_block = [block[i] for i in perm]

        # Divide the block into two halves
        left = perm_block[:BLOCK_SIZE // 2]
        right = perm_block[BLOCK_SIZE // 2:]

        # Apply the Feistel rounds
        for i in range(rounds):
            # Apply the substitution function to the right half
            new_right = []
            for j in range(BLOCK_SIZE // 2):
                temp = (right[j] + subkeys[i][j]) % 256
                temp = (temp * temp) % 251
                temp = (temp + 5) % 256
                new_right.append(temp)

            # Combine the halves using XOR
            new_left = [left[j] ^ new_right[j] for j in range(BLOCK_SIZE // 2)]
            left = right
            right = new_left

        # Apply the final permutation
        perm_block = left + right
        ciphertext += "".join([chr(perm_block[perm.index(i)]) for i in range(BLOCK_SIZE)])

    return ciphertext


def main():
    text = input('Enter a Text: ')
    key = input('Enter a key: ')
    rounds = int(input('Enter a number of Rounds: '))
    ciphertext = encrypt(text, key, rounds)
    return ciphertext


if __name__ == '__main__':
    print('Cipher Text: ', main())
