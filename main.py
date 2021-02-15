#Se deberá ingresar 2 número por consola 
# , el primer dato ingresado será el menor valor (min_nro), 
# el segundo dato ingresado será el mayor (max_nro). 
# En caso no se cumpla esta condición debera volver a ingresar los dos números.
from typing import Final
from argparse import ArgumentParser
def main() -> None:
    ap = ArgumentParser()
    ap.add_argument(dest='min_nro',help="This is help",type=float)
    ap.add_argument(dest='max_nro',help="This is help",type=float)
    args = ap.parse_args(args=[input("min_nro: "),input("max_nro: ")])

    min_nro: Final[float] = args.min_nro
    max_nro: Final[float] = args.max_nro
    if (min_nro < max_nro):
      sum: float = min_nro+max_nro
      print(min_nro, max_nro, sum)
    else:
      print("Primer argumento no es menor que el segundo, de nuevo")
      main()
main()
