""" Assignment: nuclear power plant
    Created on 28 oct. 2020
    @author: Mark Melnic """

PRINT_TIMES = 3


def message():
    print(
        """
        NUCLEAR CORE UNSTABLE!!!
        Quarantine is in effect.
        Surrounding hamlets will be evacuated.
        Anti-radiationsuits and iodine pills are mandatory.
        """
    )


for i in range(PRINT_TIMES):
    message()
