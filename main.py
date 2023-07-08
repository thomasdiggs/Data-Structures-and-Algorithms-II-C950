# Thomas Diggs 010815435

import packages


class Main:
    pid1 = packages.Package(1, "195 W Oakland Ave", "Salt Lake City", "UT", 84115, 1030, 21)

    print(pid1.address)
    print(pid1.status)