from argparse import ArgumentParser

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from modelos.knn_class import KNN
import sys

def parse_args():
    ap = ArgumentParser()

    ap.add_argument(
        '--k',
        '-k',
        required=True,
        type=int,
        help='KNN k hyper parameter'
    )

    ap.add_argument(
        '--test-size',
        required=False,
        type=float,
        default=0.2,
        help='Set test size'
    )

    ap.add_argument(
        '--random-state',
        required=False,
        type=int,
        default=1,
        help='Random state'
    )

    return ap.parse_args()

def main(args):
    (X, y) = load_iris(return_X_y=True)
    data = train_test_split(X, y, test_size=args.test_size, random_state=args.random_state)

    (X_train, X_test, y_train, y_test) = data

    clf = KNN(k=5)
    clf.fit(X_train, y_train)
    predicoes = clf.predict(X_test)

    print(predicoes)


if __name__ == '__main__':
    args = parse_args()
    main(args)
    sys.exit(0)