#numero primo

__doc__= "Essse modulo tem como objetivo retornar que um numero é primo ou não"


def primo(numero):
    if numero > 1:
        for x in range(2, numero):
            if (numero % x) == 0:
                return "numero não eh primo"
        else:
            return "numero eh primo"
    else:
        return "numero não eh primo"


if __name__ == '__main__':
    print("ola mundo do modulo primo")
