# perceptron simple para función OR
def salida(k, pesos, t):
  z=-t
  for i in range(len(k)):
    z=z+(k[i]*pesos[i])
  if z>=0:
    return 1
  else:
    return 0


def entrenar_perceptron(datos_ent, pesos, t, l):
  errores=True
  while errores:
    errores=False
    # entrenar perceptron
    for k,y in datos_ent.iteritems():
      z=salida(k, pesos, t)
      if z!=y:
        errores=True
        # error
        e=(y-z)
        # calcular ajustes
        delta_t=-(l*e)
        t=t+delta_t
        for i in range(len(k)):
          delta_w=l*e*k[i]
          pesos[i]=pesos[i]+delta_w

  return pesos, t


def clasificar(entrada, pesos, t):
  return salida(entrada, pesos, t)


if __name__ == "__main__":
  datos_ent={(0,0):0, (0,1):1, (1,0):1,(1,1):1}
  pesos=[0.2,0.6]
  t=0.4
  l=0.2
  pesos, t = entrenar_perceptron(datos_ent, pesos, t, l)
  print clasificar((0,1), pesos, t)

