#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
    let nb = 0;

    list.forEach((el) => {
        if (el === searchElement) nb++;
    });

    return nb;
}
