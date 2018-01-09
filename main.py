import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Intelligence Poem Writer.')
    help_ = 'choose to train or generate.'
    parser.add_argument('--train', dest='train', action='store_true', help=help_)
    parser.add_argument('--no-train', dest='train', action='store_false', help=help_)
    parser.set_defaults(train=True)

    args_ = parser.parse_args()
    return args_


if __name__ == '__main__':
    args = parse_args()
    
    import tang_poems
    if args.train:
        tang_poems.main(True)
    else:
        tang_poems.main(False)
    




