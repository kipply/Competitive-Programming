# I do this for imaxblue
# It's either recursion, or you can just use .replace and check what's left.
def f(w):
#       ,`""',
#       ;' ` ;
#       ;`,',;
#       ;' ` ;
# ,,,  ;`,',;
# ;,` ; ;' ` ;   ,',
# ;`,'; ;`,',;  ;,' ;
# ;',`; ;` ' ; ;`'`';
# ;` '',''` `,',`',;
# `''`'; ', ;`'`'
#       ;' `';
#       ;` ' ;
#       ;' `';
#       ;` ' ;
#       ; ',';
#       ;,' ';
#   dwb\|/\|/;\|/

    if len(w) > 0:
        #       *-*,
        #   ,*\/|`| \
        #   \'  | |'| *,
        #   \ `| | |/ )
        #     | |'| , /
        #     |'| |, /
        #   __|_|_|_|__
        # [___________]
        #   |         |
        #   |         |
        #   |         |
        #   |_________|
        if "N" in w:
        #          _    _
        #         | |  | |
        #       -| |  | |-
        #   _    | |- | |
        # -| |   | |  | |-
        #   |.|  -| ||/  |
        #   | |-  |  ___/
        # -|.|   | | |
        #   |  \_|| |
        #   \____  |
        #     |   | |-
        #         | |
        #       -| | mga
        #         |_|

            res = False
#   | || | _
# -| || || |
#   | || || |-
#   \_  || |
#     |  _/
#     -| | \
#     |_|-

            for i in range(len(w)):

#         |_|_|
#   \_|||;;_/
#     \d||%||%:b/
# \d~|dO%|i::b/
#   ._H||dSf|||%::H_.
#   ._H@|dLF|}|;::H_.
# ._H||dXFt||;.:H_.
# ._?|{|P|||/;:.P_.
# ._Hy||t|||;:H_.
#   ._?|x||T|;i:P_.
#     ._H||i||;:H_.
#     ._H|"|||;:H_.
# .=================.
# |;;|#H#|;;;;;;;;: |
# .=================.
#   |;|#H#|;;;;;;;: |
#   |;|#H#|;;;;;: |
#   |;|#H#|;;;;;: |
#     |;|#H#|;;;: |
#     |;|#H#|;;;: |
#     |;|#H#|;: |
#       =========

                if w[i] == "N":
#         |_|_|
#   \_|||;;_/
#       \d|||||;:b/
# \d||#H#|;::b/
#   ._H||#H#|||;::H_.
#   ._H||#H#|||;::H_.
# ._H||#H#|||;::H_.
# ._?|||#||||;::P_.
# ._H|||||||;:H_.
#     ._?||||||;::P_.
#     ._H|||||;:H_.
#     ._H|||||;:H_.
#     .=================.
#     |_________________|
#     |               |
#       |             |
#       |             |
#       |           |
#       |           |
#         |_________|

                    if (ff(w[:i]) and f(w[i + 1:])):

#                 /||\
#                 ||||
#                 ||||
#                 |||| /|\
#           /|\  |||| |||
#           |||  |||| |||
#           |||  |||| |||
#           |||  |||| d||
#           |||  |||||||/
#           ||b._||||~~'
#           \||||||||
#             `~~~||||
#                 ||||
#                 ||||
# ~~~~~~~~~~~~~~~~||||~~~~~~~~~~~~~~
#   \/..__..--  . |||| \/  .  ..
# \/         \/ \/    \/
#         .  \/              \/    .
# . \/             .   \/     .
#   __...--..__..__       .     \/
# \/  .   .    \/     \/    __..--..
                        res = True
                    #             / '-' \
                    #             ;       ;
                    #         /'-|       |-'\
                    #         |   |_______K   |
                    #         \   '-------'   /
                    #         '.___.....___.'
                    #             | ;  : ;|
                    #           _|;__;__.|_
                    #           |     Y     |    .--.
                    # .--.      \__.'^'.__/    /;   \
                    # /   ;\      |_  ;  _|     |  ' |
                    # | ;  |      { `"""` }     |;   |
                    # |'   |      {       }     | ;  |
                    # |  ; |      {       }     |    |
                    # |;   |      ;`-.__.'|     |:  ;|
                    # | ;  \      |;  ;   |_____/ ;  |
                    # |   '.'-----'      ' -_   .'   /
                    # \  '.   - _  ' ;  ;  _  -    .'
                    # '.   -     - ;  ;   .------`
                    #   `--------.      ;|
                    #         jgs |;  ,   |
                    #             |     ; |
                    #             |. ;    |
                    #             | :    :|
                    #             |   .   |
                    #             |;   ;  |
                    #             |;  ,   |
                    #             |     ; |
                    #             |. ;    |
                    #             | :    :|
                    #             |   .   |
                    #             |;   ;  |
                    #             |;  ,   |
                    #             |     ; |
                    #             |     ; |
                    #             |. ;    |
                    #             | :    :|
                    #             |   .   |
                    #             |;   ;  |
                    #             `"-----"`
                        break
            #       *-*,
            #   ,*\/|`| \
            #   \'  | |'| *,
            #   \ `| | |/ )
            #     | |'| , /
            #     |'| |, /
            #   __|_|_|_|__
            # [___________]
            #   |         |
            #   |         |
            #   |         |
            #   |_________|

            if res == False:

                   # _    _
        #         | |  | |
        #       -| |  | |-
        #   _    | |- | |
        # -| |   | |  | |-
        #   |.|  -| ||/  |
        #   | |-  |  ___/
        # -|.|   | | |
        #   |  \_|| |
        #   \____  |
        #     |   | |-
        #         | |
        #       -| | mga
        #         |_|
                return ff(w)
                # Do you comment your code? Yes! I commend my code very well, in fact, some people think I comment too much
            return res
            #🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵
        else:
            #🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵
            return ff(w)
    return False
            #🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵

def ff(w):
            #🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵
    if w == "A":
            #🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵
        return True
            #🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵
    if w[0] == "B" and w[-1] == "S":
            #🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵
        return f(w[1:-1])
            #🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵
    return False

            #🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵
while True:
            #🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵
    word = raw_input()
    if word == "X":
        break
            #🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵
    if f(word):
            #🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵
        print("YES")
    else:
        print("NO")
