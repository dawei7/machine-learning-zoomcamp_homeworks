from hashlib import sha1


def compute_hash(email):
    return sha1(email.lower().encode('utf-8')).hexdigest()


# 774678aec551cc8dd1fbee0595bf39af48ea7322
print(compute_hash('davidschmid121186@gmail.com'))
