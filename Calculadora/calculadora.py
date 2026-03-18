import soma
import subtrai
import multiplica
import divide


def calcular(n1: float, n2: float, operador: str) -> float:
    if operador == "+":
        return soma.somaf(n1, n2)
    if operador == "-":
        return subtrai.subtraif(n1, n2)
    if operador == "*":
        return multiplica.multiplicaf(n1, n2)
    if operador == "/":
        return divide.dividef(n1, n2)
    raise ValueError(f"Operador inválido: {operador}")


def main() -> None:
    try:
        n1 = float(input().strip())
        n2 = float(input().strip())
        operador = input().strip()
        resultado = calcular(n1, n2, operador)
        print(resultado)
    except ZeroDivisionError:
        print("Erro: divisão por zero")
    except ValueError as err:
        print(f"Erro: {err}")


if __name__ == "__main__":
    main()